import streamlit as st
import plotly.express as px
import pandas as pd


df = px.data.gapminder()
df.isnull().sum()
df.nunique()

fig_bar = px.histogram(df, x="continent", y="pop", color="continent",
                       animation_frame="year",
                       animation_group="country",
                       range_y=[0, 4000000000],
                       color_discrete_sequence=px.colors.qualitative.T10)
fig_bar.update_yaxes(showgrid=False),
fig_bar.update_xaxes(categoryorder='total descending')
fig_bar.update_traces(hovertemplate=None)
fig_bar.update_layout(margin=dict(t=70, b=0, l=70, r=40),
                      hovermode="x unified",
                      xaxis_tickangle=360,
                      xaxis_title=' ', yaxis_title=" ",
                      plot_bgcolor='#2d3035', paper_bgcolor='#2d3035',
                      title_font=dict(size=25, color='#a5a7ab',
                                      family="Lato, sans-serif"),
                      font=dict(color='#8a8d93'),
                      legend=dict(orientation="h", yanchor="bottom",
                                  y=1.02, xanchor="right", x=1)
                      )

st.plotly_chart(fig_bar)
