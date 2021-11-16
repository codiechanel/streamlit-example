import streamlit as st
import plotly.express as px
import pandas as pd
# fig = px.histogram([1, 2, 2, 3, 3, 3, 4, 4, 5])

df = px.data.gapminder().query("year==2007")
# df.head()

# fig = px.histogram(df, x="lifeExp", color="continent", hover_name="country")
# fig = px.choropleth(df, color="lifeExp",
#                     locations="iso_alpha", hover_name="country")
fig = px.sunburst(df, color="lifeExp", values="pop", path=[
                  "continent", "country"], hover_name="country")
st.plotly_chart(fig)
