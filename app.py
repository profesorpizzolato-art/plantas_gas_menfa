# app.py
import streamlit as st

# Configuración visual unificada de la plataforma MENFA
st.set_page_config(page_title="MENFA - Simulador Gas Integrado", layout="wide")

st.title("🏭 MENFA - Suite de Simulación y Entrenamiento Integrado")
st.caption("Consola unificada para la formación técnica y operativa en plantas de procesamiento y gasoductos.")

# --- INICIALIZACIÓN DE VARIABLES EN SESIÓN GLOBAL ---
if 'p_entrada' not in st.session_state:
    st.session_state.p_entrada = 3500.0
    st.session_state.t_entrada = 20.0
    st.session_state.nivel_liquido = 45.0
    st.session_state.p_descarga_gasoducto = 6100.0
    st.session_state.humedad_salida = 24.5
    st.session_state.temp_reboiler = 182.0

# --- MENÚ LATERAL DE NAVEGACIÓN ---
st.sidebar.title("🎛️ Matriz Operativa")
seccion = st.sidebar.radio("Seleccione el Módulo de Trabajo:", [
    "Panel Control General",
    "Separación de Entrada",
    "Tratamiento (TEG)",
    "Planta Criogénica",
    "Compresión y Gasoductos",
    "Calidad y Medición",
    "Matriz de Seguridad (NAG-125)",
    "1. Manual Técnico Digital",
    "2. Sistema de Evaluación",
    "3. Entrenamiento Normativo",
    "4. Entrenamiento Cognitivo"
])

st.sidebar.markdown("---")
st.sidebar.info("📌 **Control de Gestión:** Simulador configurado bajo normas de transporte y seguridad industrial.")

# --- IMPORTACIÓN EN TIEMPO DE EJECUCIÓN (Previene errores de dependencias cruzadas) ---
if seccion == "Panel Control General":
    st.subheader("📊 Resumen Operativo de la Planta")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Presión Entrada", f"{st.session_state.p_entrada:.1f} kPa")
    col2.metric("Presión Despacho", f"{st.session_state.p_descarga_gasoducto:.1f} kPa")
    col3.metric("Nivel Separador", f"{st.session_state.nivel_liquido:.1f} %")
    col4.metric("Calidad Gas", f"{st.session_state.humedad_salida:.1f} mg/m³")

elif seccion == "Separación de Entrada":
    from modulos.separacion import render_separacion
    p, t, nv = render_separacion()
    st.session_state.p_entrada = p
    st.session_state.t_entrada = t
    st.session_state.nivel_liquido = nv

elif seccion == "Tratamiento (TEG)":
    from modulos.tratamiento import render_tratamiento
    h_salida, t_reb = render_tratamiento(st.session_state.p_entrada, st.session_state.t_entrada)
    st.session_state.humedad_salida = h_salida
    st.session_state.temp_reboiler = t_reb

elif seccion == "Planta Criogénica":
    from modulos.procesamiento import render_procesamiento
    render_procesamiento(st.session_state.p_entrada, st.session_state.t_entrada)

elif seccion == "Compresión y Gasoductos":
    from modulos.transporte import render_transporte
    st.session_state.p_descarga_gasoducto = render_transporte()

elif seccion == "Calidad y Medición":
    from modulos.calidad_medicion import render_calidad_medicion
    render_calidad_medicion()

elif seccion == "Matriz de Seguridad (NAG-125)":
    from modulos.seguridad import render_seguridad
    render_seguridad()

elif seccion == "1. Manual Técnico Digital":
    from modulos.manual_digital import render_manual
    render_manual()

elif seccion == "2. Sistema de Evaluación":
    from modulos.evaluacion import render_evaluacion
    render_evaluacion()

elif seccion == "3. Entrenamiento Normativo":
    from modulos.normativo import render_normativo
    render_normativo()

elif seccion == "4. Entertainmento Cognitivo":
    from modulos.cognitivo import render_cognitivo
    render_cognitivo()
