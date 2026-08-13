# Brain Tumor Detection Using AI

An AI-based brain tumor detection system that uses deep learning to classify MRI brain images into four categories: **Glioma Tumor, Meningioma Tumor, Pituitary Tumor, and No Tumor**.

## Features

* Multi-class brain tumor classification
* MRI image preprocessing and normalization
* CNN-based deep learning model
* ResNet50 transfer learning
* Data augmentation to improve generalization
* FastAPI backend for model inference
* Simple HTML/CSS/JavaScript frontend
* Upload an MRI image and receive a predicted class

## Tech Stack

* **Python**
* **TensorFlow / Keras**
* **CNN**
* **ResNet50**
* **NumPy**
* **Pandas**
* **PIL**
* **FastAPI**
* **HTML, CSS, JavaScript**
* **Google Colab**

## Classes

The model predicts one of the following:

1. Glioma Tumor
2. Meningioma Tumor
3. No Tumor
4. Pituitary Tumor

## Project Workflow

**MRI Image → Preprocessing → Deep Learning Model → Classification → Prediction**

Images are resized to **224 × 224 pixels**, normalized, and passed to the trained model for classification.

## Backend

The trained Keras model is integrated with **FastAPI**. The API accepts an uploaded MRI image, preprocesses it, runs inference, and returns the predicted tumor category.

## Frontend

A basic web interface allows users to upload an MRI image and view the model's prediction.

## Future Improvements

* Improve model accuracy with larger datasets
* Add confidence scores
* Improve frontend design
* Deploy the application online
* Add detailed prediction reports

**Note:** This project is intended for educational and research purposes and should not be used as a substitute for professional medical diagnosis.
