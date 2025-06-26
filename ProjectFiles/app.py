import streamlit as st
from modules import disease_predict, treatment_plan, chat, analytics

st.set_page_config(page_title="HealthAI", layout="wide")

st.title("💡 HealthAI – Intelligent Healthcare Assistant")

menu = st.sidebar.radio("Navigate", ["Disease Prediction", "Treatment Plan", "Patient Chat", "Health Analytics"])

if menu == "Disease Prediction":
    disease_predict.run()

elif menu == "Treatment Plan":
    treatment_plan.run()

elif menu == "Patient Chat":
    chat.run()

elif menu == "Health Analytics":
    analytics.run()
