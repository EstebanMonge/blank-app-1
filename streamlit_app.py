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
# MEMORIA DE PERSONAS
# -----------------------------
if "personas" not in st.session_state:
    st.session_state.personas = []

if "current_persona" not in st.session_state:
    st.session_state.current_persona = None

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "results" not in st.session_state:
    st.session_state.results = {}

st.title("Votappcion")
st.write("Bienvenido a Votappcion la aplicación para escoger al mejor")

keys = list(characters.keys())

# -----------------------------
# FORMULARIO DE PERSONA
# -----------------------------
if st.session_state.current_persona is None:

    st.write("Ingresa tus datos")

    cedula = st.text_input("Cédula")
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")

    if st.button("Iniciar votación"):

        if cedula and nombre and apellido:

            persona = {
                "cedula": cedula,
                "nombre": nombre,
                "apellido": apellido,
            }

            # guardar en variable personas (como pediste)
            st.session_state.personas.append(persona)

            st.session_state.current_persona = persona

            # RESET IMPORTANTE para evitar el bug que tenías
            st.session_state.current_index = 0
            st.session_state.results = {}

            st.rerun()

        else:
            st.warning("Completa todos los campos")

# -----------------------------
# VOTACIÓN
# -----------------------------
else:

    if st.session_state.current_index < len(keys):

        current_key = keys[st.session_state.current_index]
        current_character = characters[current_key]

        st.write(
            f"Votando: {st.session_state.current_persona['nombre']} {st.session_state.current_persona['apellido']}"
        )

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
            st.write("### Persona actual")
            st.write(st.session_state.current_persona)

            st.write("### Todas las personas")
            st.write(st.session_state.personas)

            st.write("### Votos")
            st.write(st.session_state.results)