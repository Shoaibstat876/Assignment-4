# main.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Streamlit Dashboard", layout="centered")

st.title("📊 Simple Streamlit Data Dashboard")
st.markdown("### Build a Python Website in 15 Minutes With Streamlit")

# Sidebar
st.sidebar.header("Control Panel")
data_size = st.sidebar.slider("Number of data points", min_value=10, max_value=100, value=50)
chart_type = st.sidebar.selectbox("Chart Type", ["Line", "Bar", "Area"])

# Generate sample data
df = pd.DataFrame({
    "x": np.arange(data_size),
    "y": np.random.randint(0, 100, size=data_size)
})

# Display data
st.subheader("📄 Sample Data")
st.dataframe(df.head())

# Chart
st.subheader("📈 Visualization")

if chart_type == "Line":
    st.line_chart(df.set_index("x"))
elif chart_type == "Bar":
    st.bar_chart(df.set_index("x"))
elif chart_type == "Area":
    st.area_chart(df.set_index("x"))

# Additional
st.subheader("🛠 Additional Features")
if st.checkbox("Show raw data"):
    st.write(df)

st.success("Website built successfully with Streamlit! 🎉")
