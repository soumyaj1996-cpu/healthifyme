import os 
import pandas as pd
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Let's get the API key from the environment
gemini_api_key='AIzaSyCpOcjRUsyPPul6GhSYbMjBDGrN2FNlesI'

# Let's configure the model
model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=gemini_api_key)

# Design the UI of the Application
st.title(":green[Healthify Me] : Your Personal Health Assisstant 🍎🥗🏋🏽‍♀️")
st.markdown(''' 
This application will assist you to get customised health and wellness advice. 
            You can ask your health related issues and get personalized guidance '''
)
st.write('''
Follow these steps:
* Enter your details in the sidebar.
* Rate your activity and fitness on the scale of 0-5.
* Submit your details.
* Ask your question on the main page.
* Click generate to get a personalised report.''')


# Design a side bar for all the user parameters
st.sidebar.header(':red[Enter Your Details]')
Name=st.sidebar.text_input('Enter Your Name')
Gender=st.sidebar.selectbox('Select Your Gender',['Male','Female'])
Age=st.sidebar.text_input('Enter Your Age')
Weight=st.sidebar.text_input('Enter Your Weight in Kgs')
Height=st.sidebar.text_input('Enter Your Height in Cms')
BMI=pd.to_numeric(Weight)/((pd.to_numeric(Height)/100)**2)
Active=st.sidebar.slider('Rate Your Activity(0-5)',0,5,step=1)
Fitness=st.sidebar.slider('Rate Your Fitness(0-5)',0,5,step=1)
if st.sidebar.button('Submit'):
    st.sidebar.write(f'{Name}, your BMI is {round(BMI,2)} Kg/m^2')

# Lets use the gemini model to generate the report 
user_input=st.text_input('Ask your question')
prompt=f'''
<Role> You are an expert in health and welness and has 10+ experience in guiding people.
<Goal> Generate the customise report addressing the problem the user has asked;{user_input}
<Context> Here are the details user has provided
Name={Name}
Age={Age}
Height={Height}
Weight={Weight}
BMI={BMI}
Activity Rating(0-5)={Active}
Fitness Rating(0-5)={Fitness}

<Format> 
* Start with 2-3 line of comment on the details that user has prepared 
* Explain what the real problem could be on the basis ofinput user has provided.
* Suggest the possible reasons for the problem.
* What are the possible solutions .
* Mention the doctor from which sepecialization can be visited if required .
* Mention any changein the diet which is required.
* In last create a final summary of all the things that has been discussed in the report 

<Instructions>
* Use bullet points where ever possible 
* Create tables to represents any data where ever possible.
* Strictly do not advise any medicine.'''


# Design the sidebar for all the user parametre
if st.button('Generate'):
    response=model.invoke(prompt)
    st.write(response.content)