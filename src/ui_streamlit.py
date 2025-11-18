import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from src.auth import Admin
from src.main import run_query_for_admin

st.title("Dumroo Admin Panel")

admin = Admin(
    admin_id=1,
    name="Demo Admin",
    scope={"grade": 8, "class": "A", "region": "North"}
)

query = st.text_input("Ask your question:")

if st.button("Run"):
    df, note = run_query_for_admin(admin, query)

    st.write("### Result:")
    st.dataframe(df)

    if note:
        st.write("Note:", note)
