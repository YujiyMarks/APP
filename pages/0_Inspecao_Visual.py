import streamlit as st

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, LongTable, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT

styles = getSampleStyleSheet()

from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]


def capa(canvas, doc): 
    canvas.setAuthor("Bruno")
    canvas.setTitle("Relatorio")

    canvas.drawImage("cs.png", PAGE_WIDTH/2.0-100, PAGE_HEIGHT-110, width=150,height=60) 

    canvas.setFont('Times-Bold',20) 
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-130, "Relatorio de Inspeção Visual") 

    canvas.bookmarkPage("capa") 
    canvas.addOutlineEntry("Capa","capa")

    canvas.line(10,PAGE_HEIGHT-140,PAGE_WIDTH,PAGE_HEIGHT-140) 


def paginas(canvas, doc):
     canvas.drawImage("cs.png", PAGE_WIDTH-100, PAGE_HEIGHT-100, width=100,height=50)

     #canvas.drawString(10,PAGE_HEIGHT-80,f"UFV {localizacao} - {nome_proprietario}")

     canvas.setFont('Times-Roman',9)
     canvas.drawString(inch, 0.75*inch, "Page %d" % (doc.page))  
     canvas.drawString(2.5*inch, 0.70 * inch, "Canal Solar - Consultoria & Serviços | Departamento de Engenharia")
     canvas.drawString(2.5*inch, 0.55 * inch, "R. Paulo César Fidélis, - Lot. Res. Vila Bella, Campinas - SP, 13087-727")
     canvas.drawString(2.5*inch, 0.40 * inch, "engenharia@canalsolar.com.br | canalsolar.com.br")
     canvas.drawString(2.5*inch, 0.25 * inch, "(19)99605-9172 | (19) 99899-7915") 


def gerar_pdf(itens):
    doc = SimpleDocTemplate("relatorio_inspecao.pdf", pagesize=letter,leftMargin=inch,rightMargin=inch,
                    topMargin=inch,bottomMargin=inch,title='Relatorio',author='BrunoY')
    relatorio = []

    titulo_estilo = styles['Heading2']
    subtitulo_estilo = styles['Heading4']
    conteudo_estilo = ParagraphStyle('normal', fontName='Helvetica', fontSize=10, alignment=TA_JUSTIFY)
    capa_estilo = ParagraphStyle('Heading4', fontName='Helvetica', fontSize=10, alignment=TA_CENTER)

    #seção da capa
    
    relatorio.append(Spacer(1,30))
    relatorio.append(Paragraph("UFV: ",capa_estilo))

    # seção de itens
    relatorio.append(PageBreak())

    titulo = Paragraph("ITENS", titulo_estilo)
    relatorio.append(titulo)

    relatorio.append(PageBreak())
    
    doc.build(relatorio, onFirstPage=capa, onLaterPages=paginas)

    #pdf_file = "relatorio.pdf"
    #c = canvas.Canvas(pdf_file, pagesize=letter)
    #c.drawString(100, 750, "Relatório de Dados")

    #y_position = 700
    #for i, item in enumerate(itens, start=1):
    #    c.drawString(100, y_position - (i * 20), f"Item {i}: {item}")

    #c.save()
    #st.success("Relatório PDF gerado com sucesso!")
    #return pdf_file


def main():
    st.set_page_config(page_title="RelatorioCS")
    st.sidebar.header("Inspeção Visual")

    st.title("Relatório de Inspeção Visual")

    st.selectbox("UFV:",["Campo Verde I","Samambaia"])
    st.selectbox("Cliente:",["Alsol","Reenergisa"])
    st.selectbox("Responsável:",["João","Geraldo"])
    st.selectbox("Revisor:",["João","Geraldo"])
    st.date_input("Data de elaboração:")
    st.file_uploader("Insira a imagem geral:")

    st.header("ITENS")
    num_items = st.number_input("Número de itens:", min_value=1, step=1, value=1)

    itens = []
    imagens = []
    analises = []
    obs = []
    for i in range(num_items):
        st.subheader(f"Item {i+1}")
        item = st.selectbox(f"Escolha o item {i+1}:",["Módulos","Inversores"])
        itens.append(item)
        imagem = st.file_uploader(f"Insira a imagem do item {i+1}:",type=['jpg','png'])
        imagens.append(imagem)
        analise = st.radio(f"Análise do item {i+1}:",["C","NC","NA","PA"],horizontal=True)
        analises.append(analise)
        observacao = st.text_input(f"Digite a observação {i+1}:")
        obs.append(observacao)

    if st.button("Gerar Relatório PDF"):
        if itens:
            gerar_pdf(itens)
        else:
            st.warning("Adicione pelo menos um item para gerar o relatório PDF.")

if __name__ == "__main__":
    main()
