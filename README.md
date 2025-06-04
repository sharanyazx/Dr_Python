
# Dr.py – Your AI-Powered Code Doctor

Dr.py is an AI-powered code reviewer built with Python and Streamlit that helps developers analyze Python and Machine Learning projects.  
It combines traditional static analysis with intelligent AI feedback to provide meaningful suggestions and catch ML-specific issues.

---

# #Features

- ✅ **Code Quality Analysis** 
  Linting, style checks, and syntax analysis using Pylint.

- 🤖 **AI Code Suggestions**  
  Uses a Large Language Model (like OpenAI/Gemini) to generate contextual suggestions and improvements.

- 📊 **ML Model Analysis**  
  Custom logic to detect common issues in ML code: improper preprocessing, poor model practices, and more.

- 📁 **Drag & Drop UI**  
  Upload a `.py` file and get instant insights — no prompt engineering required.

---

## 🛠 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **AI Integration**: OpenAI / Gemini API  
- **Code Analysis**: AST (Abstract Syntax Tree), `pylint`, `subprocess`  
- **ML Logic Engine**: Custom static + semantic pattern matcher
---

## 🔧 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/drpy.git
   cd drpy
