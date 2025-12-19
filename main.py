
from pydantic import BaseModel
import joblib
import numpy as np
from utils import get_gpt_data
from schemas import CropRequest, ModelRequest
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(title="🌾 Crop Recommendation API")


model = joblib.load("ml_model/crop_model.pkl")
preprocessor = joblib.load("ml_model/preprocessor.pkl")


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict_crop(request: ModelRequest):
    features = np.array([[request.N, request.P, request.K, request.temperature,
                          request.humidity, request.pH, request.rainfall]])
    processed_features = preprocessor.transform(features)
    prediction = model.predict(processed_features)[0]
    return {"recommended_crop": prediction}


@app.post("/predict_with_gpt")
def predict_with_gpt(request: CropRequest):
    gpt_data = get_gpt_data(request.state, request.district)

    temperature = gpt_data.get("temperature")
    humidity = gpt_data.get("humidity")
    rainfall = gpt_data.get("rainfall")

    features = np.array([[request.N, request.P, request.K,
                          temperature, humidity, request.pH, rainfall]])

    processed_features = preprocessor.transform(features)
    prediction = model.predict(processed_features)[0]

    return {
        "location": f"{request.district}, {request.state}",
        "data_used": gpt_data,
        "recommended_crop": prediction
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
