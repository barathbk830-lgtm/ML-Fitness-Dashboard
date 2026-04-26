import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🧠 Clustering Analysis")

st.subheader("Workout Cluster Visualization")

st.image("cluster_plot.png",use_container_width=True)

st.success("Silhouette Score: 0.417")

cluster_counts = pd.DataFrame({
    "Cluster": ["Cluster 0", "Cluster 1", "Cluster 2"],
    "Users": [6700, 2800, 4600]
})

st.subheader("Cluster Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(
    x="Cluster",
    y="Users",
    data=cluster_counts,
    ax=ax
)

st.pyplot(fig)