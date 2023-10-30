import streamlit as st
import pandas as pd
import requests
from PIL import Image

#Funcao para dar o get nas informacoes da API
def get_data(valor):

    url = f'https://economia.awesomeapi.com.br/last/{valor}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df

    else:
        st.error("Falha ao obter dados da API.")
        return None

#Banner e Configs da Aplicacao
st.set_page_config(
    page_title="Exchange Currency",
    page_icon=":chart_with_upwards_trend:",  # Icone da Pagina
    layout="wide",  # Layout da Pagina
)
st.markdown("<p style='margin-top:400px;'></p>", unsafe_allow_html=True)

#Opcoes de Cambios
currency_options = [
    "USD-EUR",
    "EUR-GBP",
    "JPY-USD",
    "CAD-USD",
    "AUD-USD",
    "GBP-USD",
    "USD-CNY",
    "EUR-JPY",
    "EUR-CHF",
    "USD-INR",
    "EUR-AUD",
    "EUR-CAD",
    "EUR-SEK",
    "USD-CHF",
    "EUR-NZD",
    "GBP-EUR",
    "USD-JPY",
    "CHF-USD",
    "USD-CAD",
    "SEK-EUR",
    "EUR-NOK",
    "AUD-EUR",
    "USD-SGD",
    "HKD-USD",
    "NZD-USD",
    "SGD-USD",
    "NOK-EUR",
    "KRW-USD",
    "TRY-USD",
    "MXN-USD",
    "ZAR-USD",
    "BRL-USD",
    "INR-USD",
    "RUB-USD",
    "CNY-USD",
    "XAU-USD",
    "XAG-USD",
    "XPT-USD",
    "XPD-USD",
    "PEN-EUR"
]

#Componentes da Sidebar
st.sidebar.markdown("<p style='margin-top:250px;'></p>", unsafe_allow_html=True)
st.sidebar.markdown(
    """<div style="text-align: center;"><h1 style='color: white;'>Conversor de Moedas</h1></div>""",
    unsafe_allow_html=True
)
st.sidebar.image('logo.png',use_column_width=True)

#Select box para o usuario escolher o Cambio
select_currency = st.sidebar.selectbox("Selecione a moeda desejada:", currency_options) 

if select_currency:
    st.markdown(f'<div class="currency-box gold">Moeda selecionada: {select_currency}</div>', unsafe_allow_html=True)
    df = get_data(select_currency)

    if df is not None:
        #Aplicando estilo na pagina
        st.markdown(
            """
            <style>
            .currency-box {
                background-color: #000000;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        #Selecionar o nome da mooeda para facilitar entendimento do usuario.
        select_currency = select_currency.replace("-", "")
        selected_currency_name = df[select_currency]['name']
        st.sidebar.markdown(
            """<div style="text-align: center;"><h2 style='color: white;'>Moedas Selecionadas</h2></div>""",
            unsafe_allow_html=True
        )
        st.sidebar.markdown(f'<div class="currency-box">{selected_currency_name}</div>', unsafe_allow_html=True)

        #Novos nomes para facilitar entendimento do usuario
        new_names = {
            'ask': 'Venda',
            'bid': 'Compra',
            'code': 'De',
            'codein': 'Para',
            'create_date': 'Data de Criação',
            'high': 'Alta',
            'low': 'Baixa',
            'name': 'Nome',
            'pctChange': 'Variação Percentual',
            'timestamp': 'Timestamp',
            'varBid': 'Variação Bid'
        }
        #Alterando nomes
        df = df[select_currency].rename(new_names)
        st.table(df)