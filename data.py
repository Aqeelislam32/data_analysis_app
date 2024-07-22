import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.graph_objects as go

#title the page
st.title('Data Analysis Application 📊🚀')
st.subheader('This is Simple Data Analysis Application create by Muhammad Aqeel 😊 🤖✨')

#craete a dropdown list to choosen a dataset
dataset_option = ['iris', 'titanic', 'tips', 'diamond']
selected_dataset = st.selectbox('Select a dataset ', dataset_option)

#load the selected data
if selected_dataset == 'iris':
    df=sns.load_dataset('iris')
elif selected_dataset =='titanic':
    df= sns.load_dataset('titanic')
elif selected_dataset == 'tips':
    df= sns.load_dataset('tips')   
elif selected_dataset =='diamond':
    df =sns.load_dataset('diamond')

#upload the file 
uploaded_file = st.file_uploader('upload the custom data', type=('csv', 'xlsx'))        

if uploaded_file is not None:
    df =pd.read_csv(uploaded_file)

#display the dataset
if st.button('Display First Five Row'):
  st.write(df.head())

if st.button('Display Last Five row'):
    st.write(df.tail())  

#dispaly full data
if st.button('Display full data'):
    st.write(df)


#display the row and columns of the selected data
if st.button("Display Row and Columns"):
 st.write('Number of Row ', df.shape[0])
 st.write('Number of Columns ', df.shape[1])

#display the columns Name of selected data
if st.button('Display data types'):
 st.write("Columns Name and Data Types", df.dtypes)

#print Null value
if st.button('Check Null value'):
 if df.isnull().sum().sum() >0:
     st.write('Null Value: ', df.isnull().sum().sort_values(ascending=False))
 else:
    st.write('No Null Value')  

#display the summary statistics of selected data
if st.button("Summary Statistics"):
    st.write("summary statistics ", df.describe())



st.subheader('Pairplot')
#selected the columns to be hue  in airplot
hue_column= st.selectbox('select a cloumns to be used as hue', df.columns) 
st.pyplot(sns.pairplot(df, hue=hue_column)) 

#selected the specific columns for x axis and y axis from the dataset 
#if st.button('Display graphy'):











#load the data
df = sns.load_dataset('tips')