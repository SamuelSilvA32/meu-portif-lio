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

/* largura geral */
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

/* HERO */
.hero {
    padding: 20px 0 10px 0;
}

/* STACK GRID */
.stack-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 20px;
    text-align: center;
    margin-top: 20px;
}

.stack-item img {
    width:40px;
    margin-bottom:5px;
}

/* PROJECT GRID */
.projects-grid {
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap:25px;
    margin-top:20px;
}

/* CARD */
.card {
    border-radius:14px;
    overflow:hidden;
    box-shadow:0 2px 10px rgba(0,0,0,0.05);
    transition:0.2s;
    background:white;
}

.card:hover {
    transform:translateY(-4px);
    box-shadow:0 6px 25px rgba(0,0,0,0.08);
}

.card img {
    width:100%;
    height:200px;
    object-fit:cover;
}

.card-body {
    padding:18px;
}

/* TITULO BOTAO */
.card-title {
    display:block;
    background:black;
    color:white !important;
    text-align:center;
    padding:10px;
    border-radius:8px;
    font-weight:600;
    text-decoration:none;
    margin-bottom:10px;
}

/* MOBILE */
@media (max-width:600px){
    .card img{
        height:170px;
    }
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
stack_html = '<div class="stack-grid">'

for img, label in stack:
    base = img_to_base64(img)
    if base:
        stack_html += f"""
        <div class="stack-item">
            <img src="data:image/png;base64,{base}">
            <div>{label}</div>
        </div>
        """

stack_html += "</div>"

st.markdown(stack_html, unsafe_allow_html=True)

# ---------------- PROJETOS ---------------- #
st.markdown("## Projetos")

html = '<div class="projects-grid">'

for p in projects:
    img = img_to_base64(p["image"])

    html += f"""
    <div class="card">

        <img src="data:image/png;base64,{img}">

        <div class="card-body">

        <a href="{p["link"]}" class="card-title" target="_blank">
        {p["title"]}
        </a>

        <div style="font-size:14px; opacity:0.8">
        {p["desc"]}
        </div>

        </div>
    </div>
    """

html += "</div>"

st.markdown(html, unsafe_allow_html=True)

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
