import streamlit as st
#import reportlab

#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A4

st.set_page_config(page_title="RelatorioCS")
st.sidebar.header("Inspeção Visual")

class pagina():
  def __init__(self):
    st.title("Relatório de Inspeção Visual CS")
    st.selectbox("UFV:",["Campo Verde I","Samambaia"])
    st.selectbox("Cliente:",["Alsol","Reenergisa"])
    st.selectbox("Responsável:",["João","Geraldo"])
    st.selectbox("Revisor:",["João","Geraldo"])
    st.date_input("Data de elaboração:")
    st.file_uploader("Insira uma imagem:")
    
    

  def mostrar_item():
      st.selectbox("Escolha o item 1:",["Módulos","Inversores"])
      st.file_uploader("Insira a imagem do item 1:",type=['jpg','png'])
      st.radio("Análise:",["C","NC","NA","PA"],horizontal=True)
      st.text_input("Observação:")
    
      #botao = st.button("Insira um item")
      #if botao:
        #pagina.mostrar_item()

  #def inserir_item():
    #st.session_state['itens'] += 1



pagina()

st.write("ITENS")
botao = st.button("Insira um item")
botao.on_click(mostrar_item)
#if botao:
# pagina.mostrar_item()
#botao = False
#inserir_item(self, botao)

#for i in range(st.session_state['itens']):
    #mostrar_item()

#progress_bar = st.sidebar.progress(0)
#status_text = st.sidebar.empty()

#progress_bar.empty()
