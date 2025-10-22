import streamlit as st

#-------------------------------------------- Sidebar

st.sidebar.image("cat logo.png")
st.sidebar.image("cat aviso.png")

#--------------------------------------------- principal

st.title('informações pre-adoção')

import streamlit as st

st.markdown("""


📍 **Endereço:** Rua das Flores, nº 123 – Bairro Esperança – São Paulo/SP  
📞 **Telefone:** (11) 3456-7890  
🕙 **Visitação:** Segunda a sábado – das 10h às 18h  

---

## 📋 Requisitos para Adoção  
Para garantir a segurança e o bem-estar dos nossos gatinhos, pedimos:  
- Ser maior de **21 anos**.  
- Apresentar **RG e CPF**.  
- Comprovante de **residência atualizado**.  
- Preencher o **Termo de Responsabilidade de Adoção**.  
- Passar por uma breve **entrevista** com nossa equipe.  

---

## 📑 Documentos Necessários  
✔️ Documento de identidade com foto (RG ou CNH)  
✔️ CPF  
✔️ Comprovante de residência (conta de luz, água ou internet)  

---

## ❤️ Vantagems Cat box  
- Gatos vacinados, vermifugados e, quando possível, castrados.  
- Orientação e acompanhamento pós-adoção.  
- Apoio para adaptação no novo lar.  

---
            
## 😁 Agende uma visita aqui 

""")

import datetime
dias = st.date_input("Informe um dia para realizar a visita", value=datetime.date.today(),format="DD/MM/YYYY")
data_formada = dias.strftime("%d/%m/%y")

st.image("Gato assustado.png")