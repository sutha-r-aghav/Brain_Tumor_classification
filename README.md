# 🧠 Brain Tumor Detection Using Deep Learning

A deep learning project that classifies brain MRI images into four categories using Convolutional Neural Networks (CNN) and ResNet50 transfer learning.

## 📌 Project Overview

Brain tumor classification from MRI images is an important computer vision research task. This project explores deep learning techniques to classify MRI images into four categories.

The project includes trained models, a web interface, and a FastAPI backend for image prediction.

**Project highlights**
- Multi-class brain MRI image classification
- CNN-based image classification
- ResNet50 transfer learning
- Image preprocessing and prediction
- FastAPI backend integration
- Web-based user interface

## 🎯 Classification Classes

The models are designed to classify images into the following categories:

1. Glioma Tumor
2. Meningioma Tumor
3. No Tumor
4. Pituitary Tumor

## 🛠️ Technologies Used

- **Programming:** Python
- **Deep Learning:** TensorFlow / Keras
- **Model Architecture:** CNN and ResNet50 transfer learning
- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **Dataset:** Kaggle Brain Tumor MRI Dataset
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

*Update the filenames above to match your actual repository.*

The trained ResNet50 model is hosted separately on Hugging Face because of its large file size.

## 📊 Dataset

**Brain Tumor MRI Dataset — Masoud Nickparvar**

Dataset link: [View and download the dataset on Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

The dataset contains MRI images organized into four classes: glioma, meningioma, pituitary tumor, and no tumor.

The images are used for training and evaluating the classification models.

Please refer to the original dataset page for licensing, attribution, and usage conditions.

## 🤖 Trained Models

### 1. CNN Model

A custom Convolutional Neural Network designed to learn visual features from MRI images and classify them into four categories.

### 2. ResNet50 Transfer Learning Model

A ResNet50-based model using transfer learning for MRI image classification.

**Model repository:** [View the trained model on Hugging Face]((https://huggingface.co/Raxxxxxyyyyy/Brain_Tumor_Detection))

- Format: Keras (`.keras`)
- Input image size: 224 × 224 pixels
- Output: Four-class classification

Replace the link above with your actual Hugging Face repository URL. Confirm the input size and model configuration against your saved model before publishing.

## ⚙️ How the Project Works

1. The user uploads a brain MRI image through the frontend.
2. The frontend sends the image to the FastAPI backend.
3. The backend preprocesses the image, including resizing and normalization as required by the model.
4. The trained model generates class predictions.
5. The predicted class is returned to the frontend and displayed to the user.

## 🚀 Running the Project Locally

### Prerequisites

- Python installed
- Required Python libraries
- Frontend files
- Access to the trained model files

### 1. Install dependencies

Open a terminal in the backend directory and run:

```bash
pip install -r requirements.txt
```

### 2. Configure the model path

Place the downloaded model in the location expected by the backend, or update the model-loading path in `app.py`.

If the model is hosted on Hugging Face, download it first or configure a supported loading method.

### 3. Start the FastAPI backend

From the backend directory, run:

```bash
uvicorn app:app --reload
```

The API should be available at:

`http://127.0.0.1:8000`

FastAPI interactive API documentation is typically available at:

`http://127.0.0.1:8000/docs`

### 4. Open the frontend

Open your HTML entry file in a browser, or serve the frontend locally using a development server. Ensure the frontend API URL matches the backend address and that CORS is configured appropriately.

## 📈 Model Evaluation

Model performance should be assessed using appropriate evaluation metrics, including:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Add your actual test-set results and confusion matrix here after evaluation. No performance figures are reported in this README because verified results have not been provided.

## ⚠️ Limitations and Responsible Use

This project is intended for educational and research purposes. It is not a medical diagnostic system and must not be used to make clinical decisions.

Performance on a public dataset does not establish clinical reliability. Real-world use would require rigorous external validation and appropriate medical oversight.

## 🔮 Future Improvements

- Improve generalization using additional and diverse MRI datasets.
- Compare CNN and ResNet50 performance using the same test set.
- Add clearer prediction confidence and model evaluation reporting.
- Deploy the frontend and backend for an accessible demonstration.
- Improve error handling and input validation.

## 👨‍💻 Author

**Raghav Suthar**

Computer Science and Engineering — AI & Data Science

NIT Kurukshetra

## 📄 License and Attribution

The dataset remains subject to its original license and attribution requirements. Add a license for your own source code only after choosing one that you have the right to apply.

---

If you find this project useful, feel free to explore the code, model repository, and dataset linked above.
