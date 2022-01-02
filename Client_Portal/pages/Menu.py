import mysql.connector as connection
import pyautogui
import streamlit as st

mydb = connection.connect(host="localhost", password="qtnkwvnv7632", user="root", database="cms", use_pure=True)
mycursor = mydb.cursor()


def app():
    st.markdown('----')
    st.subheader("Menu")

    # image urls from the DB will be appened in the list below
    mycursor.execute('Select img from menu')
    images = []
    myresult = mycursor.fetchall()
    for x in myresult:
        images.append(x[0])
    # item index along with item name from the DB will be appened in the list below
    mycursor.execute('Select item from menu')
    captions = []
    myresult = mycursor.fetchall()
    for x in myresult:
        captions.append(x[0])
    pick_img = st.sidebar.radio("Choose Item",
                                [x for x in range(1, len(images) + 1)])

    st.sidebar.write('---------------')
    st.image(images, caption=captions, width=700)

    for x in range(1, len(images) + 1):
        if pick_img == x:
            st.sidebar.write('Details')
            mycursor.execute('Select rating from menu where item = %s', (captions[x - 1],))
            result = mycursor.fetchall()
            y = 'This item is rated as: ' + str(result[0][0])
            st.sidebar.write(y)
            st.sidebar.text('Enter your rating:')
            rating = st.sidebar.slider('Rating', 0, 5, 1, key='halt')
            button1 = st.sidebar.button('Submit')
            if button1:
                # add feature to add submitted rating and review into the DB
                new_rating = (rating + result[0][0]) / 2
                mycursor.execute('Update menu set rating = %s where item = %s', (new_rating, captions[x - 1],))
                st.sidebar.success("Success!")
                pyautogui.hotkey("ctrl", "F5")
