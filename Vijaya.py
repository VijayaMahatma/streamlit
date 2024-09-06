import streamlit as st

def fare(d):
    book = 2.0  # Booking fee
    start = 3.0  # Starting fee
    cost = 1.0  # Cost per distance unit
    total_fare = book + start + d * cost
    return total_fare

# Streamlit application
st.title("Fare Calculator")

# Input for distance
distance = st.number_input("What is the distance (in units)?", min_value=0.0, step=0.1)

# Calculate fare when button is pressed
if st.button("Calculate Fare"):
    total_fare = fare(distance)
    st.success(f"The total fare for {distance} units is: ${total_fare:.2f}")
