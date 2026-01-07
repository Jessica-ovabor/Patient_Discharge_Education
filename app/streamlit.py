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
user_role = st.selectbox(
    "Select user role:",
    ["Doctor", "Nurse", "Physician Assistant", "Nurse Practitioner"],
)
st.session_state["user_role"] = user_role
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

system_prompt = f""" You are an expert AI medical assistant specializing in generating patien discharge education materials. Your task is to create clear, concise discharge instructions based on the following patient details, ensuring the content is tailored to the specified language level and tone.
Do not include information not provided in the patient details.
Take into account the user role and adjust the instructions accordingly.
Your response should be structured with headings and bullet points for easy readability. It should include the patient details before the discharge instructions.
Example format:
I am provided with the following patient details:
- Procedure Type: Appendectomy
- Patient Age: 45
- Discharge Context: Post-operative
- Language Level: Simple
- Education Tone: Empathetic
Based on these details, here are the discharge instructions
Always prioritize patient safety and clarity in your instructions.
Make sure the content generated are not generic but specific to the patient details provided.
Add a disclaimer at the end: "These instructions are for informational purposes only and do not replace professional medical advice. Always follow your healthcare provider's recommendations."
"""
user_prompt = f"""
I am currently acting as a {st.session_state['user_role']}. Please generate discharge instructions based on the following patient details:
{st.session_state['patient_details']}.
"""
if st.button("Generate Discharge Instructions"):
    st.info("Generating discharge instructions...")

    # Initialize OpenAI client
    client = OpenAI(base_url=base_url, api_key=api_key)

    # Create a chat completion request
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        stream=True,
    )
    placeholder = st.empty()
    content = ""

    for chunk in response:
        chunk_message = chunk.choices[0].delta.content or ""
        content += chunk_message
        placeholder.markdown(content)
