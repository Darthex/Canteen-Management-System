import streamlit as st
from Multiapp import MultiApp
from pages import Bookings, Home, Menu


st.title('College Cafe')
app = MultiApp()

app.add_app('Home', Home.app)
app.add_app('Menu', Menu.app)
app.add_app('Bookings', Bookings.app)

app.run()
