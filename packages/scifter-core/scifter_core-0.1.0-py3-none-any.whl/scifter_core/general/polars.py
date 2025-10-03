import polars as pl

def set_schema(df: pl.DataFrame, schema: pl.Schema) -> pl.DataFrame:

    select_expressions = []
    for col_name, dtype in schema.items():
        if col_name in df.columns:
            select_expressions.append(pl.col(col_name).cast(dtype, strict=True))
        else:
            select_expressions.append(pl.lit(None, dtype=dtype).alias(col_name))
    
    df = df.select(*select_expressions)
    return df
