# main.py

import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def main():
    st.set_page_config(page_title="BMI Calculator", page_icon="🧮", layout="centered")
    st.title("🧮 Body Mass Index (BMI) Calculator")
    st.markdown("### Enter your weight and height to calculate your BMI")

    weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.5)
    height = st.number_input("Enter your height (m)", min_value=0.5, step=0.01)

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI is **{bmi}**")

            # Display category
            if bmi < 18.5:
                st.warning("You are **underweight**.")
            elif 18.5 <= bmi < 24.9:
                st.success("You have a **normal** weight.")
            elif 25 <= bmi < 29.9:
                st.warning("You are **overweight**.")
            else:
                st.error("You are in the **obese** category.")
        else:
            st.error("Height must be greater than 0.")

if __name__ == '__main__':
    main()
