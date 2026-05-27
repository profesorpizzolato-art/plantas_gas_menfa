import streamlit as st
import config as cfg
from modulos.separacion import render_separacion
from modulos.tratamiento import render_tratamiento
from modulos.calidad_medicion import render_evaluacion

# Configuración de página de Streamlit
st.set_page_config(page_title="MENFA - Simulador Planta de Gas", layout="wide")

st.title("🏭 MENFA - Plataforma de Simulación de Plantas de Gas")
st.caption("Módulos integrados para la capacitación técnica y evaluación operativa.")

# --- NAVEGACIÓN LATERAL ---
menu = st.sidebar.radio("📋 Secciones de la Planta", [
    "Panel de Control General",
    "Separación de Entrada",
    "Tratamiento y Deshidratación",
    "Evaluación Técnica"
])

# Ejecución de lógica de módulos para guardar variables en la sesión del simulador
if 'p_entrada' not in st.session_state:
    st.session_state.p_entrada = 3500
    st.session_state.t_entrada = 20
    st.session_state.nivel_liquido = 45
    st.session_state.humedad_salida = 25.0
    st.session_state.temp_reboiler = 180

# --- MATRIZ DE SEGURIDAD (CDE / Interlocks) ---
cde_activado = False
motivo_cde = ""

if st.session_state.nivel_liquido >= cfg.LIMITE_NIVEL_LIQUIDO:
    cde_activado = True
    motivo_cde = f"Alto Nivel Crítico en Separador (Segundo Interruptor >= {cfg.LIMITE_NIVEL_LIQUIDO}%)."
elif st.session_state.p_entrada >= cfg.LIMITE_PRESION_MAX:
    cde_activado = True
    motivo_cde = f"Sobrepresión Crítica en Colector de Entrada (Límite: {cfg.LIMITE_PRESION_MAX} kPa)."
elif st.session_state.temp_reboiler >= cfg.LIMITE_TEMP_REBOILER:
    cde_activado = True
    motivo_cde = f"Alta Temperatura Crítica en Reboiler de Glicol (Límite: {cfg.LIMITE_TEMP_REBOILER}°C)."

# --- DESPLIEGUE VISUAL SEGÚN EL MENÚ SELECCIONADO ---
if cde_activado:
    st.error(f"🚨 CIERRE DE EMERGENCIA ACTIVADO (CDE)\n\n**Motivo:** {motivo_cde}\n\n*El flujo de gas a planta se encuentra interrumpido automáticamente por sistemas de enclavamiento.*")

if menu == "Panel de Control General":
    st.subheader("📊 Resumen Operativo de la Planta")
    
    # KPIs generales del sistema
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Presión Entrada", f"{st.session_state.p_entrada} kPa")
    with col2:
        st.metric("Nivel Separador", f"{st.session_state.nivel_liquido} %")
    with col3:
        status_calidad = "✅ OK" if st.session_state.humedad_salida <= cfg.LIMITE_HUMEDAD_M3 else "❌ Fuera de Norma"
        st.metric("Calidad Gas (Humedad)", f"{st.session_state.humedad_salida:.2f} mg/m³", delta=status_calidad)
    with col4:
        status_planta = "🔴 Bloqueada (CDE)" if cde_activado else "🟢 Operando"
        st.metric("Estado de Planta", status_planta)

elif menu == "Separación de Entrada":
    p, t, nv = render_separacion()
    st.session_state.p_entrada = p
    st.session_state.t_entrada = t
    st.session_state.nivel_liquido = nv

elif menu == "Tratamiento y Deshidratación":
    h_salida, t_reb = render_tratamiento(st.session_state.p_entrada, st.session_state.t_entrada)
    st.session_state.humedad_salida = h_salida
    st.session_state.temp_reboiler = t_reb

elif menu == "Evaluación Técnica":
    render_evaluacion()
