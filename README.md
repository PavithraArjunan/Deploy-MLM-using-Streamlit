This is a simple web application built using **Streamlit** that predicts whether a person is diabetic based on user-inputted medical parameters. The model used in this application is trained on the **PIMA Indian Diabetes Dataset** and is loaded from a pre-trained model using **pickle**.

---

## Features
- User-friendly interface built with **Streamlit**
- Predicts diabetes based on input features
- Uses a **pre-trained machine learning model** for classification
- Displays the prediction result instantly

---

## Installation & Setup

### Prerequisites
Ensure you have **Python 3.x** installed along with the following dependencies:

```bash
pip install numpy pandas streamlit scikit-learn pickle5
```

### Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Run the Application
```bash
streamlit run app.py
```

---

## Model & Dataset
The model used is a **Supervised Learning model trained on the PIMA Indian Diabetes dataset**.

### Features Used for Prediction
- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skinfold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **DiabetesPedigreeFunction**: Likelihood of diabetes based on family history
- **Age**: Age of the person in years

---

## Usage Guide
1. **Open the web app** using Streamlit.
2. **Enter required medical parameters** in the provided input fields.
3. Click the **"Test Result"** button.
4. The app will display one of the following results:
   - **(HEALTHY) - No diabetic**
   - **DIABETIC PATIENT**

---

## Code Overview
### Model Loading
```python
load_model = pickle.load(open("diadetes_model.sav", 'rb'))
```

### Making Predictions
```python
def diabetics_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data = input_data_as_numpy_array.reshape(1, -1)
    prediction = load_model.predict(input_data)
    return '(HEALTHY)--No diabetic' if prediction[0] == 0 else 'DIABETIC PATIENT'
```

### Running the Web App
```python
if __name__ == '__main__':
    main()
```

---

## Contributing
If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License.

