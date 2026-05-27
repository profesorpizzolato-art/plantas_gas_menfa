# modulos/cognitivo.py
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import config as cfg
import time

def render_cognitivo():
    st.header("🧠 Pilar 4: Simulador de Entrenamiento Cognitivo Operacional")
    st.caption("Consola interactiva de entrenamiento bajo presión y resolución de contingencias críticas en tiempo real.")

    # --- INICIALIZACIÓN DE ESTADOS DE SESIÓN (PERSISTENCIA DE SIMULACIÓN) ---
    if "escenario_actual" not in st.session_state:
        st.session_state.escenario_actual = "A: Planta Estable en Régimen Nominal"
    if "tiempo_simulado" not in st.session_state:
        st.session_state.tiempo_simulado = 0
    if "historial_presion" not in st.session_state:
        st.session_state.historial_presion = [3200.0]
    if "historial_nivel" not in st.session_state:
        st.session_state.historial_nivel = [42.0]
    if "historial_temp" not in st.session_state:
        st.session_state.historial_temp = [182.0]
    if "sistema_bloqueado" not in st.session_state:
        st.session_state.sistema_bloqueado = False
    if "bypass_alarma" not in st.session_state:
        st.session_state.bypass_alarma = False

    # --- SELECCIÓN DE ESCENARIO ---
    escenario_seleccionado = st.selectbox(
        "Seleccione la contingencia operativa a evaluar:", 
        [
            "A: Planta Estable en Régimen Nominal",
            "B: Arrastre Masivo de Líquidos (Tapón Hidráulico en Gasoducto)",
            "C: Descontrol Térmico en Reboiler de Regeneración de Glicol"
        ]
    )

    # Si el operador cambia el escenario en el combo, reiniciamos las variables de simulación
    if escenario_seleccionado != st.session_state.escenario_actual:
        st.session_state.escenario_actual = escenario_seleccionado
        st.session_state.tiempo_simulado = 0
        st.session_state.historial_presion = [3200.0]
        st.session_state.historial_nivel = [42.0]
        st.session_state.historial_temp = [182.0]
        st.session_state.sistema_bloqueado = False
        st.session_state.bypass_alarma = False
        st.rerun()

    # --- BOTÓN DE AVANCE TEMPORAL (Simula el paso del tiempo en el turno) ---
    st.markdown("### ⏱️ Control del Tiempo del Turno")
    col_t1, col_t2 = st.columns([1, 3])
    with col_t1:
        if st.button("⏳ Avanzar Turno (+5 Minutos)", use_container_width=True):
            if not st.session_state.sistema_bloqueado:
                st.session_state.tiempo_simulado += 5
    with col_t2:
        st.info(f"Tiempo transcurrido en la guardia actual: **{st.session_state.tiempo_simulado} minutos**.")

    # --- LÓGICA MATEMÁTICA EVOLUTIVA DEL PROCESO ---
    t = st.session_state.tiempo_simulado
    
    if not st.session_state.sistema_bloqueado:
        if st.session_state.escenario_actual == "B: Arrastre Masivo de Líquidos (Tapón Hidráulico en Gasoducto)":
            # La presión y el nivel suben exponencialmente con el tiempo si no se actúa
            p_actual = 3200.0 + (t * 65.0)
            n_actual = 42.0 + (t * 1.1)
            t_actual = 182.0 + np.sin(t) * 2
            
            # Verificación automática de disparo por interlock físico (NAG-125) si no hay bypass
            if (p_actual >= cfg.PRESION_MAX_PLANTA or n_actual >= cfg.NIVEL_MAX_SEPARADOR) and not st.session_state.bypass_alarma:
                st.session_state.sistema_bloqueado = True
                p_actual = 1200.0  # Alivio automático por antorcha (Vent)
                n_actual = min(100.0, n_actual) # El líquido se retiene
                st.toast("🚨 ¡DISPARO AUTOMÁTICO POR INTERLOCK DE SEGURIDAD (CDE)!", icon="🚨")
                
        elif st.session_state.escenario_actual == "C: Descontrol Térmico en Reboiler de Regeneración de Glicol":
            p_actual = 3200.0 + np.sin(t) * 10
            n_actual = 42.0 + np.cos(t) * 0.5
            t_actual = 182.0 + (t * 2.5) # Rampa de incremento térmico descontrolado
            
            if t_actual >= cfg.TEMP_MAX_REBOILER and not st.session_state.bypass_alarma:
                st.session_state.sistema_bloqueado = True
                t_actual = 120.0 # Corte automático de combustible al quemador
                st.toast("🚨 ¡SISTEMA BLOQUEADO POR ALTA TEMPERATURA CRÍTICA EN REBOILER!", icon="🚨")
        else:
            # Estado Estable Nominal con ruido blanco normal de proceso
            p_actual = 3200.0 + np.random.uniform(-15, 15)
            n_actual = 42.0 + np.random.uniform(-0.4, 0.4)
            t_actual = 182.0 + np.random.uniform(-1, 1)
            
        # Guardar en las listas históricas de la sesión si varió el tiempo
        if len(st.session_state.historial_presion) <= (t // 5):
            st.session_state.historial_presion.append(p_actual)
            st.session_state.historial_nivel.append(n_actual)
            st.session_state.historial_temp.append(t_actual)
    else:
        # Si está bloqueado, mantiene los últimos valores de resguardo seguros
        p_actual = st.session_state.historial_presion[-1]
        n_actual = st.session_state.historial_nivel[-1]
        t_actual = st.session_state.historial_temp[-1]

    # --- ALERTAS EN TIEMPO REAL ---
    if st.session_state.sistema_bloqueado:
        st.error("🚨 PARADA DE EMERGENCIA DE PLANTA (ESD/CDE) ACTIVADA. Las válvulas automáticas SDV han aislado la instalación. El sistema está seguro, pero la producción comercial está interrumpida.")
    else:
        if st.session_state.escenario_actual == "B: Arrastre Masivo de Líquidos (Tapón Hidráulico en Gasoducto)":
            st.warning("⚠️ ALERTA DE PROCESO: El slug catcher acusa incremento violento en la tasa de llegada de líquidos. El transmisor de presión del colector registra tendencia en alza.")
        elif st.session_state.escenario_actual == "C: Descontrol Térmico en Reboiler de Regeneración de Glicol":
            st.warning("⚠️ ALERTA OPERATIVA: La válvula de control de gas de alimentación al reboiler (TCV) no responde a las señales de cierre del lazo DCS.")

    # --- PANEL DE INSTRUMENTACIÓN VIRTUAL ---
    st.subheader("🎛️ Consola de Instrumentación Digital (Valores de Campo)")
    col1, col2, col3 = st.columns(3)
    
    col1.metric(
        "Presión de Entrada", 
        f"{p_actual:.1f} kPa", 
        delta=f"+{(p_actual-3200):.1f} (CRÍTICO)" if p_actual >= cfg.PRESION_MAX_PLANTA else "Estable",
        delta_color="inverse"
    )
    col2.metric(
        "Nivel del Slug Catcher", 
        f"{n_actual:.1f} %", 
        delta="DISPARO CDE" if n_actual >= cfg.NIVEL_MAX_SEPARADOR else "Normal",
        delta_color="inverse"
    )
    col3.metric(
        "Temperatura del Reboiler", 
        f"{t_actual:.1f} °C", 
        delta="DEGRADACIÓN DE TEG" if t_actual >= cfg.TEMP_MAX_REBOILER else "Normal",
        delta_color="inverse"
    )

    # --- TENDENCIAS GRÁFICAS OPERATIVAS (VISUALIZACIÓN COGNITIVA) ---
    st.markdown("### 📈 Gráficos de Tendencia Histórica (Trend Panel)")
    eje_tiempo = list(range(0, len(st.session_state.historial_presion) * 5, 5))
    
    fig_trends = go.Figure()
    fig_trends.add_trace(go.Scatter(x=eje_tiempo, y=st.session_state.historial_presion, mode='lines+markers', name='Presión Colector (kPa)', line=dict(color='#00CC96', width=3)))
    fig_trends.add_trace(go.Scatter(x=eje_tiempo, y=[cfg.PRESION_MAX_PLANTA]*len(eje_tiempo), mode='lines', name='Límite Máximo Alarma', line=dict(color='red', dash='dash')))
    fig_trends.update_layout(template="plotly_dark", height=260, margin=dict(l=20, r=20, t=20, b=20), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig_trends, use_container_width=True)

    # --- MATRIZ COGNITIVA DE ACCIÓN DE CONTINGENCIA ---
    if st.session_state.escenario_actual != "A: Planta Estable en Régimen Nominal":
        st.markdown("---")
        st.subheader("🤔 Toma de Decisiones y Mitigación de Riesgos")
        
        opciones_operador = [
            "A) Seguir observando las tendencias de la pantalla por 15 minutos para descartar errores instrumentales o falsos positivos.",
            "B) Ejecutar manualmente el Cierre de Emergencia General (ESD) desde la consola para despresurizar la planta y contener los fluidos de forma segura.",
            "C) Puentear (Bypassear) por software el lazo de enclavamiento físico de nivel para evitar que la planta se pare y mantener el flujo comercial."
        ]
        
        decision = st.radio(
            "Como Operador de Panel de Control a cargo del turno, ¿cuál es su acción correctiva inmediata?",
            opciones_operador,
            index=None,
            key=f"decision_{st.session_state.escenario_actual}"
        )
        
        if decision:
            st.markdown("#### 📝 Evaluación del Supervisor de Operaciones:")
            if "Cierre de Emergencia" in decision:
                st.session_state.sistema_bloqueado = True
                # Simulamos la maniobra de mitigación manual exitosa
                st.session_state.historial_presion[-1] = 1200.0  # Alivio inmediato por antorcha
                if st.session_state.escenario_actual == "C":
                    st.session_state.historial_temp[-1] = 140.0 # Enfriamiento por corte de fuego
                
                st.success("""
                🎯 **RESOLUCIÓN COGNITIVA CORRECTA (Excelente Desempeño).** De acuerdo con las directivas de seguridad corporativas y la norma **NAG-125**, ante la inminencia de un daño mecánico catastrófico irreversible (inundación del compresor por bache de líquidos o craqueo térmico del inventario de solvente TEG), la protección de los activos y las personas tiene prioridad absoluta sobre la continuidad del despacho comercial. 
                *Observe cómo al oprimir el ESD, el gráfico y los indicadores de campo registraron el alivio inmediato del peligro.*
                """)
            elif "Bypassear" in decision:
                st.session_state.bypass_alarma = True
                st.error("""
                ❌ **DECISIÓN CRÍTICA INCORRECTA (Infracción de Seguridad Clase 1).**
                Anular o puentear un lazo de seguridad de proceso sin autorización formal de la Jefatura de Planta y de Ingeniería de Procesos viola los lineamientos básicos de la **NAG-125** y el Manual de Seguridad. Forzar la operación en estas condiciones incrementa críticamente el riesgo de reventón de cañerías, explosión en el tren térmico o rotura de álabes en las turbo-unidades aguas abajo.
                """)
            else:
                st.error("""
                ❌ **ERROR DE DIAGNÓSTICO (Inacción ante Riesgo Inminente).**
                En escenarios de evoluciones dinámicas exponenciales (como un tapón hidráulico), esperar 15 minutos consumirá el volumen de amortiguación operativa del slug catcher. La planta llegará al límite crítico sin control, forzando la parada por disparo de hardware de campo de manera violenta e imprevista. Debe actuar con rapidez.
                """)
