# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:20:31 2020

@author:
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:50:04 2020

@author: Dhruv.Shah
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("fifa.pkl","rb")
predicter=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    image = Image.open('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.kolpaper.com%2F4803%2Ffifa-20-bvb-wallpaper%2F&psig=AOvVaw2enWW8sVHm1RiM4UCp67LL&ust=1593449103566000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOCXnNr6pOoCFQAAAAAdAAAAABAD.jpg')
    st.image(image, caption=None, width=None, use_column_width=False, clamp=False, channels='RGB', format='JPEG')

    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_overall(WeakFoot, HeadingAccuracy, Dribbling,SprintSpeed
                    ,Reactions,Strength,Interceptions, shooting_attributes
                    ,passing_attribtes):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=predicter.predict([[WeakFoot, HeadingAccuracy, Dribbling, SprintSpeed, Reactions,Strength, Interceptions, shooting_attributes,passing_attribtes]])
    print(prediction)
    return prediction



def main():
    image = Image.open('fifa.jpg')
    st.image(image, caption=None, width=None, use_column_width=False, clamp=False, channels='RGB', format='JPEG')

    st.title("Fifa Overall predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Fifa Overall predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    #WeakFoot = st.number_input("Weak Foot",min_value=None)
    HeadingAccuracy = st.slider("HeadingAccuracy",min_value=None)
    Dribbling = st.slider("Dribbling",min_value=None)
    SprintSpeed = st.slider("SprintSpeed",min_value=None)
    Reactions = st.slider("Reactions",min_value=None)
    Strength = st.slider("Strength",min_value=None)
    Interceptions = st.slider("Interceptions",min_value=None)
    shooting_attributes = st.slider("shooting_attributes",min_value=None)
    passing_attribtes = st.slider("passing_attribtes",min_value=None )

    result=""    
    if st.button("Predict"):
        result=predict_overall(int(3), HeadingAccuracy, Dribbling,SprintSpeed
                    ,Reactions,Strength,Interceptions, shooting_attributes
                    ,passing_attribtes)
    st.success('The predicted Overall is {}'.format(result))
    if st.button("Click to know some facts about the 'Beautifull Game'"):
        st.text("FIFA has always ensured that regions across the world get customized covers. From Rooney in England to Ronaldinho in Brazil; popular regions also have access to customized club covers, which can be easily downloaded.")
        st.text("Soccer is the only major world sport in which you can't use your hands to manipulate the ball or object of play")
        st.text('A 2000 internet poll voted Argentine Diego Maradona "the player of the century." FIFA disagreed strongly enough that they appointed a special committee to render judgment. The committee selected Pelé.')
        st.text('Brazilians refer to soccer as the “jogo bonito” or “beautiful game.”')

if __name__=='__main__':
    main()
    
    
    