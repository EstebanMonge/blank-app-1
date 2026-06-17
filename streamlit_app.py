import streamlit as st

codigo="Garbanzo"
if "characters" not in st.session_state:
    st.session_state.characters = {
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

characters = st.session_state.characters

# -----------------------------
# SESSION STATE
# -----------------------------
if "personas" not in st.session_state:
    st.session_state.personas = []

if "current_persona" not in st.session_state:
    st.session_state.current_persona = None

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "results" not in st.session_state:
    st.session_state.results = {}

if "phase" not in st.session_state:
    st.session_state.phase = "form"

keys = list(characters.keys())

st.title("Votappcion")

# -----------------------------
# FORMULARIO
# -----------------------------
if st.session_state.phase == "form":

    st.write("Ingresa tus datos")

    cedula = st.text_input("Cédula")
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")

    if st.button("Iniciar votación"):

        if not cedula or not nombre or not apellido:
            st.error("Completa todos los campos.")
            st.stop()

        if not cedula.isdigit():
            st.error("La cédula debe contener solo números.")
            st.stop()

        # 2. validar duplicados
        existe = any(p["cedula"] == cedula for p in st.session_state.personas)

        if existe:
            st.error("Esta cédula ya votó anteriormente.")
            st.stop()

        # 3. validar campos vacíos
        if cedula and nombre and apellido:

            persona = {
                "cedula": cedula,
                "nombre": nombre,
                "apellido": apellido,
            }

            st.session_state.personas.append(persona)
            st.session_state.current_persona = persona

            st.session_state.current_index = 0
            st.session_state.results = {}

            st.session_state.phase = "voting"

            st.rerun()
    st.divider()

    garbanzo_input = st.text_input("Código de acceso (garbanzo)", type="password")
    if st.button("Ver resultados"):

        if garbanzo_input != codigo:
            st.error("Código incorrecto.")
            st.stop()

        st.session_state.phase = "results"
        st.rerun()

# -----------------------------
# VOTACIÓN
# -----------------------------
elif st.session_state.phase == "voting":

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
            if st.button("Sí", type="primary"):
                st.session_state.results[current_key] = True
                st.session_state.current_index += 1
                st.rerun()

        with col2:
            if st.button("No", type="secondary"):
                st.session_state.results[current_key] = False
                st.session_state.current_index += 1
                st.rerun()

    else:

        for personaje, voto in st.session_state.results.items():
            if voto:
                st.session_state.characters[personaje]["votes"] += 1

        st.session_state.phase = "done"
        st.rerun()
# -----------------------------
# RESULTADOS
# -----------------------------
elif st.session_state.phase == "results":

    st.header("Resultados de la votación")

    for key, character in st.session_state.characters.items():
        st.write(
            f"{character['name']}: {character['votes']} votos"
        )
    if st.button("Ver votantes"):
        st.session_state.phase = "voters"
        st.rerun()

    if st.button("Volver"):
        st.session_state.phase = "form"
        st.rerun()
# -----------------------------
# VOTANTES
# -----------------------------
elif st.session_state.phase == "voters":

    st.header("Lista de votantes")

    if not st.session_state.personas:
        st.info("No hay votantes aún.")
    else:
        for p in st.session_state.personas:
            st.write(f"{p['cedula']} - {p['nombre']} {p['apellido']}")

    if st.button("Volver a resultados"):
        st.session_state.phase = "results"
        st.rerun()       
# -----------------------------
# FINAL
# -----------------------------
elif st.session_state.phase == "done":

    st.success("Gracias por votar")
    st.balloons()

    if st.button("Siguiente votante"):

        st.session_state.current_persona = None
        st.session_state.current_index = 0
        st.session_state.results = {}
        st.session_state.phase = "form"

        st.rerun()