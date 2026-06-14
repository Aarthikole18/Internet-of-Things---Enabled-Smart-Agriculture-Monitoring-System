import streamlit as st
import pandas as pd

st.title("🌱 Smart Agriculture Dashboard (Simulation)")

df = pd.read_csv("data/sensor.csv")

st.subheader("📊 Sensor Data")

st.dataframe(df)

st.subheader("🌡 Temperature vs Humidity")
st.line_chart(df[["temp", "humidity"]])

st.subheader("🌱 Soil Moisture Trend")
st.line_chart(df["soil"])

st.subheader("💡 Light Intensity")
st.line_chart(df["light"])

st.subheader("🚰 Pump Status")

st.write(df["pump"].value_counts())