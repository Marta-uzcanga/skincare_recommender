import streamlit as st
import pandas as pd
import load_csv

def get_rec(name, df_filtered):
    if name in list(df_filtered['names']):
        cluster = df_filtered[df_filtered.names == name].clusters
        sample = df_filtered[df_filtered.clusters == cluster.values[0]].sample()
        st.markdown(""" <style> .new {
        font-size:20px ; font-family: 'Cooper Black'; color: #DC6100;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="new">We think you will love this:</p>', unsafe_allow_html=True)

    else:
        st.markdown(""" <style> .new {
        font-size:20px ; font-family: 'Cooper Black'; color: #DC6100;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="new">We do not recognise this product, but here is another one that we are sure you will love:</p>', unsafe_allow_html=True)
        #st.text("We don't recognise this product, but here is another one that we are sure you will love:")
        sample = df_filtered.sample()

    return sample['names']