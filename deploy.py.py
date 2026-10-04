
import streamlit as st
import pandas as pd
import joblib

model = joblib.load(r"C:\Users\HP\Desktop\ml work\LogisticRegression_heart.pkl")
scaler = joblib.load(r"C:\Users\HP\Desktop\ml work\scaler.pkl")
expected_columns = joblib.load(r"C:\Users\HP\Desktop\ml work\columns.pkl")

st.title("Heart Stroke Prediction ❤️")
st.markdown("Provide the following details")
Age = st.slider("Age",18,100,40)
Sex = st.selectbox("Sex",['M','F'])
Chest_pain = st.selectbox("Chest Pain Type",["ATA","NAP","TA","ASY"])
Resting_BP = st.number_input("Resting Blood Pressure(mm Hg)",80,200,120)
Cholesterol = st.number_input("Cholesterol(mg/dL)",100,600,200)
Fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL",[0,1])
Resting_ecg = st.selectbox("Resting ECG",["Normal","ST","LVH"])
Max_hr = st.slider("Max Heart Rate",60,220,150)
Exercise_angina = st.selectbox(" Exercise_Induced Angina",["Y","N"])
Oldpeak = st.slider("Oldpeak (ST Depression)",0.0,6.0,1.0)
St_slope = st.selectbox("ST Slope",["Up","Flat","Down"])

if st.button("Predict"):
    raw_input = {
        'Age': Age,
        'RestingBP': Resting_BP,
        'Cholesterol': Cholesterol,
        'FastingBS': Fasting_bs,
        'MaxHR': Max_hr,
        'Oldpeak': Oldpeak,
        'Sex_' + Sex: 1,
        'ChestPainType_' + Chest_pain: 1,
        'RestingECG_' + Resting_ecg: 1,
        'ExerciseAngina_' + Exercise_angina: 1,
        'ST_Slope_' + St_slope: 1
    }    

    input_df = pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col]=0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success(" ✅ Low Risk of Heart Disease")
