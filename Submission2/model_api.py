from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from trainer import train_model
from judge import evaluate_model
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/train_model")
async def train_model_api(file: UploadFile = File(...), model_type: str = Form(...)):
    contents = await file.read()
    with open("temp.csv", "wb") as f:
        f.write(contents)

    model_info = train_model("temp.csv", model_type)
    with open("models/saved_model.pkl", "wb") as f:
        pickle.dump(model_info["model"], f)

    return model_info

@app.post("/judge")
async def judge_api(model: dict):
    return evaluate_model(model)
