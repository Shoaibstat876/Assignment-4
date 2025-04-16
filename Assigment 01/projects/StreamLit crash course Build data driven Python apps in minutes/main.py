import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Streamlit Crash Course", layout="wide")

# Title & Description
st.title("🚀 Streamlit Crash Course")
st.subheader("Build Data-Driven Python Web Apps in Minutes!")

# Welcome Message
st.markdown("""
Welcome to your **Streamlit Crash Course Project**.
This app demonstrates **text formatting**, **widgets**, **data display**, and even **ML model placeholders** – all in one place.
""")

# --- TEXT FORMATTING ---
st.header("📝 Text Formatting")
st.markdown("""
- **Bold Text**
- *Italic Text*
- `Code snippet`
> Blockquote
""")

# --- WIDGETS ---
st.header("🧰 Interactive Widgets")

name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, {name}! 👋")

age = st.slider("Select your age", 0, 100, 25)
st.info(f"Your age is {age}")

option = st.selectbox("Favorite Language", ["Python", "JavaScript", "C++", "Other"])
st.write(f"You selected: {option}")

if st.checkbox("Show random chart"):
    data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
    st.line_chart(data)

# --- DISPLAYING DATA ---
st.header("📊 Displaying Data & Styling")

df = pd.DataFrame({
    "City": ["New York", "London", "Tokyo", "Karachi"],
    "Temperature": [21, 18, 27, 32]
})
st.dataframe(df.style.highlight_max(axis=0))

# --- VISUALIZATION ---
st.header("📈 Data Visualization")

chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["X", "Y", "Z"]
)
st.area_chart(chart_data)

# --- LAYOUT ---
st.header("📐 Layout Options")
col1, col2 = st.columns(2)
with col1:
    st.button("Click Me!")
with col2:
    st.write("Column 2 here!")

# --- MACHINE LEARNING PLACEHOLDER ---
st.header("🤖 Machine Learning Model Placeholder")

uploaded = st.file_uploader("Upload CSV for prediction")
if uploaded:
    st.success("File uploaded! Ready for ML model...")

st.sidebar.title("📚 Navigation")
st.sidebar.info("This is a beginner-friendly Streamlit App")

st.balloons()
