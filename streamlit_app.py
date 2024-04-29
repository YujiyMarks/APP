import streamlit as st

class Pagina():
  def __init__(self):
    st.sidebar.title("Menu")
    
    st.title("Relatório de Inspeção Visual CS")
    st.selectbox("UFV:",["Campo Verde I","Samambaia"])
    st.selectbox("Cliente:",["Alsol","Reenergisa"])
    st.selectbox("Responsável:",["João","Geraldo"])
    st.selectbox("Revisor:",["João","Geraldo"])
    st.date_input("Data de elaboração:")
    st.file_uploader("Insira uma imagem:")
    
    

  def mostrar_item():
      st.selectbox("Escolha o item 1:",["Módulos","Inversores"])
      st.file_uploader("Insira a imagem do item 1:")
      st.radio("Análise:",["C","NC","NA","PA"],horizontal=True)
      st.text_input("Observação:")

  def inserir_item():
    st.session_state['itens'] += 1



Pagina()

st.write("ITENS")
botao = st.button("Insira um item",on_click=Pagina.inserir_item)
#inserir_item(self, botao)

for i in range(st.session_state['itens']):
    mostrar_item()

