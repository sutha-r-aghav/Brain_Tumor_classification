from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from tensorflow.keras.models import load_model

from PIL import Image
import numpy as np
import io

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load_model("../Models/ResNet50.keras")

class_names = [
    "Glioma Tumor",
    "Meningioma Tumor",
    "No Tumor",
    "Pituitary Tumor"
]


def preprocess_image(image):

    image = image.convert("RGB")

    image = image.resize((224, 224))

    image = np.array(image)

  

    image = np.expand_dims(image, axis=0)

    return image


@app.get("/")
def home():
    return {"message": "Brain Tumor Detection API Running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image_bytes = await file.read()

    image = Image.open(io.BytesIO(image_bytes))

    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image)

    predicted_index = np.argmax(prediction)

    confidence = float(np.max(prediction) * 100)

    return {
        "prediction": class_names[predicted_index],
        "confidence": round(confidence, 2),
        "probabilities": {
            class_names[i]: round(float(prediction[0][i] * 100), 2)
            for i in range(len(class_names))
        }
    }

#source venv/bin/activate