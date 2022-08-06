import numpy as np
import pickle 
import streamlit as st

load_model = pickle.load(open("C:/Users/Lenovo/Documents/ML/diadetes_model.sav",'rb'))

def diabetics_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data = input_data_as_numpy_array.reshape(1,-1)
    prediction = load_model.predict(input_data)
    print(prediction)

    if(prediction[0]==0):
        return'(HEALTHY)--No diabetic'
    else:
        return'DIABETIC PATIENT'

def main():
    
    # Giving the title
    st.title('Prediction Page')
    
    Pregnancies = st.text_input("Pregnancies")
    Glucose = st.text_input("Glucose level")
    BloodPressure = st.text_input("Blood Pressure Level")
    SkinThickness = st.text_input("Skin Thickness Level")
    Insulin = st.text_input("Insulin Level")
    BMI = st.text_input("Body Mass Index Value")
    DiabetesPedigreeFunction = st.text_input("DPF")
    Age = st.text_input("Age of the Patient")
    
    # Code for Prediction
    diagnosis = ''
    
    # Creating the button 
    if st.button('Test Result'):
        diagnosis = diabetics_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
       BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()