"""
The oc_graph module provides the same operations as the Spark GraphX library,
but for an Ocient database. Graphs are represented as tables in the database,
with vertices and edges stored in separate tables.

A vertices table must contain a column named "id" that is not nullable and is
of type BIGINT. An edges table must contain two columns named "srcid" and
"destid" that are not nullable and are of type BIGINT. Besides these columns,
the vertices and edges tables can contain any number of additional columns
with any data types.
"""

import uuid
from enum import Enum
from typing import List, Optional, Set

from pyocient import Connection, Cursor, SQLException

# -----------------------------------------------------------------------------
# Private Helper Functions
# -----------------------------------------------------------------------------


def _check_not_null(obj: object, message: str) -> None:
    """Raises SQLException if the object is None."""
    if obj is None:
        raise SQLException(f"Argument Error: {message}")


def _check_not_null_or_empty(s: Optional[str], message: str) -> None:
    """Raises SQLException if the string is None, empty, or only whitespace."""
    if not s or not s.strip():
        raise SQLException(f"Argument Error: {message}")


def _check_positive(value: int, message: str) -> None:
    """Raises SQLException if the value is not positive."""
    if value <= 0:
        raise SQLException(f"Argument Error: {message}")


def _table_name(schema: str, table: str) -> str:
    """Returns a fully qualified and quoted table name."""
    return f'"{schema}"."{table}"'


def _check_table_conflict(result_schema: str, result_table: str, input_qualified_table_names: Set[str]) -> None:
    """Raises SQLException if the result table name conflicts with any input table name."""
    qualified_result_name = _table_name(result_schema, result_table)
    if qualified_result_name in input_qualified_table_names:
        raise SQLException(
            f"Naming Conflict: Result table/view '{qualified_result_name}' cannot have the same name as an input table."
        )


def _safe_drop_table(cursor: Cursor, qualified_table_name: str) -> None:
    """Safely drops a table, ignoring errors if it doesn't exist."""
    if cursor is None or not qualified_table_name:
        return
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {qualified_table_name}")
    except SQLException:
        # Ignore potential errors during cleanup
        pass


def _safe_drop_view(cursor: Cursor, qualified_view_name: str) -> None:
    """Safely drops a view, ignoring errors if it doesn't exist."""
    if cursor is None or not qualified_view_name:
        return
    try:
        cursor.execute(f"DROP VIEW IF EXISTS {qualified_view_name}")
    except SQLException:
        # Ignore potential errors during cleanup
        pass


def _create_table_from_template(
    template_schema: str,
    template_table: str,
    result_schema: str,
    result_table: str,
    result_indexes: List[str],
    cursor: Cursor,
) -> None:
    """
    Creates a new table based on an existing template table and optionally
    creates indexes on specified columns.
    """
    template_table_name = _table_name(template_schema, template_table)
    result_table_name = _table_name(result_schema, result_table)

    # Create an empty copy of the template table
    cursor.execute(f"CREATE TABLE {result_table_name} AS SELECT * FROM {template_table_name} WHERE 1=0")

    # Create indexes on specified columns
    for index_col in result_indexes:
        _check_not_null_or_empty(index_col, "Index column name cannot be null or empty.")
        clean_col_name = "".join(filter(str.isalnum, index_col))
        index_name = f"idx_{result_table}_{clean_col_name}_{uuid.uuid4().hex[:8]}"
        cursor.execute(f'CREATE INDEX "{index_name}" ON {result_table_name} ("{index_col}")')


# -----------------------------------------------------------------------------
# Public API
# -----------------------------------------------------------------------------


class EdgeDirection(Enum):
    """
    Specifies the direction of edges to follow relative to a source vertex
    when traversing a graph or collecting neighbors. Used to determine whether
    to consider incoming edges, outgoing edges, or both.
    """

    IN = "IN"
    """
    Follow incoming edges only. Selects neighbors connected by an edge pointing
    *towards* the source vertex (i.e., where the source vertex is the
    destination of the edge).
    """

    OUT = "OUT"
    """
    Follow outgoing edges only. Selects neighbors connected by an edge
    originating *from* the source vertex (i.e., where the source vertex is the
    source of the edge).
    """

    BOTH = "BOTH"
    """
    Follow edges in both directions. Selects neighbors connected by either
    incoming or outgoing edges relative to the source vertex.
    """


def subgraph(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    result_edges_table: str,
    vertex_filter: str,
    edge_filter: str,
    result_vertices_indexes: List[str],
    result_edges_indexes: List[str],
) -> None:
    """
    Creates a subgraph consisting of new vertex and edge tables based on
    filtering criteria applied to existing input graph tables.

    This method performs the following steps:
    1. Validates input parameters.
    2. Checks for potential conflicts where result tables might overwrite inputs.
    3. Creates the structure for the result vertex and edge tables, copying the
       schema from the corresponding input tables and applying specified indexes.
    4. Populates the result vertex table by selecting vertices from the input
       vertex table that satisfy the `vertex_filter`.
    5. Populates the result edge table by selecting edges from the input edge
       table that satisfy the `edge_filter` AND whose source and destination
       vertices BOTH exist in the newly created (filtered) result vertex table.

    Important Filter Logic:
    - The `vertex_filter` is a standard SQL WHERE clause applied to the input
      vertex table.
    - The `edge_filter` is a standard SQL WHERE clause condition. Within this
      filter string:
        - Reference columns from the *source vertex* using the alias `a`.
        - Reference columns from the *edge* itself using the alias `b`.
        - Reference columns from the *destination vertex* using the alias `c`.
      An edge is only included if it passes this filter AND its corresponding
      source and destination vertices are present in the *result* vertex table.

    Atomicity and Cleanup:
    The operation attempts to be atomic. If any step fails, it will attempt to
    drop the newly created result tables to avoid leaving partial results.

    :param connection: The pyocient Connection object.
    :param input_schema: The schema name for the original graph tables.
    :param input_vertices_table: The table name for the original vertices.
    :param input_edges_table: The table name for the original edges.
    :param result_schema: The schema name for the resulting subgraph tables.
    :param result_vertices_table: Name for the new table for filtered vertices.
    :param result_edges_table: Name for the new table for filtered edges.
    :param vertex_filter: An SQL WHERE clause (without "WHERE") to filter
        vertices. Use "1=1" for no filter.
    :param edge_filter: An SQL WHERE clause (without "WHERE") to filter edges.
        Use aliases a, b, and c for source vertex, edge, and destination
        vertex. Use "1=1" for no filter.
    :param result_vertices_indexes: A list of column names for indexes on the
        result vertices table.
    :param result_edges_indexes: A list of column names for indexes on the
        result edges table.
    :raises SQLException: If any database error occurs or filters are invalid.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null_or_empty(result_edges_table, "Result edges table name cannot be null or empty.")
    _check_not_null(vertex_filter, "Vertex filter cannot be null (use '1=1').")
    _check_not_null(edge_filter, "Edge filter cannot be null (use '1=1').")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")
    _check_not_null(result_edges_indexes, "Result edges index list cannot be null.")

    input_tables = {
        _table_name(input_schema, input_vertices_table),
        _table_name(input_schema, input_edges_table),
    }
    _check_table_conflict(result_schema, result_vertices_table, input_tables)
    _check_table_conflict(result_schema, result_edges_table, input_tables)

    qualified_result_vertices = _table_name(result_schema, result_vertices_table)
    qualified_result_edges = _table_name(result_schema, result_edges_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            _create_table_from_template(
                input_schema,
                input_vertices_table,
                result_schema,
                result_vertices_table,
                result_vertices_indexes,
                cursor,
            )
            _create_table_from_template(
                input_schema,
                input_edges_table,
                result_schema,
                result_edges_table,
                result_edges_indexes,
                cursor,
            )

            input_vertices_name = _table_name(input_schema, input_vertices_table)
            v_filter_clause = (
                f" WHERE {vertex_filter}" if vertex_filter.strip() and vertex_filter.strip() != "1=1" else ""
            )
            cursor.execute(
                f"INSERT INTO {qualified_result_vertices} SELECT * FROM {input_vertices_name}{v_filter_clause}"
            )

            input_edges_name = _table_name(input_schema, input_edges_table)
            e_filter_clause = f" AND ({edge_filter})" if edge_filter.strip() and edge_filter.strip() != "1=1" else ""

            # This complex join ensures edges are included only if they pass the
            # edge_filter AND their endpoints exist in the filtered result vertices.
            insert_edges_sql = f"""
                INSERT INTO {qualified_result_edges}
                SELECT b.* FROM
                    {input_vertices_name} a,
                    {input_edges_name} b,
                    {input_vertices_name} c,
                    {qualified_result_vertices} d,
                    {qualified_result_vertices} e
                WHERE a.id = b.srcid AND c.id = b.destid
                  AND d.id = b.srcid AND e.id = b.destid
                  {e_filter_clause}
            """
            cursor.execute(insert_edges_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, qualified_result_vertices)
                _safe_drop_table(cursor, qualified_result_edges)


def join_vertices(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    modification_schema: str,
    modification_vertices_table: str,
    result_schema: str,
    result_vertices_table: str,
    result_attribute_expressions: List[str],
    result_vertices_indexes: List[str],
) -> None:
    """
    Joins two sets of vertices (input and modification) into a result table.

    This method performs a join operation based on the vertex `id`.
    1. It inserts all vertices from `input_vertices_table` that are NOT
       present (by `id`) in the `modification_vertices_table`.
    2. It inserts vertices that ARE present (by `id`) in BOTH tables. For these,
       the `id` is from the input table, and other attributes are calculated
       based on the provided `result_attribute_expressions`.

    Usage of `result_attribute_expressions`:
    - Each string is a SQL expression to calculate a column value.
    - Use alias `a` to refer to columns from `input_vertices_table`.
    - Use alias `b` to refer to columns from `modification_vertices_table`.
    - It's highly recommended that each expression ends with `AS alias_name`.
    - The order of expressions must match the column order of the result table
      (after the 'id' column).

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the primary input vertices table.
    :param input_vertices_table: Name of the primary input vertices table (alias `a`).
    :param modification_schema: Schema of the modification vertices table.
    :param modification_vertices_table: Name of the modification vertices table (alias `b`).
    :param result_schema: Schema for the result table.
    :param result_vertices_table: Name of the table for the joined vertices.
    :param result_attribute_expressions: Ordered list of SQL expressions for
        merged vertex attributes.
    :param result_vertices_indexes: A list of column names for indexes on the
        result table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(modification_schema, "Modification schema cannot be null or empty.")
    _check_not_null_or_empty(
        modification_vertices_table,
        "Modification vertices table name cannot be null or empty.",
    )
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null(result_attribute_expressions, "Result attribute expressions list cannot be null.")
    if not result_attribute_expressions:
        raise SQLException("Argument Error: Result attribute expressions list cannot be empty.")

    # ADDED VALIDATION
    for expr in result_attribute_expressions:
        _check_not_null_or_empty(expr, "Result attribute expression cannot be null or empty.")

    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")

    input_tables = {
        _table_name(input_schema, input_vertices_table),
        _table_name(modification_schema, modification_vertices_table),
    }
    _check_table_conflict(result_schema, result_vertices_table, input_tables)

    result_vertices_name = _table_name(result_schema, result_vertices_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            _create_table_from_template(
                input_schema,
                input_vertices_table,
                result_schema,
                result_vertices_table,
                result_vertices_indexes,
                cursor,
            )

            input_vertices_name = _table_name(input_schema, input_vertices_table)
            mod_vertices_name = _table_name(modification_schema, modification_vertices_table)

            # Insert vertices from input not in modification table
            cursor.execute(
                f"INSERT INTO {result_vertices_name} "
                f"SELECT * FROM {input_vertices_name} "
                f"WHERE id NOT IN (SELECT id FROM {mod_vertices_name})"
            )

            # Insert vertices present in both, applying expressions
            expressions = ", ".join(result_attribute_expressions)
            cursor.execute(
                f"INSERT INTO {result_vertices_name} "
                f"SELECT a.id, {expressions} "
                f"FROM {input_vertices_name} a, {mod_vertices_name} b "
                f"WHERE a.id = b.id"
            )

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_vertices_name)


def map_vertices(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    result_schema: str,
    result_vertices_table: str,
    result_column_expressions: List[str],
    result_vertices_indexes: List[str],
) -> None:
    """
    Transforms vertex attributes from an input table to a new result table.

    This function creates a new table containing vertices with transformed
    attributes based on the data in the input table. The transformation is
    defined by the SQL expressions provided in `result_column_expressions`.

    The mandatory `id` column from the input table is always included as the
    first column in the result.

    Using `result_column_expressions`:
    - Each string defines a column in the `SELECT` list.
    - Expressions can refer to any column in the input vertices table by name.
    - It is *highly recommended* to use an alias for each expression using
      `AS alias_name` to ensure predictable column names in the result table.
    - Do *not* include the `id` column in this list; it is handled automatically.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source vertices table.
    :param input_vertices_table: Name of the source vertices table.
    :param result_schema: Schema for the target vertices table.
    :param result_vertices_table: Name for the target vertices table to create.
    :param result_column_expressions: Ordered list of SQL expressions defining
        the result columns (beyond `id`).
    :param result_vertices_indexes: A list of column names for indexes on the
        result table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null(result_column_expressions, "Result column expressions list cannot be null.")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")

    input_tables = {_table_name(input_schema, input_vertices_table)}
    _check_table_conflict(result_schema, result_vertices_table, input_tables)

    result_vertices_name = _table_name(result_schema, result_vertices_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_vertices_name = _table_name(input_schema, input_vertices_table)

            all_columns = ["id"]
            for expr in result_column_expressions:
                _check_not_null_or_empty(expr, "Result column expression cannot be null or empty.")
                all_columns.append(expr)

            columns_list_str = ", ".join(all_columns)

            create_query = (
                f"CREATE TABLE {result_vertices_name} AS SELECT {columns_list_str} FROM {input_vertices_name} WHERE 1=0"
            )
            cursor.execute(create_query)

            # Create indexes
            for col in result_vertices_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_vertices_name} ("{col}")')

            # Populate table
            insert_query = f"INSERT INTO {result_vertices_name} SELECT {columns_list_str} FROM {input_vertices_name}"
            cursor.execute(insert_query)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_vertices_name)


def map_edges(
    connection: Connection,
    input_schema: str,
    input_edges_table: str,
    result_schema: str,
    result_edges_table: str,
    result_column_expressions: List[str],
    result_edges_indexes: List[str],
) -> None:
    """
    Transforms edge attributes by creating a new edges table based on expressions.

    This method creates a new table with `srcid`, `destid`, and additional
    columns defined by `result_column_expressions`.

    Using `result_column_expressions`:
    - Each string is a SQL expression evaluated against the `input_edges_table`.
    - Expressions can refer to any column in the input edges table by name.
    - Each expression *must* define a result column name using `AS alias_name`.
    - Do *not* include expressions for `srcid` or `destid`; they are handled
      automatically.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source edges table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the target edges table.
    :param result_edges_table: Name for the target edges table to create.
    :param result_column_expressions: List of SQL expressions defining the new
        columns.
    :param result_edges_indexes: A list of column names for indexes on the
        result table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_edges_table, "Result edges table name cannot be null or empty.")
    _check_not_null(result_column_expressions, "Result column expressions list cannot be null.")
    _check_not_null(result_edges_indexes, "Result edges index list cannot be null.")

    input_tables = {_table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_edges_table, input_tables)

    result_edges_name = _table_name(result_schema, result_edges_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_edges_name = _table_name(input_schema, input_edges_table)

            all_columns = ["srcid", "destid"]
            for expr in result_column_expressions:
                _check_not_null_or_empty(expr, "Result column expression cannot be null or empty.")
                all_columns.append(expr)

            columns_list_str = ", ".join(all_columns)

            create_query = (
                f"CREATE TABLE {result_edges_name} AS SELECT {columns_list_str} FROM {input_edges_name} WHERE 1=0"
            )
            cursor.execute(create_query)

            # Create indexes
            for col in result_edges_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                index_name = f"{result_edges_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_edges_name} ("{col}")')

            # Populate table
            insert_query = f"INSERT INTO {result_edges_name} SELECT {columns_list_str} FROM {input_edges_name}"
            cursor.execute(insert_query)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_edges_name)


def map_triplets(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_edges_table: str,
    result_column_expressions: List[str],
    result_edges_indexes: List[str],
) -> None:
    """
    Transforms edge attributes by incorporating information from the source and
    destination vertices (the "triplet").

    This method creates a new edge table based on joining the input edge table
    with the input vertex table for both source and destination vertices.

    Using `result_column_expressions`:
    - Each string is a SQL expression defining a new column.
    - Expressions *must* reference columns using specific aliases:
        - `a`: for the source vertex.
        - `b`: for the edge.
        - `c`: for the destination vertex.
    - It is *highly recommended* that each expression use `AS alias_name` to
      define the result column name.
    - Do *not* include `srcid` or `destid`; they are handled automatically.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the target edges table.
    :param result_edges_table: Name for the target edges table to create.
    :param result_column_expressions: List of SQL expressions defining the new
        columns.
    :param result_edges_indexes: A list of column names for indexes on the
        result table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_edges_table, "Result edges table name cannot be null or empty.")
    _check_not_null(result_column_expressions, "Result column expressions list cannot be null.")
    _check_not_null(result_edges_indexes, "Result edges index list cannot be null.")

    input_tables = {
        _table_name(input_schema, input_vertices_table),
        _table_name(input_schema, input_edges_table),
    }
    _check_table_conflict(result_schema, result_edges_table, input_tables)

    result_edges_name = _table_name(result_schema, result_edges_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_vertices_name = _table_name(input_schema, input_vertices_table)
            input_edges_name = _table_name(input_schema, input_edges_table)

            select_expressions = ["b.srcid", "b.destid"]
            for expr in result_column_expressions:
                _check_not_null_or_empty(expr, "Result column expression cannot be null or empty.")
                select_expressions.append(expr)

            select_list_str = ", ".join(select_expressions)

            from_join_clause = (
                f"FROM {input_vertices_name} a "
                f"JOIN {input_edges_name} b ON a.id = b.srcid "
                f"JOIN {input_vertices_name} c ON c.id = b.destid"
            )

            create_query = f"CREATE TABLE {result_edges_name} AS SELECT {select_list_str} {from_join_clause} WHERE 1=0"
            cursor.execute(create_query)

            # Create indexes
            for col in result_edges_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                index_name = f"{result_edges_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_edges_name} ("{col}")')

            # Populate table
            insert_query = f"INSERT INTO {result_edges_name} SELECT {select_list_str} {from_join_clause}"
            cursor.execute(insert_query)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_edges_name)


def create_triplets_view(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_triplets_view: str,
) -> None:
    """
    Creates a database view representing graph triplets (source vertex, edge,
    destination vertex).

    The view joins the edges table with the vertices table twice (for source
    and destination). It includes all columns from the original edges table,
    plus all columns from the vertices table (except `id`), prefixed with
    `src_` and `dest_` respectively.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the new triplets view.
    :param result_triplets_view: Name for the new view to be created.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_triplets_view, "Result triplets view name cannot be null or empty.")

    input_tables = {
        _table_name(input_schema, input_vertices_table),
        _table_name(input_schema, input_edges_table),
    }
    _check_table_conflict(result_schema, result_triplets_view, input_tables)

    result_triplets_name = _table_name(result_schema, result_triplets_view)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_vertices_name = _table_name(input_schema, input_vertices_table)
            input_edges_name = _table_name(input_schema, input_edges_table)

            # Get vertex columns (excluding id) to build the select list
            cursor.execute(f"SELECT * FROM {input_vertices_name} WHERE 1=0")
            vertex_columns = [col_desc[0] for col_desc in (cursor.description or []) if col_desc[0].lower() != "id"]

            src_columns = [f'a."{col}" AS src_{col}' for col in vertex_columns]
            dest_columns = [f'c."{col}" AS dest_{col}' for col in vertex_columns]

            all_select_list = ["b.*"] + src_columns + dest_columns
            all_columns_str = ", ".join(all_select_list)

            create_view_sql = f"""
                CREATE VIEW {result_triplets_name} AS
                SELECT {all_columns_str}
                FROM {input_edges_name} b
                JOIN {input_vertices_name} a ON b.srcid = a.id
                JOIN {input_vertices_name} c ON b.destid = c.id
            """
            cursor.execute(create_view_sql)
            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_view(cursor, result_triplets_name)


def create_triplets_table(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_triplets_table: str,
    result_triplets_indexes: List[str],
) -> None:
    """
    Creates a materialized triplet table by joining vertex and edge data.

    This method is similar to `create_triplets_view` but creates a physical
    table instead of a view. It includes all columns from the edges table, plus
    prefixed columns (`src_`, `dest_`) for attributes from the source and
    destination vertices.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the new triplets table.
    :param result_triplets_table: Name for the new table to be created.
    :param result_triplets_indexes: List of column names to index in the result.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_triplets_table, "Result triplets table name cannot be null or empty.")
    _check_not_null(result_triplets_indexes, "Result triplets index list cannot be null.")

    input_tables = {
        _table_name(input_schema, input_vertices_table),
        _table_name(input_schema, input_edges_table),
    }
    _check_table_conflict(result_schema, result_triplets_table, input_tables)

    result_triplets_name = _table_name(result_schema, result_triplets_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_vertices_name = _table_name(input_schema, input_vertices_table)
            input_edges_name = _table_name(input_schema, input_edges_table)

            cursor.execute(f"SELECT * FROM {input_vertices_name} WHERE 1=0")
            vertex_columns = [col_desc[0] for col_desc in (cursor.description or []) if col_desc[0].lower() != "id"]

            src_columns = [f'a."{col}" AS src_{col}' for col in vertex_columns]
            dest_columns = [f'c."{col}" AS dest_{col}' for col in vertex_columns]
            all_select_list = ["b.*"] + src_columns + dest_columns
            select_list_str = ", ".join(all_select_list)

            from_join_clause = (
                f"FROM {input_edges_name} b "
                f"JOIN {input_vertices_name} a ON b.srcid = a.id "
                f"JOIN {input_vertices_name} c ON b.destid = c.id"
            )

            create_table_sql = (
                f"CREATE TABLE {result_triplets_name} AS SELECT {select_list_str} {from_join_clause} WHERE 1=0"
            )
            cursor.execute(create_table_sql)

            for col in result_triplets_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                index_name = f"{result_triplets_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_triplets_name} ("{col}")')

            insert_sql = f"INSERT INTO {result_triplets_name} SELECT {select_list_str} {from_join_clause}"
            cursor.execute(insert_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_triplets_name)


def reverse_edges(
    connection: Connection,
    input_schema: str,
    input_edges_table: str,
    result_schema: str,
    result_edges_table: str,
    result_edges_indexes: List[str],
) -> None:
    """
    Reverses the direction of edges stored in a database table.

    Creates a new result table with the same columns as the input table, but
    the values in `srcid` and `destid` are swapped. All other columns are
    copied verbatim.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source edges table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the target table.
    :param result_edges_table: Name for the table with reversed edges.
    :param result_edges_indexes: List of columns to index in the result table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_edges_table, "Result edges table name cannot be null or empty.")
    _check_not_null(result_edges_indexes, "Result edges index list cannot be null.")

    input_tables = {_table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_edges_table, input_tables)

    result_edges_name = _table_name(result_schema, result_edges_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            _create_table_from_template(
                input_schema,
                input_edges_table,
                result_schema,
                result_edges_table,
                result_edges_indexes,
                cursor,
            )

            input_edges_name = _table_name(input_schema, input_edges_table)
            cursor.execute(f"SELECT * FROM {input_edges_name} WHERE 1=0")
            other_columns = [
                desc[0] for desc in (cursor.description or []) if desc[0].lower() not in ("srcid", "destid")
            ]

            other_cols_quoted_str = ", ".join([f'"{c}"' for c in other_columns])
            select_clause = f"destid AS srcid, srcid AS destid"
            if other_cols_quoted_str:
                select_clause += f", {other_cols_quoted_str}"

            target_cols_str = "srcid, destid"
            if other_cols_quoted_str:
                target_cols_str += f", {other_cols_quoted_str}"

            insert_sql = (
                f"INSERT INTO {result_edges_name} ({target_cols_str}) SELECT {select_clause} FROM {input_edges_name}"
            )
            cursor.execute(insert_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_edges_name)


def filter_edges(
    connection: Connection,
    input_schema: str,
    input_edges_table: str,
    result_schema: str,
    result_edges_table: str,
    edge_filter: str,
    result_edges_indexes: List[str],
) -> None:
    """
    Filters edges from a source table into a new result table.

    The `edge_filter` is a standard SQL conditional expression (without the
    `WHERE` keyword) that references columns in the `input_edges_table`.
    Use "1=1" for no filtering.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source edges table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the target table.
    :param result_edges_table: Name for the table with filtered edges.
    :param edge_filter: SQL predicate string to filter edges.
    :param result_edges_indexes: List of columns to index in the result table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_edges_table, "Result edges table name cannot be null or empty.")
    _check_not_null(edge_filter, "Edge filter cannot be null (use '1=1').")
    _check_not_null(result_edges_indexes, "Result edges index list cannot be null.")

    input_tables = {_table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_edges_table, input_tables)

    result_edges_name = _table_name(result_schema, result_edges_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            _create_table_from_template(
                input_schema,
                input_edges_table,
                result_schema,
                result_edges_table,
                result_edges_indexes,
                cursor,
            )

            input_edges_name = _table_name(input_schema, input_edges_table)
            filter_clause = ""
            if edge_filter.strip() and edge_filter.strip() != "1=1":
                filter_clause = f" WHERE {edge_filter}"

            cursor.execute(f"INSERT INTO {result_edges_name} SELECT * FROM {input_edges_name}{filter_clause}")

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_edges_name)


def filter_vertices(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    result_edges_table: str,
    vertex_filter: str,
    result_vertices_indexes: List[str],
    result_edges_indexes: List[str],
) -> None:
    """
    Creates a new subgraph by filtering vertices and retaining their edges.

    Populates `result_vertices_table` with vertices that satisfy `vertex_filter`.
    Then populates `result_edges_table` with edges from `input_edges_table`
    where *both* endpoints are present in the new `result_vertices_table`.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the target tables.
    :param result_vertices_table: Name for the table with filtered vertices.
    :param result_edges_table: Name for the table with corresponding edges.
    :param vertex_filter: SQL predicate string to filter vertices.
    :param result_vertices_indexes: List of columns to index in the result vertices table.
    :param result_edges_indexes: List of columns to index in the result edges table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null_or_empty(result_edges_table, "Result edges table name cannot be null or empty.")
    _check_not_null(vertex_filter, "Vertex filter cannot be null (use '1=1').")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")
    _check_not_null(result_edges_indexes, "Result edges index list cannot be null.")

    input_tables = {_table_name(input_schema, input_vertices_table), _table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_vertices_table, input_tables)
    _check_table_conflict(result_schema, result_edges_table, input_tables)

    result_vertices_name = _table_name(result_schema, result_vertices_table)
    result_edges_name = _table_name(result_schema, result_edges_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            _create_table_from_template(
                input_schema,
                input_vertices_table,
                result_schema,
                result_vertices_table,
                result_vertices_indexes,
                cursor,
            )
            _create_table_from_template(
                input_schema,
                input_edges_table,
                result_schema,
                result_edges_table,
                result_edges_indexes,
                cursor,
            )

            input_vertices_name = _table_name(input_schema, input_vertices_table)
            filter_clause = ""
            if vertex_filter.strip() and vertex_filter.strip() != "1=1":
                filter_clause = f" WHERE {vertex_filter}"

            cursor.execute(f"INSERT INTO {result_vertices_name} SELECT * FROM {input_vertices_name}{filter_clause}")

            input_edges_name = _table_name(input_schema, input_edges_table)
            cursor.execute(
                f"INSERT INTO {result_edges_name} "
                f"SELECT * FROM {input_edges_name} "
                f"WHERE srcid IN (SELECT id FROM {result_vertices_name}) "
                f"AND destid IN (SELECT id FROM {result_vertices_name})"
            )

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_vertices_name)
                _safe_drop_table(cursor, result_edges_name)


def in_degrees(
    connection: Connection,
    input_schema: str,
    input_edges_table: str,
    result_schema: str,
    result_in_degrees_table: str,
    result_indexes: List[str],
) -> None:
    """
    Calculates the in-degree for each destination node in an edge table.

    The result table will contain two columns: `id` (the vertex ID) and
    `in_degree` (the count of incoming edges).

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source edges table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the target table.
    :param result_in_degrees_table: Name for the table with in-degree counts.
    :param result_indexes: List of columns to index ('id' or 'in_degree').
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_in_degrees_table, "Result in-degrees table name cannot be null or empty.")
    _check_not_null(result_indexes, "Result index list cannot be null.")

    input_tables = {_table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_in_degrees_table, input_tables)

    result_table_name = _table_name(result_schema, result_in_degrees_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            create_sql = f"CREATE TABLE {result_table_name} (id BIGINT NOT NULL, in_degree BIGINT NOT NULL)"
            cursor.execute(create_sql)

            for col in result_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                if col.lower() not in ("id", "in_degree"):
                    raise SQLException(f"Argument Error: Invalid index column '{col}' for inDegrees.")
                index_name = f"{result_in_degrees_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_table_name} ("{col}")')

            input_edges_name = _table_name(input_schema, input_edges_table)
            insert_sql = (
                f"INSERT INTO {result_table_name} (id, in_degree) "
                f"SELECT destid AS id, COUNT(*) AS in_degree "
                f"FROM {input_edges_name} "
                f"GROUP BY destid"
            )
            cursor.execute(insert_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_table_name)


def out_degrees(
    connection: Connection,
    input_schema: str,
    input_edges_table: str,
    result_schema: str,
    result_out_degrees_table: str,
    result_indexes: List[str],
) -> None:
    """
    Calculates the out-degree for each source node in an edge table.

    The result table will contain two columns: `id` (the vertex ID) and
    `out_degree` (the count of outgoing edges).

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source edges table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the target table.
    :param result_out_degrees_table: Name for the table with out-degree counts.
    :param result_indexes: List of columns to index ('id' or 'out_degree').
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_out_degrees_table, "Result out-degrees table name cannot be null or empty.")
    _check_not_null(result_indexes, "Result index list cannot be null.")

    input_tables = {_table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_out_degrees_table, input_tables)

    result_table_name = _table_name(result_schema, result_out_degrees_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            create_sql = f"CREATE TABLE {result_table_name} (id BIGINT NOT NULL, out_degree BIGINT NOT NULL)"
            cursor.execute(create_sql)

            for col in result_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                if col.lower() not in ("id", "out_degree"):
                    raise SQLException(f"Argument Error: Invalid index column '{col}' for outDegrees.")
                index_name = f"{result_out_degrees_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_table_name} ("{col}")')

            input_edges_name = _table_name(input_schema, input_edges_table)
            insert_sql = (
                f"INSERT INTO {result_table_name} (id, out_degree) "
                f"SELECT srcid AS id, COUNT(*) AS out_degree "
                f"FROM {input_edges_name} "
                f"GROUP BY srcid"
            )
            cursor.execute(insert_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_table_name)


def degrees(
    connection: Connection,
    input_schema: str,
    input_edges_table: str,
    result_schema: str,
    result_degrees_table: str,
    result_indexes: List[str],
) -> None:
    """
    Calculates the total degree (in + out) for each node in an edge table.

    The result table will contain two columns: `id` (the vertex ID) and
    `degree` (the total count of incident edges).

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source edges table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the target table.
    :param result_degrees_table: Name for the table with total degree counts.
    :param result_indexes: List of columns to index ('id' or 'degree').
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_degrees_table, "Result degrees table name cannot be null or empty.")
    _check_not_null(result_indexes, "Result index list cannot be null.")

    input_tables = {_table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_degrees_table, input_tables)

    result_table_name = _table_name(result_schema, result_degrees_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            create_sql = f"CREATE TABLE {result_table_name} (id BIGINT NOT NULL, degree BIGINT NOT NULL)"
            cursor.execute(create_sql)

            for col in result_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                if col.lower() not in ("id", "degree"):
                    raise SQLException(f"Argument Error: Invalid index column '{col}' for degrees.")
                index_name = f"{result_degrees_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_table_name} ("{col}")')

            input_edges_name = _table_name(input_schema, input_edges_table)
            insert_sql = f"""
                INSERT INTO {result_table_name} (id, degree)
                SELECT id, COUNT(*) AS degree FROM (
                    SELECT srcid AS id FROM {input_edges_name}
                    UNION ALL
                    SELECT destid AS id FROM {input_edges_name}
                ) combined_ids GROUP BY id
            """
            cursor.execute(insert_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_table_name)


def from_edges(
    connection: Connection,
    input_schema: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    result_column_expressions: List[str],
    result_vertices_indexes: List[str],
) -> None:
    """
    Creates a vertices table from an existing edges table by extracting
    unique source and destination IDs.

    Using `result_column_expressions`:
    - Expressions can define additional columns in the result table.
    - The unique vertex ID is available within expressions via the alias `ids.id`.
    - Each expression *must* use `AS alias_name` to name the result column.
    - Example: `["ids.id % 100 AS bucket_id"]`

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source edges table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the target vertices table.
    :param result_vertices_table: Name for the target vertices table.
    :param result_column_expressions: List of SQL expressions for additional columns.
    :param result_vertices_indexes: List of columns to index in the result table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null(result_column_expressions, "Result column expressions list cannot be null.")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")

    input_tables = {_table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_vertices_table, input_tables)

    result_vertices_name = _table_name(result_schema, result_vertices_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_edges_name = _table_name(input_schema, input_edges_table)
            id_sub_query = (
                f"(SELECT srcid AS id FROM {input_edges_name} "
                f"UNION DISTINCT SELECT destid AS id FROM {input_edges_name}) ids"
            )

            columns_builder = ["ids.id"]
            for expr in result_column_expressions:
                _check_not_null_or_empty(expr, "Result column expression cannot be null or empty.")
                columns_builder.append(expr)
            columns_list_str = ", ".join(columns_builder)

            create_sql = (
                f"CREATE TABLE {result_vertices_name} AS SELECT {columns_list_str} FROM {id_sub_query} WHERE 1=0"
            )
            cursor.execute(create_sql)

            for col in result_vertices_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_vertices_name} ("{col}")')

            insert_sql = f"INSERT INTO {result_vertices_name} SELECT {columns_list_str} FROM {id_sub_query}"
            cursor.execute(insert_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_vertices_name)


def inner_join_vertices(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    other_schema: str,
    other_vertices_table: str,
    result_schema: str,
    result_vertices_table: str,
    result_column_expressions: List[str],
    result_vertices_indexes: List[str],
) -> None:
    """
    Performs an SQL INNER JOIN between two vertex tables on their 'id' columns.

    Using `result_column_expressions`:
    - The `id` column from the first table is always included.
    - Each string defines an additional column in the `SELECT` list.
    - Use alias `a` for columns from `input_vertices_table`.
    - Use alias `b` for columns from `other_vertices_table`.
    - It is highly recommended to use `AS alias_name` for each expression.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the first (left) vertices table.
    :param input_vertices_table: Name of the first vertices table (alias `a`).
    :param other_schema: Schema of the second (right) vertices table.
    :param other_vertices_table: Name of the second vertices table (alias `b`).
    :param result_schema: Schema for the result table.
    :param result_vertices_table: Name for the table with join results.
    :param result_column_expressions: List of SQL expressions for result columns.
    :param result_vertices_indexes: List of columns to index in the result table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(other_schema, "Other schema cannot be null or empty.")
    _check_not_null_or_empty(other_vertices_table, "Other vertices table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null(result_column_expressions, "Result column expressions list cannot be null.")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")

    input_tables = {
        _table_name(input_schema, input_vertices_table),
        _table_name(other_schema, other_vertices_table),
    }
    _check_table_conflict(result_schema, result_vertices_table, input_tables)

    result_vertices_name = _table_name(result_schema, result_vertices_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_vertices_name = _table_name(input_schema, input_vertices_table)
            other_vertices_name = _table_name(other_schema, other_vertices_table)

            all_columns = ["a.id"]
            for expr in result_column_expressions:
                _check_not_null_or_empty(expr, "Result column expression cannot be null or empty.")
                all_columns.append(expr)

            columns_list_str = ", ".join(all_columns)

            from_join_clause = f"FROM {input_vertices_name} a INNER JOIN {other_vertices_name} b ON a.id = b.id"

            create_sql = (
                f"CREATE TABLE {result_vertices_name} AS SELECT {columns_list_str} {from_join_clause} WHERE 1=0"
            )
            cursor.execute(create_sql)

            for col in result_vertices_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_vertices_name} ("{col}")')

            insert_sql = f"INSERT INTO {result_vertices_name} SELECT {columns_list_str} {from_join_clause}"
            cursor.execute(insert_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_vertices_name)


def outer_join_vertices(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    other_schema: str,
    other_vertices_table: str,
    result_schema: str,
    result_vertices_table: str,
    result_column_expressions: List[str],
    result_vertices_indexes: List[str],
) -> None:
    """
    Performs a LEFT OUTER JOIN between two vertex tables on their 'id' columns.

    All rows from the left table (`input_vertices_table`) are included.
    If a row has no match in the right table, columns from the right table
    will be NULL.

    Using `result_column_expressions`:
    - The `id` column from the first table is always included.
    - Use alias `a` for columns from `input_vertices_table` (left).
    - Use alias `b` for columns from `other_vertices_table` (right).
    - It is highly recommended to use `AS alias_name` for each expression.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the first (left) vertices table.
    :param input_vertices_table: Name of the first vertices table (alias `a`).
    :param other_schema: Schema of the second (right) vertices table.
    :param other_vertices_table: Name of the second vertices table (alias `b`).
    :param result_schema: Schema for the result table.
    :param result_vertices_table: Name for the table with join results.
    :param result_column_expressions: List of SQL expressions for result columns.
    :param result_vertices_indexes: List of columns to index in the result table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(other_schema, "Other schema cannot be null or empty.")
    _check_not_null_or_empty(other_vertices_table, "Other vertices table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null(result_column_expressions, "Result column expressions list cannot be null.")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")

    input_tables = {
        _table_name(input_schema, input_vertices_table),
        _table_name(other_schema, other_vertices_table),
    }
    _check_table_conflict(result_schema, result_vertices_table, input_tables)

    result_vertices_name = _table_name(result_schema, result_vertices_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_vertices_name = _table_name(input_schema, input_vertices_table)
            other_vertices_name = _table_name(other_schema, other_vertices_table)

            all_columns = ["a.id"]
            for expr in result_column_expressions:
                _check_not_null_or_empty(expr, "Result column expression cannot be null or empty.")
                all_columns.append(expr)

            columns_list_str = ", ".join(all_columns)

            from_join_clause = f"FROM {input_vertices_name} a LEFT JOIN {other_vertices_name} b ON a.id = b.id"

            create_sql = (
                f"CREATE TABLE {result_vertices_name} AS SELECT {columns_list_str} {from_join_clause} WHERE 1=0"
            )
            cursor.execute(create_sql)

            for col in result_vertices_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_vertices_name} ("{col}")')

            insert_sql = f"INSERT INTO {result_vertices_name} SELECT {columns_list_str} {from_join_clause}"
            cursor.execute(insert_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_vertices_name)


def mask(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    other_schema: str,
    other_vertices_table: str,
    other_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    result_edges_table: str,
    result_vertices_indexes: List[str],
    result_edges_indexes: List[str],
) -> None:
    """
    Creates a subgraph by retaining elements from an input graph that are
    also present in an 'other' graph.

    - Vertices from the input graph are kept if an ID match is found in the
      'other' vertex table.
    - Edges are kept if a (srcid, destid) match is found in the 'other' edge
      table AND both endpoints exist in the new result vertex table.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the primary input graph.
    :param input_vertices_table: Vertices table of the primary graph.
    :param input_edges_table: Edges table of the primary graph.
    :param other_schema: Schema of the masking ('other') graph.
    :param other_vertices_table: Vertices table of the masking graph.
    :param other_edges_table: Edges table of the masking graph.
    :param result_schema: Schema for the result subgraph tables.
    :param result_vertices_table: Name for the result vertices table.
    :param result_edges_table: Name for the result edges table.
    :param result_vertices_indexes: List of columns to index in the result vertices.
    :param result_edges_indexes: List of columns to index in the result edges.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table cannot be null or empty.")
    _check_not_null_or_empty(other_schema, "Other schema cannot be null or empty.")
    _check_not_null_or_empty(other_vertices_table, "Other vertices table cannot be null or empty.")
    _check_not_null_or_empty(other_edges_table, "Other edges table cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table cannot be null or empty.")
    _check_not_null_or_empty(result_edges_table, "Result edges table cannot be null or empty.")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")
    _check_not_null(result_edges_indexes, "Result edges index list cannot be null.")

    input_v = _table_name(input_schema, input_vertices_table)
    input_e = _table_name(input_schema, input_edges_table)
    other_v = _table_name(other_schema, other_vertices_table)
    other_e = _table_name(other_schema, other_edges_table)
    result_v = _table_name(result_schema, result_vertices_table)
    result_e = _table_name(result_schema, result_edges_table)

    source_tables = {input_v, input_e, other_v, other_e}
    _check_table_conflict(result_schema, result_vertices_table, source_tables)
    _check_table_conflict(result_schema, result_edges_table, source_tables)

    operation_successful = False

    with connection.cursor() as cursor:
        try:
            _create_table_from_template(
                input_schema,
                input_vertices_table,
                result_schema,
                result_vertices_table,
                result_vertices_indexes,
                cursor,
            )
            _create_table_from_template(
                input_schema, input_edges_table, result_schema, result_edges_table, result_edges_indexes, cursor
            )

            populate_v_sql = f"INSERT INTO {result_v} SELECT v.* FROM {input_v} v JOIN {other_v} o ON v.id = o.id"
            cursor.execute(populate_v_sql)

            populate_e_sql = f"""
                INSERT INTO {result_e}
                SELECT e.* FROM {input_e} e
                INNER JOIN {other_e} oe ON e.srcid = oe.srcid AND e.destid = oe.destid
                WHERE EXISTS (SELECT 1 FROM {result_v} rv_src WHERE rv_src.id = e.srcid)
                  AND EXISTS (SELECT 1 FROM {result_v} rv_dst WHERE rv_dst.id = e.destid)
            """
            cursor.execute(populate_e_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_v)
                _safe_drop_table(cursor, result_e)


def group_edges(
    connection: Connection,
    input_schema: str,
    input_edges_table: str,
    result_schema: str,
    result_edges_table: str,
    result_column_expressions: List[str],
    result_edges_indexes: List[str],
) -> None:
    """
    Groups duplicate edges from an input table into a new result table
    using SQL aggregation.

    The result table contains unique (srcid, destid) pairs.

    Using `result_column_expressions`:
    - Each expression computes an additional column for the result table.
    - Each expression *must* use an SQL aggregate function (e.g., COUNT, SUM,
      AVG, MIN, MAX) on columns from the input table.
    - Each expression *must* include an `AS alias_name` clause to name the
      resulting column.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source edges table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the target table.
    :param result_edges_table: Name for the table with grouped edges.
    :param result_column_expressions: List of SQL aggregate expressions.
    :param result_edges_indexes: List of columns to index in the result table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_edges_table, "Result edges table name cannot be null or empty.")
    _check_not_null(result_column_expressions, "Result column expressions list cannot be null.")
    _check_not_null(result_edges_indexes, "Result edges index list cannot be null.")

    input_tables = {_table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_edges_table, input_tables)

    result_edges_name = _table_name(result_schema, result_edges_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_edges_name = _table_name(input_schema, input_edges_table)

            columns_builder = ["srcid", "destid"]
            for expr in result_column_expressions:
                _check_not_null_or_empty(expr, "Result column expression cannot be null or empty.")
                columns_builder.append(expr)
            columns_list_str = ", ".join(columns_builder)

            create_query = (
                f"CREATE TABLE {result_edges_name} AS "
                f"SELECT {columns_list_str} FROM {input_edges_name} "
                f"GROUP BY srcid, destid HAVING 1=0"
            )
            cursor.execute(create_query)

            for col in result_edges_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                index_name = f"{result_edges_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_edges_name} ("{col}")')

            insert_query = (
                f"INSERT INTO {result_edges_name} "
                f"SELECT {columns_list_str} FROM {input_edges_name} "
                f"GROUP BY srcid, destid"
            )
            cursor.execute(insert_query)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_edges_name)


def aggregate_messages(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    send_to_source_expr: Optional[str],
    send_to_dest_expr: Optional[str],
    aggregate_expr: str,
    result_vertices_indexes: List[str],
) -> None:
    """
    Aggregates messages passed between connected vertices in a graph.

    This method simulates a message-passing process. For each edge, messages
    are generated via `send_to_source_expr` and `send_to_dest_expr`. These
    messages are then grouped by target vertex and combined using `aggregate_expr`.

    Expression Aliases:
    - In `send_..._expr`, use `a` for source vertex, `b` for edge, `c` for dest vertex.
    - In `aggregate_expr`, operate on the generated message column, which is
      internally named `msg` (e.g., `SUM(msg)`).
    - It is recommended to alias the result of `aggregate_expr` (e.g.,
      `SUM(msg) AS total_value`). If no alias is given, the result column
      is named `aggregated_message`.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the result table.
    :param result_vertices_table: Name for the table with aggregated messages.
    :param send_to_source_expr: SQL expression for the message sent to the source vertex.
    :param send_to_dest_expr: SQL expression for the message sent to the destination vertex.
    :param aggregate_expr: SQL aggregate expression to combine messages (e.g., 'SUM(msg)').
    :param result_vertices_indexes: List of columns to index in the result table.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null_or_empty(aggregate_expr, "Aggregate expression cannot be null or empty.")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")

    send_source = send_to_source_expr and send_to_source_expr.strip()
    send_dest = send_to_dest_expr and send_to_dest_expr.strip()
    if not send_source and not send_dest:
        raise SQLException("Argument Error: At least one of send_to_source_expr or send_to_dest_expr must be provided.")

    aggregate_alias = "aggregated_message"
    agg_parts = aggregate_expr.lower().split(" as ")
    if len(agg_parts) > 1:
        aggregate_alias = agg_parts[-1].strip()

    current_agg_expr = aggregate_expr
    if f" as {aggregate_alias}" not in aggregate_expr.lower():
        current_agg_expr = f"{aggregate_expr} AS {aggregate_alias}"

    input_tables = {
        _table_name(input_schema, input_vertices_table),
        _table_name(input_schema, input_edges_table),
    }
    _check_table_conflict(result_schema, result_vertices_table, input_tables)

    result_vertices_name = _table_name(result_schema, result_vertices_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_v = _table_name(input_schema, input_vertices_table)
            input_e = _table_name(input_schema, input_edges_table)

            messages_sql_parts = []
            from_join_clause = (
                f"FROM {input_v} a JOIN {input_e} b ON a.id = b.srcid JOIN {input_v} c ON b.destid = c.id"
            )

            if send_source:
                messages_sql_parts.append(
                    f"SELECT b.srcid AS id, ({send_to_source_expr}) AS msg {from_join_clause} WHERE ({send_to_source_expr}) IS NOT NULL"
                )
            if send_dest:
                messages_sql_parts.append(
                    f"SELECT b.destid AS id, ({send_to_dest_expr}) AS msg {from_join_clause} WHERE ({send_to_dest_expr}) IS NOT NULL"
                )

            messages_sql = " UNION ALL ".join(messages_sql_parts)

            create_sql = (
                f"CREATE TABLE {result_vertices_name} AS "
                f"SELECT id, {current_agg_expr} FROM ({messages_sql}) msgs "
                "GROUP BY id HAVING 1=0"
            )
            cursor.execute(create_sql)

            for col in result_vertices_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                if col.lower() not in ("id", aggregate_alias.lower()):
                    raise SQLException(
                        f"Argument Error: Invalid index column '{col}'. Must be 'id' or '{aggregate_alias}'."
                    )
                index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_vertices_name} ("{col}")')

            insert_sql = (
                f"INSERT INTO {result_vertices_name} (id, {aggregate_alias}) "
                f"SELECT id, {current_agg_expr} FROM ({messages_sql}) msgs "
                "GROUP BY id"
            )
            cursor.execute(insert_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_vertices_name)


def collect_neighbors(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    direction: EdgeDirection,
    result_vertices_indexes: List[str],
) -> None:
    """
    Collects neighbor information for each vertex and stores the results
    (as an array of tuples) in a new table.

    The result table will contain `id` (the source vertex) and `neighbors`
    (an array of tuples, where each tuple represents a neighbor vertex and
    contains all of its attributes).

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the result table.
    :param result_vertices_table: Name for the table with neighbor arrays.
    :param direction: The direction of edges to follow (IN, OUT, or BOTH).
    :param result_vertices_indexes: List of columns to index ('id' or 'neighbors').
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null(direction, "Edge direction cannot be null.")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")

    input_tables = {_table_name(input_schema, input_vertices_table), _table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_vertices_table, input_tables)

    result_vertices_name = _table_name(result_schema, result_vertices_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_v = _table_name(input_schema, input_vertices_table)
            input_e = _table_name(input_schema, input_edges_table)

            cursor.execute(f"SELECT * FROM {input_v} WHERE 1=0")
            neighbor_vertex_cols = [f'n."{c[0]}"' for c in (cursor.description or []) if c[0].lower() != "id"]

            tuple_cols = ["n.id"] + neighbor_vertex_cols
            tuple_expr = f"TUPLE({', '.join(tuple_cols)})"
            tuple_alias = "neighbor_tuple"
            result_col_name = "neighbors"
            group_by_col = "vertex_id"

            if direction == EdgeDirection.IN:
                base_query = (
                    f"SELECT e.destid AS {group_by_col}, {tuple_expr} AS {tuple_alias} "
                    f"FROM {input_v} v JOIN {input_e} e ON e.destid = v.id JOIN {input_v} n ON e.srcid = n.id"
                )
            elif direction == EdgeDirection.OUT:
                base_query = (
                    f"SELECT e.srcid AS {group_by_col}, {tuple_expr} AS {tuple_alias} "
                    f"FROM {input_v} v JOIN {input_e} e ON e.srcid = v.id JOIN {input_v} n ON e.destid = n.id"
                )
            elif direction == EdgeDirection.BOTH:
                out_part = f"(SELECT e.srcid AS {group_by_col}, {tuple_expr} AS {tuple_alias} FROM {input_v} v JOIN {input_e} e ON e.srcid = v.id JOIN {input_v} n ON e.destid = n.id)"
                in_part = f"(SELECT e.destid AS {group_by_col}, {tuple_expr} AS {tuple_alias} FROM {input_v} v JOIN {input_e} e ON e.destid = v.id JOIN {input_v} n ON e.srcid = n.id)"
                # FIXED: Use UNION ALL to preserve duplicates
                base_query = f"{out_part} UNION ALL {in_part}"
            else:
                raise SQLException("Internal Error: Invalid edge direction.")

            create_sql = (
                f"CREATE TABLE {result_vertices_name} AS "
                f"SELECT {group_by_col} AS id, ARRAY_AGG({tuple_alias}) AS {result_col_name} "
                f"FROM ({base_query}) subquery GROUP BY {group_by_col} HAVING 1=0"
            )
            cursor.execute(create_sql)

            for col in result_vertices_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                if col.lower() not in ("id", result_col_name.lower()):
                    raise SQLException(
                        f"Argument Error: Invalid index column '{col}'. Must be 'id' or '{result_col_name}'."
                    )
                index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_vertices_name} ("{col}")')

            insert_sql = (
                f"INSERT INTO {result_vertices_name} (id, {result_col_name}) "
                f"SELECT {group_by_col} AS id, ARRAY_AGG({tuple_alias}) "
                f"FROM ({base_query}) subquery GROUP BY {group_by_col}"
            )
            cursor.execute(insert_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_vertices_name)


def collect_edges(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    direction: EdgeDirection,
    result_vertices_indexes: List[str],
) -> None:
    """
    Collects edge information for each vertex and stores the results
    (as an array of tuples) in a new table.

    The result table will contain `id` (the vertex) and `edges` (an array of
    tuples, where each tuple represents a connected edge and contains all of
    its attributes).

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the result table.
    :param result_vertices_table: Name for the table with edge arrays.
    :param direction: The direction of edges to follow (IN, OUT, or BOTH).
    :param result_vertices_indexes: List of columns to index ('id' or 'edges').
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null(direction, "Edge direction cannot be null.")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")

    input_tables = {_table_name(input_schema, input_vertices_table), _table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_vertices_table, input_tables)

    result_vertices_name = _table_name(result_schema, result_vertices_table)
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            input_v = _table_name(input_schema, input_vertices_table)
            input_e = _table_name(input_schema, input_edges_table)

            cursor.execute(f"SELECT * FROM {input_e} WHERE 1=0")
            edge_cols_list = [f'e."{c[0]}"' for c in (cursor.description or [])]
            if not edge_cols_list:
                raise SQLException(f"Input edges table '{input_e}' has no columns.")

            edge_tuple_expr = f"TUPLE({', '.join(edge_cols_list)})"
            edge_tuple_alias = "edge_tuple"
            result_col_name = "edges"
            group_by_col = "vertex_id"

            if direction == EdgeDirection.IN:
                base_query = f"SELECT e.destid AS {group_by_col}, {edge_tuple_expr} AS {edge_tuple_alias} FROM {input_v} v JOIN {input_e} e ON e.destid = v.id"
            elif direction == EdgeDirection.OUT:
                base_query = f"SELECT e.srcid AS {group_by_col}, {edge_tuple_expr} AS {edge_tuple_alias} FROM {input_v} v JOIN {input_e} e ON e.srcid = v.id"
            elif direction == EdgeDirection.BOTH:
                out_part = f"(SELECT e.srcid AS {group_by_col}, {edge_tuple_expr} AS {edge_tuple_alias} FROM {input_v} v JOIN {input_e} e ON e.srcid = v.id)"
                in_part = f"(SELECT e.destid AS {group_by_col}, {edge_tuple_expr} AS {edge_tuple_alias} FROM {input_v} v JOIN {input_e} e ON e.destid = v.id)"
                # FIXED: Use UNION ALL to preserve duplicates
                base_query = f"{out_part} UNION ALL {in_part}"
            else:
                raise SQLException("Internal Error: Invalid edge direction.")

            create_sql = (
                f"CREATE TABLE {result_vertices_name} AS "
                f"SELECT {group_by_col} AS id, ARRAY_AGG({edge_tuple_alias}) AS {result_col_name} "
                f"FROM ({base_query}) subquery GROUP BY {group_by_col} HAVING 1=0"
            )
            cursor.execute(create_sql)

            for col in result_vertices_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                if col.lower() not in ("id", result_col_name.lower()):
                    raise SQLException(
                        f"Argument Error: Invalid index column '{col}'. Must be 'id' or '{result_col_name}'."
                    )
                index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_vertices_name} ("{col}")')

            insert_sql = (
                f"INSERT INTO {result_vertices_name} (id, {result_col_name}) "
                f"SELECT {group_by_col} AS id, ARRAY_AGG({edge_tuple_alias}) "
                f"FROM ({base_query}) subquery GROUP BY {group_by_col}"
            )
            cursor.execute(insert_sql)

            operation_successful = True
        finally:
            if not operation_successful:
                _safe_drop_table(cursor, result_vertices_name)


def label_propagation(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    max_iterations: int,
    result_vertices_indexes: List[str],
) -> None:
    """
    Performs the Label Propagation Algorithm (LPA) iteratively to find communities.

    The algorithm initializes each vertex's label to its own ID. Then, for a
    specified number of iterations, each vertex updates its label to the most
    frequent label among its neighbors. Ties are broken by choosing the
    numerically smaller label ID.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the result and temporary tables.
    :param result_vertices_table: Name for the table with final vertex labels.
    :param max_iterations: The maximum number of iterations to perform.
    :param result_vertices_indexes: List of columns to index ('id' or 'label').
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_positive(max_iterations, "Maximum iterations must be >= 1.")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")

    input_tables = {_table_name(input_schema, input_vertices_table), _table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_vertices_table, input_tables)

    result_vertices_name = _table_name(result_schema, result_vertices_table)
    temp_base_name = f"lpa_temp_{uuid.uuid4().hex[:8]}"
    current_table = _table_name(result_schema, f"{temp_base_name}_iter0")

    temp_tables_created = []
    operation_successful = False

    with connection.cursor() as cursor:
        try:
            # Initial step (Iteration 0)
            input_vertices_name = _table_name(input_schema, input_vertices_table)
            initial_sql = f"CREATE TABLE {current_table} AS SELECT id, id AS label FROM {input_vertices_name}"
            cursor.execute(initial_sql)
            temp_tables_created.append(current_table)

            input_edges_name = _table_name(input_schema, input_edges_table)

            for i in range(max_iterations):
                is_last_iteration = i == max_iterations - 1
                next_table = (
                    result_vertices_name
                    if is_last_iteration
                    else _table_name(result_schema, f"{temp_base_name}_iter{i + 1}")
                )

                # This CTE-based query finds the most frequent neighbor label for each vertex
                new_labels_sql = f"""
                    WITH neighbors AS (
                        SELECT e.srcid AS vertex, e.destid AS neighbor FROM {input_edges_name} e
                        UNION ALL
                        SELECT e.destid AS vertex, e.srcid AS neighbor FROM {input_edges_name} e
                    ), neighbor_labels AS (
                        SELECT n.vertex, l.label FROM neighbors n JOIN {current_table} l ON n.neighbor = l.id
                    ), label_counts AS (
                        SELECT vertex, label, COUNT(*) AS cnt FROM neighbor_labels GROUP BY vertex, label
                    ), ranked_labels AS (
                        SELECT vertex, label, ROW_NUMBER() OVER (PARTITION BY vertex ORDER BY cnt DESC, label ASC) AS rn FROM label_counts
                    ), preferred_new_labels AS (
                        SELECT vertex AS id, label FROM ranked_labels WHERE rn = 1
                    )
                    SELECT ct.id, COALESCE(pnl.label, ct.label) AS label
                    FROM {current_table} ct LEFT JOIN preferred_new_labels pnl ON ct.id = pnl.id
                """

                if is_last_iteration:
                    cursor.execute(f"CREATE TABLE {next_table} (id BIGINT NOT NULL, label BIGINT)")

                    for col in result_vertices_indexes:
                        _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                        if col.lower() not in ("id", "label"):
                            raise SQLException(
                                f"Argument Error: Invalid index column '{col}'. Must be 'id' or 'label'."
                            )
                        index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                        cursor.execute(f'CREATE INDEX "{index_name}" ON {next_table} ("{col}")')

                    cursor.execute(f"INSERT INTO {next_table} (id, label) {new_labels_sql}")
                else:
                    cursor.execute(f"CREATE TABLE {next_table} AS {new_labels_sql}")
                    temp_tables_created.append(next_table)

                current_table = next_table

            operation_successful = True
        finally:
            for temp_table in temp_tables_created:
                if temp_table != result_vertices_name or not operation_successful:
                    _safe_drop_table(cursor, temp_table)
            if not operation_successful:
                _safe_drop_table(cursor, result_vertices_name)


class TriangleCount:
    """
    Provides utility methods for performing Triangle Counting operations.
    """

    @staticmethod
    def run(
        connection: Connection,
        input_schema: str,
        input_vertices_table: str,
        input_edges_table: str,
        result_schema: str,
        result_vertices_table: str,
        result_vertices_indexes: List[str],
    ) -> None:
        """
        Runs the full triangle counting process.

        This handles creating a temporary table for canonical edges (where srcid <
        destid, and duplicates/self-loops are removed), executing the core
        counting logic, and cleaning up.

        :param connection: The pyocient Connection object.
        :param input_schema: Schema of the source graph tables.
        :param input_vertices_table: Name of the source vertices table.
        :param input_edges_table: Name of the source edges table.
        :param result_schema: Schema for the result table.
        :param result_vertices_table: Name for the table with triangle counts.
        :param result_vertices_indexes: List of columns to index ('id' or 'triangle_count').
        :raises SQLException: If any database error occurs.
        """
        _check_not_null(connection, "Connection cannot be null.")

        canonical_edges_temp_name = f"tc_canon_{uuid.uuid4().hex[:8]}"
        # Create temp table in the result schema for permissions reasons
        canonical_edges_qualified_name = _table_name(result_schema, canonical_edges_temp_name)

        with connection.cursor() as cursor:
            try:
                # Store edges with srcid < destid, remove self-loops and duplicates
                qualified_input_edges = _table_name(input_schema, input_edges_table)
                cursor.execute(f"""
                    CREATE TABLE {canonical_edges_qualified_name} AS
                    SELECT
                        CASE WHEN srcid < destid THEN srcid ELSE destid END AS srcid,
                        CASE WHEN srcid < destid THEN destid ELSE srcid END AS destid
                    FROM {qualified_input_edges}
                    WHERE srcid != destid
                    GROUP BY 1, 2
                """)

                # Run the core logic on the canonicalized edges
                TriangleCount.run_pre_canonicalized(
                    connection,
                    input_schema,
                    input_vertices_table,
                    result_schema,  # Use result_schema for temp table
                    canonical_edges_temp_name,
                    result_schema,
                    result_vertices_table,
                    result_vertices_indexes,
                )
            finally:
                _safe_drop_table(cursor, canonical_edges_qualified_name)

    @staticmethod
    def run_pre_canonicalized(
        connection: Connection,
        input_schema: str,
        input_vertices_table: str,
        canonical_edges_schema: str,
        canonical_edges_table: str,
        result_schema: str,
        result_vertices_table: str,
        result_vertices_indexes: List[str],
    ) -> None:
        """
        Runs triangle count on a graph with pre-canonicalized edges.

        Assumes edges are already directed (srcid < destid) with no duplicates
        or self-loops.
        """
        _check_not_null_or_empty(canonical_edges_table, "Canonical edges table cannot be null or empty.")

        result_vertices_name = _table_name(result_schema, result_vertices_table)
        operation_successful = False

        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    f"CREATE TABLE {result_vertices_name} (id BIGINT NOT NULL, triangle_count BIGINT NOT NULL)"
                )

                for col in result_vertices_indexes:
                    if col.lower() not in ("id", "triangle_count"):
                        raise SQLException(
                            f"Argument Error: Invalid index column '{col}'. Must be 'id' or 'triangle_count'."
                        )
                    index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                    cursor.execute(f'CREATE INDEX "{index_name}" ON {result_vertices_name} ("{col}")')

                qualified_input_vertices = _table_name(input_schema, input_vertices_table)
                qualified_canonical_edges = _table_name(canonical_edges_schema, canonical_edges_table)

                insert_sql = f"""
                    INSERT INTO {result_vertices_name} (id, triangle_count)
                    WITH triangles AS (
                        SELECT e1.srcid AS a, e1.destid AS b, e2.destid AS c
                        FROM {qualified_canonical_edges} e1
                        JOIN {qualified_canonical_edges} e2 ON e1.destid = e2.srcid
                    ), closed_triangles AS (
                        SELECT t.a, t.b, t.c FROM triangles t
                        JOIN {qualified_canonical_edges} e3 ON t.a = e3.srcid AND t.c = e3.destid
                    ), vertex_counts AS (
                        SELECT a AS vertex, COUNT(*) AS cnt FROM closed_triangles GROUP BY a
                        UNION ALL
                        SELECT b AS vertex, COUNT(*) AS cnt FROM closed_triangles GROUP BY b
                        UNION ALL
                        SELECT c AS vertex, COUNT(*) AS cnt FROM closed_triangles GROUP BY c
                    ), aggregated_counts AS (
                        SELECT vertex, SUM(cnt) as total_count FROM vertex_counts GROUP BY vertex
                    )
                    SELECT v.id, COALESCE(agg.total_count, 0) AS triangle_count
                    FROM {qualified_input_vertices} v
                    LEFT JOIN aggregated_counts agg ON v.id = agg.vertex
                """
                cursor.execute(insert_sql)
                operation_successful = True
            finally:
                if not operation_successful:
                    _safe_drop_table(cursor, result_vertices_name)


def pregel(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    initializer_expr: str,
    send_to_source_expr: Optional[str],
    send_to_dest_expr: Optional[str],
    aggregate_expr: str,
    updater_expr: str,
    max_iterations: int,
    result_vertices_indexes: List[str],
) -> None:
    """
    Performs a Pregel-like graph computation using SQL.

    This method implements a vertex-centric graph processing algorithm. It
    iteratively computes vertex states based on messages passed along edges.

    Important Note on Expressions and Aliases:
    - initializer_expr: Computes the starting 'state' for each vertex. Can
      reference any column from `input_vertices_table`.
    - send_to_..._expr: Computes a message. MUST use aliases:
        - `a`: for the source vertex's current state row (`id`, `state`).
        - `b`: for the edge table row (`srcid`, `destid`, ...).
        - `c`: for the destination vertex's current state row (`id`, `state`).
      Return NULL to not send a message. Computation terminates early if all
      send expressions for an iteration return NULL.
    - aggregate_expr: Combines incoming messages. MUST operate on the `msg`
      column (e.g., `SUM(msg)`). The result is aliased as `aggregated_message`.
    - updater_expr: Computes the next state. MUST use aliases:
        - `s`: for the vertex's current state row (`id`, `state`).
        - `m`: for the aggregated messages row (`id`, `aggregated_message`).
          `m.aggregated_message` will be NULL if no messages were received.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the result and temporary tables.
    :param result_vertices_table: Name for the table with final vertex states.
    :param initializer_expr: SQL expression for the initial vertex state.
    :param send_to_source_expr: SQL expression for messages sent to the source.
    :param send_to_dest_expr: SQL expression for messages sent to the destination.
    :param aggregate_expr: SQL aggregate expression to combine messages.
    :param updater_expr: SQL expression to compute the next vertex state.
    :param max_iterations: The maximum number of iterations to perform.
    :param result_vertices_indexes: List of columns to index ('id' or 'result').
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null_or_empty(initializer_expr, "Initializer expression cannot be null or empty.")
    _check_not_null_or_empty(aggregate_expr, "Aggregate expression cannot be null or empty.")
    _check_not_null_or_empty(updater_expr, "Updater expression cannot be null or empty.")
    _check_positive(max_iterations, "Maximum iterations must be >= 1.")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")

    send_source = send_to_source_expr and send_to_source_expr.strip()
    send_dest = send_to_dest_expr and send_to_dest_expr.strip()

    current_initializer_expr = initializer_expr
    if " as state" not in initializer_expr.lower().strip():
        current_initializer_expr += " AS state"

    aggregate_alias = "aggregated_message"
    current_aggregate_expr = aggregate_expr
    if f" as {aggregate_alias}" not in aggregate_expr.lower().strip():
        current_aggregate_expr += f" AS {aggregate_alias}"

    input_tables = {_table_name(input_schema, input_vertices_table), _table_name(input_schema, input_edges_table)}
    _check_table_conflict(result_schema, result_vertices_table, input_tables)

    result_vertices_name = _table_name(result_schema, result_vertices_table)
    temp_base_name = f"pregel_temp_{uuid.uuid4().hex[:8]}"
    current_state_table = _table_name(result_schema, f"{temp_base_name}_iter0")

    operation_successful = False
    temp_tables_created = []

    with connection.cursor() as cursor:
        try:
            input_vertices_name = _table_name(input_schema, input_vertices_table)

            # Create initial state table
            initial_sql = (
                f"CREATE TABLE {current_state_table} AS "
                f"SELECT id, {current_initializer_expr} FROM {input_vertices_name}"
            )
            cursor.execute(initial_sql)
            temp_tables_created.append(current_state_table)

            input_edges_name = _table_name(input_schema, input_edges_table)

            for i in range(max_iterations):
                next_state_table = _table_name(result_schema, f"{temp_base_name}_iter{i + 1}")
                message_table = _table_name(result_schema, f"{temp_base_name}_msgs{i}")

                # 1. Send messages
                messages_sent = 0
                if send_source or send_dest:
                    messages_sql_parts = []
                    from_join_clause = (
                        f"FROM {current_state_table} a "
                        f"JOIN {input_edges_name} b ON a.id = b.srcid "
                        f"JOIN {current_state_table} c ON b.destid = c.id"
                    )

                    if send_source:
                        messages_sql_parts.append(
                            f"SELECT b.srcid AS id, ({send_to_source_expr}) AS msg {from_join_clause} "
                            f"WHERE ({send_to_source_expr}) IS NOT NULL"
                        )
                    if send_dest:
                        messages_sql_parts.append(
                            f"SELECT b.destid AS id, ({send_to_dest_expr}) AS msg {from_join_clause} "
                            f"WHERE ({send_to_dest_expr}) IS NOT NULL"
                        )

                    full_messages_sql = " UNION ALL ".join(messages_sql_parts)
                    cursor.execute(f"CREATE TABLE {message_table} AS {full_messages_sql}")
                    temp_tables_created.append(message_table)

                    cursor.execute(f"SELECT COUNT(*) FROM {message_table}")
                    count_result = cursor.fetchone()
                    if count_result:
                        messages_sent = count_result[0]

                if messages_sent == 0:
                    break  # Early termination if no messages were sent

                # 2. Aggregate messages and update state
                agg_msg_subquery = f"(SELECT id, {current_aggregate_expr} FROM {message_table} GROUP BY id) m"

                new_state_sql = (
                    f"CREATE TABLE {next_state_table} AS "
                    f"SELECT s.id, ({updater_expr}) AS state "
                    f"FROM {current_state_table} s LEFT JOIN {agg_msg_subquery} ON s.id = m.id"
                )
                cursor.execute(new_state_sql)
                temp_tables_created.append(next_state_table)

                # 3. Check for convergence
                diff_check_sql = (
                    f"SELECT COUNT(*) FROM ("
                    f"SELECT id, state FROM {next_state_table} "
                    "EXCEPT "
                    f"SELECT id, state FROM {current_state_table}"
                    ") AS diff_query"
                )
                cursor.execute(diff_check_sql)
                row = cursor.fetchone()
                diff_count = row[0] if row is not None else 0

                current_state_table = next_state_table
                if diff_count == 0:
                    break  # Converged

            # Create and populate final result table
            final_table_sql = (
                f"CREATE TABLE {result_vertices_name} AS SELECT id, state AS result FROM {current_state_table}"
            )
            cursor.execute(final_table_sql)

            for col in result_vertices_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                if col.lower() not in ("id", "result"):
                    raise SQLException(f"Argument Error: Invalid index column '{col}'. Must be 'id' or 'result'.")
                index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result_vertices_name} ("{col}")')

            operation_successful = True
        finally:
            for temp_table in temp_tables_created:
                _safe_drop_table(cursor, temp_table)
            if not operation_successful:
                _safe_drop_table(cursor, result_vertices_name)


def connected_components(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    max_iterations: int,
    result_vertices_indexes: List[str],
) -> None:
    """
    Finds the connected components of a graph using a Pregel-based algorithm.

    Each vertex is assigned a component ID, which is the minimum vertex ID
    within its connected component.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the result table.
    :param result_vertices_table: Name for the table with component results.
    :param max_iterations: The maximum number of Pregel iterations.
    :param result_vertices_indexes: List of columns to index ('id' or 'result').
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_positive(max_iterations, "Maximum iterations must be >= 1.")

    # Define Pregel parameters for Connected Components
    initializer_expr = "id"  # Initial component ID = vertex ID
    send_to_source_expr = "CASE WHEN c.state < a.state THEN c.state ELSE NULL END"
    send_to_dest_expr = "CASE WHEN a.state < c.state THEN a.state ELSE NULL END"
    aggregate_expr = "MIN(msg)"  # Aggregate by taking the minimum received ID
    # Update to smallest of current or received ID. COALESCE handles nodes with no messages.
    updater_expr = "LEAST(s.state, COALESCE(m.aggregated_message, s.state))"

    pregel(
        connection=connection,
        input_schema=input_schema,
        input_vertices_table=input_vertices_table,
        input_edges_table=input_edges_table,
        result_schema=result_schema,
        result_vertices_table=result_vertices_table,
        initializer_expr=initializer_expr,
        send_to_source_expr=send_to_source_expr,
        send_to_dest_expr=send_to_dest_expr,
        aggregate_expr=aggregate_expr,
        updater_expr=updater_expr,
        max_iterations=max_iterations,
        result_vertices_indexes=result_vertices_indexes,
    )


def strongly_connected_components(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    result_vertices_indexes: List[str],
) -> None:
    """
    Computes the Strongly Connected Components (SCCs) of a directed graph.

    This method implements a recursive algorithm to partition the graph and
    identify sets of vertices where every vertex is reachable from every other
    vertex within the same set.

    The final result is populated into the `result_vertices_table`, which maps
    each vertex `id` to a representative `component` ID (the minimum vertex
    ID within that component).

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the result and temporary tables.
    :param result_vertices_table: Name for the table with SCC results.
    :param result_vertices_indexes: List of columns to index ('id' or 'component').
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_vertices_table, "Result vertices table name cannot be null or empty.")
    _check_not_null(result_vertices_indexes, "Result vertices index list cannot be null.")

    input_tables = {
        _table_name(input_schema, input_vertices_table),
        _table_name(input_schema, input_edges_table),
    }
    _check_table_conflict(result_schema, result_vertices_table, input_tables)
    final_result_table = _table_name(result_schema, result_vertices_table)

    temp_tables = []  # Central tracker for ALL temp tables
    unique_suffix = f"scc_{uuid.uuid4().hex[:10]}"
    initial_vertices_base = f"v_start_{unique_suffix}"
    initial_edges_base = f"e_start_{unique_suffix}"

    with connection.cursor() as cursor:
        try:
            # Create the final result table structure up front
            cursor.execute(f"CREATE TABLE {final_result_table} (id BIGINT NOT NULL, component BIGINT NOT NULL)")
            for col in result_vertices_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                if col.lower() not in ("id", "component"):
                    raise SQLException(f"Argument Error: Invalid index column '{col}' for SCC result.")
                index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {final_result_table} ("{col}")')

            # Create initial temporary copies of the graph
            initial_vertices_table = _table_name(result_schema, initial_vertices_base)
            initial_edges_table = _table_name(result_schema, initial_edges_base)

            cursor.execute(
                f"CREATE TABLE {initial_vertices_table} AS SELECT * FROM {_table_name(input_schema, input_vertices_table)}"
            )
            temp_tables.append(initial_vertices_table)

            cursor.execute(
                f"CREATE TABLE {initial_edges_table} AS SELECT * FROM {_table_name(input_schema, input_edges_table)}"
            )
            temp_tables.append(initial_edges_table)

            # Start the recursive process
            _process_component(
                cursor,
                result_schema,
                initial_vertices_base,
                initial_edges_base,
                result_schema,
                result_vertices_table,
                temp_tables,
                f"{unique_suffix}_r0",
            )
        except SQLException as e:
            # If anything fails, drop the final table too
            _safe_drop_table(cursor, final_result_table)
            raise e
        finally:
            # Clean up all temporary tables
            for temp_table in reversed(temp_tables):
                _safe_drop_table(cursor, temp_table)


def _process_component(
    cursor: Cursor,
    schema: str,
    vertices_base: str,
    edges_base: str,
    result_schema: str,
    result_table: str,
    temp_tables: List[str],
    recur_suffix: str,
) -> None:
    """Recursive core of the SCC algorithm."""
    current_vertices = _table_name(schema, vertices_base)

    # Base case: if the current graph partition is empty, stop.
    cursor.execute(f"SELECT COUNT(*) FROM {current_vertices}")
    row = cursor.fetchone()
    if row is None or row[0] == 0:
        return

    # 1. Select a pivot vertex
    cursor.execute(f"SELECT MIN(id) FROM {current_vertices}")
    pivot_result = cursor.fetchone()
    if not pivot_result or pivot_result[0] is None:
        return
    pivot = pivot_result[0]

    # 2. Compute predecessors (Pred) and descendants (Desc) of the pivot
    pred_base = f"pred_{recur_suffix}"
    desc_base = f"desc_{recur_suffix}"

    _compute_descendants(cursor, schema, edges_base, pivot, desc_base, temp_tables)
    _compute_predecessors(cursor, schema, edges_base, pivot, pred_base, temp_tables, recur_suffix)

    # 3. The current SCC is the intersection of Pred and Desc
    scc_base = f"scc_{recur_suffix}"
    scc_table = _table_name(schema, scc_base)
    pred_table = _table_name(schema, pred_base)
    desc_table = _table_name(schema, desc_base)

    cursor.execute(f"CREATE TABLE {scc_table} AS SELECT p.id FROM {pred_table} p JOIN {desc_table} d ON p.id = d.id")
    temp_tables.append(scc_table)

    # 4. Insert the found SCC into the final result table
    final_result_table = _table_name(result_schema, result_table)
    cursor.execute(
        f"INSERT INTO {final_result_table} (id, component) SELECT id, MIN(id) OVER () AS component FROM {scc_table}"
    )

    # 5. Recurse on the three remaining partitions of the graph
    # Partition 1: Desc \ SCC
    _process_partition(
        cursor,
        schema,
        vertices_base,
        edges_base,
        result_schema,
        result_table,
        desc_base,
        scc_base,
        "desc",
        temp_tables,
        f"{recur_suffix}_d",
    )

    # Partition 2: Pred \ SCC
    _process_partition(
        cursor,
        schema,
        vertices_base,
        edges_base,
        result_schema,
        result_table,
        pred_base,
        scc_base,
        "pred",
        temp_tables,
        f"{recur_suffix}_p",
    )

    # Partition 3: Remainder = V \ (Pred U Desc)
    _process_remaining(
        cursor,
        schema,
        vertices_base,
        edges_base,
        result_schema,
        result_table,
        pred_base,
        desc_base,
        temp_tables,
        f"{recur_suffix}_r",
    )


def _compute_descendants(
    cursor: Cursor, schema: str, edges_base: str, pivot: int, result_base: str, temp_tables: List[str]
) -> None:
    """Iteratively finds all vertices reachable from the pivot."""
    result_table = _table_name(schema, result_base)
    current_edges = _table_name(schema, edges_base)

    cursor.execute(f"CREATE TABLE {result_table} (id BIGINT NOT NULL)")
    temp_tables.append(result_table)
    cursor.execute(f"INSERT INTO {result_table} (id) VALUES ({pivot})")

    while True:
        new_nodes_sql = f"""
            INSERT INTO {result_table} (id)
            SELECT DISTINCT e.destid FROM {result_table} d JOIN {current_edges} e ON d.id = e.srcid
            WHERE NOT EXISTS (SELECT 1 FROM {result_table} existed WHERE existed.id = e.destid)
        """
        cursor.execute(new_nodes_sql)
        if cursor.rowcount == 0:
            break


def _compute_predecessors(
    cursor: Cursor,
    schema: str,
    edges_base: str,
    pivot: int,
    result_base: str,
    temp_tables: List[str],
    recur_suffix: str,
) -> None:
    """Finds all vertices that can reach the pivot by reversing edges and finding descendants."""
    temp_rev_edges_base = f"rev_{recur_suffix}"
    temp_rev_edges_table = _table_name(schema, temp_rev_edges_base)

    try:
        # Create a temporary reversed graph
        reverse_edges(
            connection=cursor.connection,
            input_schema=schema,
            input_edges_table=edges_base,
            result_schema=schema,
            result_edges_table=temp_rev_edges_base,
            result_edges_indexes=[],
        )
        temp_tables.append(temp_rev_edges_table)

        # Find "descendants" in the reversed graph, which are predecessors in the original
        _compute_descendants(cursor, schema, temp_rev_edges_base, pivot, result_base, temp_tables)
    finally:
        _safe_drop_table(cursor, temp_rev_edges_table)


def _process_partition(
    cursor: Cursor,
    schema: str,
    vertices_base: str,
    edges_base: str,
    result_schema: str,
    result_table: str,
    partition_set_base: str,
    scc_base: str,
    type_prefix: str,
    temp_tables: List[str],
    recur_suffix: str,
) -> None:
    r"""Creates a subgraph for a partition (e.g., Desc \ SCC) and recurses."""
    filtered_v_base = f"{type_prefix}_v_{recur_suffix}"
    filtered_e_base = f"{type_prefix}_e_{recur_suffix}"

    current_vertices = _table_name(schema, vertices_base)
    current_edges = _table_name(schema, edges_base)
    partition_set_table = _table_name(schema, partition_set_base)
    scc_table = _table_name(schema, scc_base)

    # Create the new vertex set for the partition
    filtered_v_table = _table_name(schema, filtered_v_base)
    cursor.execute(f"""
        CREATE TABLE {filtered_v_table} AS
        SELECT v.* FROM {current_vertices} v JOIN {partition_set_table} p ON v.id = p.id
        WHERE NOT EXISTS (SELECT 1 FROM {scc_table} scc WHERE scc.id = v.id)
    """)
    temp_tables.append(filtered_v_table)

    cursor.execute(f"SELECT COUNT(*) FROM {filtered_v_table}")
    row = cursor.fetchone()
    if row is not None and row[0] > 0:
        # Create the corresponding edge set
        filtered_e_table = _table_name(schema, filtered_e_base)
        cursor.execute(f"""
            CREATE TABLE {filtered_e_table} AS
            SELECT e.* FROM {current_edges} e
            JOIN {filtered_v_table} src_v ON e.srcid = src_v.id
            JOIN {filtered_v_table} dest_v ON e.destid = dest_v.id
        """)
        temp_tables.append(filtered_e_table)

        # Recurse on this new subgraph
        _process_component(
            cursor, schema, filtered_v_base, filtered_e_base, result_schema, result_table, temp_tables, recur_suffix
        )


def _process_remaining(
    cursor: Cursor,
    schema: str,
    vertices_base: str,
    edges_base: str,
    result_schema: str,
    result_table: str,
    pred_base: str,
    desc_base: str,
    temp_tables: List[str],
    recur_suffix: str,
) -> None:
    r"""Creates the subgraph for the remainder partition V \ (Pred U Desc) and recurses."""
    remaining_v_base = f"rem_v_{recur_suffix}"
    remaining_e_base = f"rem_e_{recur_suffix}"

    current_vertices = _table_name(schema, vertices_base)
    current_edges = _table_name(schema, edges_base)
    pred_table = _table_name(schema, pred_base)
    desc_table = _table_name(schema, desc_base)

    # Create the vertex set for the remainder
    remaining_v_table = _table_name(schema, remaining_v_base)
    cursor.execute(f"""
        CREATE TABLE {remaining_v_table} AS
        SELECT v.* FROM {current_vertices} v
        WHERE NOT EXISTS (SELECT 1 FROM {pred_table} pred WHERE pred.id = v.id)
          AND NOT EXISTS (SELECT 1 FROM {desc_table} desc WHERE desc.id = v.id)
    """)
    temp_tables.append(remaining_v_table)

    cursor.execute(f"SELECT COUNT(*) FROM {remaining_v_table}")
    row = cursor.fetchone()
    if row is not None and row[0] > 0:
        # Create the corresponding edge set
        remaining_e_table = _table_name(schema, remaining_e_base)
        cursor.execute(f"""
            CREATE TABLE {remaining_e_table} AS
            SELECT e.* FROM {current_edges} e
            JOIN {remaining_v_table} src_v ON e.srcid = src_v.id
            JOIN {remaining_v_table} dest_v ON e.destid = dest_v.id
        """)
        temp_tables.append(remaining_e_table)

        # Recurse on this new subgraph
        _process_component(
            cursor, schema, remaining_v_base, remaining_e_base, result_schema, result_table, temp_tables, recur_suffix
        )


def shortest_paths(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_table: str,
    landmarks: List[int],
    edge_weight_column: Optional[str],
    max_iterations: int,
    result_indexes: List[str],
) -> None:
    """
    Computes the shortest paths from all vertices to a set of landmark vertices.
    This method uses an iterative relaxation algorithm (similar to Bellman-Ford)
    to find the shortest distance from every vertex to each landmark. It assumes
    all edge weights are non-negative. If no weight column is specified,
    edges have a uniform weight of 1.0.
    The result table will contain `srcid`, `destid` (the landmark), and the
    computed `distance`. Only paths with finite distances are stored.
    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the result and temporary tables.
    :param result_table: Name for the table with shortest path results.
    :param landmarks: A non-empty list of vertex IDs to use as landmarks.
    :param edge_weight_column: The name of the column containing edge weights.
        If None or empty, weight is 1.0.
    :param max_iterations: Maximum number of iterations for the algorithm.
    :param result_indexes: List of columns to index ('srcid', 'destid', 'distance').
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_not_null_or_empty(input_schema, "Input schema cannot be null or empty.")
    _check_not_null_or_empty(input_vertices_table, "Input vertices table name cannot be null or empty.")
    _check_not_null_or_empty(input_edges_table, "Input edges table name cannot be null or empty.")
    _check_not_null_or_empty(result_schema, "Result schema cannot be null or empty.")
    _check_not_null_or_empty(result_table, "Result table name cannot be null or empty.")
    _check_not_null(landmarks, "Landmarks list cannot be null.")
    if not landmarks:
        raise SQLException("Argument Error: Landmarks list cannot be empty.")
    if any(lm is None for lm in landmarks):
        raise SQLException("Argument Error: Landmarks list cannot contain null values.")
    _check_positive(max_iterations, "Maximum iterations must be >= 1.")
    _check_not_null(result_indexes, "Result index list cannot be null.")

    input_tables = {
        _table_name(input_schema, input_vertices_table),
        _table_name(input_schema, input_edges_table),
    }
    _check_table_conflict(result_schema, result_table, input_tables)

    weight_expr = f'e."{edge_weight_column.strip()}"' if edge_weight_column and edge_weight_column.strip() else "1.0"

    vertices = _table_name(input_schema, input_vertices_table)
    edges = _table_name(input_schema, input_edges_table)
    result = _table_name(result_schema, result_table)

    temp_base = f"sp_temp_{uuid.uuid4().hex[:8]}"
    current_dists_base = f"{temp_base}_curr"
    next_dists_base = f"{temp_base}_next"

    qualified_current_dists = _table_name(result_schema, current_dists_base)
    qualified_next_dists = _table_name(result_schema, next_dists_base)

    temp_tables_created = []

    with connection.cursor() as cursor:
        try:
            landmarks_str = f"ARRAY[{','.join(map(str, landmarks))}]"

            init_sql = f"""
                CREATE TABLE {qualified_current_dists} AS
                SELECT v.id AS srcid, l.landmark AS destid,
                       CASE WHEN v.id = l.landmark THEN 0.0 ELSE CAST('1.0e308' AS DOUBLE PRECISION) END AS distance
                FROM {vertices} v
                CROSS JOIN (SELECT UNNEST({landmarks_str}) AS landmark) l
            """
            cursor.execute(init_sql)
            temp_tables_created.append(qualified_current_dists)  # CORRECTED

            changed = True
            for i in range(max_iterations):
                if not changed:
                    break

                _safe_drop_table(cursor, qualified_next_dists)

                merge_sql = f"""
                    CREATE TABLE {qualified_next_dists} AS
                    WITH new_paths AS (
                        SELECT e.srcid, d.destid, MIN(d.distance + {weight_expr}) AS new_distance
                        FROM {qualified_current_dists} d JOIN {edges} e ON d.srcid = e.destid
                        WHERE d.distance != CAST('1.0e308' AS DOUBLE PRECISION)
                        GROUP BY e.srcid, d.destid
                    )
                    SELECT
                        COALESCE(d.srcid, n.srcid) AS srcid,
                        COALESCE(d.destid, n.destid) AS destid,
                        LEAST(
                            COALESCE(d.distance, CAST('1.0e308' AS DOUBLE PRECISION)),
                            COALESCE(n.new_distance, CAST('1.0e308' AS DOUBLE PRECISION))
                        ) AS distance
                    FROM {qualified_current_dists} d FULL OUTER JOIN new_paths n
                    ON d.srcid = n.srcid AND d.destid = n.destid
                """
                cursor.execute(merge_sql)
                temp_tables_created.append(qualified_next_dists)  # CORRECTED

                check_change_sql = f"""
                    SELECT COUNT(*) FROM {qualified_next_dists} next JOIN {qualified_current_dists} curr
                    ON next.srcid = curr.srcid AND next.destid = curr.destid
                    WHERE next.distance < curr.distance
                """
                cursor.execute(check_change_sql)
                row = cursor.fetchone()
                num_changes = row[0] if row is not None else 0
                changed = num_changes > 0

                qualified_current_dists, qualified_next_dists = qualified_next_dists, qualified_current_dists

            cursor.execute(
                f"CREATE TABLE {result} (srcid BIGINT NOT NULL, destid BIGINT NOT NULL, distance DOUBLE PRECISION)"
            )
            for col in result_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                if col.lower() not in ("srcid", "destid", "distance"):
                    raise SQLException(f"Argument Error: Invalid index column '{col}'.")
                index_name = f"{result_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {result} ("{col}")')

            cursor.execute(
                f"INSERT INTO {result} (srcid, destid, distance) "
                f"SELECT srcid, destid, distance FROM {qualified_current_dists} "
                f"WHERE distance != CAST('1.0e308' AS DOUBLE PRECISION)"
            )
        finally:
            _safe_drop_table(cursor, qualified_current_dists)
            _safe_drop_table(cursor, qualified_next_dists)


def _get_vertex_count(cursor: Cursor, schema: str, table: str) -> int:
    """Gets the total number of rows from a table."""
    qualified_table_name = _table_name(schema, table)
    cursor.execute(f"SELECT COUNT(*) FROM {qualified_table_name}")
    result = cursor.fetchone()
    if result and result[0] is not None:
        return int(result[0])
    raise SQLException(f"Database Error: Could not retrieve vertex count from {qualified_table_name}.")


def static_page_rank(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    num_iterations: int,
    reset_prob: float,
    result_vertices_indexes: List[str],
    personalization_src_id: Optional[int],
) -> None:
    """
    Computes static PageRank for a fixed number of iterations.

    This implementation is optimized to avoid copying tables between iterations
    by swapping the roles of two temporary tables.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the result table.
    :param result_vertices_table: Name for the table with PageRank scores.
    :param num_iterations: The number of PageRank iterations to perform.
    :param reset_prob: The reset probability (damping factor), typically 0.85.
    :param result_vertices_indexes: List of columns to index in the result.
    :param personalization_src_id: If not None, computes Personalized PageRank
        biased towards this vertex ID.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    _check_positive(num_iterations, "Number of iterations must be positive.")
    if not (0.0 <= reset_prob <= 1.0):
        raise SQLException("Reset probability must be between 0.0 and 1.0.")

    qualified_input_v = _table_name(input_schema, input_vertices_table)
    qualified_input_e = _table_name(input_schema, input_edges_table)
    qualified_result_v = _table_name(result_schema, result_vertices_table)

    _check_table_conflict(result_schema, result_vertices_table, {qualified_input_v, qualified_input_e})

    unique_suffix = uuid.uuid4().hex
    current_ranks_base = f"pagerank_curr_{unique_suffix}"
    previous_ranks_base = f"pagerank_prev_{unique_suffix}"
    qualified_current_ranks = _table_name(result_schema, current_ranks_base)
    qualified_previous_ranks = _table_name(result_schema, previous_ranks_base)

    created_tables = set()

    with connection.cursor() as cursor:
        try:
            vertex_count = _get_vertex_count(cursor, input_schema, input_vertices_table)
            if vertex_count == 0:
                cursor.execute(
                    f"CREATE TABLE {qualified_result_v} AS "
                    f"SELECT v.*, CAST(NULL AS DOUBLE PRECISION) AS pagerank "
                    f"FROM {qualified_input_v} v WHERE 1=0"
                )
                return

            # Initialize the first "current" ranks table
            if personalization_src_id is not None:
                init_sql = (
                    f"SELECT id, CASE WHEN id = {personalization_src_id} "
                    f"THEN 1.0 ELSE 0.0 END AS rank FROM {qualified_input_v}"
                )
            else:
                init_rank = 1.0 / vertex_count
                init_sql = f"SELECT id, CAST({init_rank} AS DOUBLE PRECISION) AS rank FROM {qualified_input_v}"
            cursor.execute(f"CREATE TABLE {qualified_current_ranks} AS {init_sql}")
            created_tables.add(qualified_current_ranks)

            # --- Iterations ---
            for _ in range(num_iterations):
                # OPTIMIZATION: Swap variables, not table data.
                # This is an instantaneous metadata change.
                qualified_current_ranks, qualified_previous_ranks = (
                    qualified_previous_ranks,
                    qualified_current_ranks,
                )

                _safe_drop_table(cursor, qualified_current_ranks)
                created_tables.discard(qualified_current_ranks)

                # The `qualified_previous_ranks` table now holds the ranks from the last iteration.
                # The iteration SQL will create a new `qualified_current_ranks` table.

                teleport_sql = f"(1.0 - {reset_prob}) / {vertex_count}" if personalization_src_id is None else "0.0"
                personalization_sql = (
                    ""
                    if personalization_src_id is None
                    else (f" + CASE WHEN v.id = {personalization_src_id} THEN {1.0 - reset_prob} ELSE 0.0 END")
                )

                iteration_sql = f"""
                    CREATE TABLE {qualified_current_ranks} AS
                    WITH EdgeContributions AS (
                        SELECT e.destid, SUM(pr.rank / out_degree.out_cnt) as contrib
                        FROM {qualified_input_e} e
                        JOIN {qualified_previous_ranks} pr ON e.srcid = pr.id
                        JOIN (SELECT srcid, COUNT(*) AS out_cnt FROM {qualified_input_e} GROUP BY srcid HAVING COUNT(*) > 0) out_degree ON e.srcid = out_degree.srcid
                        GROUP BY e.destid
                    ), DanglingRank AS (
                        SELECT COALESCE(SUM(pr.rank), 0.0) as total_rank
                        FROM {qualified_previous_ranks} pr
                        WHERE pr.id NOT IN (SELECT DISTINCT srcid FROM {qualified_input_e})
                    )
                    SELECT
                        v.id,
                        CAST( ({teleport_sql})
                             + ({reset_prob} * COALESCE(ec.contrib, 0.0))
                             + ({reset_prob} * dr.total_rank / {vertex_count})
                             {personalization_sql}
                             AS DOUBLE PRECISION) AS rank
                    FROM {qualified_input_v} v
                    LEFT JOIN EdgeContributions ec ON v.id = ec.destid
                    CROSS JOIN DanglingRank dr
                """
                cursor.execute(iteration_sql)
                created_tables.add(qualified_current_ranks)

            # Final result is in the last table pointed to by `qualified_current_ranks`
            cursor.execute(
                f"CREATE TABLE {qualified_result_v} AS "
                f"SELECT v.*, tr.rank AS pagerank "
                f"FROM {qualified_input_v} v JOIN {qualified_current_ranks} tr ON v.id = tr.id"
            )
            created_tables.add(qualified_result_v)

            for col in result_vertices_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {qualified_result_v} ("{col}")')

        finally:
            _safe_drop_table(cursor, qualified_current_ranks)
            _safe_drop_table(cursor, qualified_previous_ranks)


def dynamic_page_rank(
    connection: Connection,
    input_schema: str,
    input_vertices_table: str,
    input_edges_table: str,
    result_schema: str,
    result_vertices_table: str,
    tolerance: float,
    reset_prob: float,
    result_vertices_indexes: List[str],
    personalization_src_id: Optional[int],
) -> None:
    """
    Computes PageRank scores, iterating until the scores converge.

    This implementation is optimized to avoid copying tables between iterations
    by swapping the roles of two temporary tables.

    :param connection: The pyocient Connection object.
    :param input_schema: Schema of the source graph tables.
    :param input_vertices_table: Name of the source vertices table.
    :param input_edges_table: Name of the source edges table.
    :param result_schema: Schema for the result table.
    :param result_vertices_table: Name for the table with PageRank scores.
    :param tolerance: The convergence tolerance.
    :param reset_prob: The reset probability (damping factor), typically 0.85.
    :param result_vertices_indexes: List of columns to index in the result.
    :param personalization_src_id: If not None, computes Personalized PageRank
        biased towards this vertex ID.
    :raises SQLException: If any database error occurs.
    """
    _check_not_null(connection, "Connection cannot be null.")
    if tolerance < 0.0:
        raise SQLException("Tolerance must be non-negative.")
    if not (0.0 <= reset_prob <= 1.0):
        raise SQLException("Reset probability must be between 0.0 and 1.0.")

    qualified_input_v = _table_name(input_schema, input_vertices_table)
    qualified_input_e = _table_name(input_schema, input_edges_table)
    qualified_result_v = _table_name(result_schema, result_vertices_table)

    _check_table_conflict(result_schema, result_vertices_table, {qualified_input_v, qualified_input_e})

    unique_suffix = uuid.uuid4().hex
    current_ranks_base = f"pagerank_curr_{unique_suffix}"
    previous_ranks_base = f"pagerank_prev_{unique_suffix}"
    qualified_current_ranks = _table_name(result_schema, current_ranks_base)
    qualified_previous_ranks = _table_name(result_schema, previous_ranks_base)

    created_tables = set()

    with connection.cursor() as cursor:
        try:
            vertex_count = _get_vertex_count(cursor, input_schema, input_vertices_table)
            if vertex_count == 0:
                cursor.execute(
                    f"CREATE TABLE {qualified_result_v} AS "
                    f"SELECT v.*, CAST(NULL AS DOUBLE PRECISION) AS pagerank "
                    f"FROM {qualified_input_v} v WHERE 1=0"
                )
                return

            # Initialize the first "current" ranks table
            if personalization_src_id is not None:
                init_sql = (
                    f"SELECT id, CASE WHEN id = {personalization_src_id} "
                    f"THEN 1.0 ELSE 0.0 END AS rank FROM {qualified_input_v}"
                )
            else:
                init_rank = 1.0 / vertex_count
                init_sql = f"SELECT id, CAST({init_rank} AS DOUBLE PRECISION) AS rank FROM {qualified_input_v}"
            cursor.execute(f"CREATE TABLE {qualified_current_ranks} AS {init_sql}")
            created_tables.add(qualified_current_ranks)

            delta = float("inf")
            while delta > tolerance:
                # OPTIMIZATION: Swap variables, not table data.
                qualified_current_ranks, qualified_previous_ranks = (
                    qualified_previous_ranks,
                    qualified_current_ranks,
                )

                _safe_drop_table(cursor, qualified_current_ranks)
                created_tables.discard(qualified_current_ranks)

                teleport_sql = f"(1.0 - {reset_prob}) / {vertex_count}" if personalization_src_id is None else "0.0"
                personalization_sql = (
                    ""
                    if personalization_src_id is None
                    else (f" + CASE WHEN v.id = {personalization_src_id} THEN {1.0 - reset_prob} ELSE 0.0 END")
                )

                iteration_sql = f"""
                    CREATE TABLE {qualified_current_ranks} AS
                    WITH EdgeContributions AS (
                        SELECT e.destid, SUM(pr.rank / out_degree.out_cnt) as contrib
                        FROM {qualified_input_e} e
                        JOIN {qualified_previous_ranks} pr ON e.srcid = pr.id
                        JOIN (SELECT srcid, COUNT(*) AS out_cnt FROM {qualified_input_e} GROUP BY srcid HAVING COUNT(*) > 0) out_degree ON e.srcid = out_degree.srcid
                        GROUP BY e.destid
                    ), DanglingRank AS (
                        SELECT COALESCE(SUM(pr.rank), 0.0) as total_rank
                        FROM {qualified_previous_ranks} pr
                        WHERE pr.id NOT IN (SELECT DISTINCT srcid FROM {qualified_input_e})
                    )
                    SELECT
                        v.id,
                        CAST( ({teleport_sql})
                             + ({reset_prob} * COALESCE(ec.contrib, 0.0))
                             + ({reset_prob} * dr.total_rank / {vertex_count})
                             {personalization_sql}
                             AS DOUBLE PRECISION) AS rank
                    FROM {qualified_input_v} v
                    LEFT JOIN EdgeContributions ec ON v.id = ec.destid
                    CROSS JOIN DanglingRank dr
                """
                cursor.execute(iteration_sql)
                created_tables.add(qualified_current_ranks)

                # Check for convergence by comparing the new and old tables
                delta_sql = (
                    f"SELECT SUM(ABS(curr.rank - prev.rank)) "
                    f"FROM {qualified_current_ranks} curr "
                    f"JOIN {qualified_previous_ranks} prev ON curr.id = prev.id"
                )
                cursor.execute(delta_sql)
                delta_result = cursor.fetchone()
                delta = delta_result[0] if delta_result and delta_result[0] is not None else 0.0

            # Final result
            cursor.execute(
                f"CREATE TABLE {qualified_result_v} AS "
                f"SELECT v.*, tr.rank AS pagerank "
                f"FROM {qualified_input_v} v JOIN {qualified_current_ranks} tr ON v.id = tr.id"
            )
            created_tables.add(qualified_result_v)

            for col in result_vertices_indexes:
                _check_not_null_or_empty(col, "Index column name cannot be null or empty.")
                index_name = f"{result_vertices_table}_{col}_idx".replace('"', "")
                cursor.execute(f'CREATE INDEX "{index_name}" ON {qualified_result_v} ("{col}")')

        finally:
            _safe_drop_table(cursor, qualified_current_ranks)
            _safe_drop_table(cursor, qualified_previous_ranks)
