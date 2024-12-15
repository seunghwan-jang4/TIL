import streamlit as st
import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=YOUR_API_KEY")
if response.status_code == 200:
    data = response.json()
    st.write(f"Temperature: {data['main']['temp']}K")