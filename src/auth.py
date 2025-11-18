from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Admin:
    admin_id: int
    name: str
    scope: Dict[str, Any]

def apply_scope_filter(df, scope):
    df_scoped = df.copy()
    for k, v in scope.items():
        if v is not None:
            df_scoped = df_scoped[df_scoped[k].astype(str) == str(v)]
    return df_scoped

def enforce_admin_scope_on_filters(parsed_filters, admin_scope):
    corrected = []
    for f in parsed_filters:
        field = f.get("field")
        if field in admin_scope and admin_scope[field] is not None:
            f = dict(f)
            f["value"] = admin_scope[field]
        corrected.append(f)
    return corrected
