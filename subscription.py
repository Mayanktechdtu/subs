import streamlit as st
import yfinance as yf
import pandas as pd

# Function to fetch data
def fetch_data(symbol, start, end):
    data = yf.download(symbol, start=start, end=end)
    return data

# Streamlit App
st.title("Reliance Industries Limited - 2023 Historical Data")

# Fetching Reliance data for 2023
symbol = "RELIANCE.NS"  # NSE symbol for Reliance Industries
start_date = "2023-01-01"
end_date = "2023-12-31"

data = fetch_data(symbol, start_date, end_date)

# Display DataFrame
st.write("### Historical Data for 2023")
st.dataframe(data)

# Plotting the closing price
st.write("### Closing Price over Time")
st.line_chart(data['Close'])

# Plotting the volume
st.write("### Volume over Time")
st.bar_chart(data['Volume'])

# Additional Statistics
st.write("### Basic Statistics")
st.write(data.describe())

