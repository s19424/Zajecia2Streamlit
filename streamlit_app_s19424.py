import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os

from PIL import Image
img = Image.open("flaga.png")
st.image(img)

st.header('Tłumacz języka z angielskiego na niemiecki')
st.subheader('O Tłumaczu')
st.write('Aplikacja ma na celu tłumaczenie języka angielskiego na niemiecki')
st.text('Wybierz opcję z listy, a następnie wpisz w pole poniżej tekst do przetłumaczenia i naciśnij Ctrl + Enter')

import streamlit as st
from transformers import pipeline
option = st.selectbox(
    "Opcje",
    [
        "Tłumacz angielsko niemiecki",
    ],
)

if option == "Tłumacz angielsko niemiecki":
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner(text="Poczekaj chwilę. Przetwarzam dla ciebie informację."):
            translator = pipeline("translation_en_to_de")
            answer = translator(text)[0]
            st.success("Udało się! Twoje tłumaczenie to: ")
            st.code(answer["translation_text"])

st.subheader('S19424')
st.write('Tomasz Krasieńko')
#st.write('🐞 Na końcu umieść swój numer indeksu')
#st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
#st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
