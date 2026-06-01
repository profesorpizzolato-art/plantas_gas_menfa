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

# --- REHABILITACIÓN COMPLETA DEL BLOQUE PEDAGÓGICO ---

elif seccion == "1. Manual Técnico Digital":
    st.title("📘 1. Manual Técnico Digital de Operaciones")
    st.caption("Fundamentos teóricos e ingeniería de procesos de la planta según la bibliografía técnica oficial de la Suite MENFA.")
    st.markdown("---")
    
    m_tabs = st.tabs(["🕳️ Dinámica de Pozos", "💧 Deshidratación por TEG", "🌀 Turbocompresión & Surge"])
    
    with m_tabs[0]:
        st.markdown("### Mecanismos de Empuje e Interfaz de Fluidos")
        st.write("Según *El Pozo Ilustrado*, la energía natural del yacimiento gobierna las proporciones de gas y corte de agua (BS&W) en la entrada de la planta. Comprender si el empuje es por capa de gas o hidráulico permite anticipar inundaciones en el separador primario V-101.")
        
    with m_tabs[1]:
        st.markdown("### Absorción e Interlocks Térmicos en Torres de Glicol")
        st.write("Basado en los estudios de deshidratación de *Dialnet*, el gas natural debe reducir su vapor de agua por debajo del límite regulatorio. El manual establece que ante fallas de temperatura en el reboiler, la degradación del Trietilanglicol (TEG) es crítica si supera los 204°C, activando un interlock de corte automático.")
        
    with m_tabs[2]:
        st.markdown("### Termodinámica y Control de Surge en Compresores")
        st.write("De acuerdo con la ingeniería de *Techint* e *Instrumentation*, el fenómeno de Surge (bombeo aerodinámico) ocurre por caídas bruscas de caudal o contrapresiones extremas del gasoducto. Esto induce vibración axial violenta destructiva para los álabes, requiriendo la apertura rápida de la Anti-Surge Valve (ASV).")

elif seccion == "2. Guías Rápidas de Campo":
    render_guias_rapidas()

elif seccion == "3. System de Evaluación":
    render_evaluacion()

elif seccion == "4. Entrenamiento Normativo":
    st.title("📜 4. Entrenamiento Normativo & Regulatorio")
    st.caption("Módulo de adiestramiento en legislación técnica y resoluciones del ENARGAS.")
    st.markdown("---")
    st.info("💡 **Marco de Aplicación Nacional:** En este espacio los alumnos se entrenan bajo las especificaciones de calidad de la NAG-100 y resoluciones vigentes para la entrega conforme de gas natural a los gasoductos de transporte interconectados.")

elif seccion == "5. Entrenamiento Cognitivo":
    st.title("🧠 5. Entrenamiento Cognitivo y Análisis de Fallas")
    st.caption("Simulación de escenarios complejos ocultos para el desarrollo del criterio operativo.")
    st.markdown("---")
    st.warning("⚠️ **Módulo Avanzado:** Espacio diseñado para inyectar fallas encadenadas en la planta (ej: pérdida de señal de telemetría IIoT coincidente con un golpe de bomba en el Upstream), obligando al operador a diagnosticar la raíz del problema mediante telemetría desactualizada.")
