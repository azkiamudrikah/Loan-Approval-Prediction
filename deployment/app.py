import streamlit as st
from eda import run_eda
from prediction import run_prediction

# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = "EDA"

# Title for the app
st.title("Loan Prediction App")

# Sidebar for navigation
menu = st.sidebar.selectbox("Select a Page", ["EDA", "Prediction"], 
                            index=0 if st.session_state['page'] == "EDA" else 1)

# Store the current page in session state
st.session_state['page'] = menu

# Run selected page
if st.session_state['page'] == "EDA":
    run_eda()
elif st.session_state['page'] == "Prediction":
    run_prediction()