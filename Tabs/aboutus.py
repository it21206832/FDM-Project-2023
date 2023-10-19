# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:37:31 2023

@author: tharu
"""

# Import necessary modules
import streamlit as st
import requests  # Add this import
import json
from streamlit_lottie import st_lottie


def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("About Us ")

    # Add image to the home page
 
    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
    <h3>Our Mission</h3>
           Our mission is simple yet impactful: 
               to provide accurate, accessible, and user-friendly tools that enable people to assess their risk of diabetes.
               By putting the latest advancements in data science and healthcare technology to work, we aim to make diabetes risk assessment easy, informative, and actionable.
        </p>
    """, unsafe_allow_html=True)
    
    
    st.markdown(
        
    """
    <p style="font-size:30px;">
    <h3>Our Team</h3>
          Our team comprises three enthusiastic undergraduate students pursuing degrees in Data Science at SLIIT, collaborating on an FDM (3rd Year Project) initiative. 
          Although we are still on our academic journey, we share a collective aspiration: to create a meaningful impact on the lives of individuals susceptible to diabetes.
        </p>
    """, unsafe_allow_html=True)
    
    lottie_coding = load_lottieurl("https://lottie.host/292f93b0-28ad-49a9-88dd-be55af3ae732/wjHIIx2YT6.json")
    

    st_lottie(lottie_coding, width=500, height=500)
    
    
    
    
    
    
    
    
    
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()    
    
    