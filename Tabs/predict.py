import streamlit as st
from myfunction import evaluate_model, load_data, split_data

def app(df, rf, X_test, Y_test):
    """This function creates the prediction page"""

    st.title("Prediction Page")

   
    st.markdown(
        """
<p style="font-size:25px">
                This app uses <b style="color:#4BFFF6">Random Forest Classifier</b> for the Early Prediction of Diabetes.
</p>
        """, unsafe_allow_html=True)

    # Create a sidebar
    st.sidebar.title("Select Input Method")

    input_method = st.sidebar.radio("Choose Input Method", ("Slider Input", "Text Input"))

    if input_method == "Slider Input":
       
        st.subheader("Select Values:")
        pg = st.slider("Pregnancies", int(df["Pregnancies"].min()), int(df["Pregnancies"].max()))
        ag = st.slider("Aftermeal Glucose", int(df["Glucose"].min()), int(df["Glucose"].max()))
        bp = st.slider("Blood Pressure", int(df["BloodPressure"].min()), int(df["BloodPressure"].max()))
        sth = st.slider("Skin Thickness", int(df["SkinThickness"].min()), int(df["SkinThickness"].max()))
        insulin = st.slider("Insulin", int(df["Insulin"].min()), int(df["Insulin"].max()))
        bmi = st.slider("BMI", float(df["BMI"].min()), float(df["BMI"].max()))
        dc = st.slider("DiabetesPedigreeFunction", float(df["DiabetesPedigreeFunction"].min()), float(df["DiabetesPedigreeFunction"].max()))
        age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))

       
        if st.button("Predict"):
            # Preprocess the user input data
            input_data = [pg, ag, bp, sth, insulin, bmi, dc, age]

            # Use the trained model to predict
            prediction = rf.predict([input_data])
            test_data_accuracy = evaluate_model(rf, X_test, Y_test)

            st.info("Prediction Completed")

            # Display the prediction
            if prediction[0] == 0:
                st.success("The person is predicted to be free from diabetes.")
            else:
                st.warning("The person is predicted to have a high risk of diabetes mellitus.")

            # Display the model's confidence score
            st.write("The model used is trusted by doctors and has an accuracy of", (test_data_accuracy * 100), "%")



    elif input_method == "Text Input":
        
        st.subheader("Enter Values:")

        pg = st.text_input("Pregnancies")
        ag = st.text_input("Glucose")
        bp = st.text_input("Blood Pressure")
        sth = st.text_input("Skin Thickness")
        insulin = st.text_input("Insulin")
        bmi = st.text_input("BMI")
        dc = st.text_input("DiabetesPedigreeFunction")
        age = st.text_input("Age")

        # Validation function to check if the input is numeric
        def is_numeric(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        # Check if the input is valid before making predictions
        if st.button("Predict"):
            if all(is_numeric(val) for val in [pg, ag, bp, sth, insulin, bmi, dc, age]):
                # Preprocess the user input data
                input_data = [float(pg), float(ag), float(bp), float(sth), float(insulin), float(bmi), float(dc), float(age)]

                # Use the trained model to predict
                prediction = rf.predict([input_data])
                test_data_accuracy = evaluate_model(rf, X_test, Y_test)

                st.info("Prediction Completed")

                # Display the prediction
                if prediction[0] == 0:
                    st.success("The person is predicted to be free from diabetes.")
                else:
                    st.warning("The person is predicted to have a high risk of diabetes mellitus")

                # Display the model's confidence score
                st.write("The model used is trusted by doctors and has an accuracy of", (test_data_accuracy * 100), "%")
            else:
                st.error("Please enter valid numeric values for all input fields.")
