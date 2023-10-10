# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 07:55:34 2023

@author: tharu
"""

import streamlit as st
import requests  
from streamlit_lottie import st_lottie

def app(df):
    """This function creates the Data Info page"""

    # Add title to the page
    st.title("Our Preprocessed Data Info page")
 
   
    
    st.subheader("View Data")

    # Create an expansion option to check the data
    with st.expander("View data"):
        st.dataframe(df)

    # Create a section to columns values
    # Give subheader
    st.subheader("Columns Description:")

    # Create a checkbox to get the summary.
    if st.checkbox("View Summary"):
        st.dataframe(df.describe())

    # Create multiple checkboxes in a row
    col_name, col_dtype, col_data = st.columns(3)

    # Show name of all dataframe
    with col_name:
        if st.checkbox("Column Names"):
            st.dataframe(df.columns)

    # Show datatype of all columns 
    with col_dtype:
        if st.checkbox("Columns data types"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)
    
    # Show data for each columns
    with col_data: 
        if st.checkbox("Columns Data"):
            col = st.selectbox("Column Name", list(df.columns))
            st.dataframe(df[col])


  
    # Add the link to your dataset
    st.markdown("""
                    <p style="font-size:16px">
                        <a 
                            href="https://www.kaggle.com/uciml/pima-indians-diabetes-database"
                            target=_blank
                            style="text-decoration:none;"
                        >Get Original Dataset
                        </a> 
                    </p>
                """, unsafe_allow_html=True)

def load_lottieurl(url: str):
    re = requests.get(url)
    if re.status_code != 200:
        return None
    return re.json()
