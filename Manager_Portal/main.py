import streamlit as st
import pandas as pd
import mysql
import mysql.connector as connection
import pyautogui

mydb = connection.connect(host="localhost", password="qtnkwvnv7632", user="root", database="cms", use_pure=True)
mycursor = mydb.cursor()

st.title('Manage')
status = st.radio("Select Option: ", ('Offers', 'Menu', 'Check booking'))

i = 1
if (status == 'Offers'):
    frame = pd.read_sql("Select * from offers", mydb);
    st.dataframe(frame, 800, 800)
    status = st.radio("Select Operation: ", ('Add', 'Delete'))
    if (status == 'Add'):
        item = st.text_input("Enter Item")
        old_price = st.text_input("Enter old price")
        new_price = st.text_input("Enter new price")
        img = st.text_input("Enter img url")
        if (st.button('Submit')):
            item = item.title()
            old_price = old_price.title()
            new_price = new_price.title()
            img = img.title()
            val = [(item, old_price, new_price, img)]
            mycursor.executemany("INSERT INTO offers (item, old_price, new_price, img) VALUES (%s, %s, %s, %s)", val)
            mydb.commit()
            st.success("Success")
            pyautogui.hotkey("ctrl", "F5")
        else:
            st.error("All fields are required")
    elif (status == 'Delete'):
        to_del = st.text_input("Enter offer to delete")
        mycursor.execute('Select item from offers')
        myresult = mycursor.fetchall()
        delete = to_del.title()
        if (st.button('Submit')):
            for item in myresult:
                if delete == item[0]:
                    mycursor.execute('delete from offers where item = %s', (delete,))
                    mydb.commit()
                    st.success('Success')
                    pyautogui.hotkey("ctrl", "F5")
                    break
                elif delete != item[0]:
                    pass
                else:
                    print('No such item!')
elif (status == 'Menu'):
    status = st.selectbox("Select Category: ", ('VEG', 'NON-VEG'))
    if (status == 'VEG'):
        frame = pd.read_sql("Select item, price, about from menu where category = 'VEG'", mydb);
        st.dataframe(frame, 800, 800)
        status = st.radio("Select Operation: ", ('Add', 'Delete'))
        if (status == 'Add'):
            item = st.text_input("Enter Item")
            price = st.text_input("Enter price")
            about = st.text_input("Enter about")
            img = st.text_input("Enter img url")
            if (st.button('Submit') and len(item)>0 and len(price)>0 and len(about)>0):
                item = item.title()
                price = price.title()
                about = about.title()
                img = img.title()
                val = [(item, price, about, img)]
                mycursor.executemany("INSERT INTO menu (category, item, price, about, img) VALUES ('VEG', %s, %s, %s, %s)", val)
                mydb.commit()
                st.success("Success")
                pyautogui.hotkey("ctrl", "F5")
            else:
                st.error("All fields are required")
        elif(status == 'Delete'):
            to_del = st.text_input("Enter Item to delete")
            mycursor.execute('Select item from menu')
            myresult = mycursor.fetchall()
            delete = to_del.title()
            if (st.button('Submit')):
                for item in myresult:
                    if delete == item[0]:
                        mycursor.execute('delete from menu where item = %s', (delete,))
                        mydb.commit()
                        st.success('Success')
                        pyautogui.hotkey("ctrl", "F5")
                        break
                    elif delete != item[0]:
                        pass
                    else:
                        print('No such item!')

    elif (status == 'NON-VEG'):
        frame = pd.read_sql("Select item, price, about from menu where category = 'NON-VEG'", mydb)
        st.dataframe(frame, 900, 1200)
        status = st.radio("Select Operation: ", ('Add', 'Delete'))
        if (status == 'Add'):
            item = st.text_input("Enter Item")
            price = st.text_input("Enter price")
            about = st.text_input("Enter about")
            if (st.button('Submit') and len(item) > 0 and len(price) > 0 and len(about) > 0):
                item = item.title()
                price = price.title()
                about = about.title()
                val = [(item, price, about)]
                mycursor.executemany("INSERT INTO menu (category, item, price, about) VALUES ('VEG', %s, %s, %s)",
                                     val)
                mydb.commit()
                st.success("Success")
                pyautogui.hotkey("ctrl", "F5")
            else:
                st.error("All fields are required")
        elif (status == 'Delete'):
            to_del = st.text_input("Enter Item to delete")
            mycursor.execute('Select item from menu')
            myresult = mycursor.fetchall()
            delete = to_del.title()
            if (st.button('Submit')):
                for item in myresult:
                    if delete == item[0]:
                        mycursor.execute('delete from menu where item = %s', (delete,))
                        mydb.commit()
                        st.success('Success')
                        pyautogui.hotkey("ctrl", "F5")
                        break
                    elif delete != item[0]:
                        pass
                    else:
                        print('No such item!')


elif (status == 'Check booking'):
    mycursor.execute('Select stud_id from book')
    myresult = mycursor.fetchall()
    stud_id = st.text_input("Enter Student ID:")
    stud_id = stud_id.title()
    if (st.button('Submit')):
        for id in myresult:
            if int(stud_id) == id[0]:
                st.text('Booking found!')
                mycursor.execute('Select stud_id, no_seats, time from book where stud_id = %s', (stud_id, ))
                myresult = mycursor.fetchall()
                for x in myresult:
                    st.text('ID: ' + str(x[0]))
                    st.text('Number of tables: ' + str(x[1]))
                    st.text('Time: ' + str(x[2]))
                break
            elif stud_id != id[0]:
                pass
    else:
        st.error('No booking found!')
