
import streamlit as st
import pandas as pd

#python -m streamlit run app.py

#-------------------------------------------- Sidebar

st.sidebar.image("cat logo.png")
st.sidebar.image("cat aviso.png")

#--------------------------------------------- principal

st.image('Retangulo gato.png')

st.title('Cat box')

st.markdown('Cat Box – Porque eles merecem mais que um olhar de indiferença')

st.markdown('Todos os dias, milhares de gatos enfrentam a dor do abandono, da fome e da violência. Olhos que antes brilhavam de curiosidade e carinho, muitas vezes são apagados pela crueldade humana. Cada gato maltratado é uma vida que sofre em silêncio, esperando por compaixão.')

st.markdown('A campanha Cat Box nasceu para dar voz a esses pequenos guerreiros, que tantas vezes são esquecidos ou tratados como descartáveis. Não se trata apenas de proteger gatos: trata-se de resgatar vidas, de mostrar que amor e respeito devem ser estendidos a todos os seres que compartilham o mundo conosco.')

st.markdown('Ao abrir uma Cat Box, você abre também a chance de transformar histórias de dor em histórias de esperança. Você oferece alimento, abrigo, cuidado e, acima de tudo, dignidade.')

st.markdown('Diga não à crueldade. Diga sim à empatia. Porque cada gato merece muito mais do que sobreviver — merece viver com carinho, segurança e amor.')


st.markdown(' ')

st.markdown('Seja bem vindo ao Cat Box! Nós somos uma ong comunitária que tem como objetivo dar um lar dignos a gatos que foram abandonados os sofreram por maus tratos')

st.markdown('Estamos sempre de portas abertas para pessoas de bom coração com intenções de ajudar os pequenos felinos, venha fazer parte dessa grante família ')

st.markdown(' ')

st.markdown(' ')

st.title('Vantagems da adoção')

left, middle, right = st.columns(3, border=True)

left.markdown("Salva uma vida - dá um lar a um animal que poderia continuar nas ruas ou em abrigos")
middle.markdown("Amor e gratidão – animais adotados costumam criar laços fortes e retribuir com muito carinho." )
right.markdown("Custo menor – muitos adotados já vêm vacinados, castrados e vermifugados, reduzindo despesas iniciais.")

st.markdown(' ')

st.markdown("Adotar um gato é muito mais do que oferecer um lar: é transformar vidas. Ao abrir espaço na sua casa e no seu coração, você salva um animal que muitas vezes já sofreu com abandono ou maus-tratos e ganha em troca uma amizade verdadeira, cheia de carinho e gratidão. Além de ajudar a reduzir a superlotação dos abrigos e a combater o abandono, a adoção é também um ato de amor e cidadania, que promove bem-estar tanto para o animal quanto para a família que o recebe.")

st.markdown(' ')

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Gato Laranja")
    st.image("Gato Laranja.png")

with col2:
    st.header("Gato pretinho")
    st.image("Gato Preto.png")

with col3:
    st.header("Gato Siâmes")
    st.image("Gato Siames.png")


col1, col2 = st.columns(2)

with col1:
    st.header("Gato Rajado")
    st.image("Gato Rajado.png")

with col2:
    st.header("Gato sem pelo")
    st.image("Gato Pelado.png")

#--------------------------------------------- avaliação

st.markdown('Gostou do site? Não esqueça de deixar sua avaliação!')


sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")