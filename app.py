import pip
import streamlit as st
st.title(" My first streamlit app created by Pranaya")
st.write("Welcome  this app calculate the numbers")
st.header("select a number")
number = st.slider("pick a number", 0, 100, 50)
st.write("You selected:", number)
st.write("The square of the number is:", number * number)
st.write("The cube of the number is:", number * number * number)    
