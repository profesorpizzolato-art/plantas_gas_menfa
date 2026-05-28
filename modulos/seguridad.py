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

    # --- NUEVA UBICACIÓN: PANEL DE INYECCIÓN DE FALLAS EN CUERPO PRINCIPAL ---
    with st.expander("🚨 PANEL DE CONTROL: Inyección de Alarmas para Alumnos", expanded=True):
        st.write("Active las contingencias operativas para evaluar la respuesta automática del sistema:")
        
        # Organizamos los interruptores en columnas para que no ocupen tanto espacio vertical
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.session_state.alarma_hi_p_entrada = st.checkbox(
                "⚠️ Alta Presión Entrada (> 4000 kPa)", value=st.session_state.alarma_hi_p_entrada
            )
            st.session_state.alarma_low_level_separator = st.checkbox(
                "⚠️ Bajo Nivel Separador (< 15%)", value=st.session_state.alarma_low_level_separator
            )
            st.session_state.alarma_vibracion_axial = st.checkbox(
                "🌀 Alta Vibración Axial Compresor (Surge)", value=st.session_state.alarma_vibracion_axial
            )
        with col_f2:
            st.session_state.alarma_hi_hi_p_gasoducto = st.checkbox(
                "🚨 Muy Alta Presión Despacho (> 7400 kPa)", value=st.session_state.alarma_hi_hi_p_gasoducto
            )
            st.session_state.alarma_falla_llama_reboiler = st.checkbox(
                "🔥 Falla de Llama en Reboiler TEG", value=st.session_state.alarma_falla_llama_reboiler
            )
            
            # Botón de reset justo abajo de las alarmas
            if st.button("🔄 Restablecer Matriz (Reset Alarms)", use_container_width=True):
                st.session_state.alarma_hi_p_entrada = False
                st.session_state.alarma_low_level_separator = False
                st.session_state.alarma_hi_hi_p_gasoducto = False
                st.session_state.alarma_falla_llama_reboiler = False
                st.session_state.alarma_vibracion_axial = False
                st.rerun()

    st.markdown("---")

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
        st.info("💡 **Consejo de Clase:** Use el panel desplegable de arriba para activar un desbalance de proceso.")
    else:
        st.error("🔴 DISPARO AUTOMÁTICO DEL SIS - CONDICIÓN DE RIESGO DETECTADA")
        st.warning("⚠️ **Acción Fail-Safe Activada:** Se han disparado los resortes mecánicos de seguridad. Revise el estado en la matriz de abajo.")

    st.markdown("---")

    # --- MATRIZ CAUSA Y EFECTO AUTOMATIZADA ---
    st.subheader("📊 Matriz de Causa y Efecto Automatizada")
    
    matriz_datos = [
        {
            "Variable Iniciadora (Causa)": "Presión Colector de Entrada > 4000 kPa",
            "Lógica Votación": "2oo3",
            "Estado Actual": "🚨 ALARMA" if st.session_state.alarma_hi_p_entrada else "🟢 NORMAL",
            "Actuador Afectado (Efecto)": "SDV-101 (Válvula de Entrada)",
            "Posición Fail-Safe": "CERRAR (Fail-Close)",
            "Acción SIS": "❌ BLOQUEADA" if st.session_state.alarma_hi_p_entrada else "✔️ ABIERTA"
        },
        {
            "Variable Iniciadora (Causa)": "Nivel Líquido Separador < 15%",
            "Lógica Votación": "2oo3",
            "Estado Actual": "🚨 ALARMA" if st.session_state.alarma_low_level_separator else "🟢 NORMAL",
            "Actuador Afectado (Efecto)": "LCV-102 (Línea de Purga)",
            "Posición Fail-Safe": "CERRAR (Fail-Close)",
            "Acción SIS": "❌ CORTE TOTAL" if st.session_state.alarma_low_level_separator else "✔️ REGULANDO"
        },
        {
            "Variable Iniciadora (Causa)": "Presión Despacho Gasoducto > 7400 kPa",
            "Lógica Votación": "2oo3",
            "Estado Actual": "🚨 ALARMA" if st.session_state.alarma_hi_hi_p_gasoducto else "🟢 NORMAL",
            "Actuador Afectado (Efecto)": "SDV-501 (Troncal) + BDV-502",
            "Posición Fail-Safe": "SDV Cierra / BDV Abre",
            "Acción SIS": "💥 EVACUACIÓN" if st.session_state.alarma_hi_hi_p_gasoducto else "✔️ DESPACHANDO"
        },
        {
            "Variable Iniciadora (Causa)": "Falla de Llama en Quemador (Reboiler)",
            "Lógica Votación": "1oo2",
            "Estado Actual": "🚨 ALARMA" if st.session_state.alarma_falla_llama_reboiler else "🟢 NORMAL",
            "Actuador Afectado (Efecto)": "XV-301 (Gas Combustible)",
            "Posición Fail-Safe": "CERRAR (Fail-Close)",
            "Acción SIS": "❌ CORTE GAS" if st.session_state.alarma_falla_llama_reboiler else "✔️ IGNICIÓN OK"
        },
        {
            "Variable Iniciadora (Causa)": "Vibración Axial Extrema en Rodete",
            "Lógica Votación": "2oo2",
            "Estado Actual": "🚨 ALARMA" if st.session_state.alarma_vibracion_axial else "🟢 NORMAL",
            "Actuador Afectado (Efecto)": "ESD Tren de Compresión",
            "Posición Fail-Safe": "PARADA DE EMERGENCIA",
            "Acción SIS": "❌ TRIP TURBINA" if st.session_state.alarma_vibracion_axial else "✔️ EN TRABAJO"
        }
    ]

    df_matriz = pd.DataFrame(matriz_datos)
    st.dataframe(df_matriz, use_container_width=True, hide_index=True)

    # --- ANALISIS PEDAGÓGICO DINÁMICO ---
    if hay_emergencia:
        st.markdown("---")
        st.subheader("🔍 Análisis Técnico de la Célula de Seguridad")
        
        if st.session_state.alarma_hi_hi_p_gasoducto:
            st.error("👉 **Análisis NAG-125:** Al superar los 7400 kPa, se ejecuta un ESD de la línea de transporte. La SDV de despacho aísla la planta para proteger la cañería externa de una sobrepresión mecánica destructiva, y las BDV abren para aliviar el inventario interno hacia la antorcha.")
        if st.session_state.alarma_vibracion_axial:
            st.warning("👉 **Análisis de Compresión:** El aumento crítico en la vibración axial indica inestabilidad aerodinámica (Surge). El sistema instrumentado detiene la turbina de inmediato para evitar que el flujo retrógrado destruya los cojinetes de empuje.")
        if st.session_state.alarma_falla_llama_reboiler:
            st.info("👉 **Análisis Térmico:** Si el sensor óptico o la termocupla detectan pérdida de llama, el enclavamiento interrumpe el paso de gas combustible por la solenoide (XV-301) para evitar la acumulación de mezclas explosivas en el hogar del reboiler.")
