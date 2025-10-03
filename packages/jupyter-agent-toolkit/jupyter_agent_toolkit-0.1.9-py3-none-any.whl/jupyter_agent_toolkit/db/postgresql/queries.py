from __future__ import annotations

import contextlib
import logging
import tempfile
from pathlib import Path
from typing import Any, List, Mapping, Optional, Sequence, Union

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from .connection import ConnectionManager
from .io import rows_to_dataframe

_LOG = logging.getLogger("jupyter_agent_toolkit.db.postgresql.queries")


# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------

def _import_sql():
    """
    Lazy import for psycopg.sql utilities so this module can be imported
    even before the kernel has psycopg installed.

    Returns:
        The psycopg.sql module (provides SQL, Identifier, Literal, Composed, etc.).
    """
    from psycopg import sql  # type: ignore
    return sql


# -------------------------------------------------------------------
# Unified query helpers
# -------------------------------------------------------------------

def query_rows(
    manager: ConnectionManager,
    sql: str | None = None,
    *,
    # Table mode (identifier-safe) arguments:
    schema_name: str | None = None,
    table_name: str | None = None,
    columns: Union[str, Sequence[str]] = "*",
    where: str | None = None,
    order_by: str | None = None,
    # Common arguments:
    limit: Optional[int] = None,
    params: Optional[Mapping[str, Any]] = None,
) -> List[dict]:
    """
    Execute a query and return rows, supporting two modes.

    Two usage modes
    --------------
    1) Raw SQL mode:
       - Provide `sql="SELECT ..."`
       - Optional: `params`, `limit`
       If `limit` is provided, the SQL is wrapped as a subquery and a LIMIT is
       injected using `psycopg.sql.Literal(int(limit))`. **No DB-API placeholders**
       are introduced by us in this path, so percent signs inside string literals
       (e.g., `ILIKE '%foo%'`) are never misinterpreted as placeholders.

    2) Table mode (identifier-safe):
       - Provide `schema_name="...", table_name="..."`
       - Optional: `columns`, `where`, `order_by`, `limit`, `params`
       Statement is constructed with `psycopg.sql` using proper identifier quoting.
       `where`/`order_by` are treated as **trusted** SQL fragments (bind values via
       `params`). `LIMIT` is injected with `sql.Literal(int(limit))`.

    Important psycopg3 behavior
    ---------------------------
    Passing an **empty dict** `{}` as `params` makes psycopg treat the query as
    parametrized and scan it for `%` placeholders, which breaks queries that have
    percent signs inside string literals (e.g., `ILIKE '%term%'`) with:
        ProgrammingError: only '%s', '%b', '%t' are allowed as placeholders, got '%M'
    To avoid this, **pass no params at all** when you don't have any (i.e., pass
    `None` to `cursor.execute()`).

    Args:
        manager: ConnectionManager instance.
        sql: Raw SQL text (use this OR the table-mode args).
        schema_name: Schema for table mode.
        table_name: Table for table mode.
        columns: "*" or a sequence of column names (table mode only).
        where: **Trusted** WHERE clause (table mode only). Bind values via `params`.
        order_by: **Trusted** ORDER BY clause (table mode only).
        limit: Optional LIMIT to apply. In raw mode, applied as an outer LIMIT.
        params: Mapping of bind parameters for the underlying query (or None).

    Returns:
        List[dict]: Result rows (possibly empty).

    Raises:
        ValueError: If inputs are invalid or neither mode is selected.
        RuntimeError: If execution fails.
    """
    # We may pass None to cursor.execute() when there are no params.
    exec_params: Optional[Mapping[str, Any]]
    sql_mod = None  # lazy import only if/when needed

    # ---- Mode selection & statement building ----
    if sql is not None:
        # Raw SQL mode
        if not isinstance(sql, str) or not sql.strip():
            raise ValueError("SQL query must be a non-empty string.")
        if params is not None and not isinstance(params, Mapping):
            raise ValueError("Query parameters must be a Mapping or None.")

        sql_clean = sql.strip()
        if sql_clean.endswith(";"):
            sql_clean = sql_clean[:-1]

        if limit is not None:
            # Compose without DB-API-style placeholders so '%' in literals is harmless.
            if sql_mod is None:
                sql_mod = _import_sql()
            sql_final = sql_mod.SQL("SELECT * FROM ({}) AS jat_sub LIMIT {}").format(
                sql_mod.SQL(sql_clean),
                sql_mod.Literal(int(limit)),
            )
            exec_params = params if params is not None else None
        else:
            # Use the raw SQL as-is (caller may include its own LIMIT).
            sql_final = sql_clean
            exec_params = params if params is not None else None

    elif schema_name and table_name:
        # Table mode (identifier-safe)
        if params is not None and not isinstance(params, Mapping):
            raise ValueError("Query parameters must be a Mapping or None.")

        sql_mod = _import_sql()

        # Columns
        if columns == "*":
            cols_sql = sql_mod.SQL("*")
        else:
            if not isinstance(columns, Sequence) or isinstance(columns, str):
                raise ValueError("columns must be '*' or a sequence of column names")
            cols_sql = sql_mod.SQL(", ").join(sql_mod.Identifier(c) for c in columns)

        # Base + optional clauses
        base = sql_mod.SQL("SELECT {} FROM {}.{}").format(
            cols_sql, sql_mod.Identifier(schema_name), sql_mod.Identifier(table_name)
        )
        parts = [base]
        if where:
            # `where` is a trusted string fragment. Bind values via `params`.
            parts.append(sql_mod.SQL(" WHERE " + where))
        if order_by:
            parts.append(sql_mod.SQL(" ORDER BY " + order_by))
        if limit is not None:
            parts.append(sql_mod.SQL(" LIMIT {}").format(sql_mod.Literal(int(limit))))

        sql_final = sql_mod.Composed(parts)
        exec_params = params if params is not None else None

    else:
        raise ValueError("Provide either `sql` (raw SQL mode) OR `schema_name` + `table_name` (table mode).")

    # ---- Execute ----
    try:
        with manager.connection() as conn, conn.cursor() as cur:
            # Safe to log (identifiers quoted). Truncate to keep logs tidy.
            _LOG.debug("Executing query: %s", str(sql_final)[:200].replace("\n", " "))

            # ⚠️ Critical: only pass params when present to avoid '%' placeholder scan
            if exec_params is None:
                cur.execute(sql_final)
            else:
                cur.execute(sql_final, exec_params)

            rows = list(cur.fetchall()) if cur.description else []
            _LOG.debug("Query executed successfully, %d rows returned.", len(rows))
            return rows
    except Exception as e:
        _LOG.error("Query execution failed: %s", str(e))
        raise RuntimeError(f"Query execution failed: {e}") from e

def query_df(
    manager: ConnectionManager,
    sql: str | None = None,
    *,
    # Table mode (identifier-safe) arguments:
    schema_name: str | None = None,
    table_name: str | None = None,
    columns: Union[str, Sequence[str]] = "*",
    where: str | None = None,
    order_by: str | None = None,
    # Common arguments:
    limit: Optional[int] = None,
    params: Optional[Mapping[str, Any]] = None,
) -> pd.DataFrame:
    """
    DataFrame wrapper of `query_rows` (supports both raw SQL and table modes).

    See `query_rows` for argument semantics.
    """
    rows = query_rows(
        manager,
        sql,
        schema_name=schema_name,
        table_name=table_name,
        columns=columns,
        where=where,
        order_by=order_by,
        limit=limit,
        params=params,
    )
    return rows_to_dataframe(rows)


def stream_to_parquet(
    manager: ConnectionManager,
    sql: str,
    path: str | Path,
    params: Optional[Mapping[str, Any]] = None,
    *,
    chunk_rows: int = 50_000,
    progress_every: int = 10,
) -> str:
    """
    Stream a large SELECT result directly to a Parquet file via a server-side cursor.

    Note on params:
        As with `query_rows`, **do not pass `{}`** to `cursor.execute()` when there
        are no parameters. Pass `None` (by omitting the second arg) so psycopg does
        not scan the SQL for `%` placeholders and break on string-literal percents.

    Args:
        manager: ConnectionManager instance.
        sql: SQL SELECT to execute (raw SQL mode). Use `params` for values.
        path: Output Parquet file path.
        params: Mapping of parameters (or None).
        chunk_rows: fetchmany() chunk size (> 0).
        progress_every: Log a DEBUG message every N chunks.

    Returns:
        str: Absolute output file path.

    Raises:
        ValueError: If arguments are invalid.
        RuntimeError: If streaming or file writing fails.
    """
    if not isinstance(sql, str) or not sql.strip():
        raise ValueError("SQL query must be a non-empty string.")
    if params is not None and not isinstance(params, Mapping):
        raise ValueError("Query parameters must be a Mapping or None.")
    if not isinstance(chunk_rows, int) or chunk_rows <= 0:
        raise ValueError("chunk_rows must be a positive integer.")

    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    writer: pq.ParquetWriter | None = None
    tmp_path: Path | None = None
    total_rows = 0

    try:
        with manager.connection() as conn:
            _LOG.debug("Streaming query to parquet (first 200 chars): %s", sql[:200].replace("\n", " "))

            # Ensure transaction for the named server-side cursor
            with conn.transaction():
                with conn.cursor(name="jat_stream") as cur:
                    cur.itersize = chunk_rows

                    # ⚠️ Only pass params when you actually have them
                    if params is None:
                        cur.execute(sql)
                    else:
                        cur.execute(sql, params)

                    # temp file for atomic move
                    with tempfile.NamedTemporaryFile(dir=p.parent, delete=False) as tmp:
                        tmp_path = Path(tmp.name)

                    chunks = 0
                    while True:
                        chunk = cur.fetchmany(chunk_rows)
                        if not chunk:
                            break
                        df = pd.DataFrame(chunk)
                        table = pa.Table.from_pandas(df, preserve_index=False)
                        if writer is None:
                            writer = pq.ParquetWriter(tmp_path, table.schema)
                        writer.write_table(table)

                        chunks += 1
                        total_rows += len(df)
                        if progress_every and (chunks % progress_every == 0):
                            _LOG.debug("... streamed %d chunks / %d rows so far", chunks, total_rows)

        if writer is not None:
            writer.close()

        if tmp_path is not None:
            tmp_path.replace(p)

        _LOG.debug("Streaming to parquet complete: %s (~%d rows)", str(p.resolve()), total_rows)
        return str(p.resolve())

    except Exception as e:
        _LOG.error("Failed to stream query to parquet: %s", str(e))
        raise RuntimeError(f"Failed to stream query to parquet: {e}") from e
    finally:
        if writer is not None:
            with contextlib.suppress(Exception):
                writer.close()
        if tmp_path is not None and tmp_path.exists():
            with contextlib.suppress(Exception):
                tmp_path.unlink()