from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np

app = FastAPI(title="Boston Housing Predictor")

# Setup templates and static files
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Load the model
with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    rm: float = Form(...),
    lstat: float = Form(...),
    ptratio: float = Form(...)
):
    try:
        # Create input array
        features = np.array([[rm, lstat, ptratio]])
        
        # Predict
        prediction = model.predict(features)[0]
        
        # Format the price
        formatted_price = f"${prediction:,.2f}"
        
        return templates.TemplateResponse("index.html", {
            "request": request,
            "prediction_text": f"Estimated House Price: {formatted_price}",
            "rm": rm,
            "lstat": lstat,
            "ptratio": ptratio
        })
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "prediction_text": f"Error: {str(e)}"
        })
