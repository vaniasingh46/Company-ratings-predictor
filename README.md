# Company Ratings Predictor

## Overview

The Company Ratings Predictor is a Machine Learning project that predicts a company's rating based on various company-related features. The project demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, and prediction through a user-friendly interface.

## Features

* Data preprocessing and cleaning
* Machine Learning model training
* Company rating prediction
* Interactive user interface
* Model persistence using Joblib

## Project Structure

projectml/

├── frontend.py

├── company_rating_model.pkl

├── dataset.csv

├── requirements.txt

└── README.md

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

## Machine Learning Workflow

### 1. Data Collection

The dataset contains company-related information used for predicting ratings.

### 2. Data Preprocessing

* Handling missing values
* Feature selection
* Data transformation
* Preparing data for model training

### 3. Model Training

A machine learning model was trained on the processed dataset to learn patterns between company features and ratings.

### 4. Model Evaluation

The model performance was evaluated using standard regression metrics.

### 5. Prediction

Users can input company details and obtain predicted company ratings through the application interface.

## Installation

Clone the repository:

git clone https://github.com/vaniasingh46/Company-ratings-predictor.git

Move to the project directory:

cd Company-ratings-predictor

Install dependencies:

pip install -r requirements.txt

## Running the Application

Run the Streamlit application:

streamlit run frontend.py

The application will open automatically in your browser.

## Future Improvements

* Improve prediction accuracy with additional data
* Deploy the application online
* Add more company-related features
* Implement advanced machine learning models
