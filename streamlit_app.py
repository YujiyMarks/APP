import streamlit as st

st.sidebar.title("Menu")

st.title("Relatório de inspeção visual CS")
st.selectbox("UFV:",["Campo Verde I","Samambaia"])
st.selectbox("Cliente:",["Alsol","Reenergisa"])
st.selectbox("Responsável:",["João","Geraldo"])
st.selectbox("Revisor:",["João","Geraldo"])
st.date_input("Data de elaboração:")
st.file_uploader("Insira uma imagem:")


st.write("ITENS")
st.selectbox("",["Módulos","Inversores"])
st.file_uploader("Insira:")
#st.radio("Análise")
st.text_input("Observação")

