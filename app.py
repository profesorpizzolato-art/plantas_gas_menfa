# app.py
import streamlit as st
from modulos.separacion import render_separacion
from modulos.tratamiento import render_tratamiento
from modulos.procesamiento import render_procesamiento
from modulos.transporte import render_transporte
from modulos.seguridad import procesar_matriz_seguridad
from modulos.calidad_medicion import render_evaluacion

st.set_page_config(page_title="MENFA - Simulador Integrado de Gas", layout="wide")

st.title("🏭 MENFA - Simulador de Plantas de Procesamiento y Gasoductos")
st.caption("Plataforma integrada de capacitación técnica basada en normativas operativas de la industria del gas natural.")

# --- INICIALIZACIÓN DE VARIABLES EN SESIÓN ---
if 'p_entrada' not in st.session_state:
    st.session_state.p_entrada = 3500
    st.session_state.t_entrada = 20
    st.session_state.nivel_liquido = 45
    st.session_state.p_descarga_gasoducto = 6100

# --- NAVEGACIÓN ---
menu = st.sidebar.radio("📋 Secciones de la Planta", [
    "Panel General Operativo",
    "Separación de Entrada",
    "Tratamiento (TEG)",
    "Planta Criogénica",
    "Compresión y Gasoductos",
    "Matriz de Seguridad (NAG-125)",
    "Evaluación Técnica"
])

# --- MENÚ LATERAL DE MONITOREO RÁPIDO ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🚦 Alertas del Sistema")
procesar_matriz_seguridad() # Se ejecuta en segundo plano para actualizar alarmas

# --- CONTROLADORES DE RENDERIZADO DE INTERFAZ ---
if menu == "Panel General Operativo":
    st.subheader("📊 Panel General de Supervisión (KPIs)")
    col1, col2, col3 = st.columns(3)
    col1.metric("Presión Entrada", f"{st.session_state.p_entrada} kPa")
    col2.metric("Presión Despacho", f"{st.session_state.p_descarga_gasoducto} kPa")
    col3.metric("Nivel Separador", f"{st.session_state.nivel_liquido} %")

elif menu == "Separación de Entrada":
    p, t, nv = render_separacion()
    st.session_state.p_entrada = p
    st.session_state.t_entrada = t
    st.session_state.nivel_liquido = nv

elif menu == "Tratamiento (TEG)":
    render_tratamiento(st.session_state.p_entrada, st.session_state.t_entrada)

elif menu == "Planta Criogénica":
    render_procesamiento(st.session_state.p_entrada, st.session_state.t_entrada)

elif menu == "Compresión y Gasoductos":
    p_desc = render_transporte()
    st.session_state.p_descarga_gasoducto = p_desc

elif menu == "Matriz de Seguridad (NAG-125)":
    st.info("Consulte la pestaña lateral para ver la lógica de enclavamiento activa.")

elif menu == "Evaluación Técnica":
    render_evaluacion()
# app.py
import streamlit as st
from modulos.manual_digital import render_manual
from modulos.evaluacion import render_evaluacion
from modulos.normativo import render_normativo
from modulos.cognitivo import render_cognitivo

st.set_page_config(page_title="MENFA - Entrenamiento Integrado", layout="wide")

# Inicialización de estados de sesión
if 'p_entrada' not in st.session_state:
    st.session_state.nivel_liquido = 45

# Menú lateral estructurado por pilares de formación profesional
st.sidebar.title("🏭 MENFA Gas & Proceso")
st.sidebar.markdown("### Sistema de Entrenamiento Integrado")

pilar_seleccionado = st.sidebar.radio("📚 Pilares de Capacitación:", [
    "1. Manual Técnico Digital",
    "2. Sistema de Evaluación",
    "3. Entrenamiento Normativo",
    "4. Entrenamiento Cognitivo Operacional"
])

st.sidebar.markdown("---")
st.sidebar.caption("Desarrollado para la formación avanzada de técnicos y operadores de plantas de proceso.")

# Enrutador de módulos
if "Manual" in pilar_seleccionado:
    render_manual()
elif "Evaluación" in pilar_seleccionado:
    render_evaluacion()
elif "Normativo" in pilar_seleccionado:
    render_normativo()
elif "Cognitivo" in pilar_seleccionado:
    render_cognitivo()
