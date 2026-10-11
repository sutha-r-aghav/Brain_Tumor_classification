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
