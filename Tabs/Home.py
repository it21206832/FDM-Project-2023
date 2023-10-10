# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:31:03 2023

@author: tharu
"""

# Import necessary modules
import streamlit as st
import requests  # Add this import
import json
from streamlit_lottie import st_lottie


def app():
    st.title("Welcome to DiabetesPredict ")
    st.subheader("Your Premier Diabetes Risk Assessment Solution")

    # Add image to the home page

    # Add a brief description of your web app
    st.markdown(
        
        """<p style="font-size:28px;">
         
          
    Are you concerned about your risk of developing diabetes?
    Are you a healthcare professional looking for a reliable tool to assess your patients' diabetes risk? 
    Look no further! DiabetesPredict is here to provide you with accurate predictions based on relevant data.

        
    """, unsafe_allow_html=True)
    
    # Load Lottie animation
    lottie_coding = load_lottieurl("https://lottie.host/d0f8084d-8fec-4be8-a604-d9b817fc3158/S2huryZzXk.json")
    

    st_lottie(lottie_coding, width=500, height=500)
    
    
    
    st.write(
        
        """<p style="font-size:20px;">
         <h1>Why Focus on Women's Health?</h1>
      
     Diabetes is a significant health concern, affecting millions of people worldwide. 
    Research has shown that gender can play a role in diabetes risk factors and outcomes. 
    That's why we've chosen to emphasize women's health in our prediction model. 
    By considering gender-specific factors, we can offer more tailored and accurate predictions for women.


    """, unsafe_allow_html=True)
    
    
    st.markdown(
        
        """<p style="font-size:20px;">
         <h1>Who Can Use DiabetesPredict?</h1>
      
    Patients: 
             Are you curious about your diabetes risk?
             Input your relevant details into our user-friendly interface, 
             and we'll provide you with a personalized assessment of your risk
             
    Healthcare Professionals: 
             Use DiabetesPredict as a valuable tool to assess your patients diabetes risk quickly and accurately.
             Our system generates detailed reports that can aid in treatment planning and prevention strategies.

       """, unsafe_allow_html=True)
    
    
    
    
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

