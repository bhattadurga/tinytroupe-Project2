# AutoModeler AI 🤖

## Overview
AutoModeler AI is an intelligent end-to-end chatbot application that guides users through building machine learning models based on their data and goals. It features a conversational UI that allows users to upload CSV files, describe their objectives, and receive trained models with performance insights—completely code-free. It dynamically identifies whether the task is regression or classification and handles preprocessing, evaluation, and reporting.

## Features
- **Conversational UI:** Interact with a data science chatbot that understands your problem and guides you through modeling.
- **Dynamic Model Recommendation:** Automatically classifies tasks (e.g., regression vs. classification) and suggests appropriate models.
- **Model Building Pipeline:** Handles missing values, encodes categorical features, scales numerical data, and trains a suitable model.
- **Evaluation Summary:** Outputs performance metrics including R², accuracy, confusion matrix, and p-values.
- **AI Judge:** Evaluates model quality and offers suggestions for improvement.
- **Downloadable Report:** Users can download a PDF report summarizing the model, performance, and visualizations.

## Tech Stack
- **Frontend:** Streamlit (for chatbot interface and file upload)
- **Backend:** Python 3.10, FastAPI
- **ML Libraries:** Scikit-learn, Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Report Generation:** ReportLab
- **AI/LLM Integration:** OpenAI or Hugging Face for conversation interpretation

**Deployment (Bonus):** AWS Lambda + API Gateway

## Installation
## Prerequisites
Make sure you have the following installed:
- Python 3.10+
- pip
- (Optional) Virtual Environment

### Steps
1.Clone the repository:
  ```sh
  git clone https://github.com/your-repo/automodeler-ai.git
  cd automodeler-ai
  ```
2.Create and activate a virtual environment:
  ```sh
  python -m venv venv
  source venv/bin/activate  # On macOS/Linux
  venv\Scripts\activate     # On Windows
  ```
3.Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```
4.Running AutoModeler AI
  Launch the application by running:
  ```sh
  streamlit run app.py
  ```

## Configuration
Adjust these parameters in `app.py` sidebar to customize behavior:
```python
model_type = st.selectbox("Choose Model Type", ["Auto", "Regression", "Classification"])
api_base_url = st.text_input("API URL", value="http://localhost:8000")
enable_ai_judge = st.checkbox("Enable AI Judge", value=True)
```

## Usage
## User Journey
**Scenario 1 (Regression):**
1.User: “I want to predict housing prices.”
AutoModeler: “That sounds like a continuous variable. Would you like to use linear regression?”
→ Backend trains a linear regression model and returns R² and coefficients.

**Scenario 2 (Classification):**
2.User: “I want to classify housing prices into 'low', 'medium', 'high'.”
AutoModeler: “Great, I’ll bin the target variable and apply logistic regression. Shall we proceed?”
→ Backend bins the target and trains logistic regression, returning a confusion matrix and accuracy.

## Code Structure
```
automodeler-ai/
│── api/
│   └── model_api.py          # FastAPI endpoints for model training and evaluation
│── core/
│   └── trainer.py            # Preprocessing and training logic
│   └── judge.py              # Evaluation and metrics generation
│── utils/
│   └── plotter.py            # Visualization functions
│── frontend/
│   └── app.py                # Streamlit application
│── models/
│   └── saved_model.pkl       # Serialized model
│── requirements.txt          # Python dependencies
│── README.md                 # Project documentation
```

## API and AI Integration
- **POST /train_model:** Accepts a CSV dataset and model type, then returns the trained model and metrics.

- **POST /predict:** Accepts new input data and returns predictions using the saved model.

- **POST /judge:** Evaluates the trained model (accuracy, R², confusion matrix, etc.).

**Sample FastAPI Endpoint:**
python
@app.post("/train_model")
def train_model(file: UploadFile, model_type: str):
    ...
LLM Support: Uses OpenAI/HuggingFace models to parse user intent and classify tasks as regression or classification.

Custom Rule Engine: Detects data types and selects modeling approaches in fallback scenarios.

## AWS Deployment (Optional)
You can deploy the FastAPI backend using:
1.Frameworks: serverless, zappa
2.Cloud Tools: AWS Lambda, API Gateway, boto3
3.Testing Tools: Postman, cURL for verifying endpoints

## Troubleshooting
Streamlit fails to load:
```sh
pip install streamlit --upgrade
```
FastAPI not running:


uvicorn api.model_api:app --reload
CORS issues (for frontend-backend communication): Add CORSMiddleware in model_api.py.

## Contribution
1.Fork the repository.
2.Create a feature branch (`git checkout -b feature-name`).
3.Commit your changes (`git commit -m "Add new feature"`).
4.Push to GitHub (`git push origin feature-name`).
5.Submit a Pull Request.

## Contact
For questions or contributions, reach out to: vb46901n@pace.edu
