import streamlit as st
import plotly.express as px
fig = px.histogram([1,2,2,3,3,3,4,4,5])

st.plotly_chart(fig)