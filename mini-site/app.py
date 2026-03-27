import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    layout="wide",
    page_title="Curriculo digital",
    page_icon="mini-site/imgs/icons8-manager-48.png"
)

# ============================================
# CSS RESPONSIVO COMPLETO
# ============================================
st.markdown("""
<style>
/* Reset e configurações gerais */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    max-width: 1200px;
    margin: 0 auto;
}

/* Títulos */
h1, h2, h3, h4 {
    font-weight: 600;
    word-break: break-word;
}

h1 {
    font-size: clamp(1.5rem, 5vw, 2.2rem);
}

h2 {
    font-size: clamp(1.3rem, 4vw, 1.8rem);
}

h3 {
    font-size: clamp(1.1rem, 3vw, 1.5rem);
}

/* Texto */
p, li, .stMarkdown {
    font-size: clamp(0.9rem, 2vw, 1rem);
    line-height: 1.5;
    word-break: break-word;
}

/* Imagem de perfil responsiva */
.profile-img {
    width: min(140px, 25vw);
    height: min(140px, 25vw);
    border-radius: 50%;
    object-fit: cover;
    display: block;
    margin: 0 auto;
}

/* ========== CORREÇÃO DAS STACKS ========== */
/* Container das stacks */
.stacks-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    gap: 1rem;
    margin: 1rem 0;
}

.stack-item {
    text-align: center;
    flex: 1 1 auto;
    min-width: 70px;
    padding: 0.5rem;
}

.stack-item img {
    width: clamp(35px, 6vw, 45px);
    height: auto;
    display: block;
    margin: 0 auto;
}

.stack-item p {
    margin-top: 0.5rem;
    font-size: clamp(0.7rem, 2vw, 0.9rem);
    margin-bottom: 0;
}

/* Para mobile - mantém na horizontal */
@media (max-width: 768px) {
    .stacks-container {
        gap: 0.5rem;
    }
    
    .stack-item {
        min-width: 60px;
    }
    
    .stack-item img {
        width: clamp(30px, 8vw, 40px);
    }
}

/* Cards de projetos */
.project-card {
    transition: 0.2s;
    border-radius: 12px;
    padding: 1rem;
    background: transparent;
}

.project-card:hover {
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    transform: translateY(-3px);
}

/* Imagens dos cards */
.project-img {
    width: 100%;
    height: auto;
    max-height: 220px;
    object-fit: cover;
    border-radius: 10px;
}

/* Botões */
.stButton button, .stLinkButton a {
    width: 100%;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-size: clamp(0.8rem, 2vw, 0.9rem);
}

/* ========== RESPONSIVIDADE MOBILE ========== */
@media (max-width: 768px) {
    /* Ajuste geral */
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    
    /* Colunas viram blocos verticais */
    div[data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
        margin-bottom: 1.5rem;
    }
    
    /* Container de linhas */
    div[data-testid="stHorizontalBlock"] {
        flex-wrap: wrap !important;
    }
    
    /* Espaçamento entre seções */
    hr {
        margin: 1.5rem 0;
    }
    
    /* Centraliza textos em colunas */
    div[data-testid="column"]:first-child {
        text-align: center;
    }
    
    div[data-testid="column"]:nth-child(2) {
        text-align: left;
    }
    
    /* Cards de projetos no mobile */
    .project-card {
        margin-bottom: 1.5rem;
    }
}

/* ========== TABLET (entre 769px e 1024px) ========== */
@media (min-width: 769px) and (max-width: 1024px) {
    div[data-testid="column"] {
        width: 50% !important;
        flex: 1 1 45% !important;
    }
    
    .block-container {
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }
}

/* ========== DESKTOP (acima de 1024px) ========== */
@media (min-width: 1025px) {
    .block-container {
        padding-left: 2rem;
        padding-right: 2rem;
    }
}

/* Links e ícones sociais */
.social-links {
    text-align: center;
    margin: 1rem 0;
}

.social-links a {
    display: inline-block;
    margin: 0 0.75rem;
    transition: transform 0.2s;
}

.social-links a:hover {
    transform: translateY(-2px);
}

.social-links img {
    width: clamp(24px, 5vw, 28px);
    height: auto;
}

/* Rodapé */
.footer {
    text-align: center;
    opacity: 0.6;
    font-size: clamp(0.7rem, 2vw, 0.8rem);
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(128, 128, 128, 0.2);
}
</style>
""", unsafe_allow_html=True)


def get_image_path(path):
    """Retorna o caminho correto da imagem"""
    script_dir = Path(__file__).parent
    
    # Possíveis caminhos para procurar a imagem
    possible_paths = [
        script_dir / path,  # Relativo ao script
        script_dir / "mini-site" / path,  # Caso esteja na pasta mini-site
        Path(f"/mount/src/meu-portif-lio/mini-site/{path}"),  # Caminho absoluto do deploy
        Path(path),  # Caminho direto
    ]
    
    # Retorna o primeiro caminho que existe
    for try_path in possible_paths:
        if try_path.exists():
            return try_path
    
    return None


@st.cache_data
def img_to_base64(path):
    """Converte imagem para base64"""
    img_path = get_image_path(path)
    
    if img_path and img_path.exists():
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    
    # Se não encontrar, mostra erro
    st.error(f"❌ Imagem não encontrada: {path}")
    return None


def safe_image(image_path, width=None):
    """Função segura para exibir imagens"""
    img_path = get_image_path(image_path)
    if img_path and img_path.exists():
        st.image(str(img_path), width=width)
    else:
        st.warning(f"⚠️ Imagem não carregada: {image_path}")


# ---------- FUNÇÃO CARD IMG ----------
def img_card(path):
    img = img_to_base64(path)
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


# FOTO PERFIL
img = img_to_base64("imgs/perfilprof.jpg")

if img:
    col1, col2 = st.columns([1,3])

    with col1:
        st.markdown(f"""
            <img src="data:image/jpeg;base64,{img}"
            style="
            width:140px;
            height:140px;
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


    # STACK - Usando safe_image para todas as imagens
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        safe_image("imgs/python_18894.png", width=40)
        st.caption("Python")

    with c2:
        safe_image("imgs/icons8-pandas-48.png", width=40)
        st.caption("Pandas")

    with c3:
        safe_image("imgs/icons8-sql-48.png", width=40)
        st.caption("SQL")

    with c4:
        safe_image("imgs/icons8-microsoft-excel-2019-48.png", width=40)
        st.caption("Excel")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        safe_image("imgs/icons8-iluminado-48.png", width=40)
        st.caption("Streamlit")

    with c2:
        safe_image("imgs/icons8-poder-bi-2021-48.png", width=40)
        st.caption("Power BI")

    with c3:
        safe_image("imgs/icons8-entorpecido-48.png", width=40)
        st.caption("NumPy")

    with c4:
        pass


    st.markdown("---")

    # PROJETOS
    st.markdown("## Projetos")

    col1, col2 = st.columns(2)

    with col1:
        img_card("imgs/project02.png")
        st.subheader("Análise da Arrecadação de IPVA no Estado do Rio de Janeiro (2017)")
        st.write("""
Este projeto apresenta uma análise exploratória da arrecadação de IPVA no estado do Rio de Janeiro no ano de 2017, utilizando dados públicos disponibilizados pelo portal de dados abertos do governo brasileiro.
O objetivo da análise é compreender como a arrecadação do imposto se distribui ao longo do ano e entre diferentes municípios e regiões do estado.
""")
        st.link_button(
            "Ver Projeto",
            "https://github.com/SamuelSilvA32/An-lise-da-Arrecada-o-de-IPVA-no-Estado-do-Rio-de-Janeiro-2017-.git"
        )

    with col2:
        img_card("imgs/project01.png")
        st.subheader("Análise Exploratória e Visualização de Dados com Streamlit")
        st.write("""
Este projeto consiste em uma análise exploratória de dados aplicada a um conjunto fictício de informações sobre saúde mental. O objetivo foi compreender padrões demográficos e clínicos da amostra, estruturando a análise de forma organizada e profissional por meio de uma aplicação interativa desenvolvida em Streamlit.
""")
        st.link_button(
            "Ver Projeto",
            "https://zwrvbm342tawpbqrbomzzb.streamlit.app/"
        )

    st.markdown("---")

    # ICONES CONTATO
    github = img_to_base64("imgs/icons8-github-24.png")
    linkedin = img_to_base64("imgs/icons8-linkedin-24.png")
    email = img_to_base64("imgs/icons8-gmail-novo-50.png")
    whatsapp = img_to_base64("imgs/icons8-whatsapp-32.png")

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

    st.markdown("<br>", unsafe_allow_html=True)

    # COPYRIGHT
    st.markdown("""
    <div style="
    text-align:center;
    opacity:0.6;
    font-size:12px;
    margin-top:20px;
    ">
    <br>
    <br>
    © 2026 Samuel de Andrade da Silva • Currículo Digital  
    Desenvolvido com Streamlit • Icons by Icons8

    </div>
    """, unsafe_allow_html=True)
else:
    st.error("""
    ❌ **Erro: Imagem de perfil não encontrada!**
    
    Por favor, verifique se:
    1. A pasta `imgs/` existe no repositório
    2. O arquivo `perfilprof.jpg` está dentro da pasta `imgs/`
    3. Todos os arquivos foram commitados e pushados para o GitHub
    
    **Lista de imagens necessárias:**
    - imgs/perfilprof.jpg
    - imgs/python_18894.png
    - imgs/icons8-pandas-48.png
    - imgs/icons8-sql-48.png
    - imgs/icons8-microsoft-excel-2019-48.png
    - imgs/icons8-iluminado-48.png
    - imgs/icons8-poder-bi-2021-48.png
    - imgs/icons8-entorpecido-48.png
    - imgs/project01.png
    - imgs/project02.png
    - imgs/icons8-github-24.png
    - imgs/icons8-linkedin-24.png
    - imgs/icons8-gmail-novo-50.png
    - imgs/icons8-whatsapp-32.png
    """)
