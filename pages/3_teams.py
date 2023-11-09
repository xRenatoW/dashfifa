import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Times",
    page_icon="⚽",  # Ícone de uma bola de futebol
)

df_data = st.session_state['data']

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filter = df_data[df_data["Club"] == club].set_index("Name")

st.image(df_filter.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined",
           "Height(cm.)", "Weight(lbs.)",
           "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filter[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
                 "Value(£)": st.column_config.NumberColumn(),
                 "Wage(£)": st.column_config.ProgressColumn("Salário Semanal", format="£%f", min_value=0, max_value=df_filter["Wage(£)"].max()),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country")
}, height=1000)
