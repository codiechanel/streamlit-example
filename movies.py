import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import json
# import json

df = pd.read_csv('./input/tmdb_5000_movies.csv')

df.drop(['homepage', 'tagline', 'id'], axis=1, inplace=True)
df['runtime'].fillna(df['runtime'].mean(), inplace=True)
df.dropna(inplace=True)

# We can add a new column "year" to make it easier while working with date

df['release_date'] = pd.to_datetime(df['release_date'])
df['year'] = df['release_date'].dt.year


def get_insights_popularity(year_1=0, year_2=0):
    # this function will give us the most popular genres
    # Parameters :
    #    year_1 : int ( year between 1960 to 2016)
    #           if you not give any number the function will give you insights of all years
    #           if you give a specific year the function will give you insights of this years
    #    year_2 : int (year between year_1 to 2016)
    #            if you give a specific year the function will give you insights between year_1 and year_2
    sorted_popularity = df.sort_values(by='popularity', ascending=False)
    if year_2 == 0:
        year_2 = year_1
    if year_1 != 0:
        sorted_popularity.query(
            'year >= @year_1 and year <= @year_2', inplace=True)
    cool = plt.subplots(figsize=(10, 8))
    plt.gca().invert_yaxis()
    plt.barh(sorted_popularity['title'].head(10),
             sorted_popularity['popularity'].head(10))
    return cool


fig, ax = get_insights_popularity()
# fig, ax = plt.subplots()
# print(fig)
st.header('All time popular (till 2016)')
st.pyplot(fig)

fig, ax = get_insights_popularity(2016)
st.header('Popular in 2016')
st.pyplot(fig)

# budget column has values in some records equal zero
# So, we replace the 0s values with mean to get approximate value

df['budget'].replace(0, df['budget'].mean(), inplace=True)

df['profit'] = df['revenue'] - df['budget']

sorted_movies_pr = df.sort_values(by='profit', ascending=False)
# sorted_movies_pr.head(10)
fig, ax = plt.subplots(figsize=(10, 5))
plt.gca().invert_yaxis()
plt.title('Highest movies profit')
plt.ylabel('Movies')
plt.xlabel("The Profit ($)")
plt.barh(sorted_movies_pr.original_title.head(
    10), sorted_movies_pr.profit.head(10))

st.header('Profits')
st.pyplot(fig)
