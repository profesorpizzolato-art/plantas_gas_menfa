# app.py
import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Suite MENFA - Simulador de Producción y Plantas de Gas",
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

# --- IMPORTACIÓN SEGURA DE MÓDULOS DE INGENIERÍA ---
try:
    from modulos.separacion import render_separacion
    from modulos.procesamiento import render_procesamiento
    from modulos.calidad_medicion import render_calidad_medicion
    from modulos.servicios_auxiliares import render_servicios
    from modulos.guias_rapidas import render_guias_rapidas
    from modulos.evaluacion import render_evaluacion
except ImportError as e:
    st.error(f"⚠️ Error de consistencia en arquitectura modular: {e}")
    st.stop()

# --- MENÚ LATERAL CON IDENTIDAD CORPORATIVA MENFA ---
st.sidebar.image("logo_menfa.png", use_container_width=True)
st.sidebar.title("🎛️ Matriz Operativa")

seccion = st.sidebar.radio("Seleccione el Módulo de Trabajo:", [
    "Panel Control General",
    "Separación de Entrada",
    "Planta Criogénica y LGN",
    "Calidad y Medición (ENARGAS)",
    "Servicios Auxiliares & IIoT",
    "--------------------------------",  # Separador visual en la interfaz
    "1. Manual Técnico Digital",
    "2. Guías Rápidas de Campo",      
    "3. Sistema de Evaluación",
    "4. Entrenamiento Normativo",
    "5. Entrenamiento Cognitivo"
])

st.sidebar.markdown("---")
st.sidebar.info("📌 **Control de Gestión:** Suite MENFA parametrizada bajo normas de transporte y seguridad industrial argentina (ENARGAS).")

# =====================================================================
# --- RUTEO LOGÍSTICO Y DESPLIEGUE DE PESTAÑAS ---
# =====================================================================

if seccion == "Panel Control General":
    st.title("🖥️ Consola Central SCADA - Suite MENFA")
    st.caption("Resumen ejecutivo del estado de las variables de proceso y lazos cerrados de control de la planta.")
    st.markdown("---")
    
    # Matriz de KPI en tiempo real
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Presión de Entrada (V-101)", f"{st.session_state['p_entrada']:.1f} kPa")
    col2.metric("Nivel Domo Líquidos", f"{st.session_state['nivel_liquido']:.1f} %")
    col3.metric("Humedad Control ENARGAS", f"{st.session_state['humedad_salida']:.1f} mg/m³")
    col4.metric("Presión Despacho Troncal", f"{st.session_state['p_descarga_gasoducto']:.1f} kPa")
    
    st.markdown("### 🗺️ Diagrama de Flujo de Procesos (PFD)")
    st.info("💡 **Indicación al Operador:** Seleccione un módulo de la barra lateral para intervenir las variables analógicas o gestionar los escenarios de開contingencia de las cuencas.")

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

# =====================================================================
# --- MANUAL TÉCNICO DIGITAL EXHAUSTIVO DE PROCESOS (RECONSTRUIDO) ---
# =====================================================================
elif seccion == "1. Manual Técnico Digital":
    st.title("📘 Manual Técnico de Ingeniería de Procesos y Operaciones")
    st.caption("Documentación oficial de diseño, ecuaciones fundamentales de control y matrices de enclavamiento de la Suite MENFA.")
    st.markdown("---")
    
    # Índice modularizado de alta densidad teórica
    m_tabs = st.tabs([
        "🛢️ Cap. 1: Separación Primaria", 
        "💧 Cap. 2: Absorción y Deshidratación", 
        "❄️ Cap. 3: Termodinámica Criogénica", 
        "🌀 Cap. 4: Turbocompresión y Dinámica",
        "🛡️ Cap. 5: Protocolos de Custodia ENARGAS"
    ])
    
    # --- CAPÍTULO 1 ---
    with m_tabs[0]:
        st.header("Capítulo 1: Separación de Entrada y Dinámica del Subsuelo")
        st.markdown("""
        El comportamiento hidrodinámico del separador horizontal primario (V-101) responde directamente a la caracterización física y energética del subsuelo según los lineamientos de *El Pozo Ilustrado*. 
        """)
        
        col_c1_1, col_c1_2 = st.columns(2)
        with col_c1_1:
            st.subheader("1.1 Parámetros de Diseño y Leyes de Asentamiento")
            st.markdown("""
            El volumen útil está dimensionado para garantizar un **tiempo de residencia mínimo ($\tau$) de 3 a 5 minutos**, permitiendo que la diferencia de densidades segregue las fases y evitando el fenómeno de arrastre de líquido en la corriente de gas (*Carry-over*).
            
            La velocidad de diseño del gas para impedir que gotas de líquido mayores a 150 micrones alcancen el tope del recipiente se rige por la ecuación de Saunders-Brown:
            """)
            st.latex(r"V_c = K \cdot \sqrt{\frac{\rho_L - \rho_G}{\rho_G}}")
            st.caption("Donde $K$ representa el factor empírico del extractor de niebla (*mist extractor*), y $\rho_L, \rho_G$ son las densidades de las fases líquida y gaseosa.")
            
        with col_c1_2:
            st.subheader("1.2 Mecanismos de Empuje y Modos de Falla")
            st.markdown("""
            * **Empuje Hidráulico Activo (*Water Drive*):
