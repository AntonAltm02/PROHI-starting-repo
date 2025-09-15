import streamlit as st
import neurokit2 as nk
import pandas as pd

st.set_page_config(
    page_title="Dashboard", layout="wide"
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a Page")

# # Page information
st.write("Synthetic NeuroKit2 Signals")

# Input widgets
duration = st.sidebar.slider("Duration (sec)", 5, 30, 10)
heart_rate = st.sidebar.slider("Heart Rate (bpm)", 50, 120, 70)
fs = st.sidebar.selectbox("Sampling Rate (Hz)", [250, 500, 1000], index=1)

# Generate synthetic ECG
ecg = nk.ecg_simulate(duration=duration, sampling_rate=fs, heart_rate=heart_rate)
time = pd.Series(range(len(ecg))) / fs
ecg_df = pd.DataFrame({"Time (s)": time, "ECG": ecg})

# Data element
st.subheader("Data Sample")
st.dataframe(ecg_df.head())

# Chart
st.subheader("ECG Plot")
st.line_chart(ecg_df, x="Time (s)", y="ECG")
