# app.py
import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="MENFA - Suite Integral de Simulación de Plantas de Gas",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INICIALIZACIÓN EXPANDIDA DEL ESTADO GLOBAL (MEMORIA OPERATIVA DE PLANTA) ---
# Variables base de proceso
if 'p_entrada' not in st.session_state: st.session_state['p_entrada'] = 3500.0          # kPa
if 't_entrada' not in st.session_state: st.session_state['t_entrada'] = 22.0            # °C
if 'caudal_gas' not in st.session_state: st.session_state['caudal_gas'] = 5.0           # MMm³/día
if 'nivel_liquido' not in st.session_state: st.session_state['nivel_liquido'] = 45.0     # %
if 'humedad_salida' not in st.session_state: st.session_state['humedad_salida'] = 24.5   # mg/m³
if 'p_descarga_gasoducto' not in st.session_state: st.session_state['p_descarga_gasoducto'] = 6100.0 # kPa

# Variables de fraccionamiento y tratamiento adicionales
if 'c2_en_glp' not in st.session_state: st.session_state['c2_en_glp'] = 1.1             # % mol
if 'co2_salida' not in st.session_state: st.session_state['co2_salida'] = 1.5           # % mol

# Variables de control cognitivo e inyección de fallas desde el manual
if 'falla_surge_activa' not in st.session_state: st.session_state['falla_surge_activa'] = False
if 'falla_hidratos_activa' not in st.session_state: st.session_state['falla_hidratos_activa'] = False
if 'esd_bloqueo_general' not in st.session_state: st.session_state['esd_bloqueo_general'] = False

# --- IMPORTACIÓN SEGURA DE LA SUITE MODULAR MENFA ---
try:
    from modulos.separacion import render_separacion
    from modulos.tratamiento import render_tratamiento
    from modulos.procesamiento import render_procesamiento
    from modulos.fraccionamiento_lgn import render_fraccionamiento
    from modulos.calidad_medicion import render_calidad_medicion
    from modulos.transporte import render_transporte
    from modulos.servicios_auxiliares import render_servicios
    from modulos.seguridad import render_seguridad
    
    # Módulos Pedagógicos y de Soporte Académico
    from modulos.manual_digital import render_manual
    from modulos.guias_rapidas import render_guias_rapidas
    from modulos.cognitivo import render_cognitivo
    from modulos.evaluacion import render_evaluacion
    from modulos.normativo import render_normativo
except ImportError as e:
    st.error(f"⚠️ Error Crítico en Arquitectura Modular: {e}")
    st.stop()

# --- MENÚ LATERAL INDUSTRIAL MENFA ---
st.sidebar.image("logo_menfa.png", use_container_width=True)

st.sidebar.markdown("### 🏭 Operación de Planta")
seccion = st.sidebar.radio(
    label="Módulo Activo:",
    options=[
        "Consola SCADA Central",
        "Separación de Entrada",
        "Tratamiento de Gas (Endulzamiento)",
        "Planta Criogénica (Acondicionamiento)",
        "Fraccionamiento de LGN",
        "Calidad y Medición (ENARGAS)",
        "Sistemas de Transporte y Despacho",
        "Servicios Auxiliares & IIoT",
        "Matriz de Seguridad Operacional"
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📘 Academia e Instrucción")
pedagogico = st.sidebar.radio(
    label="Herramientas de Estudio:",
    options=[
        "Ninguno - Modo Operativo Activo",
        "1. Manual Técnico Completo",
        "2. Guías Rápidas de Campo (SOP)",
        "3. Aula de Entrenamiento Cognitivo",
        "4. Sistema de Evaluación Digital",
        "5. Auditoría de Cumplimiento Normativo"
    ]
)

st.sidebar.markdown("---")
if st.session_state['esd_bloqueo_general']:
    st.sidebar.error("🚨 SISTEMA EN PARADA DE EMERGENCIA (ESD)")
else:
    st.sidebar.success("🟢 DCS Planta Operativa en Línea")

# =====================================================================
# --- ENRUTADOR LOGÍSTICO COMPLETO ---
# =====================================================================

# Prioridad al ruteo de herramientas pedagógicas si están seleccionadas
if pedagogico != "Ninguno - Modo Operativo Activo":
    if "1. Manual" in pedagogico:
        render_manual()
    elif "2. Guías" in pedagogico:
        render_guias_rapidas()
    elif "3. Aula" in pedagogico:
        render_cognitivo()
    elif "4. Sistema" in pedagogico:
        render_evaluacion()
    elif "5. Auditoría" in pedagogico:
        render_normativo()

else:
    # Despliegue de Módulos de Operación de Planta en base a la Selección
    if seccion == "Consola SCADA Central":
        st.title("🖥️ Consola Central SCADA - Suite MENFA")
        st.caption("Panel general de supervisión de variables de proceso integradas.")
        st.markdown("---")
        
        if st.session_state['esd_bloqueo_general']:
            st.error("🚨 PARADA DE EMERGENCIA ACTIVA: Todas las plantas se encuentran aisladas y despresurizadas hacia la antorcha.")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Presión Entrada (V-101)", f"{st.session_state['p_entrada']:.1f} kPa")
        col2.metric("Nivel Domo Separador", f"{st.session_state['nivel_liquido']:.1f} %")
        col3.metric("Humedad Gas de Salida", f"{st.session_state['humedad_salida']:.1f} mg/m³")
        col4.metric("Presión Despacho Troncal", f"{st.session_state['p_descarga_gasoducto']:.1f} kPa")
        
        st.markdown("### 🗺️ Diagrama de Flujo de Procesos Integral (PFD)")
        st.info("💡 **Guía del Instructor:** Modifique las condiciones de diseño dentro del **Manual Técnico** para evaluar cómo reaccionan estos indicadores analógicos en tiempo real.")

    elif seccion == "Separación de Entrada":
        render_separacion()

    elif seccion == "Tratamiento de Gas (Endulzamiento)":
        render_tratamiento()

    elif seccion == "Planta Criogénica (Acondicionamiento)":
        render_procesamiento()

    elif seccion == "Fraccionamiento de LGN":
        render_fraccionamiento()

    elif seccion == "Calidad y Medición (ENARGAS)":
        render_calidad_medicion()

    elif seccion == "Sistemas de Transporte y Despacho":
        render_transporte()

    elif seccion == "Servicios Auxiliares & IIoT":
        render_servicios()

    elif seccion == "Matriz de Seguridad Operacional":
        render_seguridad()
