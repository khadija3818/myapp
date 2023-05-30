import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.set_page_config(page_title="BMI Calculator", page_icon="🧮")
    st.title("BMI Calculator")
    st.markdown(
        """
        *Body Mass Index (BMI)* is a measure of body fat based on height and weight. 
        It helps determine whether you are underweight, normal weight, overweight, or obese.
        """
    )

    col1, col2 = st.beta_columns(2)

    with col1:
        weight = st.number_input("Weight (in kg)")
    
    with col2:
        height = st.number_input("Height (in meters)")

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = interpret_bmi(bmi)

        st.markdown("---")
        st.subheader("BMI Result")
        bmi_text = f"**Your BMI:** {bmi:.2f}"
        st.markdown(bmi_text, unsafe_allow_html=True)
        category_text = f"**Category:** {category}"
        st.markdown(category_text, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("BMI Categories")
        categories = {
            "Underweight": "BMI < 18.5",
            "Normal weight": "18.5 <= BMI < 25",
            "Overweight": "25 <= BMI < 30",
            "Obese": "BMI >= 30"
        }
        for cat, range_text in categories.items():
            st.markdown(f"- **{cat}:** {range_text}")

if __name__ == "__main__":
    main()
