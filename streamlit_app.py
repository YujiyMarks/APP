import streamlit as st

def inserir_item():
  st.selectbox("Escolha o item 1:",["Módulos","Inversores"])
  st.file_uploader("Insira a imagem do item 1:")
  st.radio("Análise:",["C","NC","NA","PA"],horizontal=True)
  st.text_input("Observação:")

st.sidebar.title("Menu")

st.title("Relatório de Inspeção Visual CS")
st.selectbox("UFV:",["Campo Verde I","Samambaia"])
st.selectbox("Cliente:",["Alsol","Reenergisa"])
st.selectbox("Responsável:",["João","Geraldo"])
st.selectbox("Revisor:",["João","Geraldo"])
st.date_input("Data de elaboração:")
st.file_uploader("Insira uma imagem:")

st.button("Insira um item",on_click=inserir_item())
st.write("ITENS")


