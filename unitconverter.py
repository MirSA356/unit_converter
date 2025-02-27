import streamlit as st
import time

# Page configuration
st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")

# Title with animation
st.title("📏 Stylish Unit Converter.... Created by Naseem Ahmed Detho")
st.write("Convert between various units with style!")

# Add a fun animation (balloons only once)
if "balloons_shown" not in st.session_state:
    with st.spinner("Loading the converter..."):
        time.sleep(2)
    st.balloons()
    st.session_state.balloons_shown = True

# Sidebar for user input
st.sidebar.header("Settings")
theme = st.sidebar.selectbox("Choose a theme", ["Light", "Dark"])

# Set theme
if theme == "Dark":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ffffff;
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_conversions = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "inches": 39.3701,
        "feet": 3.28084,
        "yards": 1.09361,
        "miles": 0.000621371,
    }
    return value * (length_conversions[to_unit] / length_conversions[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        "grams": 1,
        "kilograms": 0.001,
        "milligrams": 1000,
        "pounds": 0.00220462,
        "ounces": 0.035274,
        "tons": 0.00000110231,
    }
    return value * (weight_conversions[to_unit] / weight_conversions[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    else:
        return value

def convert_time(value, from_unit, to_unit):
    time_conversions = {
        "seconds": 1,
        "minutes": 1/60,
        "hours": 1/3600,
        "days": 1/86400,
        "weeks": 1/604800,
        "months": 1/2628000,
        "years": 1/31536000,
    }
    return value * (time_conversions[to_unit] / time_conversions[from_unit])

def convert_area(value, from_unit, to_unit):
    area_conversions = {
        "square meters": 1,
        "square kilometers": 0.000001,
        "square feet": 10.7639,
        "square miles": 0.000000386102,
        "acres": 0.000247105,
    }
    return value * (area_conversions[to_unit] / area_conversions[from_unit])

def convert_volume(value, from_unit, to_unit):
    volume_conversions = {
        "liters": 1,
        "milliliters": 1000,
        "cubic meters": 0.001,
        "gallons": 0.264172,
        "cubic feet": 0.0353147,
    }
    return value * (volume_conversions[to_unit] / volume_conversions[from_unit])

# Main converter
st.header("Unit Converter")

# Select conversion type
conversion_type = st.selectbox(
    "Select conversion type",
    ["Length", "Weight", "Temperature", "Time", "Area", "Volume"]
)

# Input value
value = st.number_input("Enter value to convert", min_value=0.0)

# Conversion logic
if conversion_type == "Length":
    from_unit = st.selectbox("From", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"])
    to_unit = st.selectbox("To", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"])
    result = convert_length(value, from_unit, to_unit)

elif conversion_type == "Weight":
    from_unit = st.selectbox("From", ["grams", "kilograms", "milligrams", "pounds", "ounces", "tons"])
    to_unit = st.selectbox("To", ["grams", "kilograms", "milligrams", "pounds", "ounces", "tons"])
    result = convert_weight(value, from_unit, to_unit)

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From", ["celsius", "fahrenheit", "kelvin"])
    to_unit = st.selectbox("To", ["celsius", "fahrenheit", "kelvin"])
    result = convert_temperature(value, from_unit, to_unit)

elif conversion_type == "Time":
    from_unit = st.selectbox("From", ["seconds", "minutes", "hours", "days", "weeks", "months", "years"])
    to_unit = st.selectbox("To", ["seconds", "minutes", "hours", "days", "weeks", "months", "years"])
    result = convert_time(value, from_unit, to_unit)

elif conversion_type == "Area":
    from_unit = st.selectbox("From", ["square meters", "square kilometers", "square feet", "square miles", "acres"])
    to_unit = st.selectbox("To", ["square meters", "square kilometers", "square feet", "square miles", "acres"])
    result = convert_area(value, from_unit, to_unit)

elif conversion_type == "Volume":
    from_unit = st.selectbox("From", ["liters", "milliliters", "cubic meters", "gallons", "cubic feet"])
    to_unit = st.selectbox("To", ["liters", "milliliters", "cubic meters", "gallons", "cubic feet"])
    result = convert_volume(value, from_unit, to_unit)

# Display result
if st.button("Convert"):
    st.success(f"Converted value: {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")