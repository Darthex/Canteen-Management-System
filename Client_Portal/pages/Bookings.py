import mysql.connector as connection
import pandas as pd
import streamlit as st

mydb = connection.connect(host="localhost", password="qtnkwvnv7632", user="root", database="cms", use_pure=True)
mycursor = mydb.cursor()


def app():
    st.subheader("Seat bookings")
    frame = pd.read_sql("Select stud_id, no_seats from book", mydb)
    st.dataframe(frame, 900, 1200)

    #    def taken(se):
    #       seats[se] = "Booked"

    #   def book(tk):
    #      for i in range(1, tk + 1):
    #         if seats[i] != "available":
    #            tk += 1
    #           continue
    #      taken(i)

    st.sidebar.subheader("Book Seats")
    input = st.sidebar.number_input("Number of seats to be booked", step=1)
    std_id = st.sidebar.text_input("Student ID:")

    button = st.sidebar.button("submit")
    if button:
        mycursor.execute('INSERT INTO book(stud_id, no_seats) VALUES (%s, %s)', (std_id, input,))
        st.success("Success!")
