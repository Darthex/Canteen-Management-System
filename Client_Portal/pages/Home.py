from datetime import datetime as dt

import mysql.connector as connection
import streamlit as st

mydb = connection.connect(host="localhost", password="qtnkwvnv7632", user="root", database="cms", use_pure=True)
mycursor = mydb.cursor()


def app():
    st.markdown('----')
    st.subheader('Feeling Lucky?')

    day = dt.today().strftime("%A")
    st.write('Its ' + str(day) + ' today!')

    if day == 'Sunday':
        special = 'Mushroom Sandwich'
        image = 'https://www.archanaskitchen.com/images/archanaskitchen/World_Sandwiches_Burgers_Wraps/Grilled_Mushroom_Sandwich_Recipe_with_Herbs-1.jpg'
    elif day == 'Monday':
        special = 'Aloo Samosa'
        image = 'https://www.masala.tv/wp-content/uploads/2017/05/mutton-mince-samosa.jpg'
    elif day == 'Tuesday':
        special = 'Chicken Sandwich'
        image = 'https://www.thasneen.com/cooking/wp-content/uploads/2021/06/Grilled-chicken-sandwich-crispy-golden-best-recipe.jpg'
    elif day == 'Wednesday':
        special = 'Beef Sandwich'
        image = 'https://www.sargento.com/assets/Uploads/Recipe/Image/BeefSandwich__FillWzExNzAsNTgzXQ.jpg'
    elif day == 'Thursday':
        special = 'Biryani'
        image = 'https://ichef.bbci.co.uk/news/976/cpsprodpb/E264/production/_116965975_gettyimages-639704020.jpg'
    elif day == 'Friday':
        special = 'Shawarma'
        image = 'https://b.zmtcdn.com/data/pictures/chains/3/19519883/5048a0f29a77271a19f623ac67488f34.jpg'
    else:
        special = 'Momos'
        image = 'https://www.cookforindia.com/wp-content/uploads/2016/02/Momos-snap.jpg'

    st.write('Today\'s special is: ' + str(special))
    st.image(image)

    st.markdown('----')
    mycursor.execute('Select img from offers')
    images = []
    myresult = mycursor.fetchall()
    for x in myresult:
        images.append(x[0])
    # item index along with item name from the DB will be appened in the list below
    mycursor.execute('Select item from offers')
    captions = []
    myresult = mycursor.fetchall()
    for x in myresult:
        captions.append(x[0])
    st.subheader("Today's Offers:")
    st.image(images, caption=captions, width=700)
