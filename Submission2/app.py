import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="AutoModeler AI", layout="wide")
st.title("AutoModeler AI 🤖")

st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
model_type = st.sidebar.selectbox("Choose Model Type", ["Auto", "Regression", "Classification"])
api_base_url = st.sidebar.text_input("API URL", value="http://localhost:8000")
enable_ai_judge = st.sidebar.checkbox("Enable AI Judge", value=True)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview", df.head())
    task_description = st.text_input("Describe your task (e.g., 'Predict housing prices')")

    if task_description:
        st.write("### Chatbot: Analyzing your task...")
        files = {'file': uploaded_file.getvalue()}
        response = requests.post(f"{api_base_url}/train_model", files={'file': uploaded_file}, data={'model_type': model_type})

        if response.status_code == 200:
            model_info = response.json()
            st.write("### Model Trained Successfully!")
            st.write(f"Model Type: {model_info['model_type']}")
            st.write(f"Training Metrics: {model_info['metrics']}")
            st.write(f"Performance Summary: {model_info['performance_summary']}")

            if enable_ai_judge:
                judge_response = requests.post(f"{api_base_url}/judge", json=model_info)
                if judge_response.status_code == 200:
                    judge_result = judge_response.json()
                    st.write("### AI Judge Evaluation")
                    st.write(f"Judge Score: {judge_result['score']}")
                    st.write(f"Suggestions: {judge_result['suggestions']}")
                else:
                    st.write("AI Judge Evaluation failed.")
        else:
            st.write("Error in training the model.")
else:
    st.write("Please upload a CSV file to get started.")

st.markdown("### Contact")
st.markdown("For any questions, contact: vb46901n@pace.edu")
