import pandas as pd
from src.auth import apply_scope_filter, enforce_admin_scope_on_filters
from src.db_layer import load_data

def apply_filters(df: pd.DataFrame, filters):
    df2 = df.copy()
    for f in filters:
        field, op, value = f["field"], f["op"], f["value"]

        if op == "=":
            df2 = df2[df2[field].astype(str) == str(value)]

    return df2

def execute_parsed_query(admin, parsed):
    df = load_data()
    df = apply_scope_filter(df, admin.scope)

    filters = enforce_admin_scope_on_filters(parsed["filters"], admin.scope)
    df = apply_filters(df, filters)

    if parsed["date_range"] and parsed["target"] in ("quiz", "performance"):
        start, end = parsed["date_range"]
        df = df[df["quiz_date"].notna()]
        df = df[(df["quiz_date"].dt.date >= start) & (df["quiz_date"].dt.date <= end)]

    return df, parsed.get("note", "")
