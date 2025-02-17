import streamlit as st
# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1  # kgCO2/kg
    }
}

# Set wide layout and page name with dark theme
st.set_page_config(
    layout="wide",
    page_title="Personal Carbon Calculator",
    page_icon="🌍",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful and unique design
st.markdown("""
<style>
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
    
    .stApp {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }

    
    .st-bb {
        background-color: #262730;
        transition: all 0.3s ease;
    }
    
    .st-bd {
        border-color: #262730;
        transition: border-color 0.3s ease;
    }
    
    .stButton>button {
        background: linear-gradient(145deg, #6a11cb, #2575fc);
        color: white;
        border-radius: 25px;
        padding: 15px 30px;
        border: none;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        font-weight: 600;
        letter-spacing: 1px;
        animation: float 3s ease-in-out infinite;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }

    
    .stSlider .thumb {
        background: #ffffff !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        border: 2px solid #6a11cb;
        transition: all 0.3s ease;
    }
    
    .stSlider .track {
        background: linear-gradient(90deg, #6a11cb, #2575fc) !important;
        height: 8px;
        border-radius: 4px;
        transition: all 0.3s ease;
    }

    
    .stNumberInput input {
        background: rgba(255,255,255,0.1);
        color: #ffffff;
        border: 2px solid rgba(255,255,255,0.2);
        border-radius: 12px;
        padding: 10px 15px;
        transition: all 0.3s ease;
        backdrop-filter: blur(5px);
    }
    
    .stNumberInput input:focus {
        border-color: #6a11cb;
        box-shadow: 0 0 0 3px rgba(106,17,203,0.2);
    }

    
    .stHeader {
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: float 4s ease-in-out infinite;
    }
    
    .stSubheader {
        color: rgba(255,255,255,0.9);
        font-weight: 500;
        margin-bottom: 1.5rem;
    }
    
    .stMarkdown {
        background: rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .stProgress > div > div {
        background: linear-gradient(90deg, #6a11cb, #2575fc) !important;
        transition: width 0.5s ease-in-out;
        border-radius: 4px;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
</style>
""", unsafe_allow_html=True)




# Streamlit app code
st.title("Personal Carbon Calculator App 🌱")


# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", ["India"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Daily commute distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🍽️ Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍽️ Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")

# Normalize inputs
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if meals > 0:
    meals = meals * 365  # Convert daily meals to yearly
if waste > 0:
    waste = waste * 52  # Convert weekly waste to yearly

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste

# Convert emissions to tonnes and round off to 2 decimal points
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)

if st.button("Calculate CO2 Emissions", key="calculate_button"):
    with st.spinner('Calculating your carbon footprint...'):
        import time
        time.sleep(1.5)  # Simulate calculation time
        st.markdown("""
        <style>
        @keyframes fall {
            0% { transform: translateY(-100px) rotate(0deg); }
            100% { transform: translateY(100vh) rotate(360deg); }
        }
        
        .leaf {
            position: fixed;
            top: -100px;
            color: #4CAF50;
            font-size: 24px;
            animation: fall linear infinite;
        }
        </style>
        <div class="leaf" style="left: 10%; animation-duration: 5s;">🍃</div>
        <div class="leaf" style="left: 30%; animation-duration: 7s;">🍃</div>
        <div class="leaf" style="left: 50%; animation-duration: 6s;">🍃</div>
        <div class="leaf" style="left: 70%; animation-duration: 8s;">🍃</div>
        <div class="leaf" style="left: 90%; animation-duration: 9s;">🍃</div>
        """, unsafe_allow_html=True)





    # Display results
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year", icon="✅")
        st.toast('Calculation complete!', icon='🎉')


        st.warning("In 2021, CO2 emissions per capita for India was 1.9 tons of CO2 per capita. Between 1972 and 2021, CO2 emissions per capita of India grew substantially from 0.39 to 1.9 tons of CO2 per capita rising at an increasing annual rate that reached a maximum of 9.41% in 2021")
