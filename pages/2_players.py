import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Players",
    page_icon="⚽",  # Ícone de uma bola de futebol
)


df_data = st.session_state['data']

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

# Verifique se o jogador foi selecionado
if player:
    player_stats = df_players[df_players["Name"] == player].iloc[0]

    st.image(player_stats["Photo"], width=100)
    st.title(f"{player_stats['Name']}")

    st.markdown(f"**Clube:** {player_stats['Club']}")
    st.markdown(f"**Posição:** {player_stats['Position']}")

    col1, col2, col3 = st.columns(3)
    col1.markdown(f"**Idade:** {player_stats['Age']}")
    col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
    col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}")


st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado", value=f"£{player_stats['Value(£)']:,}")
col2.metric(label="Valor semanal", value=f"£{player_stats['Wage(£)']:,}")
col3.metric(label="Valor de rescisão",
            value=f"£{player_stats['Release Clause(£)']:,}")
