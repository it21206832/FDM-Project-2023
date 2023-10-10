# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:43:44 2023

@author: tharu
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report

st.cache_data 
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('dataset_new.csv')

    # Perform feature and target split
    X = df[["Pregnancies","Glucose", "BloodPressure","SkinThickness","Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]]
    Y = df['Outcome']

    return df, X, Y

st.cache_data 
def split_data(X,Y):
  X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2)
  return X_train,Y_train,Y_test,X_test


st.cache_data  
def train_model(X_train, Y_train, n_estimators=100, max_depth=10, random_state=100):

  # Create a Random Forest classifier
  rf = RandomForestClassifier(n_estimators= 10 , max_depth=5 , random_state=0)

  # Training the Random Forest Classifier
  rf.fit(X_train, Y_train)

  # Accuracy score on the training data
  X_train_prediction = rf.predict(X_train)
  training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

  return rf, training_data_accuracy





def evaluate_model(rf, X_test, Y_test):
   
    # Make predictions on the test data
    predictions = rf.predict(X_test)

    # Calculate the accuracy score
    test_data_accuracy = accuracy_score(predictions,Y_test)

    # Generate a classification report
    report = classification_report(Y_test, predictions)
    
    return test_data_accuracy