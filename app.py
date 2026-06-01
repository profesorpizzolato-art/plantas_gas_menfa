# app.py
import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="MENFA - Simulador de Producción y Plantas de Gas",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INICIALIZACIÓN DEL ESTADO GLOBAL (MEMORIA DINÁMICA DE LA PLANTA) ---
if 'p_entrada' not in st.session_state:
    st.session_state['p_entrada'] = 3500.0  # kPa
if 't_entrada' not in st.session_state:
    st.session_state['t_entrada'] = 22.0    # °C
if 'nivel_liquido' not in st.session_state:
    st.session_state['nivel_liquido'] = 45.0 # %
if 'humedad_salida' not in st.session_state:
    st.session_state['humedad_salida'] = 24.5 # mg/m³
if 'p_descarga_gasoducto' not in st.session_state:
    st.session_state['p_descarga_gasoducto'] = 6100.0 # kPa

# --- IMPORTACIÓN SEGURA DE MÓDULOS DE INGENIERÍA Y ACADÉMICOS ---
try:
    from modulos.separacion import render_separacion
    from modulos.procesamiento import render_procesamiento
    from modulos.calidad_medicion import render_calidad_medicion
    from modulos.servicios_auxiliares import render_servicios
    from modulos.manual_digital import render_manual_digital  # <- Movido a su módulo propio
    from modulos.guias_rapidas import render_guias_rapidas
    from modulos.evaluacion import render_evaluacion
    from modulos.normativo import render_normativo        # <- Conexión real al módulo normativo
    from modulos.cognitivo import render_cognitivo        # <- Conexión real al módulo cognitivo
except ImportError as e:
    st.error(f"⚠️ Error de consistencia en arquitectura modular: {e}")
    st.stop()

# --- MENÚ LATERAL CON IDENTIDAD CORPORATIVA MENFA ---
st.sidebar.image("logo_menfa.png", use_container_width=True)

st.sidebar.markdown("### 🏭 Operación de Planta")
# Un solo radio unificado para evitar duplicidad de selección visual en la UI
seccion = st.sidebar.radio(
    label="Seleccione el Módulo Activo:",
    options=[
        "Panel Control General",
        "Separación de Entrada",
        "Planta Criogénica y LGN",
        "Calidad y Medición (ENARGAS)",
        "Servicios Auxiliares & IIoT",
        "1. Manual Técnico Digital",
        "2. Guías Rápidas de Campo",      
        "3. Sistema de Evaluación",
        "4. Entrenamiento Normativo",
        "5. Entrenamiento Cognitivo"
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📘 Soporte Académico")
st.sidebar.caption("Acceda al material técnico de base, normativas de transporte y escenarios dinámicos avanzados.")

st.sidebar.markdown("---")
st.sidebar.info("📌 **Control de Gestión:** Suite MENFA parametrizada bajo normas de transporte y seguridad industrial argentina (ENARGAS).")

# =====================================================================
# --- RUTEO LOGÍSTICO Y DESPLIEGUE DE INTERFACES ---
# =====================================================================

if seccion == "Panel Control General":
    st.title("🖥️ Consola Central SCADA - Suite MENFA")
    st.caption("Resumen ejecutivo del estado de las variables de proceso y lazos cerrados de control de la planta.")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Presión de Entrada (V-101)", f"{st.session_state['p_entrada']:.1f} kPa")
    col2.metric("Nivel Domo Líquidos", f"{st.session_state['nivel_liquido']:.1f} %")
    col3.metric("Humedad Control ENARGAS", f"{st.session_state['humedad_salida']:.1f} mg/m³")
    col4.metric("Presión Despacho Troncal", f"{st.session_state['p_descarga_gasoducto']:.1f} kPa")
    
    st.markdown("### 🗺️ Diagrama de Flujo de Procesos (PFD)")
    st.info("💡 **Indicación al Operador:** Seleccione un módulo de la barra lateral para intervenir las variables analógicas o gestionar los escenarios de contingencia de las cuencas.")

elif seccion == "Separación de Entrada":
    p_op, t_op, niv_op = render_separacion()
    st.session_state['p_entrada'] = p_op
    st.session_state['t_entrada'] = t_op
    st.session_state['nivel_liquido'] = niv_op

elif seccion == "Planta Criogénica y LGN":
    render_procesamiento(st.session_state['p_entrada'], st.session_state['t_entrada'])

elif seccion == "Calidad y Medición (ENARGAS)":
    render_calidad_medicion()

elif seccion == "Servicios Auxiliares & IIoT":
    render_servicios()

# --- RUTEO DE MÓDULOS PEDAGÓGICOS ASOCIADOS A TU CARPETA ---

elif seccion == "1. Manual Técnico Digital":
    render_manual_digital()  # <- Ahora llama directamente al script 'manual_digital.py'

elif seccion == "2. Guías Rápidas de Campo":
    render_guias_rapidas()

elif seccion == "3. Sistema de Evaluación":
    render_evaluacion()

elif seccion == "4. Entrenamiento Normativo":
    render_normativo()     # <- EJECUTA TU MÓDULO 'normativo.py' REAL

elif seccion == "5. Entrenamiento Cognitivo":
    render_cognitivo()     # <- EJECUTA TU MÓDULO 'cognitivo.py' REAL
