# ML Fitness Analytics Project

A Machine Learning project focused on predicting calories burned and identifying workout behavior patterns using regression and clustering techniques.

---

# Project Overview

This project analyzes fitness workout data to:

* Predict calories burned using Machine Learning
* Compare multiple regression models
* Identify important workout features
* Group users into workout behavior clusters
* Build an interactive Streamlit dashboard

---

# Objectives

### Regression Task

Predict calories burned based on workout and body metrics.

### Clustering Task

Segment users into different workout behavior groups.

### Visualization

Present insights using graphs and Streamlit dashboard.

---

# Dataset Information

Dataset includes:

* Age
* Weight
* Height
* Max BPM
* Avg BPM
* Resting BPM
* Workout Duration
* Workout Type
* Water Intake
* BMI
* Calories Burned

---

# Machine Learning Workflow

```text
Data Collection
       ↓
Data Cleaning
       ↓
EDA (Histogram + Heatmap)
       ↓
Encoding
       ↓
Scaling
       ↓
Train-Test Split
       ↓
Regression Models
       ↓
Evaluation
       ↓
Clustering
       ↓
Dashboard
```

---

# Models Used

## 1. Linear Regression

* R² Score: 0.911
* Used for baseline prediction.

## 2. Random Forest Regressor

* R² Score: 0.997
* Best-performing model.

---

# Key Insights

* Session Duration strongly affects calories burned.
* HR Intensity has major influence.
* Effective MET contributes significantly.
* Random Forest outperformed Linear Regression.

---

# Clustering Results

Used:

* PCA for dimensionality reduction
* KMeans clustering

### Cluster Groups

| Cluster   | User Type              |
| --------- | ---------------------- |
| Cluster 0 | Moderate Users         |
| Cluster 1 | Beginner / Yoga Users  |
| Cluster 2 | Advanced Workout Users |

### Silhouette Score

0.417 — Indicates good cluster separation.

---

# Streamlit Dashboard

Dashboard includes:

* Dataset Overview
* EDA Analysis
* Model Comparison
* Feature Importance
* Cluster Visualization
* Project Insights

---

# Project Structure

```text
Fitbit/
│
├── app.py
├── Fitbit_dataset.csv
├── actual_vs_predicted.png
├── cluster_plot.png
├── ml_project.ipynb
├── pages/
│   ├── 1_Dataset_Overview.py
│   ├── 2_EDA_Analysis.py
│   ├── 3_Model_Comparison.py
│   ├── 4_Clustering.py
│   ├── 5_Project_Insights.py
```

---

# Installation

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

---

# Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit

---

# Business Impact

This project helps:

* Fitness applications
* Health analytics systems
* Personal trainers
* Workout recommendation systems

---

# Future Scope

* Real-time wearable device integration
* Personalized workout recommendations
* Live prediction system
* AI-based health assistant

---

# Author

Your Name
Machine Learning Project — Fitness Analytics

---

# Conclusion

This project successfully demonstrates:

* Machine Learning Regression
* Clustering Analysis
* Feature Engineering
* Data Visualization
* Dashboard Development

Random Forest achieved the best performance with 99.7% accuracy.
