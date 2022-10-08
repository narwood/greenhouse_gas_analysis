import streamlit as st
import pandas as pd

@st.cache()
def load_data(path: str):
    data = pd.read_csv(path, index_col=[0])
    return data

@st.cache()
def df_to_csv(df: pd.DataFrame):
    return df.to_csv().encode('utf-8')