from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from core.trainer import train_model, preprocess_data
from core.judge import evaluate_model
import pickle

app = FastAPI()

# Model type options
class ModelRequest(BaseModel):
    model_type: str

@app.post("/train_model")
async def train_model_endpoint(file: UploadFile = File(...), model_type: str = "auto"):
    # Read the CSV file
    content = await file.read()
    dataset = preprocess_data(content)

    # Train the model
    model, metrics = train_model(dataset, model_type)

    # Save the trained model
    with open('models/saved_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    return {"model_type": model_type, "metrics": metrics, "model": "Model Trained Successfully!"}

@app.post("/predict")
async def predict(data: dict):
    model = pickle.load(open('models/saved_model.pkl', 'rb'))
    prediction = model.predict([data["features"]])
    return {"prediction": prediction}

@app.post("/judge")
async def judge(model: dict):
    model_obj = pickle.load(open('models/saved_model.pkl', 'rb'))
    score, suggestions = evaluate_model(model_obj)
    return {"score": score, "suggestions": suggestions}
