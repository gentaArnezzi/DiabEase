# README for Diabetes Prediction App

## DiabEase: Application Description

**DiabEase** is an application designed to predict diabetes risk based on user-input health data. Utilizing a machine learning model, **DiabEase** helps users understand their likelihood of developing diabetes by analyzing specific health parameters. With a user-friendly interface and quick analysis, this application provides valuable insights for taking proactive steps in managing health.

## Features

- Input health data such as the number of pregnancies, glucose level, blood pressure, and more.
- Predict outcomes: Whether you have diabetes or not.
- A simple and intuitive user interface using Streamlit.

## Model Information

- **Model Type**: Support Vector Machine (SVM)
- **Kernel**: Linear
- **Training Data**: The model was trained on a dataset with 768 entries, which includes features like pregnancies, glucose, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function, and age.
- **Performance**: The model achieved an accuracy score of 79% on the test data.

## How to Use

1. **Run the Application**:

   - Make sure you have installed all the required dependencies.
   - Run the application using the command:
     ```bash
     streamlit run app.py
     ```

2. **Enter Data**:

   Fill in all the requested fields, including:

   - Number of Pregnancies
   - Glucose Level
   - Blood Pressure
   - Skin Thickness
   - Insulin Level
   - Body Mass Index (BMI)
   - Diabetes Pedigree Function
   - Age

3. **Get Prediction**:
   - Click the "Predict" button to see the prediction result, whether you have diabetes or not.

## Dependencies

- Python
- Streamlit
- Pandas
- Scikit-learn

## Contribution

If you want to contribute to the development of this application, please fork this repository and create a pull request.

## License

This application is licensed under the MIT License.

## Contact

If you have any questions or suggestions, please contact:

- Irgya Genta Arnezzi
  - irgyagentaarnezzi@gmail.com
- Afzie Muhammad Nurlan
  - afziemuhammad@gmail.com
