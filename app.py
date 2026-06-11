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

# Control de acceso en Session State
if 'autenticado' not in st.session_state: st.session_state['autenticado'] = False
if 'rol' not in st.session_state: st.session_state['rol'] = None

# 1. Variables Base de Entrada y Colector Principal
if 'p_entrada' not in st.session_state: st.session_state['p_entrada'] = 3500.0          # kPa
if 't_entrada' not in st.session_state: st.session_state['t_entrada'] = 22.0            # °C
if 'caudal_gas' not in st.session_state: st.session_state['caudal_gas'] = 5.0           # MMm³/día
if 'nivel_liquido' not in st.session_state: st.session_state['nivel_liquido'] = 45.0     # %
if 'humedad_salida' not in st.session_state: st.session_state['humedad_salida'] = 24.5   # mg/m³
if 'p_descarga_gasoducto' not in st.session_state: st.session_state['p_descarga_gasoducto'] = 6100.0 # kPa

# 2. Variables de Tratamiento, Endulzamiento y Calidad
if 'co2_salida' not in st.session_state: st.session_state['co2_salida'] = 1.5           # % mol
if 't_reboiler_teg' not in st.session_state: st.session_state['t_reboiler_teg'] = 200.0 # °C
if 'tasa_glicol' not in st.session_state: st.session_state['tasa_glicol'] = 3.0         # gal/lb H2O

# 3. Variables Críticas para la Planta Criogénica y Turboexpansión
if 'eficiencia_isentropica' not in st.session_state: st.session_state['eficiencia_isentropica'] = 85.0 # %
if 'rpm_turboexpansor' not in st.session_state: st.session_state['rpm_turboexpansor'] = 22000.0        # RPM
if 'delta_p_coldbox' not in st.session_state: st.session_state['delta_p_coldbox'] = 50.0               # kPa
if 't_separador_frio' not in st.session_state: st.session_state['t_separador_frio'] = -65.0            # °C
if 'caudal_lgn' not in st.session_state: st.session_state['caudal_lgn'] = 120.0                        # m³/día
if 'apertura_asv' not in st.session_state: st.session_state['apertura_asv'] = 0.0                      # % (Válvula Anti-Surge)

# 4. Variables de Fraccionamiento de LGN (Demetanizadora / Deetanizadora)
if 'c2_en_glp' not in st.session_state: st.session_state['c2_en_glp'] = 1.1             # % mol
if 'p_demetanizadora' not in st.session_state: st.session_state['p_demetanizadora'] = 2100.0 # kPa

# 5. Variables de Control Cognitivo e Inyección de Fallas Operativas
if 'falla_surge_activa' not in st.session_state: st.session_state['falla_surge_activa'] = False
if 'falla_hidratos_activa' not in st.session_state: st.session_state['falla_hidratos_activa'] = False
if 'esd_bloqueo_general' not in st.session_state: st.session_state['esd_bloqueo_general'] = False


# =====================================================================
# --- INTERFAZ DE PORTADA INSTITUCIONAL Y SISTEMA DE LOGIN ---
# =====================================================================

def login_usuario(usuario, password):
    if usuario == "admin" and password == "menfa2026":
        st.session_state['autenticado'] = True
        st.session_state['rol'] = "Instructor"
        st.rerun()
    elif usuario == "alumno" and password == "alumno2026":
        st.session_state['autenticado'] = True
        st.session_state['rol'] = "Operador en Entrenamiento"
        st.rerun()
    else:
        st.error("❌ Credenciales incorrectas. Verifique el Usuario o la Clave de Acceso.")

if not st.session_state['autenticado']:
    col_izq, col_centro, col_der = st.columns([1, 5, 1])
    
    with col_centro:
        st.image("logo_menfa.png", width=280)
        st.title("🏭 SUITE INTEGRAL DE SIMULACIÓN DE PLANTAS DE GAS")
        st.subheader("Plataforma Digital de Entrenamiento Avanzado y Control de Procesos")
        
        st.markdown("""
        Bienvenido al entorno virtual de simulación **MENFA**. Esta plataforma ha sido diseñada para la formación 
        y el entrenamiento técnico operativo en procesos de tratamiento, acondicionamiento y fraccionamiento de gas natural.
        
        * **Módulos Operativos:** Separación Líquido-Gas, Endulzamiento por Aminas, Planta Criogénica y Despacho.
        * **Entorno de Aprendizaje:** Enlace directo con guías de campo (SOP) y simulación dinámica de fallas en sala de control.
        """)
        
        st.markdown("---")
        
        with st.container(border=True):
            st.markdown("### 🔐 Control de Acceso al DCS Central")
            input_user = st.text_input("Usuario del Sistema (Legajo):", placeholder="Ej: alumno")
            input_pass = st.text_input("Clave de Seguridad Operativa:", type="password", placeholder="••••••••")
            
            btn_ingresar = st.button("Validar Credenciales e Ingresar", use_container_width=True)
            if btn_ingresar:
                login_usuario(input_user, input_pass)
                
        st.caption("🔒 Acceso restringido. Los intentos de inicio de sesión quedan registrados en la auditoría del servidor.")
    st.stop()


# --- IMPORTACIÓN SEGURA DE LA SUITE MODULAR MENFA (SOLO SI PASÓ EL LOGIN) ---
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

# Muestra el rol autenticado en la barra lateral
st.sidebar.markdown(f"**👤 Perfil:** {st.session_state['rol']}")

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
if st.sidebar.button("🚪 Cerrar Sesión", use_container_width=True):
    st.session_state['autenticado'] = False
    st.session_state['rol'] = None
    st.rerun()

st.sidebar.markdown("---")
if st.session_state['esd_bloqueo_general']:
    st.sidebar.error("🚨 SISTEMA EN PARADA DE EMERGENCIA (ESD)")
else:
    st.sidebar.success("🟢 DCS Planta Operativa en Línea")


# =====================================================================
# --- ENRUTADOR LOGÍSTICO COMPLETO ---
# =====================================================================

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
    if seccion == "Consola SCADA Central":
        st.title("🖥️ Consola Central SCADA - Suite MENFA")
        st.caption("Panel general de supervisión de variables de proceso de producción petrolera y gasífera.")
        st.markdown("---")
        
        if st.session_state['esd_bloqueo_general']:
            st.error("🚨 PARADA DE EMERGENCIA ACTIVA: Todas las plantas se encuentran aisladas y despresurizadas hacia la antorcha.")
        
        nivel_separador = st.session_state.get('nivel_liquido', 45.0)
        temp_criogenica = st.session_state.get('t_separador_frio', -65.0)
        eficiencia_lgn = st.session_state.get('rendimiento_liquidos', 85.0)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Presión Entrada (V-101)", f"{st.session_state['p_entrada']:.1f} kPa")
        col2.metric("Nivel Domo Separador", f"{nivel_separador:.1f} %")
        col3.metric("Humedad Gas de Salida", f"{st.session_state['humedad_salida']:.1f} mg/m³")
        col4.metric("Presión Despacho Troncal", f"{st.session_state['p_descarga_gasoducto']:.1f} kPa")
        
        st.markdown("---")
        
        st.markdown("### 📈 Historial de Tendencias DCS (Línea de Proceso Integral)")
        
        import numpy as np
        import plotly.graph_objects as go
        
        t_eje = np.linspace(0, 24, 50)
        ruido_p = np.sin(t_eje) * 15.0 
        ruido_t = np.cos(t_eje) * 0.8
        
        curva_p = np.full(50, st.session_state['p_entrada']) + ruido_p
        curva_t = np.full(50, temp_criogenica) + ruido_t
        
        fig_scada = go.Figure()
        
        fig_scada.add_trace(go.Scatter(
            x=t_eje, y=curva_p, name="Presión Entrada (kPa)",
            line=dict(color="#00cc96", width=2.5), yaxis="y1"
        ))
        
        fig_scada.add_trace(go.Scatter(
            x=t_eje, y=curva_t, name="Temp. Separador Frío (°C)",
            line=dict(color="#636efa", width=2.5, dash="dash"), yaxis="y2"
        ))
        
        fig_scada.update_layout(
            template="plotly_dark",
            height=320,
            margin=dict(l=40, r=40, t=20, b=20),
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            xaxis=dict(title="Tiempo Operativo Reciente (Horas)", gridcolor="#2d3138"),
            yaxis=dict(title="Presión Base (kPa)", side="left", gridcolor="#2d3138"),
            yaxis2=dict(title="Temperatura (°C)", side="right", overlaying="y", gridcolor="rgba(0,0,0,0)")
        )
        
        st.plotly_chart(fig_scada, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 🗺️ Diagrama de Flujo de Procesos Integral (PFD)")
        st.info("💡 **Guía del Instructor:** Modifique las condiciones de diseño dentro del **Manual Técnico** o altere las perillas de la **Planta Criogénica** para evaluar cómo reaccionan estos indicadores analógicos en tiempo real.")

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
