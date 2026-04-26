import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📈 Model Comparison")

comparison_df = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "R2 Score": [0.911345, 0.997911]
})

st.dataframe(comparison_df)

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(
    x="Model",
    y="R2 Score",
    data=comparison_df,
    ax=ax
)

plt.title("Model Performance")

st.pyplot(fig)

st.subheader("Actual vs Predicted")

st.image("actual_vs_predicted.png")