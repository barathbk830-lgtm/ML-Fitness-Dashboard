import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🔥 Project Insights")

importance_df = pd.DataFrame({
    "Feature": [
        "Session Duration",
        "HR Intensity",
        "Effective MET",
        "Weight",
        "Base MET"
    ],
    "Importance": [0.366, 0.326, 0.130, 0.129, 0.030]
})

st.subheader("Top Feature Importance")

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(
    x="Importance",
    y="Feature",
    data=importance_df,
    ax=ax
)

st.pyplot(fig)

st.subheader("Business Insights")

st.markdown("""
### Key Findings

- Session Duration strongly impacts calories.
- HR Intensity affects workout performance.
- Random Forest performed best.
- Clustering grouped users into 3 workout categories.
""")

st.subheader("Recommendation System")

st.info("Cluster 0 → Moderate Users")
st.info("Cluster 1 → Beginner Yoga Users")
st.info("Cluster 2 → Advanced Workout Users")