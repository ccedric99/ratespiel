import streamlit as st
from random import randint

st.title("🎯 Zahlenratespiel")

# Zufallszahl nur einmal erzeugen
if "zahl" not in st.session_state:
    st.session_state.zahl = randint(1, 100)

st.write("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht 🙂")

guess = st.number_input("Was ist die gesuchte Zahl?", min_value=1, max_value=100, step=1)

if st.button("Raten"):

    if guess > st.session_state.zahl:
        st.warning("Deine Zahl ist zu groß.")

    elif guess < st.session_state.zahl:
        st.warning("Deine Zahl ist zu klein.")

    else:
        st.success("🎉 Super! Du hast die richtige Zahl gefunden!")
        st.session_state.zahl = randint(1, 100)