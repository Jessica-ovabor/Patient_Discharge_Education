import streamlit as st
from openai import OpenAI
from IPython.display import display, Markdown, update_display
from dotenv import load_dotenv
import os

load_dotenv()

# Set OpenAI API key from environment variable
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL")

# Streamlit
st.set_page_config(page_title="Patient Discharge Education Generator", page_icon="🏥")

st.header("AI-Assisted Patient Discharge Education Generator", divider="rainbow")
st.selectbox(
    "Select user role:",
    ["Doctor", "Nurse", "Physician Assistant", "Nurse Practitioner"],
)
st.write("Provide patient details below to generate discharge instructions.")
procedure_type = st.text_input(
    "Procedure Type", placeholder="e.g., Appendectomy, Hip Replacement"
)
patient_age = st.number_input("Patient Age", min_value=0, max_value=120, step=1)
discharge_context = st.text_input(
    "Discharge Context", placeholder="e.g., Chronic,Post-operative, Follow-up"
)
language_level = st.text_input(
    "Language Level", placeholder="e.g., Simple, Medical Terminology"
)
education_tone = st.text_input(
    "Education Tone", placeholder="e.g., Empathetic, Formal, Casual"
)
st.session_state["patient_details"] = (
    f"Procedure Type: {procedure_type}\nPatient Age: {patient_age}\nDischarge Context: {discharge_context}\nLanguage Level: {language_level}\nEducation Tone: {education_tone}"
)


if st.button("Generate Discharge Instructions"):
    st.info("Generating discharge instructions...")

    # Initialize OpenAI client
    client = OpenAI(base_url=base_url, api_key=api_key)

    # Create a chat completion request
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates patient discharge instructions."},
            {"role": "user", "content": st.session_state.get("patient_details", "")}
        ],
        stream=True
    )
    placeholder = st.empty()
    content = ""

    for chunk in response:
        chunk_message = chunk.choices[0].delta.content or ""
        content += chunk_message
        placeholder.markdown(content)
       
  
