# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:40:54 2023

@author: tharu
"""

"""This modules contains data about the visualization page"""

# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_lottie import st_lottie  # Import st_lottie
import requests  

# Import necessary functions from web_functions
# Import your functions from myfunction.py
from myfunction import train_model, load_data

def app(df, X, Y):
    """This function creates the visualization page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualize the Diabetes Prediction Web app")

    # Load Lottie animation
    lottie_coding = load_lottieurl("https://lottie.host/a8916b30-1f36-4deb-be31-122ab42dac76/g0seIisTOK.json")
    st_lottie(lottie_coding, width=700, height=500)

    # Create a checkbox to show the correlation heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")

        fig = plt.figure(figsize=(10, 6))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot=True)  # Creating an object of seaborn axis and storing it in 'ax' variable
        bottom, top = ax.get_ylim()  # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5)  # Increasing the bottom and decreasing the top margins respectively.
        st.pyplot(fig)

    if st.checkbox("Glucose Level vs Blood Pressure Plot"):
        fig = plt.figure(figsize=(10, 6))
        sns.color_palette("rocket", as_cmap=True)
        ax = sns.scatterplot(x="Glucose", y="BloodPressure", data=df)
        st.pyplot(fig)

    if st.checkbox("SkinThickness Level vs Insulin"):
        fig = plt.figure(figsize=(10, 6))
        sns.color_palette("rocket", as_cmap=True)
        ax = sns.scatterplot(x="SkinThickness", y="Insulin", data=df)
        st.pyplot(fig)

    if st.checkbox("Blood Pressure Level vs Skin Thickness Plot"):
        fig = plt.figure(figsize=(10, 6))
        sns.color_palette("rocket")
        ax = sns.scatterplot(x="BloodPressure", y="SkinThickness", data=df)
        st.pyplot(fig)

    if st.checkbox("Show Histogram"):
        fig = plt.figure(figsize=(10, 6))
        sns.color_palette("rocket", as_cmap=True)
        ax = sns.histplot(data=df, x="Age", y="BloodPressure")
        st.pyplot(fig)

def load_lottieurl(url: str):
    re = requests.get(url)
    if re.status_code != 200:
        return None
    return re.json()
