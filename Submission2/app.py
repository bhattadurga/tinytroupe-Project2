import streamlit as st
import requests
import pandas as pd

# Set the page title and layout
st.set_page_config(page_title="AutoModeler AI", layout="wide")
st.title("AutoModeler AI 🤖")

# Sidebar - file upload
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Sidebar - model type selection
model_type = st.sidebar.selectbox("Choose Model Type", ["Auto", "Regression", "Classification"])

# API URL for backend FastAPI
api_base_url = st.sidebar.text_input("API URL", value="http://localhost:8000")

# Checkbox to enable AI Judge for evaluating models
enable_ai_judge = st.sidebar.checkbox("Enable AI Judge", value=True)

# Chatbot message container
if uploaded_file is not None:
    # Load and display the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview", df.head())

    # Ask the user to describe the objective (Regression or Classification)
    task_description = st.text_input("Describe your task (e.g., 'Predict housing prices' or 'Classify housing prices')")

    if task_description:
        # Process the task and send to FastAPI backend
        st.write("### Chatbot: Analyzing your task...")

        # Prepare the data for the request
        files = {'file': uploaded_file}
        response = requests.post(f"{api_base_url}/train_model", files=files, data={'model_type': model_type})

        if response.status_code == 200:
            # If training is successful, display the model and performance metrics
            model_info = response.json()
            st.write("### Model Trained Successfully!")
            st.write(f"Model Type: {model_info['model_type']}")
            st.write(f"Training Metrics: {model_info['metrics']}")
            st.write(f"Model: {model_info['model']}")
            st.write(f"Performance Summary: {model_info['performance_summary']}")

            # Optionally, evaluate the model with AI Judge if enabled
            if enable_ai_judge:
                judge_response = requests.post(f"{api_base_url}/judge", json={'model': model_info['model']})
                if judge_response.status_code == 200:
                    judge_result = judge_response.json()
                    st.write("### AI Judge Evaluation")
                    st.write(f"Judge Score: {judge_result['score']}")
                    st.write(f"Suggestions: {judge_result['suggestions']}")
                else:
                    st.write("AI Judge Evaluation failed.")
        else:
            st.write("Error in training the model. Please try again.")
else:
    st.write("Please upload a CSV file to get started.")

# Footer for contact or additional information
st.markdown("### Contact")
st.markdown("For any questions or contributions, please reach out to: vb46901n@pace.edu")
