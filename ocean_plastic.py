import streamlit as st
import pickle
import numpy as np

# ==========================
# Ocean Plastic Pollution Prediction App 🌊
# ==========================

import streamlit as st
import pandas as pd
import pickle

# --------------------------
# Load the trained model
# --------------------------
try:
    with open("LinearRegression.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("❌ LinearRegression.pkl not found. Make sure it is in the same folder as this app.")
    st.stop()

# --------------------------
# App Title
# --------------------------
st.title("🌍 Ocean Plastic Pollution Prediction App")
st.markdown(
    "Use this app to predict **Plastic Weight (kg)** in ocean regions based on pollution data."
)

# --------------------------
# Sidebar - Single Prediction Inputs
# --------------------------
st.sidebar.header("🔧 Input Features for Single Prediction")

data_Source_encoded = st.sidebar.number_input("Data Source Encoded", min_value=0, value=1)
country_encoded = st.sidebar.number_input("Country Encoded", min_value=0, value=1)
region_encoded = st.sidebar.number_input("Region Encoded", min_value=0, value=1)
year = st.sidebar.number_input("Year", min_value=1900, max_value=2100, value=2024)
pollution_level_encoded = st.sidebar.number_input(
    "Pollution Level Encoded (Low=0, Moderate=1, High=2)", min_value=0, max_value=2, value=1
)
waste_efficiency = st.sidebar.number_input(
    "Waste Management Efficiency (0-1)", min_value=0.0, max_value=1.0, step=0.01, value=0.5
)
nearby_population = st.sidebar.number_input("Nearby Population", min_value=0, value=10000)

# --------------------------
# Prepare input dataframe for single prediction
# --------------------------
input_data = pd.DataFrame({
    'data_Source_encoded': [data_Source_encoded],
    'Country_encoded': [country_encoded],
    'Region_encoded': [region_encoded],
    'Year': [year],
    'Pollution_Level_encoded': [pollution_level_encoded],
    'Waste_Management_Efficiency': [waste_efficiency],
    'Nearby_Population': [nearby_population]
})

st.subheader("🧾 Input Data Preview")
st.write(input_data)

# --------------------------
# Single Prediction
# --------------------------
if st.button("Predict Plastic Weight (kg)"):
    prediction = model.predict(input_data)
    st.success(f"🌊 **Predicted Plastic Weight:** {prediction[0]:,.2f} kg")

# --------------------------
# Batch Prediction from Excel
# --------------------------
st.markdown("---")
st.subheader("📤 Upload Excel File for Batch Prediction")
uploaded_file = st.file_uploader("Upload Excel file (.xlsx) with required columns", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.write("📄 Uploaded Data Preview:", df.head())

        # Required columns
        required_cols = ['data_Source_encoded','Country_encoded','Region_encoded','Year',
                         'Pollution_Level_encoded','Waste_Management_Efficiency','Nearby_Population']

        if all(col in df.columns for col in required_cols):
            preds = model.predict(df[required_cols])
            df['Predicted_Plastic_Weight_kg'] = preds
            st.write("✅ Prediction Results:", df.head())

            # Download predictions as CSV
            st.download_button(
                label="⬇️ Download Predictions as CSV",
                data=df.to_csv(index=False).encode('utf-8'),
                file_name='Predicted_Ocean_Plastic.csv',
                mime='text/csv'
            )
        else:
            st.error(f"Uploaded file must contain all required columns: {required_cols}")
    except Exception as e:
        st.error(f"Error reading file: {e}")

st.markdown("---")
st.caption("Developed with ❤️ using Streamlit & Scikit-learn")

import streamlit as st

st.title("🌊 Ocean Pollution Prevention Suggestions")
st.write("Here are simple, easy-to-understand tips to help prevent ocean pollution.")

# ------------------------------
# 1️⃣ Waste Management
# ------------------------------
with st.expander("📦 Waste Management"):
    st.markdown("""
### • **Reduce single-use plastics**  
Plastic items are used once and thrown away. Avoid them to keep oceans clean.

### • **Use reusable containers**  
Carry your own bottle or box. It reduces waste and protects sea life.

### • **Dispose garbage properly**  
Always put waste in bins. This stops trash from entering rivers and oceans.

### • **Promote recycling**  
Recycle paper, plastic, and metal. It reduces pollution in land and water.
""")

# ------------------------------
# 2️⃣ Chemical & Industrial Control
# ------------------------------
with st.expander("🧪 Chemical & Industrial Control"):
    st.markdown("""
### • **Limit chemical runoff**  
Factories should not let dirty water flow into rivers. This keeps oceans cleaner.

### • **Reduce fertilizers & pesticides**  
Too many farm chemicals wash into water and harm fish. Use them carefully.

### • **Improve wastewater treatment**  
Used water must be cleaned before release. This stops harmful toxins.

### • **Use eco-friendly cleaning products**  
Choose natural cleaners. They are safer for water and marine life.
""")

# ------------------------------
# 3️⃣ Marine & Coastal Protection
# ------------------------------
with st.expander("🐠 Marine & Coastal Protection"):
    st.markdown("""
### • **Prevent oil spills**  
Check boats and ships regularly. This avoids oil leaking into the sea.

### • **Protect coral reefs**  
Corals are home for many fish. Do not damage or touch them.

### • **Avoid overfishing**  
Catch only what is needed. This helps ocean animals survive.

### • **Maintain ships & boats**  
Well-maintained boats release fewer harmful liquids into the ocean.
""")

# ------------------------------
# 4️⃣ Community Awareness & Action
# ------------------------------
with st.expander("👥 Community Awareness & Action"):
    st.markdown("""
### • **Conduct beach clean-ups**  
Cleaning beaches removes trash before waves pull it into the sea.

### • **Increase public education**  
Teach people how their actions impact the ocean. Better knowledge means better habits.

### • **Encourage responsible tourism**  
Visitors should avoid littering and respect marine life and beaches.

### • **Support conservation groups**  
Help groups that work to save oceans. Even small support makes a difference.
""")

# ------------------------------
# 5️⃣ Climate & Energy Control
# ------------------------------
with st.expander("⚡ Climate & Energy Control"):
    st.markdown("""
### • **Reduce carbon footprint**  
Use less fuel and energy. This helps slow down ocean warming.

### • **Save electricity**  
Turn off lights and devices when not needed. It reduces pollution.

### • **Use renewable energy**  
Solar and wind power are clean and safe for the environment.

### • **Reduce vehicle emissions**  
Use public transport or share rides. This lowers pollution that affects oceans.
""")

