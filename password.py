import streamlit as st
from src.main import PinGenerator, RandomPassword, Memorablepassword

st.image('https://i.pinimg.com/564x/4a/23/6c/4a236c68e2b1e50daba048d62a2d09a9.jpg', width=200)
st.title(':zap: Password Generator')

option = st.radio(
    'Select a Password Generator',
    ("Pin code","Random Password", "Memorable Generatore")
)

if option =='Pin code':
    length = st.slider("Select the length of the pin code", 4, 12)

    generatore = PinGenerator(length)

elif option == 'Random Password':
    length = st.slider("Select the length the password", 4, 12)
    include_numbers =st.toggle("Include number")

    include_symbols =st.toggle("Include_symbol")
    generatore = RandomPassword(length, include_numbers, include_symbols)

elif option == 'Memorable Generatore':
    separator = st.text_input("Seprator", value='-')
    number_of_word = st.slider("select number of words:", 2, 8)
    capitalize = st.toggle("Capitalization")

    generatore = Memorablepassword(separator, number_of_word, capitalize)









password = generatore.generate()
st.write(f" Your Password is: ```{password}```   ")