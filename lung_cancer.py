import pickle
import streamlit as st

#membaca model
survey_lung_cancer_model=pickle.load(open('survey_lung_cancer.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Lung Cancer')
GENDER = st.text_input ('input nilai GENDER')

AGE = st.text_input ('input nilai AGE')


SMOKING = st.text_input ('input nilai SMOKING')


YELLOW_FINGERS = st.text_input ('input nilai YELLOW_FINGERS')


ANXIETY = st.text_input ('input nilai ANXIETY')


PEER_PRESSURE = st.text_input ('input nilai PEER_PRESSURE')


CHRONIC_DISEASE = st.text_input ('input nilai CHRONIC_DISEASE')


FATIGUE = st.text_input ('input nilai FATIGUE')


ALLERGY = st.text_input ('input nilai ALLERGY')


WHEEZING = st.text_input ('input nilai WHEEZING')


ALCOHOL_CONSUMING = st.text_input ('input nilai ALCOHOL_CONSUMING')


COUGHING = st.text_input ('input nilai COUGHING')


SHORTNESS_OF_BREATH = st.text_input ('input nilai SHORTNESS_OF_BREATH')


SWALLOWING_DIFFICULTY = st.text_input ('input nilai SWALLOWING_DIFFICULTY')


CHEST_PAIN = st.text_input ('input nilai CHEST_PAIN')

# code untuk prediksi penyakit lung cancer
survey_lung_cancer_diagnosis =''

# membuat tombol untuk prediksi
if st.button ('Test Prediksi') :
    survey_lung_cancer_prediction = survey_lung_cancer_model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING,ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])

    if(survey_lung_cancer_prediction[0] == 1) :
       survey_lung_cancer_diagnosis = 'Pasien memiliki penyakit Lung Cancer'
    else :
       survey_lung_cancer_diagnosis = ' Pasien tidak memiliki penyakit Lung Cancer'

st.success(survey_lung_cancer_diagnosis)