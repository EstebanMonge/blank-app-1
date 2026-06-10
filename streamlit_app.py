import streamlit as st

characters = {
    "subzero": {
        "name": "Sub Zero",
        "image": "imagenes/subzero.webp",
        "votes": 0,
    },
    "johnnycage": {
        "name": "Johnny Cage",
        "image": "imagenes/johnnycage.webp",
        "votes": 0,
    },
    "noobsaibot": {
        "name": "Noob Saibot",
        "image": "imagenes/noobsaibot.webp",
        "votes": 0,
    },
    "liukang": {
        "name": "Liu Kang",
        "image": "imagenes/liukang.webp",
        "votes": 0,
    },
}
# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = "form"

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "results" not in st.session_state:
    st.session_state.results = []

# -----------------------------
# FORMULARIO DE USUARIO
# -----------------------------
st.title("Votappcion")

if st.session_state.step == "form":

    st.write("Ingresa tus datos para votar")

    cedula = st.text_input("Cédula")
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")

    if st.button("Iniciar votación"):
        if cedula and nombre and apellido:
            st.session_state.user = {
                "cedula": cedula,
                "nombre": nombre,
                "apellido": apellido,
            }
            st.session_state.step = "votacion"
            st.rerun()
        else:
            st.warning("Completa todos los campos")

# -----------------------------
# VOTACIÓN
# -----------------------------
elif st.session_state.step == "votacion":

    keys = list(characters.keys())

    if st.session_state.current_index < len(keys):

        key = keys[st.session_state.current_index]
        character = characters[key]

        st.write(f"Votando como: {st.session_state.user['nombre']} {st.session_state.user['apellido']}")

        st.subheader(character["name"])
        st.image(character["image"])

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Sí"):
                st.session_state.results.append({
                    "user": st.session_state.user,
                    "character": key,
                    "vote": True
                })
                st.session_state.current_index += 1
                st.rerun()

        with col2:
            if st.button("No"):
                st.session_state.results.append({
                    "user": st.session_state.user,
                    "character": key,
                    "vote": False
                })
                st.session_state.current_index += 1
                st.rerun()

    else:
        st.success("Terminaste la votación de este usuario")

        if st.button("Ver resultados"):
            st.session_state.step = "results"
            st.rerun()

# -----------------------------
# RESULTADOS
# -----------------------------
elif st.session_state.step == "results":

    st.write("## Resultados")

    for r in st.session_state.results:
        user = r["user"]
        character = characters[r["character"]]
        vote = "Sí" if r["vote"] else "No"

        st.write(
            f"{user['nombre']} {user['apellido']} ({user['cedula']}) -> "
            f"{character['name']} : {vote}"
        )