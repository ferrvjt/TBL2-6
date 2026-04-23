import streamlit as st
from modules.RegisterModule import crear_usuario, registrar_sueno, registrar_alimentacion, registrar_ejercicio
from modules.StatModule import evaluar_sueno, evaluar_alimentacion, evaluar_ejercicio

st.set_page_config(page_title="Hábitos Saludables", layout="wide")

# CSS
def load_css():
    with open("styles/styles.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("Sistema de Hábitos Saludables")

if "usuario" not in st.session_state:
    st.session_state.usuario = None

if st.session_state.usuario is None:

    st.subheader("Registro de usuario")

    with st.form("form_usuario"):
        nombre = st.text_input("Nombre")
        edad = st.number_input("Edad", min_value=1)

        submitted = st.form_submit_button("Crear usuario")

        if submitted:
            if nombre.strip() == "":
                st.error("Ingresa un nombre válido")
            else:
                st.session_state.usuario = crear_usuario(nombre, edad)
                st.rerun()

else:
    usuario = st.session_state.usuario

    st.success(f"Usuario: {usuario['nombre']}")

    opcion = st.selectbox("Menú", [
        "Registrar hábitos",
        "Evaluar usuario",
        "Recomendaciones",
        "Retroalimentación"
    ])

    if opcion == "Registrar hábitos":
        st.subheader("Registrar hábitos")

        with st.form("form_habitos"):
            col1, col2, col3 = st.columns(3)

            with col1:
                horas = st.number_input("Horas de sueño", 0.0, 24.0)

            with col2:
                comidas = st.number_input("Comidas saludables", 0)

            with col3:
                minutos = st.number_input("Minutos de ejercicio", 0)

            guardar = st.form_submit_button("Guardar")

            if guardar:
                registrar_sueno(usuario, horas)
                registrar_alimentacion(usuario, comidas)
                registrar_ejercicio(usuario, minutos)
                st.success("Datos guardados correctamente")

    elif opcion == "Evaluar usuario":
        st.subheader("Evaluación")

        s = evaluar_sueno(usuario)
        a = evaluar_alimentacion(usuario)
        e = evaluar_ejercicio(usuario)

        col1, col2, col3 = st.columns(3)
        col1.metric("Sueño", s)
        col2.metric("Alimentación", a)
        col3.metric("Ejercicio", e)

        promedio = (s + a + e) / 3
        st.write("Promedio general:", round(promedio, 2))

    elif opcion == "Recomendaciones":
        st.subheader("Recomendaciones")

        s = evaluar_sueno(usuario)
        a = evaluar_alimentacion(usuario)
        e = evaluar_ejercicio(usuario)

        if s < 60:
            st.warning("Debes dormir más horas")
        else:
            st.success("Buen nivel de sueño")

        if a < 60:
            st.warning("Mejora tu alimentación")
        else:
            st.success("Buena alimentación")

        if e < 60:
            st.warning("Debes hacer más ejercicio")
        else:
            st.success("Buen nivel de actividad")

    elif opcion == "Retroalimentación":
        st.subheader("Retroalimentación")

        s = evaluar_sueno(usuario)
        a = evaluar_alimentacion(usuario)
        e = evaluar_ejercicio(usuario)

        promedio = (s + a + e) / 3

        if promedio >= 80:
            st.success("Estilo de vida saludable")
        elif promedio >= 60:
            st.info("Vas bien, pero puedes mejorar")
        elif promedio >= 40:
            st.warning("Necesitas mejorar tus hábitos")
        else:
            st.error("Debes hacer cambios importantes")

    st.markdown("---")
    if st.button("Cerrar sesión"):
        st.session_state.usuario = None
        st.rerun()