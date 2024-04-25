import streamlit as st

st.sidebar.title("Menu")

st.title("Relatório de inspeção visual CS")
st.selectbox("Box",["Opção1","Opção2"])
st.file_uploader("Insira uma imagem")
st.radio("Análise")
st.date_input("Data de Elaboração")
