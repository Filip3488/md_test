import streamlit as st
import pandas as pd
from loadData import load_data, get_tables

st.title("DuckDB — md_test")

try:
    tables = get_tables()
except Exception as e:
    st.error(f"Could not connect to MotherDuck: {e}")
    st.stop()

table = st.selectbox("Table", tables)

if st.button("Load Data"):
    with st.spinner("Loading…"):
        try:
            columns, rows = load_data(table)
            df = pd.DataFrame(rows, columns=columns)
            st.dataframe(df, use_container_width=True)
            st.caption(f"{len(df)} rows")
        except Exception as e:
            st.error(str(e))