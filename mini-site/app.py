import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    layout="wide",
    page_title="Samuel Silva | Portfólio de Dados",
    page_icon="📊"
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

/* Ícones de stack */
.stack-icon {
    text-align: center;
    padding: 0.5rem;
}

.stack-icon img {
    width: clamp(30px, 6vw, 40px);
    height: auto;
}

.stack-icon p {
    margin-top: 0.5rem;
    font-size: clamp(0.7rem, 2vw, 0.9rem);
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
    div[data-testid="column"] {
        text-align: center;
    }
    
    /* Ajusta texto da coluna 2 */
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


# ============================================
# FUNÇÕES AUXILIARES
# ============================================
def get_image_path(path):
    """Retorna o caminho correto da imagem"""
    script_dir = Path(__file__).parent
    
    possible_paths = [
        script_dir / path,
        script_dir / "mini-site" / path,
        Path(f"/mount/src/meu-portif-lio/mini-site/{path}"),
        Path(path),
    ]
    
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
    return None


def safe_image(image_path, width=None):
    """Função segura para exibir imagens"""
    img_path = get_image_path(image_path)
    if img_path and img_path.exists():
        st.image(str(img_path), width=width)
    else:
        st.warning(f"⚠️ Imagem não encontrada: {image_path}")


def img_card(path):
    """Exibe imagem em card de projeto"""
    img = img_to_base64(path)
    if img:
        st.markdown(f"""
            <img src="data:image/png;base64,{img}" class="project-img">
        """, unsafe_allow_html=True)


# ============================================
# HEADER COM FOTO DE PERFIL
# ============================================
img = img_to_base64("imgs/perfilprof.jpg")

if img:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(f"""
            <img src="data:image/jpeg;base64,{img}" class="profile-img">
        """, unsafe_allow_html=True)

    with col2:
        st.title("Samuel de Andrade da Silva")
        st.write("📊 Analista de Dados Jr")
        
        st.markdown("""
        **Analiso, construo, comunico. Próximo passo: o mercado.**
        
        Projetos práticos com **Python, Pandas, Streamlit e SQL** — todos em código aberto.  
        Crio dashboards interativos também no **Power BI**, transformando dados em insights claros para decisões estratégicas.
        
        Mais que ferramentas, desenvolvi uma abordagem: entender o problema antes de resolver.
        
        Aberto a **CLT, freelance ou colaborações pontuais**. O que me move é resolver problemas reais com dados.
        """)
        
        st.markdown("📍 **Vamos conversar?**")


# ============================================
# STACK TECNOLÓGICA
# ============================================
st.markdown("---")
st.markdown("## 🛠️ Stack Tecnológica")

# Primeira linha de stacks
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

# Segunda linha de stacks
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
    safe_image("imgs/icons8-github-48.png", width=40)
    st.caption("Git/GitHub")


# ============================================
# PROJETOS
# ============================================
st.markdown("---")
st.markdown("## 📁 Projetos")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    img_card("imgs/project02.png")
    st.subheader("Análise da Arrecadação de IPVA no Estado do Rio de Janeiro (2017)")
    st.write("""
    Análise exploratória da arrecadação de IPVA no estado do Rio de Janeiro em 2017, 
    utilizando dados públicos. O objetivo foi compreender como a arrecadação se distribui 
    ao longo do ano e entre diferentes municípios.
    """)
    st.link_button(
        "🔗 Ver Projeto",
        "https://github.com/SamuelSilvA32/An-lise-da-Arrecada-o-de-IPVA-no-Estado-do-Rio-de-Janeiro-2017-.git"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    img_card("imgs/project01.png")
    st.subheader("Análise Exploratória e Visualização de Dados com Streamlit")
    st.write("""
    Análise exploratória de dados aplicada a um conjunto fictício de informações 
    sobre saúde mental. O projeto inclui dashboards interativos desenvolvidos 
    em Streamlit para compreensão de padrões demográficos e clínicos.
    """)
    st.link_button(
        "🔗 Ver Projeto",
        "https://zwrvbm342tawpbqrbomzzb.streamlit.app/"
    )
    st.markdown('</div>', unsafe_allow_html=True)


# ============================================
# CONTATO E REDES SOCIAIS
# ============================================
st.markdown("---")
st.markdown("## 📬 Contato")

# Carrega ícones
github = img_to_base64("imgs/icons8-github-24.png")
linkedin = img_to_base64("imgs/icons8-linkedin-24.png")
email = img_to_base64("imgs/icons8-gmail-novo-50.png")
whatsapp = img_to_base64("imgs/icons8-whatsapp-32.png")

st.markdown(f"""
<div class="social-links">
    <a href="https://github.com/SamuelSilvA32" target="_blank">
        <img src="data:image/png;base64,{github}" alt="GitHub">
    </a>
    <a href="https://linkedin.com/in/samuel-d-a03266399" target="_blank">
        <img src="data:image/png;base64,{linkedin}" alt="LinkedIn">
    </a>
    <a href="mailto:samuelsilva00935@gmail.com">
        <img src="data:image/png;base64,{email}" alt="Email">
    </a>
    <a href="https://wa.me/5524998163999?text=Olá!%20Vi%20seu%20portfólio%20e%20gostaria%20de%20conversar" target="_blank">
        <img src="data:image/png;base64,{whatsapp}" alt="WhatsApp">
    </a>
</div>
""", unsafe_allow_html=True)


# ============================================
# RODAPÉ
# ============================================
st.markdown("""
<div class="footer">
    <strong>Samuel de Andrade da Silva</strong><br>
    Versão 2.0 • Portfólio Responsivo<br>
    Dados e análises para decisões estratégicas<br>
    <br>
    © 2026 • Desenvolvido com Streamlit
</div>
""", unsafe_allow_html=True)
