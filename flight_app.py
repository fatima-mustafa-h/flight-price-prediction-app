import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="Flight Price Predictor", layout="wide")

# Load model
model = joblib.load("model.pkl")

    
# Background
# Build CSS string
css = """
<style>
div[data-testid="stAppViewContainer"] {
    background: url("https://i.postimg.cc/NGpPGfjq/airplane_bg.jpg") !important;
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
    background-blend-mode: overlay !important;}

/* Title styling */
.title {
    font-size: 4.3vw !important;
    font-weight: 800 !important;
    font-family: 'Arial Black', sans-serif;
    color: #032C47 !important;
    text-align: center !important;
    line-height: 1.2 !important;
    margin-bottom: 40px;
}

.subtitle {
    font-size: 1.9vw !important;
    font-weight: 600 !important;
    font-family: 'Arial Black', sans-serif;
    color: #242424 !important;
    text-align: center !important;
    margin-bottom: 30px;
}

.label-col1, .label-col2 {
    font-size: 20px !important;
    font-weight: bold !important;
    line-height: 1.2 !important;
    margin-top: 25px !important;
    margin-bottom: 0 !important;   
    display:block !important;
    color: #032C47 !important;     
    text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff,
                 -1px  1px 0 #fff, 1px  1px 0 #fff;
}


/* Slider track */
div[data-testid="stSlider"] input[type=range]::-webkit-slider-runnable-track {
    background: #032C47 !important;  
    height: 6px !important;
    border-radius: 3px !important;
}

/* Slider thumb (the draggable circle) */
div[data-testid="stSlider"] input[type=range]::-webkit-slider-thumb {
    background: #032C47 !important;   
    border: 2px solid #fff !important;
    height: 18px !important;
    width: 18px !important;
    border-radius: 50% !important;
    cursor: pointer !important;
    -webkit-appearance: none !important;
    margin-top: -6px !important;
}


/* Button styling */
div.stButton > button {
    background-color: #032C47 !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 8px !important;
    padding: 0.5em 1.2em !important;
    margin-top: 20px !important;
    width: 100% !important;
    font-size: 1.2vw !important;
    transition: background-color 0.3s ease !important;
}

div.stButton > button:hover {
    background-color: #449BDB !important;
    color: #032C47 !important;
    font-weight: bold !important;
    transform: scale(1.05) !important;
    transition: background-color 0.3s ease, transform 0.3s ease !important;
}

</style>
"""

# Inject CSS into Streamlit
st.markdown(css, unsafe_allow_html=True)




# Title with minimal airplane icon
st.markdown('<p class="title">✈️ Flight Ticket Price Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enter flight details to estimate the ticket price</p>', unsafe_allow_html=True)
st.write("")  # spacing

# Layout in two columns
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="label-col1">Airline</div>', unsafe_allow_html=True)
    airline = st.selectbox("", ["Air_India", "Indigo", "Vistara", "SpiceJet", "GO_FIRST"], key="airline")

    st.markdown('<div class="label-col1">Source City</div>', unsafe_allow_html=True)
    source_city = st.selectbox("", ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"], key="source_city")

    st.markdown('<div class="label-col1">Departure Time</div>', unsafe_allow_html=True)
    departure_time = st.selectbox("", ["Morning", "Afternoon", "Evening", "Night"], key="departure_time")

    st.markdown('<div class="label-col1">Stops</div>', unsafe_allow_html=True)
    stops = st.selectbox("", ["zero", "one", "two_or_more"], key="stops")

    st.markdown('<div class="label-col1">Duration (minutes)</div>', unsafe_allow_html=True)
    duration = st.number_input("", min_value=30, max_value=2000, value=120, key="duration")

with col2:
    st.markdown('<div class="label-col2">Destination City</div>', unsafe_allow_html=True)
    destination_city = st.selectbox("", ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"], key="destination_city")

    st.markdown('<div class="label-col2">Arrival Time</div>', unsafe_allow_html=True)
    arrival_time = st.selectbox("", ["Morning", "Afternoon", "Evening", "Night"], key="arrival_time")

    st.markdown('<div class="label-col2">Class</div>', unsafe_allow_html=True)
    travel_class = st.selectbox("", ["Economy", "Business"], key="travel_class")

    st.markdown('<div class="label-col2">Days Left Before Departure</div>', unsafe_allow_html=True)
    days_left = st.slider("", 1, 60, 10, key="days_left")




# Prepare input for prediction
input_df = pd.DataFrame({
    "airline": [airline],
    "source_city": [source_city],
    "departure_time": [departure_time],
    "stops": [stops],
    "arrival_time": [arrival_time],
    "destination_city": [destination_city],
    "class": [travel_class],
    "duration": [duration],
    "days_left": [days_left]
})

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Price: ₹ {int(prediction[0])}")