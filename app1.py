import pickle
import streamlit as st
import numpy as np
#import requests
#from streamlit.components.v1 import html
st.set_page_config(page_title="Autism Specturm Disorder", layout='wide')

st.title("Autism Specturm Disorder")

model = pickle.load(open('asd.pkl', 'rb'))
values = ["yes", "No"]
val = ["Male", "Female"]
selected_val1 = st.selectbox(
    "Social Communication - Do you find it difficult to start conversations with people you don’t know well?",
    values
)
selected_val2 = st.selectbox(
    "Restrictive Behaviors -  Are there specific sounds or lights that you find overwhelming?",
    values
)
selected_val3 = st.selectbox(
    "excellency - Do you have any specific interests or activities that you focus on intensely?",
    values
)
selected_val4 = st.selectbox(
    "Sensory Issues - Are there specific sounds or lights that you find overwhelming?",
    values
)
selected_val5 = st.selectbox(
    "Aggression - Do you often find it hard to manage feelings of frustration or anger?",
    values
)
selected_val6 = st.selectbox(
    "Hyperactivity - Do you find it challenging to stay still or calm for extended periods?",
    values
)
selected_val7 = st.selectbox(
    "Attention Problems - Do you have difficulty staying focused on tasks for a long time?",
    values
)
selected_val8 = st.selectbox(
    "Anxiety - Do you often feel anxious in certain situations or events?",
    values
)
selected_val9 = st.selectbox(
    "Depression - Do you frequently experience feelings of sadness?",
    values
)
selected_val10 = st.selectbox(
    "Irritability - Do you get irritable in response to specific situations or events?",
    values
)
selected_val_age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

selected_val_gender = st.selectbox(
    "gender - Gender of the patient",
    val
)
selected_val_jaundice = st.selectbox(
    "jaundice - Whether the you had jaundice at the time of birth",
    values
)
selected_val_autism = st.selectbox(
    "autism - Whether an immediate family member has been diagnosed with autism",
    values
)
selected_val_app = st.selectbox(
    "used_app_before - Whether the patient has undergone a screening test before",
    values
)
data = [selected_val1, selected_val2, selected_val3, selected_val4, selected_val5, selected_val6, selected_val7, selected_val8,selected_val9, selected_val10, selected_val_age, selected_val_gender, selected_val_jaundice, selected_val_autism, selected_val_app]
dict = {"yes": 1, "No": 0, "Male": 0, "Female": 1}
def map_values(data, dict):
    return [dict.get(item, item) for item in data]
data = map_values(data, dict)
data = np.array(data)
data = data.reshape(1,-1)
prediction = model.predict(data)
final_prediction = int(prediction )

if st.button('Predict'):
    if final_prediction==0:
        st.text("The test indicates that you don't have Autism Specturm Disorder")
    else:
        st.text("The test indicates that you  have Autism Specturm Disorder")

