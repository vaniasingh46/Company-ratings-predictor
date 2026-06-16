# Company Ratings Predictor

## Overview

Company Ratings Predictor is an end-to-end Machine Learning project that predicts company ratings using company-related information collected through web scraping. The project covers the complete ML pipeline, including data collection, data preprocessing, model training, evaluation, and prediction.

## Project Workflow

### 1. Web Scraping

Data was collected from online sources using web scraping techniques. Relevant company information was extracted and stored for further analysis.

### 2. Data Preprocessing

The collected data was cleaned and prepared for machine learning by:

* Handling missing values
* Removing inconsistencies
* Selecting relevant features
* Converting data into a suitable format for model training

### 3. Model Training

A machine learning model was trained using the processed dataset to learn relationships between company features and company ratings.

### 4. Model Evaluation

The model's performance was evaluated using regression metrics to measure prediction accuracy.

### 5. Prediction Interface

A user-friendly interface was developed to allow users to enter company information and receive predicted company ratings.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Web Scraping
* Git & GitHub

## Project Structure

```text
projectml/
│
├── frontend.py
├── company_rating_model.pkl
├── dataset.csv
├── requirements.txt
└── README.md
```

## Features

* Automated data collection through web scraping
* Data cleaning and preprocessing
* Machine learning-based rating prediction
* Interactive prediction interface
* Model persistence using Joblib

## Installation

Clone the repository:

```bash
git clone https://github.com/vaniasingh46/Company-ratings-predictor.git
```

Move to the project directory:

```bash
cd Company-ratings-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

```bash
streamlit run frontend.py
```

The application will start in your browser and allow users to predict company ratings.

## Future Improvements

* Collect larger datasets through web scraping
* Improve prediction accuracy
* Add more company-related features
* Deploy the application online
* Explore advanced machine learning models
*Improve frontend

