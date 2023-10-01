import streamlit as st
import pandas as pd
import time
import numpy as np

st.title('Streamlit 101')

# dataframe
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=(f'col {i+1}' for i in range(20))
)
st.write(dataframe.style.highlight_max(axis=0))

# chart data and checkbox
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

if st.checkbox('Show dataframe'):
    chart_data

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [200,200] + [-18.92400, -48.28512],
    columns=['lat', 'lon'])

st.map(map_data, color='#00ff00', zoom=13, size=1)


# side bar and write
x = st.sidebar.slider('x') # isso é um widget
st.write(x, 'squared is', x*x)


left_column, right_column = st.columns(2)

with left_column:
    st.button(label='Desligar', type='primary')
    if st.button(label='Ligar'):
        st.write('Lâmpada ligada')
    else:
        st.write('Lâmpada desligada')

right_column.radio(
    'Escolha a sua casa:' ,
    ('Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slythefin')
)

# o text_input é um widget de entrada de texto
st.text_input('Seu nome: ', key='name')

# acessando o valor digitado pela chave
st.session_state.name

# selectbox and side bar
option =  st.sidebar.selectbox(
    'Qual o melhor framework?',
    ['Pandas', 'Polars', 'Pyspark', 'Dask'],
    index=None,
    placeholder='Selecione o seu favorito'
    )

'Você escolheu ', option

# viewing the progress
start = st.button('Start pipeline')
latest_iteration = st.empty()
bar = st.progress(0)
if start:
    for i in range(100):
        latest_iteration.text(f'Iteration: {i+1}')
        bar.progress(i+1)
        time.sleep(0.1)

