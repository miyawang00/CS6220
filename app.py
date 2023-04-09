
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import numpy as np
import streamlit as st  # pip install streamlit
import json
import re
import urllib

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(layout="centered", page_icon="🗺️", page_title="Flight")

# ---- READ CSV ----

df = pd.read_csv("flight data.csv")

# Drop duplicate values
df.drop_duplicates(inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)

# remove the airline_name column in  pandas DataFrame that contains square brackets []

df['airline_name'] = df['airline_name'].str.replace('[','').str.replace(']','')

# delete the duplicate flight number in column flight_number behind the strings with a | separator

df['flight_number'] = df['flight_number'].str.split('|').str[0]

transaction_df = df.head(5)

st.title( " Flight Price Prediction")

with st.expander("About this app 💙"):

    st.write("")

    st.markdown(
        """
    This dataset comes from the  `BARKING DATA`, Global Flight Datasets Covering top airports from Europe, Asia, America, Africa.
    The data spans from `04/30/2022` to `10/31/2022` and is available in CSV format (downloadable [here](https://www.kaggle.com/datasets/polartech/flight-data-with-1-million-or-more-records)).
    Each row in the dataset contains information about flight price:
    - The name of the airline company that operates the flight.
    - Contry name of the arrival location
    - Contry name of the departure location
    - The number assigned to the flight by the airline company.
    - The scheduled departure time of the flight.
    - The scheduled arrival time of the flight.
    - The duration of the flight.
    - The distance between the departure and arrival locations.
    - The price of the flight ticket.
    - The number of stops on the flight.
    - Co2 emission for each flight route
    """
    )
    
with st.expander("Show the top 5 lines of the dataframe ❤️"):
    st.write(transaction_df)








# Create a Plotly figure
# fig = px.scatter(df, x='duration', y='price', color='airline_name', size='co2_emissions', hover_data=['from_country', 'dest_country'])
# st.plotly_chart(fig)
