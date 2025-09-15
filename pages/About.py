import streamlit as st

st.set_page_config(
    page_title="About", layout="wide"
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a Page")

st.markdown(
"""
    ## Anton

    During this project I analyzed a heart-disease dataset from Mendeley Data containing 1,000 patient records with 
    12 clinical features and a binary target. The goal was to explore patterns and predict early-stage heart disease. 
    I began with data understanding and preprocessing, examining numerical variables such as blood pressure, 
    cholesterol, and heart rate alongside categorical and binary indicators like chest-pain type and 
    exercise-induced angina.

    Unsupervised learning was first applied to uncover latent structure: K-Means and DBSCAN clustering highlighted 
    natural groupings of patients based on cardiovascular risk factors. I then built several supervised models for 
    classification, including Logistic Regression, Random Forest, and XGBoost, comparing performance with metrics
    such as accuracy, precision, and ROC-AUC. The combination of clustering insights and high-performing ensemble 
    classifiers demonstrated how machine-learning techniques can provide actionable support for early detection and 
    risk stratification of heart disease in clinical settings.
"""
)