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

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())

#--to format data in table (json to table)
streamlit.header('FRUITYVICE FRUIT ADVICE !')

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
