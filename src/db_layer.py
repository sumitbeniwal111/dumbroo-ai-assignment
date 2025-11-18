import pandas as pd
from dateutil import parser as date_parser
import numpy as np

def load_data(path="data/students.csv"):
    df = pd.read_csv(path, keep_default_na=False)

    def to_dt(x):
        try:
            if x in (None, "", " "): return pd.NaT
            return pd.to_datetime(x)
        except: return pd.NaT

    df["quiz_date"] = df["quiz_date"].apply(to_dt)
    df["last_activity"] = df["last_activity"].apply(to_dt)

    def normalize_hw(x):
        x = str(x).strip().lower()
        if x in ["yes", "y", "true", "1"]: return True
        if x in ["no", "n", "false", "0"]: return False
        return None

    df["homework_submitted"] = df["homework_submitted"].apply(normalize_hw)
    df["quiz_score"] = pd.to_numeric(df["quiz_score"], errors="coerce")

    return df
