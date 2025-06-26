import streamlit as st
import pandas as pd

def run():
    st.subheader("📊 Health Analytics Dashboard")
    uploaded_file = st.file_uploader("Upload a CSV file with health metrics", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("📄 Preview of Uploaded Data:")
        st.dataframe(df)

        numeric_columns = df.select_dtypes(include=['float64', 'int']).columns.tolist()

        if numeric_columns:
            selected_metric = st.selectbox("Select a health metric to visualize:", numeric_columns)
            st.line_chart(df[selected_metric])
        else:
            st.error("No numeric data found in file.")
