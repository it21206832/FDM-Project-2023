# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 07:52:13 2023

@author: tharu
"""
import streamlit as st
from myfunction import load_data, split_data, train_model # Import evaluate_model as well
from Tabs import data,predict,Home,aboutus,visualise_data

st.set_page_config(
    page_title = 'Diabetes Prediction',
    page_icon = 'random',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

Tabs = {
    "Home": Home,
    "Prediction": predict,
    "Data Info": data,

    "Visualisation": visualise_data,
    "About Us": aboutus
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))



# Loading the dataset.
df, X, Y = load_data()
X_train, Y_train, Y_test, X_test = split_data(X, Y)
rf, training_data_accuracy = train_model(X_train, Y_train)


# Call the app function of the selected page to run
if page == "Prediction":
    Tabs[page].app(df, rf, X_test, Y_test)
elif page == "Visualisation":
    Tabs[page].app(df, X, Y)
elif page == "Data Info":
    Tabs[page].app(df)
else:
    Tabs[page].app()

    