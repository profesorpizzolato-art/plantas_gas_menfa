# modulos/seguridad.py
import streamlit as st
import pandas as pd

def render_seguridad():
    st.header("🛡️ Matriz de Enclavamientos de Seguridad (SIS / NAG-125)")
    st.caption("Consola interactiva para la simulación de disparos por Parada de Emergencia (ESD) y Control de Eventos (CDE).")
    st.markdown("---")

    # --- INICIALIZACIÓN DE ALARMAS EN EL ESTADO DE SESIÓN ---
    if 'alarma_hi_p_entrada' not in st.session_state:
        st.session_state.alarma_hi_p_entrada = False
    if 'alarma_low_level_separator' not in st.session_state:
        st.session_state.alarma_low_level_separator = False
    if 'alarma_hi_hi_p_gasoducto' not in st.session_state:
        st.session_state.alarma_hi_hi_p_gasoducto = False
    if 'alarma_falla_llama_reboiler' not in st.session_state:
        st.session_state.alarma_falla_llama_reboiler = False
    if 'alarma_vibracion_axial' not in st.session_state:
        st.session_state.alarma_vibracion_axial = False

    # --- PANEL DE INYECCIÓN DE FALLAS (SOLO PARA ALUMNOS / INSTRUCTORES) ---
    st.sidebar.markdown("### 🚨 Inyección de Alarmas (Simulador)")
    st.sidebar.caption("Active una o más contingencias operativas para evaluar la respuesta de la matriz:")
    
    st.session_state.alarma_hi_p_entrada = st.sidebar.checkbox("⚠️ Alta Presión Entrada (>4000 kPa)", value=st.session_state.alarma_hi_p_entrada)
    st.session_state.alarma_low_level_separator = st.sidebar.checkbox("⚠️ Bajo Nivel Separador (<15%)", value=st.session_state.alarma_low_level_separator)
    st.session_state.alarma_hi_hi_p_gasoducto = st.sidebar.checkbox("🚨 Muy Alta Presión Despacho (>7400 kPa)", value=st.session_state.alarma_hi_hi_p_gasoducto)
    st.session_state.alarma_falla_llama_reboiler = st.sidebar.checkbox("🔥 Falla de Llama en Reboiler TEG", value=st.session_state.alarma_falla_llama_reboiler)
    st.session_state.alarma_vibracion_axial = st.sidebar.checkbox("🌀 Alta Vibración Axial Compresor (Surge)", value=st.session_state.alarma_vibracion_axial)

    if st.sidebar.button("🔄 Restablecer Matriz (Reset Alarms)", use_container_width=True):
        st.session_state.alarma_hi_p_entrada = False
        st.session_state.alarma_low_level_separator = False
        st.session_state.alarma_hi_hi_p_gasoducto = False
        st.session_state.alarma_falla_llama_reboiler = False
        st.session_state.alarma_vibracion_axial = False
        st.rerun()

    # --- EVALUACIÓN DE ESTADO GENERAL DE LA PLANTA ---
    alarmas_activas = [
        st.session_state.alarma_hi_p_entrada,
        st.session_state.alarma_low_level_separator,
        st.session_state.alarma_hi_hi_p_gasoducto,
        st.session_state.alarma_falla_llama_reboiler,
        st.session_state.alarma_vibracion_axial
    ]

    hay_emergencia = any(alarmas_activas)

    # Banner de Estado Dinámico
    if not hay_emergencia:
        st.success("🟢 SISTEMA DE ENCLAVAMIENTO EN LÍNEA - SIN ALARMAS ACTIVAS")
        st.info("💡 **Consejo de Clase:** Diríjase al panel lateral 'Inyección de Alarmas' para simular un desbalance de proceso.")
    else:
        st.error("🔴 DISPARO AUTOMÁTICO DEL SIS - CONDICIÓN DE RIESGO DETECTADA")
        st.warning("⚠️ **Acción Fail-Safe Activada:** Se han disparado los resortes mecánicos de seguridad. Revisar la matriz de causa y efecto abajo.")

    st.markdown("---")

    # --- LÓGICA DE DETALLE: MATRIZ CAUSA Y EFECTO (2oo3 / NAG-125) ---
    st.subheader("📊 Matriz de Causa y Efecto Automatizada")
    st.write("Esta tabla simula las acciones lógicas que ejecuta el PLC de Seguridad de forma desacoplada al DCS operativo:")

    # Construcción dinámica de las filas de la matriz
    matriz_datos = [
        {
            "Variable Iniciadora (Causa)": "Presión Colector de Entrada > 4000 kPa",
            "Lógica Votación": "2oo3",
            "Estado Actual": "🚨 ALARMA ACTIVA" if st.session_state.alarma_hi_p_entrada else "🟢 NORMAL",
            "Actuador Afectado (Efecto)": "SDV-101 (Válvula de Entrada)",
            "Posición Fail-Safe": "CERRAR (Fail-Close)",
            "Acción SIS": "❌ BLOQUEADA" if st.session_state.alarma_hi_p_entrada else "✔️ ABIERTA"
        },
        {
            "Variable Iniciadora (Causa)": "Nivel Líquido Separador < 15%",
            "Lógica Votación": "2oo3",
            "Estado Actual": "🚨 ALARMA ACTIVA" if st.session_state.alarma_low_level_separator else "🟢 NORMAL",
            "Actuador Afectado (Efecto)": "LCV-102 (Línea de Purga)",
            "Posición Fail-Safe": "CERRAR (Fail-Close)",
            "Acción SIS": "❌ CORTE TOTAL" if st.session_state.alarma_low_level_separator else "✔️ REGULANDO"
        },
        {
            "Variable Iniciadora (Causa)": "Presión Despacho Gasoducto > 7400 kPa",
            "Lógica Votación": "2oo3",
            "Estado Actual": "🚨 ALARMA ACTIVA" if st.session_state.alarma_hi_hi_p_gasoducto else "🟢 NORMAL",
            "Actuador Afectado (Efecto)": "SDV-501 (Troncal) + BDV-502",
            "Posición Fail-Safe": "SDV Cierra / BDV Abre",
            "Acción SIS": "💥 EVACUACIÓN A ANTORCHA" if st.session_state.alarma_hi_hi_p_gasoducto else "✔️ DESPACHANDO"
        },
        {
            "Variable Iniciadora (Causa)": "Falla de Llama en Quemador (Reboiler)",
            "Lógica Votación": "1oo2",
            "Estado Actual": "🚨 ALARMA ACTIVA" if st.session_state.alarma_falla_llama_reboiler else "🟢 NORMAL",
            "Actuador Afectado (Efecto)": "XV-301 (Gas Combustible)",
            "Posición Fail-Safe": "CERRAR (Fail-Close)",
            "Acción SIS": "❌ CORTE DE GAS" if st.session_state.alarma_falla_llama_reboiler else "✔️ IGNICIÓN OK"
        },
        {
            "Variable Iniciadora (Causa)": "Vibración Axial Extrema en Rodete",
            "Lógica Votación": "2oo2",
            "Estado Actual": "🚨 ALARMA ACTIVA" if st.session_state.alarma_vibracion_axial else "🟢 NORMAL",
            "Actuador Afectado (Efecto)": "ESD Tren de Compresión",
            "Posición Fail-Safe": "PARADA DE EMERGENCIA",
            "Acción SIS": "❌ TRIP DE TURBINA" if st.session_state.alarma_vibracion_axial else "✔️ EN CLASE"
        }
    ]

    df_matriz = pd.DataFrame(matriz_datos)
    
    # Renderizado estético usando dataframe nativo de streamlit configurado a pantalla completa
    st.dataframe(df_matriz, use_container_width=True, hide_index=True)

    # --- SECCIÓN PEDAGÓGICA INTERACTIVA ---
    if hay_emergencia:
        st.markdown("---")
        st.subheader("🔍 Análisis de Célula de Seguridad")
        
        # Le explicamos dinámicamente al alumno qué pasó según el switch que activó
        if st.session_state.alarma_hi_hi_p_gasoducto:
            st.error("👉 **Caso Crítico - Despresurización Directa (NAG-125):** Al activarse la alarma de Presión de Despacho, se inició un **ESD Nivel 1**. La Válvula de Bloqueo Troncal se cerró para no reventar el gasoducto comercial, y las BDV abrieron de forma automática enviando el inventario remanente hacia la antorcha para despresurizar el sistema en minutos.")
            
        if st.session_state.alarma_vibracion_axial:
            st.warning("👉 **Caso Crítico - Fenómeno de Surge Compresor:** La vibración axial del eje indica que la contrapresión venció la inercia aerodinámica del rodete. El SIS intervino de inmediato apagando la turbina antes de que el flujo retrógrado rompa los cojinetes basculantes (*Tilting Pad Bearings*).")
            
        if st.session_state.alarma_falla_llama_reboiler:
            st.info("👉 **Caso de Seguridad Térmica:** Sin llama detectada en el tubo de fuego, continuar inyectando gas combustible generaría una atmósfera explosiva dentro del reboiler de TEG. El enclavamiento corta de raíz el suministro mecánico.")
