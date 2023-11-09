import streamlit as st
import pandas as pd
import webbrowser

st.set_page_config(
    layout="wide",
    page_title="Página Inicial",
    page_icon="⚽",  # Ícone de uma bola de futebol
)
if "data" not in st.session_state:
    df_data = pd.read_csv(
        "datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state['data'] = df_data


st.write("# Conjunto de Dados de Jogadores de Futebol - 2023")
st.sidebar.markdown(
    "Desenvolvido por [Renato Firmino](https://www.linkedin.com/in/renato-firmino)")


btn = st.button("Acesse os dados no Keagle")
if btn:
    webbrowser.open_new_tab(
        "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data/data")

st.markdown(
    """# Documentação do Conjunto de Dados de Jogadores de Futebol - 2023

## Introdução
O Conjunto de Dados de Jogadores de Futebol (2023) é uma fonte rica em informações que fornece detalhes abrangentes sobre jogadores profissionais de futebol. Este conjunto de dados concentra-se nas informações disponíveis no ano de 2023 e oferece uma visão detalhada do mundo do futebol, incluindo características demográficas dos jogadores, estatísticas de jogo, detalhes de contrato e afiliações a clubes.

## Conteúdo do Conjunto de Dados
- **ID:** Identificador único de cada jogador.
- **Nome:** Nome do jogador.
- **Idade:** Idade do jogador na data da coleta de dados.
- **Photo:** Link ou referência à fotografia do jogador.
- **Nacionalidade:** Nacionalidade do jogador.
- **Flag:** Bandeira nacional associada à nacionalidade do jogador.
- **Overall:** Classificação geral das habilidades e capacidades do jogador.
- **Potential:** Classificação de potencial que representa o desenvolvimento futuro do jogador.
- **Club:** Afiliação atual do jogador a um clube.
- **Club Logo:** Link ou referência ao logotipo do clube do jogador.
- **Value (£):** Valor de mercado estimado do jogador em libras (£).
- **Wage (£):** Salário semanal do jogador em libras (£).
- **Special:** Valor numérico que representa habilidades especiais do jogador.
- **Preferred Foot:** Pé preferido pelo jogador para jogar.
- **International Reputation:** Classificação que indica a reputação internacional do jogador.
- **Weak Foot:** Classificação que representa a habilidade do pé mais fraco do jogador.
- **Skill Moves:** Número de movimentos de habilidade que o jogador possui.
- **Work Rate:** Taxa de trabalho do jogador.
- **Body Type:** Estrutura física ou tipo de corpo do jogador.
- **Real Face:** Indica se o jogador tem uma representação facial realista.
- **Position:** Posição preferida de jogo do jogador.
- **Joined:** Data em que o jogador ingressou no clube atual.
- **Loaned From:** Clube do qual o jogador está atualmente emprestado.
- **Contract Valid Until:** Data até a qual o contrato do jogador é válido.
- **Height (cm):** Altura do jogador em centímetros.
- **Weight (lbs):** Peso do jogador em libras.
- **Release Clause (£):** Valor da cláusula de liberação do jogador em libras (£).
- **Kit Number:** Número da camisa usada pelo jogador.
- **Best Overall Rating:** Classificação geral mais alta já alcançada pelo jogador.
- **Year Joined:** Ano em que o jogador ingressou no clube atual.

## Utilização
Este conjunto de dados é uma ferramenta valiosa para analistas de futebol, pesquisadores e entusiastas do esporte que desejam explorar dados detalhados sobre jogadores e clubes no ano de 2023. Ele possibilita análises relacionadas às habilidades dos jogadores, avaliações de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento ao longo do tempo.

## Agradecimentos
Gostaríamos de expressar nossa gratidão ao contribuinte original, cujo conjunto de dados serviu como base para esta versão focada em 2023. Para obter mais informações e acesso ao conjunto de dados original, você pode visitar o link [aqui](https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?rvi=1).
"""
)
