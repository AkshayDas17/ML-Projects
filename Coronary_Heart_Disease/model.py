
# importing dependencies
import joblib
import streamlit as st

# load model
Model=joblib.load('Coronary_Heart_Disease/Model')
# Header
st.header('Coronary Heart Disease Prediction')
# text
st.subheader('''Coronary Heart Disease (CHD), also known as coronary artery disease (CAD) or ischemic heart disease (IHD), is a condition where the coronary arteries (which supply oxygen-rich blood to the heart muscle) become narrowed or blocked due to a buildup of plaque (fat, cholesterol, and other substances''')
st.subheader('''Coronary heart disease is a leading cause of heart attacks and can be life-threatening if left untreated. However, with proper lifestyle changes, medications, and medical interventions, it can be managed and prevented.''')
st.subheader('Ckeck your chance of having heart disease')
st.subheader('')

#inserting image
st.image("Coronary_Heart_Disease/Heart.jpg",width=500)
st.subheader('')

# name 
name=st.text_input('Enter name')
# radio button
st.radio('Sex',('Male','Female'))
# Age
st.slider('Age',1,80)
# name,sex and age doesn't need for the prediction.Just for details.
st.subheader('')
st.text('Fill cells below ')
# creating a 3*3 structure
col1,col2,col3=st.columns(3)
with col1:
    iv=st.number_input('IV')
    a5=st.number_input('A5')
    a6=st.number_input('A6')
with col2:    
    a7=st.number_input('A7')
    a8=st.number_input('A8')
    a9=st.number_input('A9')
with col3:    
    a10=st.number_input('A10')
    a12=st.number_input('A12')
    a15=st.number_input('A15')
    
# Button
if st.button('Check'):
    predicted=Model.predict([[iv,a5,a6,a7,a8,a9,a10,a12,a15]])
    if (predicted==0):
        st.success('Congrats, No risk of Heart disease')
    else:
        st.warning('Consult a doctor immediately')    
