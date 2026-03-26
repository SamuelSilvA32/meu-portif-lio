import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    layout="wide",
    page_title="Curriculo digital",
    page_icon="imgs/icons8-manager-48.png"
)

st.markdown("""
<style>

/* reduz espaço topo */
.block-container {
    padding-top: 2.9rem;
    padding-bottom: 1rem;
}

/* títulos */
h1, h2, h3 {
    font-weight: 600;
}

/* cards apenas dentro da seção projetos */
div[data-testid="stHorizontalBlock"] > div:nth-child(1),
div[data-testid="stHorizontalBlock"] > div:nth-child(2) {
    transition: 0.2s;
    border-radius: 12px;
}

/* hover */
div[data-testid="stHorizontalBlock"] > div:nth-child(1):hover,
div[data-testid="stHorizontalBlock"] > div:nth-child(2):hover {
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    transform: translateY(-3px);
}

/* botão */
.stLinkButton a {
    border-radius: 8px;
    padding: 8px 16px;
}

</style>
""", unsafe_allow_html=True)


@st.cache_data
def img_to_base64(path):
    """Converte imagem para base64 com busca automática em múltiplos caminhos"""
    
    # Diretório base do script
    script_dir = Path(__file__).parent
    
    # Possíveis caminhos para procurar a imagem
    possible_paths = [
        script_dir / path,  # Relativo ao script
        script_dir / "mini-site" / path,  # Caso esteja na pasta mini-site
        Path(f"/mount/src/meu-portif-lio/mini-site/{path}"),  # Caminho absoluto do deploy
        Path(path),  # Caminho direto
    ]
    
    # Tenta cada caminho
    for try_path in possible_paths:
        if try_path.exists():
            with open(try_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    
    # Se não encontrar, mostra erro detalhado
    st.error(f"""
    ❌ **Imagem não encontrada!**
    
    **Arquivo procurado:** {path}
    
    **Caminhos testados:**
    {chr(10).join(f'• {p}' for p in possible_paths)}
    
    **Verifique se a imagem existe na pasta `imgs/` e foi commitada no repositório.**
    """)
    return None


# ---------- FUNÇÃO CARD IMG (NOVA) ----------
def img_card(path):
    img = img_to_base64(path)
    if img:  # Só mostra se a imagem foi encontrada
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

if img:  # Só continua se a imagem foi encontrada
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
    Estudante de Análise e Desenvolvimento de Sistemas com foco em análise de dados.
    Experiência prática com Python, Pandas, Streamlit e tratamento de dados públicos.
    Desenvolvo dashboards, automatizações e análises para geração de insights.
    Busco oportunidade como Analista de Dados Júnior ou área administrativa com dados.
    """)


    # STACK
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.image("imgs/python_18894.png", width=40)
        st.caption("Python")

    with c2:
        st.image("imgs/icons8-pandas-48.png", width=40)
        st.caption("Pandas")

    with c3:
        st.image("imgs/icons8-sql-48.png", width=40)
        st.caption("SQL")

    with c4:
        st.image("imgs/icons8-microsoft-excel-2019-48.png", width=40)
        st.caption("Excel")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.image("imgs/icons8-iluminado-48.png", width=40)
        st.caption("Streamlit")

    with c2:
        st.image("imgs/icons8-poder-bi-2021-48.png", width=40)
        st.caption("Power BI")

    with c3:
        st.image("imgs/icons8-entorpecido-48.png", width=40)
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
