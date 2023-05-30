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
    st.title("BMI Calculator")
    st.write("Enter your weight and height to calculate your BMI.")

    weight = st.number_input("Weight (in kg)")
    height = st.number_input("Height (in meters)")

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = interpret_bmi(bmi)

        st.write(f"Your BMI: {bmi:.2f}")
        st.write(f"Category: {category}")

if __name__ == "__main__":
    main()
