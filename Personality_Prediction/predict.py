import streamlit as st
import joblib

st.title("🧠 Personality Prediction App")

col1,col2,col3=st.columns([1,2,1])
with col2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGXdBw9N0SS-jWD7iSHdBBb4UzkBBmVL-RtQ&s",width=500)

st.markdown("""
### Discover Your Personality Type
Are you more **Extroverted** or **Introverted**? 🤔  
This intelligent application analyzes your **social behavior and lifestyle patterns** to predict your 
personality type using a **Machine Learning model**.

📌 **Provide the following details about your daily social habits:**  
- Time you prefer to spend alone  
- Your comfort with stage presence  
- Participation in social events  
- Frequency of going outside  
- Energy levels after socializing  
- Size of your friend circle  
- Social media activity""")
st.divider()
st.header("Let's get started!")
st.subheader("📝 Enter Your Social Behavior Details")

col1,col2,col3=st.columns(3)
with col1:
    Stage_fear=st.radio("Stage_fear",("Yes","No"))
    Drained_after_socializing=st.radio("Drained_after_socializing",("Yes","No"))
with col2:
    Time_spent_Alone=st.number_input("Time_spent_Alone",min_value=0)
    Going_outside=st.number_input("Going_outside",min_value=0)
with col3:
    Social_event_attendance=st.number_input("Social_event_attendance",min_value=0)
    Friends_circle_size=st.number_input("Friends_circle_size",min_value=0)
    Post_frequency=st.number_input("Post_frequency",min_value=0)

model = joblib.load('best_model_RF')
le1 = joblib.load('label_encoder_stage_fear_RF')
le2 = joblib.load('label_encoder_drained_after_socializing_RF')

if st.button("Check Personality"):
    Stage_fear = le1.transform([Stage_fear])[0]
    Drained_after_socializing = le2.transform([Drained_after_socializing])[0]
    prediction = model.predict([[Time_spent_Alone,Stage_fear,Social_event_attendance,
            Going_outside,Drained_after_socializing,Friends_circle_size,Post_frequency]])
    st.subheader("🔎 Personality Prediction Result")
    if prediction[0]==0:
        st.success("🎉 You are likely an **Extrovert**!")
        st.write("You tend to gain energy from social interactions and enjoy engaging with people.")
    else:
        st.info("🙂 You are likely an **Introvert**!")
        st.write("You may prefer quieter environments and recharge through time alone.")
