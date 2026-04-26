import streamlit as st
import pandas as pd

st.title("📁 Dataset Overview")

@st.cache_data
def load_data():
    return pd.read_csv("Fitbit_dataset.csv")

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Shape")
st.write(df.shape)

st.subheader("Column Names")
st.write(df.columns.tolist())

st.subheader("Missing Values")
st.write(df.isnull().sum())