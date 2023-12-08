import streamlit
from urllib.error import URLError
streamlit.title('My Parents New healthy dinner')

streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry and Oatmeal')
streamlit.text('🥗 Kale, spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled  free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



import pandas


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected =streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado' ,'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#streamlit.dataframe(my_fruit_list)

#   --------------------------------------
#   -------------------------------------
#--upto this its commeented           

   # --new code for      --for select value in textbox   ***
import requests
# create repeatable code block ( called as -function)
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized
   
streamlit.header('FRUITYVICE FRUIT ADVICE !')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to Get Information ??")
  else:    
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
   # -- end of new code                                  ***      

#streamlit.stop()  # it will will stop to implement from here

#---  snowflake connectivity 

import snowflake.connector

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()

#  --my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()") --
#my_cur.execute("SELECT * from fruit_load_list")
#my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")  # test pusrpose will give error >> data inserted from streamlit to sf


#my_data_row = my_cur.fetchone()   --will retrieve only one row 
#my_data_rows = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
#streamlit.text("The Fruit Load List Contains: ")
#streamlit.header("The Fruit Load List Contains: ")

#streamlit.text(my_data_row)
#streamlit.dataframe(my_data_row)
#streamlit.dataframe(my_data_rows)

#add_my_fruit = streamlit.text_input('What fruit would you like to add?')
#streamlit.write('Thanks For Adding ', add_my_fruit)


# allow end user to add fruit to list
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')") 
      return "Thanks For adding ", + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function =insert_row_snowflake(add_my_fruit)
   streamlit.text =back_from_function
   





streamlit.stop()
'''
#-----------------

---commented multiline for exception handleing to show error
#--to format data in table (json to table)
streamlit.header('FRUITYVICE FRUIT ADVICE !')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
# -- fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")--  COMMENTED FOR RUN NEXT LINE SAME BUT CAN ACCESS UNIQUE FRUIT FROM API
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "KIWI")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#streamlit.text(fruityvice_response.json())


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


#-------------------
'''

'''
import requests
streamlit.header('FRUITYVICE FRUIT ADVICE !')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to Get Information ??")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()

  '''
