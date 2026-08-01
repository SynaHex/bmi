import google.genai as genai
import streamlit as st

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]   # Replace with your actual API key

client = genai.Client(api_key=GOOGLE_API_KEY)

st.title("BMI Calculator with AI Nutritionist")

wt = st.number_input("Enter your weight in kilograms:", min_value=10.0)
ht = st.number_input("Enter your height in meters:", min_value=0.5)

if st.button("Analyse your BMI with AI"):

    height_m = ht / 100
    bmi = wt / ((ht/100) ** 2)

    st.write(f"Your BMI is: {bmi:.2f}")

    prompt = f"Act like an expert nutritionist and fitness coach. My weight is {wt} kg, my height is {ht} meters, and my BMI is {bmi:.2f}. Analyze my BMI, tell me my BMI category, explain whether it is healthy, mention any possible health risks, provide diet and exercise recommendations, suggest daily water intake, lifestyle improvements, and end with a short motivational message. Keep the response simple, beginner-friendly, and under 250 words. Do not provide medical diagnoses or prescribe medication."

    st.write("Waiting for AI response...")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )


    st.write(response.text)