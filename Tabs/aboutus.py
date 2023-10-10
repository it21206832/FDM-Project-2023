# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:37:31 2023

@author: tharu
"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("about Us")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
           about us.
        </p>
    """, unsafe_allow_html=True)