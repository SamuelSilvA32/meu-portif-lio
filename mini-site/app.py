import streamlit as st
import base64
from pathlib import Path

# ---------------- CONFIG ---------------- #

BASE_DIR = Path(__file__).parent
IMG_DIR = BASE_DIR / "imgs"

st.set_page_config(
    layout="wide",
    page_title="Curriculo digital",
    page_icon=str(IMG_DIR / "icons8-manager-48.png")
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.block-container {
    padding-top: 2.9rem;
    padding-bottom: 1rem;
}

h1, h2, h3 {
    font-weight: 600;
}

div[data-testid="stHorizontalBlock"] > div {
    transition: 0.2s;
    border-radius: 12px;
    padding: 12px;
}

div[data-testid="stHorizontalBlock"] > div:hover {
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    transform: translateY(-3px);
}

/* titulo clicável estilo botão */
.project-title a {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 8px;
    background-color: #000000;
    color: #ffffff !important;
    text-decoration: none;
    font-weight: 600;
    margin-top: 8px;
    margin-bottom: 8px;
}

.project-title a:hover {
    background-color: #1a1a1a;
    color: #ffffff !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HELPERS ---------------- #

def img_path(name):
    return IMG_DIR / name


@st.cache_data
def img_to_base64(name):
    path = img_path(name)
    if path.exists():
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None


def safe_image(name, width=None):
    path = img_path(name)
    if path.exists():
        st.image(str(path), width=width)
    else:
        st.empty()


def img_card(name):
    img = img_to_base64(name)
    if img:
        st.markdown(f"""
            <img src="data:image/png;base64,{img}"
            style="
            width:100%;
            height:220px;
            object-fit:cover;
            border-radius:10px;
            ">
        """, unsafe_allow_html=True)


# ---------------- HEADER ---------------- #

img = img_to_base64("perfilprof.jpg")

col1, col2 = st.columns([1,3])

with col1:
    if img:
        st.markdown(f"""
            <img src="data:image/jpeg;base64,{img}"
            style="
            width:143px;
            height:143px;
            border-radius:50%;
            object-fit:cover;
            ">
        """, unsafe_allow_html=True)

with col2:
    st.title("Samuel de Andrade da Silva")
    st.write("Analista de Dados Jr")

    st.subheader("Sobre mim")

    st.write("""
📊 Analiso, construo, comunico. Meu objetivo agora é transpor esses 
projetos para o mercado.

Desenvolvo análises e dashboards com Python, Pandas, Streamlit e SQL — 
tudo disponível em código aberto no GitHub. Cada projeto foi uma oportunidade 
de refinar não apenas a técnica, mas também a capacidade de transformar dados 
em narrativas claras e acionáveis.

Tenho clareza do que posso entregar hoje e, sobretudo, consciência de que 
o ambiente real exige adaptação, resiliência e aprendizado contínuo. 
É justamente isso que busco.

Estou aberto a relações profissionais nas mais diversas modalidades — 
seja CLT, colaboração freelance ou projetos pontuais. O que me move é 
a oportunidade de estar onde os problemas de fato acontecem e contribuir 
com soluções sustentadas em dados.

📍 Se você procura alguém disposto a aprender fazendo, com base sólida 
e compromisso com resultado: estou à disposição para conversarmos.
""")

# ---------------- STACK ---------------- #
# ---------------- STACK ---------------- #



st.markdown("""
<div style="
text-align:center;
font-size:15px;
opacity:0.85;
margin-top:10px;
margin-bottom:25px;
">

Python • Pandas • NumPy • SQL • Excel • Power BI • Streamlit

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- PROJETOS ---------------- #

st.markdown("## Projetos")

projects = [
    {
        "title": "Análise da Arrecadação de IPVA no Estado do Rio de Janeiro (2017)",
        "image": "project02.png",
        "desc": """Este projeto apresenta uma análise exploratória da arrecadação de IPVA 
        no estado do Rio de Janeiro no ano de 2017, utilizando dados públicos 
        disponibilizados pelo portal de dados abertos do governo brasileiro.""",
        "link": "https://github.com/SamuelSilvA32/An-lise-da-Arrecada-o-de-IPVA-no-Estado-do-Rio-de-Janeiro-2017-.git"
    },
    {
        "title": "Análise Exploratória e Visualização de Dados com Streamlit",
        "image": "project01.png",
        "desc": """Análise exploratória aplicada a dados fictícios de saúde mental, 
        estruturada em uma aplicação interativa com Streamlit.""",
        "link": "https://zwrvbm342tawpbqrbomzzb.streamlit.app/"
    },

    {
    "title": "Agente IA",
    "image": "project03.png",
    "desc": """
    Um protótipo de assistente de análise de requisitos para transformar ideias de projeto em documentação prática,
    organizado como uma aplicação web via Streamlit e alimentado por LLM (Groq / llama-3).
    O foco é gerar rapidamente o escopo MVP e sugerir arquitetura, dependências e fases de desenvolvimento.
    """,
    "link": "https://github.com/SamuelSilvA32/Agente_de_IA_v1.0.git"
    }

]

cols = st.columns(2)

for i, p in enumerate(projects):
    with cols[i % 2]:
        img_card(p["image"])

        st.markdown(
            f'''<div class="project-title">
<a href="{p["link"]}" target="_blank">{p["title"]}</a>
</div>''',
            unsafe_allow_html=True
        )

        st.write(p["desc"])

st.markdown("---")

# ---------------- CONTATO ---------------- #

github = img_to_base64("icons8-github-24.png")
linkedin = img_to_base64("icons8-linkedin-24.png")
email = img_to_base64("icons8-gmail-novo-50.png")
whatsapp = img_to_base64("icons8-whatsapp-32.png")

st.markdown(f"""
<div style="text-align:center">

<a href="https://github.com/SamuelSilvA32" style="margin: 0 10px;">
<img src="data:image/png;base64,{github}" width="28">
</a>

<a href="https://linkedin.com/in/samuel-d-a03266399" style="margin: 0 10px;">
<img src="data:image/png;base64,{linkedin}" width="28">
</a>

<a href="mailto:samuelsilva00935@gmail.com" style="margin: 0 10px;">
<img src="data:image/png;base64,{email}" width="28">
</a>

<a href="https://wa.me/+5524998163999" style="margin: 0 10px;">
<img src="data:image/png;base64,{whatsapp}" width="28">
</a>

</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ---------------- #

st.markdown("""
<div style="
text-align:center;
opacity:0.6;
font-size:12px;
margin-top:20px;
">

<br><br>

© 2026 Samuel de Andrade da Silva • Currículo Digital  
Desenvolvido com Streamlit • Icons by Icons8

</div>
""", unsafe_allow_html=True)
