
# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

st.markdown(
    """
    <style>
    
    
    .footer-text {
        font-size: 12px; /* Ukuran font kecil */
        color: #a9a9a9; /* Warna teks abu-abu */
        text-align: center; /* Rata tengah */
        margin-top: 200px; /* Margin atas */
        margin-bottom: -150px;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# Load the trained model
with open('model/svm_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the dataset for preprocessing (same steps as during training)
df = pd.read_csv('data/diabetes.csv')
columns_to_check = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for column in columns_to_check:
    df[column].replace(0, df[column].mean(), inplace=True)

# Set up the Streamlit app
st.title("🩸DiabEase | Diabetes Prediction")

st.markdown("""
### <h5 style="margin-top:-50px; margin-bottom: 20px;">Let’s check if you may have diabetes.</h5>
<small>Input the following details to predict whether you has diabetes or not.<small><br>
<small>For input format details, please place the cursor over the question mark bubble.</small>
<br></br>
""", unsafe_allow_html=True)


# Create input fields for user with explanation and empty initial value
pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=None, 
                              help="Enter the number of pregnancies (e.g., 0, 1, 2, etc.)")
glucose = st.number_input('Glucose', min_value=0, max_value=200, value=None, 
                          help="Enter the glucose level in blood (e.g., 90, 120, 150, etc.)")
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=150, value=None, 
                                 help="Enter the blood pressure measurement (e.g., 80, 120, etc.)")
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=99, value=None, 
                                 help="Enter the skin thickness value (e.g., 20, 35, etc.)")
insulin = st.number_input('Insulin', min_value=0, max_value=900, value=None, 
                          help="Enter the insulin level in blood (e.g., 70, 120, 150, etc.)")
bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=None, step=0.1, 
                      help="Enter the Body Mass Index (BMI) value (e.g., 25.5, 32.0, etc.)")
diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=None, step=0.001, 
                                             help="Enter the diabetes pedigree function (e.g., 0.3, 0.471, etc.)")
age = st.number_input('Age', min_value=1, max_value=120, value=None, 
                      help="Enter the age in years (e.g., 25, 30, 45, etc.)")

# Prediction button
if st.button('Predict'):
    # Check if all fields are filled
    if None in [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]:
        st.error("Please fill in all the required fields!")
    else:
        # Prepare input data
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        
        # Scale the input data
        scaler = StandardScaler()
        df_clean = df.drop(columns=['Outcome'])
        scaler.fit(df_clean)
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_data_scaled)
        
        # Display result with advice
        if prediction[0] == 1:
            st.write("**You might have diabetes.**")
            st.write("""
            Please consult with your healthcare provider for a detailed diagnosis and treatment plan. 
            It's important to monitor your glucose levels, maintain a healthy diet, exercise regularly, and follow any medical advice.
            """)
        else:
            st.write("**You do not have diabetes according to this prediction.**")
            st.write("""
            However, it's still important to maintain a healthy lifestyle to prevent any future risks. 
            Keep up with regular check-ups, eat a balanced diet, stay active, and monitor your health.
            """)
else:
    st.info("Please enter the details and click 'Predict' button to see the result")
        


# Footer
st.markdown("---")
st.markdown("### About")
st.markdown("This app uses a machine learning model to predict diabetes based on user input.")

st.markdown("<p class='footer-text'>Made by Irgya Genta Arnezzi & Afzie Muhammad Nurlan</p>", unsafe_allow_html=True)