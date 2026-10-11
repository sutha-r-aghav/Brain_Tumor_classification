# 🧠 Brain Tumor Detection Using Deep Learning

A deep learning project that classifies brain MRI images into four categories using a custom Convolutional Neural Network (CNN) and ResNet50 transfer learning, with a web interface and FastAPI backend.

## 📌 Project Overview

Brain tumor classification from MRI scans is an important computer vision task. This project explores deep learning techniques to classify MRI images into four categories and provides a web interface for users to upload an image and receive a model prediction.

### Key Features

- Multi-class brain MRI image classification
- Custom CNN model
- ResNet50 transfer learning model
- Image preprocessing and prediction
- FastAPI backend
- HTML, CSS, and JavaScript frontend
- Trained model hosted on Hugging Face

## 🎯 Classification Categories

The project classifies MRI images into four categories:

1. Glioma Tumor
2. Meningioma Tumor
3. No Tumor
4. Pituitary Tumor

## 🛠️ Tech Stack

- **Language:** Python
- **Deep Learning:** TensorFlow, Keras
- **Model Architectures:** CNN, ResNet50
- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **Dataset:** Kaggle
- **Model Hosting:** Hugging Face

## 📂 Project Structure

```text
brain-tumor-detection/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── models/
│   └── README.md
│
└── README.md
```

*Adjust the filenames to match your actual repository.*

The trained model files are hosted separately to keep the GitHub repository lightweight.

## 📊 Dataset

**Brain Tumor MRI Dataset by Masoud Nickparvar**

🔗 [Access the dataset on Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

The dataset contains brain MRI images belonging to four classes: glioma, meningioma, pituitary tumor, and no tumor.

The images are used for training and evaluating the classification models.

Refer to the original dataset page for its license, attribution requirements, and permitted uses.

## 🤖 Trained Models

### 1. Custom CNN

A Convolutional Neural Network built to learn image features and classify MRI images into four categories.

### 2. ResNet50 Transfer Learning

A ResNet50-based transfer learning model trained for multi-class brain MRI image classification.

🔗 **[View and access the trained model on Hugging Face](https://huggingface.co/Raxxxxxyyyyy/Brain_Tumor_Detection)**

- Model format: Keras (`.keras`)
- Input image size: 224 × 224 pixels, if matching the saved model configuration
- Task: Four-class image classification

Check the Hugging Face repository for the exact model filename and download instructions.

## ⚙️ How It Works

1. The user uploads a brain MRI image through the frontend.
2. The frontend sends the image to the FastAPI backend.
3. The backend preprocesses the image according to the model's requirements.
4. The trained model generates a prediction.
5. The backend returns the prediction to the frontend.
6. The frontend displays the result to the user.

## 🚀 Run Locally

### Prerequisites

- Python installed
- Required Python libraries
- Frontend source files
- Access to the trained model

### 1. Install dependencies

Navigate to the backend directory and install the dependencies:

```bash
pip install -r requirements.txt
```

### 2. Download the model

Download the trained model from the Hugging Face repository:

https://huggingface.co/Raxxxxxyyyyy/Brain_Tumor_Detection

Place the downloaded `.keras` file at the path expected by your backend, or update the model-loading path in `app.py`.

### 3. Start the backend

From the backend directory, run:

```bash
uvicorn app:app --reload
```

The backend should be accessible at:

`http://127.0.0.1:8000`

FastAPI documentation:

`http://127.0.0.1:8000/docs`

### 4. Open the frontend

Open the frontend entry HTML file in a browser or use a local development server. Ensure the frontend API URL matches the running backend and that CORS is configured correctly.

## 📈 Model Evaluation

Model performance should be evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Add your actual test-set results here after evaluation. No accuracy figures are claimed until verified results are available.

## 🔮 Future Improvements

- Compare CNN and ResNet50 using the same held-out test set.
- Improve generalization through additional and diverse MRI datasets.
- Add prediction confidence and clearer evaluation reporting.
- Deploy the frontend and backend for public access.
- Improve input validation and error handling.

## ⚠️ Limitations and Responsible Use

This project is intended for educational and research purposes only. It is not a clinically validated medical diagnostic system and must not be used to make medical decisions.

Performance on a public dataset does not guarantee reliable performance on real-world MRI scans.

## 👨‍💻 Author

**Raghav Suthar**  
Computer Science and Engineering — AI & Data Science  
NIT Kurukshetra

## 📄 Dataset Attribution

Dataset: [Brain Tumor MRI Dataset — Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

Model repository: [Brain Tumor Detection — Hugging Face](https://huggingface.co/Raxxxxxyyyyy/Brain_Tumor_Detection)

---

⭐ If you find this project useful, explore the code, dataset, and trained model linked above.
