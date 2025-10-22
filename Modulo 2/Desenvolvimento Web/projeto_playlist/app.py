import streamlit as st

#python -m streamlit run app.py

# Dados de exemplo
generos_musicais = ["Pop", "Mpb", "sertanejo", "Funk"]

# Dicioário relacionando gêneros a cantores

cantor_por_genero = {

   "Pop": ["Jão", "Gloria Groove", "sabrina carpenter"],
   "Mpb": ["anavitória", "Marina Sena", "Rita Lee"],
   "sertanejo": ["gustavo mioto", "Ana Castela", "Gusttavo Lima"],
   "Funk": ["Pedro Sampaio", "Mc livinho", "luisa sonza"],
}


# Selectbox para escolher o genero

st.sidebar.image("logo.png")
st.sidebar.markdown("Selecione um Gênero musical e um cantor")

genero_selecinado = st.sidebar.selectbox("Selecione o gênero:", generos_musicais)

# select para escolher o cantor (apenas do gênero selecionado)

if genero_selecinado:
    cantor_selecionado = st.sidebar.selectbox(
        "Selecione um cantor",
        cantor_por_genero[genero_selecinado]
    )

# Mostrar apenas o cantor selecionado

if genero_selecinado and cantor_selecionado:
    st.write(f"**Cantor selecionado:** {cantor_selecionado}")
    st.write(f"**Gênero musical** {genero_selecinado}")
    st.image(f"{cantor_selecionado}.png", width=700)


# adicionador de video e botão

if genero_selecinado == "Pop" and cantor_selecionado == "Jão":
    st.markdown(" 🎤 Jão " \
    "Cantor e compositor paulista, **Jão** é um dos nomes mais expressivos da música pop atual no Brasil. Suas canções transitam entre o pop romântico, MPB e até referências do rock e da música alternativa, sempre carregadas de emoção e melancolia. Ele é conhecido por transformar experiências pessoais em letras intensas, criando forte identificação com o público jovem.")
    st.video('https://youtu.be/m96wah3ACi8?si=qksFAKfOJMTWsk0R')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/j%C3%A3o")

elif genero_selecinado == "Pop" and cantor_selecionado == "Gloria Groove":
    st.markdown(" 🎭 Gloria Groove  **Gloria Groove** é drag queen, cantora, rapper e dubladora brasileira que se tornou um dos maiores fenômenos da música pop nacional. Sua obra é marcada pela mistura de ritmos como rap, R&B, pop, funk e samba, sempre acompanhada de performances impactantes. Além do talento vocal, é símbolo de representatividade e empoderamento da comunidade LGBTQIA+.")
    st.video('https://youtu.be/mBvcHrwuAjs?si=EiGY9RwwA2Ktnidb')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Gloria%20groove")

elif genero_selecinado == "Pop" and cantor_selecionado == "sabrina carpenter":
    st.markdown("🌟 Sabrina Carpenter  Cantora, compositora e atriz norte-americana, **Sabrina Carpenter** começou sua carreira na Disney e evoluiu para uma das artistas mais versáteis do pop internacional. Suas músicas exploram desde baladas emocionais até faixas dançantes, sempre com uma identidade jovem, divertida e confessional. Ela também se destaca pela presença de palco carismática e proximidade com os fãs.")
    st.video('https://youtu.be/eVli-tstM5E?si=S8nAZAsClKoSVTl_')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Sabrina%20Carpenter")

elif genero_selecinado == "Mpb" and cantor_selecionado == "anavitória":
    st.markdown("🎶 Anavitória  A dupla formada por **Ana Caetano** e **Vitória Falcão** ganhou espaço com sua sonoridade única que mistura folk, MPB e pop acústico. Com vozes suaves e letras poéticas, elas se consolidaram como porta-vozes de uma geração que busca leveza e sensibilidade na música. O duo é marcado por uma estética intimista e por parcerias com grandes nomes da música brasileira.")
    st.video('https://youtu.be/KS_TrJOQB-g?si=OdSAmkUwZk8ZpHKP')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/anavit%C3%B3ria")

elif genero_selecinado == "Mpb" and cantor_selecionado == "Marina Sena":
    st.markdown("💫 Marina Sena  Cantora mineira que explodiu nacionalmente com o hit **“Por Supuesto”**, **Marina Sena** é dona de um estilo autêntico que mistura pop, MPB e elementos eletrônicos. Suas letras exploram liberdade, desejo e intensidade emocional, enquanto sua estética ousada e moderna a colocam como uma das artistas mais inovadoras da nova geração da música brasileira.")
    st.video('https://youtu.be/z2ZmXRkXREw?si=3BnuWhc5zfqxRNtV')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Marina%20Sena")

elif genero_selecinado == "Mpb" and cantor_selecionado == "Rita Lee":
    st.markdown("👑 Rita Lee  Considerada a **“Rainha do Rock Brasileiro”**, **Rita Lee** foi cantora, compositora e multi-instrumentista. Ex-integrante dos Mutantes, revolucionou a música com irreverência, humor e atitude, tornando-se um ícone da cultura pop no Brasil. Sua carreira solo é marcada por sucessos atemporais e por uma postura transgressora que influenciou gerações inteiras.")
    st.video('https://youtu.be/XyveLQfO9XA?si=YS7cSBeE_TeWCRP6')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Rita%20Lee")

elif genero_selecinado == "sertanejo" and cantor_selecionado == "gustavo mioto":
    st.markdown("🎵 Gustavo Mioto  Um dos principais nomes da nova geração do sertanejo, **Gustavo Mioto** conquistou espaço com canções românticas que mesclam modernidade e tradição. Suas letras falam de amor, encontros e desencontros, sempre com melodias envolventes. Além disso, suas parcerias com artistas de diferentes estilos ajudaram a ampliar seu alcance nacional.")
    st.video('https://youtu.be/U-XSEj31lgI?si=9vdKq05igy7FCk46')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/gustavo%20mioto")

elif genero_selecinado == "sertanejo" and cantor_selecionado == "Ana Castela":
    st.markdown("🐎 Ana Castela  Conhecida como a **“boiadeira”**, **Ana Castela** é uma jovem cantora sertaneja que representa o movimento do agronejo. Com uma imagem ligada ao campo e ao estilo de vida rural, suas músicas falam de amor, liberdade e da força do interior. Mesmo com pouco tempo de carreira, já se tornou uma das vozes mais populares do sertanejo atual.")
    st.video('https://youtu.be/fGOXDdvfEeM?si=5_SxZZhFWJnP0bpD')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Ana%20Castela")

elif genero_selecinado == "sertanejo" and cantor_selecionado == "Gusttavo Lima":
    st.markdown("Gusttavo Lima  Apelidado de **“Embaixador”**, **Gusttavo Lima** é um dos artistas sertanejos mais bem-sucedidos do Brasil. Reconhecido por sua potência vocal e por shows grandiosos, ele mistura canções românticas com batidas animadas, conquistando públicos diversos. Sua carreira é marcada por grandes turnês e por ser referência no mercado do sertanejo universitário.")
    st.video('https://youtu.be/54d04ReqKDM?si=XE8AY9ANWq8Szxtn')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Gusttavo%20Lima")

elif genero_selecinado == "Funk" and cantor_selecionado == "Pedro Sampaio":
    st.markdown("🎧 Pedro Sampaio  **Pedro Sampaio** é DJ, produtor e cantor, sendo um dos principais nomes do funk pop brasileiro. Conhecido por suas produções inovadoras e mashups criativos, ele transforma suas apresentações em verdadeiros espetáculos de energia. Sua identidade artística mistura humor, irreverência e hits que rapidamente se tornam virais.")
    st.video('https://youtu.be/_zKnEm9xPWw?si=XqUySQ_R5UuCVmwB')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Pedro%20sampaio")

elif genero_selecinado == "Funk" and cantor_selecionado == "Mc livinho":
    st.markdown("🎵 MC Livinho  Cantor e compositor de funk paulista, **MC Livinho** é conhecido por unir sensualidade, romantismo e versatilidade musical. Sua voz marcante permite transitar entre o funk, o R&B e até o pagode, o que o diferencia no cenário musical. Com letras intensas e presença de palco cativante, é um dos nomes mais populares do gênero.")
    st.video('https://youtu.be/iE3N0H98wCw?si=Kk2yFRSK3LLBlXTK')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Mc%20livinho")

elif genero_selecinado == "Funk" and cantor_selecionado == "luisa sonza":
    st.markdown("🌟 Luísa Sonza  Uma das maiores estrelas do pop brasileiro, **Luísa Sonza** é cantora e compositora que se destaca pela ousadia e pela constante reinvenção. Sua música mistura pop, funk, R&B e até influências internacionais, sempre acompanhada de letras pessoais e visuais arrojados. É reconhecida por sua postura autêntica e pela capacidade de se reinventar a cada projeto.")
    st.video('https://youtu.be/1zEnA9qpyF0?si=r0pC_hvCEacrLauJ')
    st.link_button(label="Spotify", url="https://open.spotify.com/search/Luisa%20sonza")





