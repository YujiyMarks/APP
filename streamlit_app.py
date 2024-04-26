import streamlit as st

st.sidebar.title("Menu")

st.title("Relatório de inspeção visual CS")
st.selectbox("UFV:",["Campo Verde I","Samambaia"])
st.selectbox("Cliente:",["Alsol","Reenergisa"])
st.selectbox("Responsável:",["João","Geraldo"])
st.selectbox("Revisor:",["João","Geraldo"])
st.date_input("Data de elaboração:")
st.file_uploader("Insira uma imagem:")

#st.radio("Análise")

st.write("ITENS")
st.selectbox("",["Módulos","Inversores"])

