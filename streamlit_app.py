import streamlit as st

characters = {
    "subzero": {
        "name": "Sub Zero",
        "image": "images/subzero.webp",
        "votes": 0,
    },
    "johnnycage": {
        "name": "Johnny Cage",
        "image": "images/johnnycage.webp",
        "votes": 0,
    },
    "noobsaibot": {
        "name": "Noob Saibot",
        "image": "images/noobsaibot.webp",
        "votes": 0,
    },
    "liukang": {
        "name": "Liu Kang",
        "image": "images/liukang.webp",
        "votes": 0,
    },
}

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "results" not in st.session_state:
    st.session_state.results = {}

st.title("Votappcion")
st.write(
    "Bienvenido a Votappcion la aplicación para escoger al mejor"
)

keys = list(characters.keys())

if st.session_state.current_index < len(keys):

    current_key = keys[st.session_state.current_index]
    current_character = characters[current_key]

    st.write("¿Vota por?")
    st.subheader(current_character["name"])
    st.image(current_character["image"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Sí"):
            st.session_state.results[current_key] = True
            st.session_state.current_index += 1
            st.rerun()

    with col2:
        if st.button("No"):
            st.session_state.results[current_key] = False
            st.session_state.current_index += 1
            st.rerun()

else:
    st.success("Ya votaste por todos los personajes.")

if st.button("Ver resultados"):
    st.write(st.session_state.results)