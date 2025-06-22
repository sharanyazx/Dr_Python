import streamlit as st
import ast
import subprocess
import tempfile
import os
from code_review import analyze_code_quality, ai_code_suggestions
from model_analysis import analyze_ml_code

st.set_page_config(page_title="Dr.Python", layout="wide")
st.title("🩺 Dr Python  : AI-Powered Code Reviewer")

uploaded_file = st.file_uploader("Upload your Python or ML project file (.py)", type=["py"])


if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    with open(tmp_path, 'r') as f:
        code = f.read()

    st.subheader("🔍 Code Quality Analysis")
    lint_output = analyze_code_quality(tmp_path)
    st.code(lint_output, language="bash")

    st.subheader("🤖 AI-Powered Code Suggestions")
    suggestions = ai_code_suggestions(code)
    st.markdown(suggestions)

    st.subheader("📊 ML Model Analysis")
    model_analysis = analyze_ml_code(code)
    st.markdown(model_analysis)
else:
    st.warning("Please upload a file to analyze.")
