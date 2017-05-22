def build_schema_query(table_schema):
    schema_query = """
    SELECT      c.table_name,
                c.column_name,
                c.column_default,
                c.is_nullable,
                c.data_type,
                c.character_maximum_length,
                pgd.description
    FROM pg_catalog.pg_statio_all_tables as st
      inner join pg_catalog.pg_description pgd on (pgd.objoid=st.relid)
      right join information_schema.columns c on (pgd.objsubid=c.ordinal_position
        and  c.table_schema=st.schemaname and c.table_name=st.relname)
    WHERE       c.table_schema = '{0}'
    ORDER BY    c.table_name, ordinal_position;
    """.format(table_schema)
    return schema_query
