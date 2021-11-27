import streamlit as st
from sub import say_hello, get_csv

hello = say_hello("Masa")
st.write(hello)
my_df = get_csv('my_csv.csv')
st.dataframe(my_df)
