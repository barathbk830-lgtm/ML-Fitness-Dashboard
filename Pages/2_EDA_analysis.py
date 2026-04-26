import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 EDA Analysis")

@st.cache_data
def load_data():
    return pd.read_csv("Fitbit_dataset.csv")

df = load_data()

st.subheader("Calories Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(df["Calories_Burned (kcal)"], kde=True, ax=ax)

st.pyplot(fig)

st.subheader("Correlation Heatmap")

numeric_df = df.select_dtypes(include=['number'])

fig2, ax2 = plt.subplots(figsize=(10,6))

sns.heatmap(numeric_df.corr(), annot=False, cmap="coolwarm", ax=ax2)

st.pyplot(fig2)