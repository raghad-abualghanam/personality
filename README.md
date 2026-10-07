Behind the Personality : Predicting Introversion & Extroversion

Project Overview

This project explores behavioral patterns related to personality and uses Machine Learning to predict whether a person is an Introvert or an Extrovert.

The project focuses on understanding how daily social behaviors such as time spent alone, social event attendance, going outside, and friends circle size are related to personality.

Dataset

The dataset contains 2,900 records and 8 columns.

Features

Time_spent_Alone
Stage_fear
Social_event_attendance
Going_outside
Drained_after_socializing
Friends_circle_size
Post_frequency

Target

Personality

Introvert
Extrovert

Exploratory Data Analysis

The dataset was explored by checking:

Dataset shape and columns
Missing values
Duplicate records
Descriptive statistics
Behavioral patterns between Introverts and Extroverts
The relationship between Stage Fear and Personality

Key Findings

Introverts spend more time alone on average than Extroverts.

Extroverts attend social events more frequently on average than Introverts.

Stage Fear shows a strong relationship with Personality in this dataset.

Machine Learning

A Logistic Regression model was used to predict personality type.

The model achieved approximately 92.4% accuracy on the test data.

Streamlit Application

A simple Streamlit application was created to allow users to enter behavioral information and receive a personality prediction.

The application predicts:

Introvert

or

Extrovert

Technologies Used

Python
Pandas
Scikit-learn
Matplotlib
Jupyter Notebook
Streamlit
Joblib

Project Files

personality.ipynb
personality_dataset.csv
personality_model.pkl
app.py

Author

raghad-abualghanam
