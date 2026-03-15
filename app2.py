import streamlit as st
from datetime import datetime

st.title("Υπολογιστής Έτους που θα Γίνεις 100")

# Εισαγωγή δεδομένων
name = st.text_input("What's your name?")
age = st.number_input("How old are you?", min_value=0, max_value=120)

# Κουμπί για υπολογισμό
if st.button("Υπολόγισε"):
    current_year = datetime.now().year
    years_to_100 = current_year + (100 - age)
    st.write(f"{name}, you will turn 100 in the year {years_to_100}!")