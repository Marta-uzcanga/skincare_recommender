import streamlit as st
import pandas as pd
import numpy as np
import subprocess
import recommender
import df_filter
import load_csv

st.set_page_config(layout="wide")

st.markdown(""" <style> .font {
font-size:40px ; font-family: 'Cooper Black'; color: #DC6100;} 
</style> """, unsafe_allow_html=True)


st.markdown(""" <style> .second {
font-size:20px ; font-family: 'Cooper Black'; color: #DC6100;} 
</style> """, unsafe_allow_html=True)

st.markdown(""" <style> .third {
font-size:25px ; font-family: 'Cooper Black'; color: #BB7600;} 
</style> """, unsafe_allow_html=True)

st.markdown(""" <style>.stTextInput > label {font-size:20px; font-family: 'Cooper Black'; color:#DC6100;} </style> """,unsafe_allow_html=True)

df1 = load_csv.load_csv('recommender_data.csv')


st.markdown('<p class="font">Find your new favourite skincare product!🧴</p>', unsafe_allow_html=True)



st.markdown('<p class="second">Select your non-negotiables:</p>', unsafe_allow_html=True)

Vegan = st.checkbox('Vegan 🌱')
if Vegan:
    vegan = 1
else:
    vegan = 0
        
Cruelty_Free = st.checkbox('Cruelty free 🐰')
if Cruelty_Free:
    cruelty_free = 1
else:
    cruelty_free = 0
    
Gluten_Free = st.checkbox('Gluten free 🌾')
if Gluten_Free:
    gluten_free = 1
else:
    gluten_free = 0

df_filtered = df_filter.filter_df(df1, vegan, gluten_free, cruelty_free)



name = st.text_input('Share with us a product you like:', 'Name')



primaryColor = st.get_option("theme.textColor")
s = f"""
<style>
div.stButton > button:first-child {{ border: 5px solid {primaryColor}; border-radius:25px 25px 25px 25px; font-family: 'Cooper Black'; ont-size:20px}}
<style>
"""
st.markdown(s, unsafe_allow_html=True)

# c = f"""
# <style>
# div.sttext_input > text_imput:first-child {{ border: 5px solid {primaryColor}; border-radius:20px 20px 20px 20px; font-family: 'Cooper Black'}}
# <style>
# """

# st.markdown(c, unsafe_allow_html=True)


if st.button('Blow my mind!'):
    
 

    sample = recommender.get_rec(name, df_filtered)
    st.markdown('<p class="third">{}</p>'.format(sample.iloc[0]), unsafe_allow_html=True)

  
   
