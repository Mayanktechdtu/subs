import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta

# Simulated user database with subscription expiry dates
users = {
    "user1@example.com": datetime.now() + timedelta(days=7),  # Valid for 7 more days
    "user2@example.com": datetime.now() - timedelta(days=1),  # Expired 1 day ago
}

# Function to check subscription status
def check_subscription(email):
    if email in users:
        expiry_date = users[email]
        if datetime.now() < expiry_date:
            return True, expiry_date
    return False, None

# Streamlit App
st.title("Subscription-based Dashboard: Reliance Industries Limited - 2023 Historical Data")

email = st.text_input("Enter your email")
if st.button("Login"):
    is_valid, expiry_date = check_subscription(email)
    if is_valid:
        st.success(f"Welcome! Your subscription is valid until {expiry_date.date()}")
        
        # Fetching Reliance data for 2023
        symbol = "RELIANCE.NS"  # NSE symbol for Reliance Industries
        start_date = "2023-01-01"
        end_date = "2023-12-31"

        data = yf.download(symbol, start=start_date, end=end_date)

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
    else:
        st.error("Your subscription has expired. Please renew to access the dashboard.")
