# 🏥 AI-Assisted Patient Discharge Education Generator

This project is a **Python-based AI application** that helps healthcare professionals generate clear, patient-friendly discharge education materials. Using the **OpenAI API** and a **Streamlit web interface**, the tool transforms clinician-provided context into structured, empathetic discharge instructions tailored to patient needs.

The application supports role-aware prompting, tone control, and language-level customization to improve patient understanding and continuity of care.

---

## ✨ Features

* AI-generated patient discharge instructions
* Role-aware input (Doctor, Nurse, PA, NP)
* Customizable:

  * Procedure type
  * Patient age
  * Discharge context
  * Language level
  * Education tone
* Real-time web UI with **Streamlit**
* Secure environment configuration using **python-dotenv**
* Streaming AI responses (optional)

---

## 🛠 Tech Stack

* **Python 3.11.8**
* **OpenAI API**
* **Streamlit**
* **uv** (fast dependency management)
* **python-dotenv**

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Jessica-ovabor/patient-discharge-education.git
cd patient-discharge-education
```

### 2️⃣ Install dependencies using `uv`

```bash
uv sync
```

> If `uv` is not installed:

```bash
pip install uv
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_BASE_URL=openai_api_base_url_if_applicable
```

⚠️ Do **not** commit your `.env` file to source control.

---

## 🚀 Running the Application

Start the Streamlit app:

```bash
streamlit run app/streamlit.py
```

Then open the provided local URL in your browser.

---

## 🧠 How It Works

1. Clinician selects their role
2. Patient and discharge details are entered
3. Inputs are stored in `st.session_state`
4. A structured prompt is built using:

   * System instructions
   * Role context
   * Patient-specific details
5. OpenAI generates tailored discharge education text
6. Output is rendered in real-time using Markdown

---

## 🧾 Example Prompt Structure

**System Prompt (Example):**

```text
You are a healthcare education assistant who provides safe, clear, and empathetic patient discharge instructions.
```

**User Context (Generated):**

```text
Procedure Type: Appendectomy
Patient Age: 45
Discharge Context: Post-operative
Language Level: Simple
Education Tone: Empathetic
```

---

## 📁 Project Structure

```text
app
├── discharge_tool.ipynb
├── streamlit.py
├── .env
├── README.md
```

---

## 🛡 Safety & Disclaimer

⚠️ **This application is for educational and support purposes only.**
It does **not** replace professional medical judgment or institutional discharge protocols.

Always review and validate AI-generated content before sharing with patients.

---

## 📄 License

This project is intended for **experimental use**.
You are free to modify and extend it for your own learning or internal tools.

---

