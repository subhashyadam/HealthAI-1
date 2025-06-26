import streamlit as st

def run():
    st.subheader("💬 Patient Chat Assistant")
    question = st.text_input("Ask a health-related question:")

    if st.button("Get Answer"):
        if question:
            # Simulated response
            answer = f"You asked: {question}\n\n💡 Here's a general response: Stay hydrated, rest well, and consult a doctor if symptoms persist."
            st.success(answer)
        else:
            st.warning("Please enter a question.")
