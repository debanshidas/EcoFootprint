import streamlit as st
import time
import plotly.express as px

# Define emission factors (replace with accurate data)
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1  # kgCO2/kg
    }
}

# Set page layout and config
st.set_page_config(
    layout="wide",
    page_title="🌱 Personal Carbon Calculator",
    page_icon="🌍",
    initial_sidebar_state="expanded"
)

# Custom CSS for unique design
st.markdown("""
<style>
    body { background-color: #0E1117; color: #FAFAFA; }
    .stApp { animation: fadeIn 0.5s ease-out; }
    .stButton>button { background-color: #28a745; color: white; border-radius: 10px; }
    .stButton>button:hover { background-color: #218838; }
    .stSelectbox div { background-color: #262730; color: white; }
    .stSlider .thumb, .stSlider .track { background-color: #4CAF50 !important; }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🌱 Personal Carbon Footprint Calculator")

# User Inputs
st.sidebar.header("Input Your Data")
country = st.sidebar.selectbox("🌍 Select Your Country", ["India"], index=0)

distance = st.sidebar.slider("🚗 Daily Commute Distance (km)", 0.0, 100.0, 10.0)
electricity = st.sidebar.slider("💡 Monthly Electricity Usage (kWh)", 0.0, 1000.0, 200.0)
waste = st.sidebar.slider("🗑️ Weekly Waste Generated (kg)", 0.0, 100.0, 5.0)
meals = st.sidebar.number_input("🍽️ Meals Per Day", min_value=0, max_value=10, value=3)

# Normalize inputs
distance *= 365  # Convert to yearly
electricity *= 12  # Convert to yearly
meals *= 365  # Convert to yearly
waste *= 52  # Convert to yearly

# Calculate emissions
transportation_emissions = round(EMISSION_FACTORS[country]["Transportation"] * distance / 1000, 2)
electricity_emissions = round(EMISSION_FACTORS[country]["Electricity"] * electricity / 1000, 2)
diet_emissions = round(EMISSION_FACTORS[country]["Diet"] * meals / 1000, 2)
waste_emissions = round(EMISSION_FACTORS[country]["Waste"] * waste / 1000, 2)
total_emissions = round(transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2)

# Calculate Button
if st.sidebar.button("🔢 Calculate Carbon Footprint"):
    with st.spinner("Calculating your carbon footprint..."):
        time.sleep(1.5)
    st.balloons()

    # Display results
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("🌍 Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2/year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2/year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2/year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2/year")
    
    with col2:
        st.header("📊 Your Total Carbon Footprint")
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        st.success(f"🌍 Total: {total_emissions} tonnes CO2/year")
        st.toast("Calculation complete!", icon="🎉")

    # Pie Chart Visualization
    labels = ["Transportation", "Electricity", "Diet", "Waste"]
    values = [transportation_emissions, electricity_emissions, diet_emissions, waste_emissions]
    fig = px.pie(names=labels, values=values, title="Carbon Footprint Breakdown", color=labels,
                 color_discrete_map={"Transportation": "#FF5733", "Electricity": "#33FFBD", "Diet": "#337BFF", "Waste": "#A533FF"})
    st.plotly_chart(fig)

    # Warning message
    st.warning("In 2021, India's per capita CO2 emissions were 1.9 tons. Reduce your footprint by making sustainable choices!")
