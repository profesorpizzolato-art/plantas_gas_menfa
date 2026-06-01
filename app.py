# app.py
import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Suite MENFA - Simulador de Producción y Plantas de Gas",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INICIALIZACIÓN DEL ESTADO GLOBAL (MEMORIA DINÁMICA) ---
if 'p_entrada' not in st.session_state:
    st.session_state['p_entrada'] = 3500.0  # kPa base
if 't_entrada' not in st.session_state:
    st.session_state['t_entrada'] = 22.0    # °C base
if 'nivel_liquido' not in st.session_state:
    st.session_state['nivel_liquido'] = 45.0 # % base
if 'humedad_salida' not in st.session_state:
    st.session_state['humedad_salida'] = 24.5 # mg/m³ base
if 'p_descarga_gasoducto' not in st.session_state:
    st.session_state['p_descarga_gasoducto'] = 6100.0 # kPa base

# --- IMPORTACIÓN DE LOS MÓDULOS DE INGENIERÍA ---
try:
    from modulos.separacion import render_separacion
    from modulos.procesamiento import render_procesamiento
    from modulos.calidad_medicion import render_calidad_medicion
    from modulos.servicios_auxiliares import render_servicios
    from modulos.guias_rapidas import render_guias_rapidas
    from modulos.evaluacion import render_evaluacion
except ImportError as e:
    st.error(f"Error al cargar los módulos secundarios: {e}")
    st.stop()

# --- MENÚ LATERAL DE NAVEGACIÓN (CON IDENTIDAD CORPORATIVA) ---
# Se inserta el logo oficial cargado en la raíz del proyecto
st.sidebar.image("logo_menfa.png", use_container_width=True)

st.sidebar.title("🎛️ Matriz Operativa")
seccion = st.sidebar.radio("Seleccione el Módulo de Trabajo:", [
    "Panel Control General",
    "Separación de Entrada",
    "Planta Criogénica y LGN",
    "Calidad y Medición (ENARGAS)",
    "Servicios Auxiliares & IIoT",
    "--------------------------------",  # Separador visual
    "Guías Rápidas de Campo",      
    "Sistema de Evaluación"
])

st.sidebar.markdown("---")
st.sidebar.info("📌 **Control de Gestión:** Suite MENFA parametrizada bajo normas de transporte y seguridad industrial argentina (ENARGAS).")

# --- RUTEO LOGÍSTICO DE LAS PESTAÑAS ---

if seccion == "Panel Control General":
    st.title("🖥️ Consola Central Scada - Suite MENFA")
    st.caption("Resumen ejecutivo del estado de las variables de proceso y lazos cerrados de control de la planta.")
    st.markdown("---")
    
    # Vista sinóptica general empleando las variables en memoria activa
    col1, col2, col3 = st.columns(3)
    col1.metric("Presión Separador V-101", f"{st.session_state['p_entrada']:.1f} kPa")
    col2.metric("Nivel de Líquido de Entrada", f"{st.session_state['nivel_liquido']:.1f} %")
    col3.metric("Humedad de Despacho Comercial", f"{st.session_state['humedad_salida']:.1f} mg/m³")
    
    st.markdown("### 🗺️ Diagrama de Flujo del Proceso (PFD)")
    st.info("💡 **Guía de Navegación:** Utilice la 'Matriz Operativa' del panel izquierdo para ingresar a cada bloque específico de ingeniería, modificar las aperturas de válvulas de control o alterar los escenarios dinámicos del yacimiento.")

elif seccion == "Separación de Entrada":
    # Ejecuta el motor hidrodinámico de separación (El Pozo Ilustrado)
    p_op, t_op, niv_op = render_separacion()
    # Actualiza los estados globales para que los otros módulos lean los desvíos en vivo
    st.session_state['p_entrada'] = p_op
    st.session_state['t_entrada'] = t_op
    st.session_state['nivel_liquido'] = niv_op

elif seccion == "Planta Criogénica y LGN":
    # Pasa las condiciones de entrada actuales para calcular el enfriamiento por expansión isentrópica
    render_procesamiento(st.session_state['p_entrada'], st.session_state['t_entrada'])

elif seccion == "Calidad y Medición (ENARGAS)":
    # Evalúa el cumplimiento normativo de la transferencia de custodia
    render_calidad_medicion()

elif seccion == "Servicios Auxiliares & IIoT":
    # Despliega el módulo predictivo basado en LoRaWAN para el equipo de bombeo
    render_servicios()

elif seccion == "Guías Rápidas de Campo":
    # Despliega el soporte técnico y el glosario bilingüe de Weatherford
    render_guias_rapidas()

elif seccion == "Sistema de Evaluación":
    # Audita las variables de sesión y califica al alumno con Nombre y DNI
    render_evaluacion()
