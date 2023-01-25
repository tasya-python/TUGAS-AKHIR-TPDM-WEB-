import pickle
import streamlit as st
import base64

#import background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('backround.jpeg')

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

#judul web
st.title('Data Mining Prediksi Diabetes')

#bagi kolom
col1,col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('Input nilai Pregnancies')
    Glocouse = st.text_input ('Input nilai Glocouse')
    BloodPresure = st.text_input ('Input nilai BloodPresure')
    SkinThickness = st.text_input ('Input nilai SkinThickness')
with col2 :
    Insulin = st.text_input ('Input nilai pregnancies')
    BMI = st.text_input ('Input nilai Insulin')

    DiabetesPedigreeFunction =st.text_input('Input nilai diabetes Pedigree function')
    Age = st.text_input('Input nilai Age')

# code untuk prediksi
diab_diagnosis =''

#tombol
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glocouse, BloodPresure, SkinThickness, Insulin, BMI,DiabetesPedigreeFunction,Age]])

    if(diab_prediction[0]==1):
        diab_diagnosis= 'Pasien terkena Diabetes'
    else:
        diab_diagnosis='Pasien terkena Diabetes'
    st.success(diab_diagnosis)
