import streamlit as st

# Simple symptom to disease mapping
disease_mapping = {
    "headache": "Migraine",
    "fever": "Viral Fever",
    "fatigue": "Fatigue Syndrome",
    "cough": "Common Cold",
    "chest pain": "Heart Disease",
    "shortness of breath": "Asthma",
    "nausea": "Food Poisoning",
}

def predict_disease(symptoms):
    matched_diseases = []
    for symptom, disease in disease_mapping.items():
        if symptom.lower() in symptoms.lower():
            matched_diseases.append(disease)
    
    if matched_diseases:
        return f"Based on your symptoms, possible conditions include:\n- " + "\n- ".join(set(matched_diseases))
    else:
        return "No matching disease found. Please consult a doctor for an accurate diagnosis."

def run():
    st.subheader("🧠 Disease Prediction")
    symptoms = st.text_area("Enter your symptoms (comma-separated):", "")

    if st.button("Predict Disease"):
        if symptoms:
            response = predict_disease(symptoms)
            st.success(response)
        else:
            st.warning("Please enter some symptoms.")

if __name__ == "__main__":
    run()
