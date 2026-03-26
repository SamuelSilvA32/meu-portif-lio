import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    layout="wide",
    page_title="Curriculo digital",
    page_icon="mini-site/imgs/icons8-manager-48.png"
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
  Analiso, construo, comunico. Meu objetivo agora é transpor esses 
projetos para o mercado.

 Desenvolvo análises e dashboards com: Python, Pandas, Streamlit Power BI etc.
 Cada projeto foi uma oportunidade 
de refinar não apenas a técnica, mas também a capacidade de transformar dados 
em narrativas claras e acionáveis.
 Tenho clareza do que posso entregar hoje e, sobretudo, consciência de que 
o ambiente real exige adaptação, resiliência e aprendizado contínuo. 
É justamente isso que busco.
 Estou aberto a relações profissionais nas mais diversas modalidades,
seja CLT, colaboração freelance ou projetos pontuais. O que me move é 
a oportunidade de estar onde os problemas de fato acontecem e contribuir 
com soluções sustentadas em dados.

 Se você procura alguém disposto a aprender fazendo, com base sólida 
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
