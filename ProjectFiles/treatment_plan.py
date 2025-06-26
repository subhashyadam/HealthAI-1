import streamlit as st

def run():
    st.subheader("💊 Treatment Plan Generator")
    condition = st.text_input("Enter your diagnosed condition:", "")

    if st.button("Generate Treatment Plan"):
        if condition:
            # Simulated output
            plan = f"Suggested treatment for {condition}:\n\n• Medication: Paracetamol, Ibuprofen\n• Lifestyle: Rest, Hydration\n• Tests: CBC, follow-up in 1 week"
            st.success(plan)
        else:
            st.warning("Please enter a condition.")
