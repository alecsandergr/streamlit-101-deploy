import os
from dotenv import load_dotenv
import numpy as np
import streamlit as st
import pandas as pd
from datetime import time

load_dotenv() # <- carrega as variáveis de ambiente do .env

DATE_COLUMN = 'date/time'
DATA_URL = os.getenv('USER_DATA_URL') # define a varíavel de ambiente na variável DATA_URL
print(DATA_URL)

@st.cache_data
def load_df(nrows: int):
    df = pd.read_csv(DATA_URL, nrows=nrows)
    df.columns = df.columns.str.lower()
    df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])

    return df

st.title('Uber - Corridas em NYC')

data_load_state = st.text('Carregando os dados...')
df = load_df(10000)

if st.checkbox('Mostrar tabela'):
    st.subheader('Tabela com os dados brutos')
    st.dataframe(df)

st.subheader('Número de corridas por hora')
hist_values = np.histogram(
    df[DATE_COLUMN].dt.hour, bins=24, range=(0,24)
)[0]

st.bar_chart(hist_values)

# filtro de hora
hour_to_filter = st.sidebar.slider(
    'Hora', 
    time(0, 0), time(23, 59), (time(12, 0), time(23, 0)))

lower, upper = hour_to_filter
cond = ((df[DATE_COLUMN].dt.time >= lower) & (df[DATE_COLUMN].dt.time <= upper))
filtered_data = df[cond]

st.subheader(f'Mapa de todas as viagens de {lower.strftime("%H:%M")} até às {upper.strftime("%H:%M")}')
st.map(filtered_data)


