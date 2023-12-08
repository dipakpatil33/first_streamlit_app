import streamlit
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




#---  snowflake connectivity 

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

#  --my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()") --
my_cur.execute("SELECT * from fruit_load_list")

my_data_row = my_cur.fetchone()
# ----streamlit.text("Hello from Snowflake:")
#streamlit.text("The Fruit Load List Contains: ")
streamlit.header("The Fruit Load List Contains: ")

#streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)

