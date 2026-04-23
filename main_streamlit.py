import streamlit as st
from modules.RegisterModule import (
    crear_usuario, registrar_sueno, registrar_alimentacion,
    registrar_ejercicio, registrar_bienestar
)
from modules.StatModule import (
    evaluar_sueno, evaluar_alimentacion, evaluar_ejercicio,
    evaluar_bienestar, evaluar_general, rendimiento
)
from modules.RecommendationModule import obtener_recomendaciones, obtener_retroalimentacion

st.set_page_config(page_title="Vida Saludable", layout="wide")


# CSS
def load_css():
    with open("styles/styles.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()

# Inicializar estado
if "usuario" not in st.session_state:
    st.session_state.usuario = None

if "cuestionario_completo" not in st.session_state:
    st.session_state.cuestionario_completo = False


# ============================================================
# PASO 1: REGISTRO DE USUARIO
# ============================================================
if st.session_state.usuario is None:
    st.title("Vida Saludable")
    st.markdown("#### Tu asistente personal de habitos saludables")
    st.markdown("---")

    with st.form("form_usuario"):
        st.subheader("Crea tu perfil")
        nombre = st.text_input("¿Cuál es tu nombre?")
        edad = st.number_input("¿Cuántos años tienes?", min_value=1, max_value=120, value=20)

        submitted = st.form_submit_button("Comenzar")

        if submitted:
            if nombre.strip() == "":
                st.error("Ingresa un nombre válido")
            else:
                st.session_state.usuario = crear_usuario(nombre, int(edad))
                st.rerun()


# ============================================================
# PASO 2: CUESTIONARIO INICIAL
# ============================================================
elif not st.session_state.cuestionario_completo:
    usuario = st.session_state.usuario

    st.title("Vida Saludable")
    st.markdown(f"### Hola, {usuario['nombre']}! Cuentanos sobre tu estilo de vida")
    st.markdown("Responde estas preguntas para conocer tu estado actual y darte recomendaciones personalizadas.")
    st.markdown("---")

    with st.form("cuestionario_inicial"):

        # --- Sueño ---
        st.subheader("Sueno")
        col1, col2 = st.columns(2)
        with col1:
            horas = st.slider("Cuantas horas duermes normalmente?", 0.0, 14.0, 7.0, 0.5)
            calidad = st.slider("Como calificas tu calidad de sueno?", 1, 5, 3)
        with col2:
            despierta = st.selectbox("Te despiertas durante la noche?", ["No", "Si"], key="q_desp") == "Si"
            pantalla = st.selectbox("Usas pantallas antes de dormir?", ["No", "Si"], key="q_pant") == "Si"

        st.markdown("---")

        # --- Alimentación ---
        st.subheader("Alimentacion")
        col1, col2 = st.columns(2)
        with col1:
            comidas = st.number_input("Cuantas comidas saludables comes al dia?", 0, 10, 2)
            agua = st.number_input("Cuantos vasos de agua tomas al dia?", 0, 20, 4)
        with col2:
            frutas = st.number_input("Porciones de frutas/verduras al dia?", 0, 15, 2)
            comida_rapida = st.selectbox("Comes comida rapida frecuentemente?", ["No", "Si"], key="q_rapida") == "Si"

        st.markdown("---")

        # --- Ejercicio ---
        st.subheader("Ejercicio")
        col1, col2 = st.columns(2)
        with col1:
            minutos = st.number_input("Minutos de ejercicio al dia?", 0, 300, 15)
            tipo = st.selectbox("Que tipo de actividad haces?",
                                ["caminar", "correr", "deporte", "gimnasio", "otro", "ninguno"])
        with col2:
            intensidad = st.selectbox("Que intensidad?", ["baja", "media", "alta"])

        st.markdown("---")

        # --- Bienestar ---
        st.subheader("Bienestar General")
        col1, col2 = st.columns(2)
        with col1:
            pantalla_horas = st.number_input("Horas frente a pantalla al dia?", 0.0, 24.0, 6.0, 0.5)
        with col2:
            estres = st.slider("Tu nivel de estres? (1 = bajo, 5 = alto)", 1, 5, 3)

        enviado = st.form_submit_button("Ver mi reporte")

        if enviado:
            registrar_sueno(usuario, horas, calidad, despierta, pantalla)
            registrar_alimentacion(usuario, int(comidas), int(agua), int(frutas), comida_rapida)
            registrar_ejercicio(usuario, int(minutos), tipo, intensidad)
            registrar_bienestar(usuario, pantalla_horas, estres)
            st.session_state.cuestionario_completo = True
            st.rerun()


# ============================================================
# PASO 3: MENÚ PRINCIPAL (después del cuestionario)
# ============================================================
else:
    usuario = st.session_state.usuario

    # --- Sidebar ---
    with st.sidebar:
        st.markdown("### Vida Saludable")
        st.markdown(f"**{usuario['nombre']}** - {usuario['edad']} anios")
        st.markdown("---")

        pagina = st.radio("Navegacion", [
            "Mi Reporte",
            "Actualizacion Diaria",
            "Recomendaciones"
        ], label_visibility="collapsed")

        st.markdown("---")
        if st.button("Cerrar sesion"):
            st.session_state.usuario = None
            st.session_state.cuestionario_completo = False
            st.rerun()

    # --- PAGINA: MI REPORTE ---
    if pagina == "Mi Reporte":
        st.title("Mi Reporte de Salud")

        retro = obtener_retroalimentacion(usuario)
        promedio = retro["promedio"]
        nivel = retro["nivel"]

        st.markdown(f"### Estado General: {promedio}/100 - {nivel.upper()}")
        st.progress(min(promedio, 100))
        st.info(retro["mensaje"])

        st.markdown("---")

        # Metricas por categoria
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Sueno", f"{retro['sueno']}/100", rendimiento(retro["sueno"]))
        col2.metric("Alimentacion", f"{retro['alimentacion']}/100", rendimiento(retro["alimentacion"]))
        col3.metric("Ejercicio", f"{retro['ejercicio']}/100", rendimiento(retro["ejercicio"]))
        col4.metric("Bienestar", f"{retro['bienestar']}/100", rendimiento(retro["bienestar"]))

        dias = len(usuario["habitos"]["sueno"])
        st.markdown(f"---\n*Basado en **{dias}** dia(s) de registro.*")

    # --- PAGINA: ACTUALIZACION DIARIA ---
    elif pagina == "Actualizacion Diaria":
        st.title("Actualizar mi dia")
        st.markdown("Registra como fue tu dia de hoy para actualizar tu reporte.")

        tab1, tab2, tab3, tab4 = st.tabs(["Sueno", "Alimentacion", "Ejercicio", "Bienestar"])

        with tab1:
            with st.form("form_sueno"):
                st.subheader("Como dormiste?")
                horas = st.slider("Horas de sueno", 0.0, 14.0, 7.0, 0.5)
                calidad = st.slider("Calidad del sueno", 1, 5, 3)
                despierta = st.selectbox("Te despertaste en la noche?", ["No", "Si"], key="d_desp") == "Si"
                pantalla = st.selectbox("Usaste pantallas antes de dormir?", ["No", "Si"], key="d_pant") == "Si"

                if st.form_submit_button("Guardar sueno"):
                    registrar_sueno(usuario, horas, calidad, despierta, pantalla)
                    st.success("Registro de sueno guardado")

        with tab2:
            with st.form("form_alimentacion"):
                st.subheader("Como comiste hoy?")
                comidas = st.number_input("Comidas saludables", 0, 10, 2)
                agua = st.number_input("Vasos de agua", 0, 20, 4)
                frutas = st.number_input("Porciones de frutas/verduras", 0, 15, 2)
                comida_rapida = st.selectbox("Comiste comida rapida?", ["No", "Si"], key="d_rapida") == "Si"

                if st.form_submit_button("Guardar alimentacion"):
                    registrar_alimentacion(usuario, int(comidas), int(agua), int(frutas), comida_rapida)
                    st.success("Registro de alimentacion guardado")

        with tab3:
            with st.form("form_ejercicio"):
                st.subheader("Hiciste ejercicio?")
                minutos = st.number_input("Minutos de ejercicio", 0, 300, 15)
                tipo = st.selectbox("Tipo de actividad",
                                    ["caminar", "correr", "deporte", "gimnasio", "otro", "ninguno"])
                intensidad = st.selectbox("Intensidad", ["baja", "media", "alta"])

                if st.form_submit_button("Guardar ejercicio"):
                    registrar_ejercicio(usuario, int(minutos), tipo, intensidad)
                    st.success("Registro de ejercicio guardado")

        with tab4:
            with st.form("form_bienestar"):
                st.subheader("Como te sentiste?")
                pantalla_horas = st.number_input("Horas frente a pantalla", 0.0, 24.0, 6.0, 0.5)
                estres = st.slider("Nivel de estres (1 = bajo, 5 = alto)", 1, 5, 3)

                if st.form_submit_button("Guardar bienestar"):
                    registrar_bienestar(usuario, pantalla_horas, estres)
                    st.success("Registro de bienestar guardado")

    # --- PAGINA: RECOMENDACIONES ---
    elif pagina == "Recomendaciones":
        st.title("Recomendaciones Personalizadas")

        lista_rec = obtener_recomendaciones(usuario)

        if len(lista_rec) == 0:
            st.info("No hay datos suficientes para generar recomendaciones.")
        else:
            # Agrupar por categoría
            categorias = []
            for rec in lista_rec:
                if rec["categoria"] not in categorias:
                    categorias.append(rec["categoria"])

            for cat in categorias:
                st.subheader(cat)
                for rec in lista_rec:
                    if rec["categoria"] == cat:
                        if rec["tipo"] == "warning":
                            st.warning(rec["mensaje"])
                        else:
                            st.success(rec["mensaje"])

        st.markdown("---")
        dias = len(usuario["habitos"]["sueno"])
        st.markdown(f"*Basado en **{dias}** dia(s) de registro. Agrega mas dias para recomendaciones mas precisas.*")