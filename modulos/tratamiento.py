# modulos/tratamiento.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render_treatment(p_entrada, t_entrada):
    st.header("💧 Módulo de Proceso: Deshidratación por Trietilenglicol (TEG)")
    st.caption("Simulación hidrodinámica del contacto interfacial gas/solvente y tren de regeneración térmica.")
    st.markdown("---")

    # --- PANEL DE OPERACIÓN (CONTROLES DE ALUMNO) ---
    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns(3)
    
    with col_ctrl1:
        st.markdown("##### 🌀 Torre Contactora")
        tasa_circ = st.slider("Tasa de Circulación (gal TEG / lb H2O):", 1.0, 5.0, 2.5, step=0.1, help="Estándar industrial: 1.5 a 3.0 gal/lb.")
        t_glicol_in = st.slider("Temperatura Glicol Pobre Entrada (°C):", 15.0, 60.0, 25.0, step=1.0)
        
    with col_ctrl2:
        st.markdown("##### 🔥 Tren de Regeneración")
        # El alumno controla el setpoint del quemador (TIC)
        sp_reboiler = st.slider("Setpoint Temperatura Reboiler (°C):", 170.0, 210.0, 198.0, step=0.5)
        stripping_gas = st.toggle("Inyectar Stripping Gas (Gas de Despojamiento)", value=False, help="Reduce la presión parcial del agua en el reboiler para máxima pureza.")

    with col_ctrl3:
        st.markdown("##### 🚨 Simulación de Fallas")
        foaming_activo = st.checkbox("Simular Espumado (Foaming)", value=False, help="Inyecta contaminantes para alterar la tensión interfacial del solvente.")

    st.markdown("---")

    # --- LÓGICA MATEMÁTICA Y TERMODINÁMICA (DIALNET / INSTRUMENTATION) ---
    # 1. Determinación de la eficiencia de regeneración (Pureza del TEG pobre)
    pureza_base = 98.5 + ((sp_reboiler - 170.0) * 0.04)
    if stripping_gas:
        pureza_base += 0.8  # El stripping gas eleva la concentración al remover trazas finales de agua
    pureza_teg = min(float(pureza_base), 99.99)

    # 2. Lógica de Enclavamiento SIS por temperatura límite del glicol
    # A 204°C el TEG sufre degradación térmica irreversible
    sis_tripped = sp_reboiler >= 204.0 
    t_reboiler_real = 15.0 if sis_tripped else sp_reboiler

    # 3. Cálculo dinámico de la Humedad de Salida (Equilibrio Líquido-Vapor)
    # A mayor tasa de circulación y mayor pureza, menor humedad residual
    if sis_tripped:
        # Sin fuego en el reboiler, el glicol se satura de agua inmediatamente y pierde eficiencia
        humedad_calculada = 140.0 + (t_entrada * 0.5)
    else:
        humedad_ideal = 110.0 / (tasa_circ * (pureza_teg - 97.0))
        # El espumado rompe el contacto interfacial provocando arrastre por cabeza (Carry-over)
        factor_foaming = 4.5 if foaming_activo else 1.0
        # Variación por temperatura de entrada del gas
        humedad_calculada = humedad_ideal * factor_foaming * (1.0 + (t_entrada - 20.0) * 0.03)

    # 4. Cálculo de Caída de Presión (ΔP) en la torre
    dp_base = 15.0 + (tasa_circ * 2.1)
    if foaming_activo:
        dp_base += 45.0  # El espumado obstruye mecánicamente los platos o empaques de la torre
    dp_torre = float(dp_base)

    # --- EXPOSICIÓN DE RESULTADOS (METRICS) ---
    st.subheader("📊 Indicadores de Instrumentación en Tiempo Real")
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    
    col_m1.metric("Humedad de Salida", f"{humedad_calculada:.1f} mg/m³", 
                  delta="FUERA DE NORMA" if humedad_calculada > 64.0 else "DENTRO DE NORMA",
                  delta_color="inverse" if humedad_calculada > 64.0 else "normal")
    
    col_m2.metric("Pureza TEG Pobre", f"{pureza_teg:.2f} %", help="La pureza requerida depende del punto de rocío objetivo.")
    
    col_m3.metric("ΔP Torre Contactora", f"{dp_torre:.1f} kPa",
                  delta="PRESIÓN CRÍTICA" if dp_torre > 40.0 else "NORMAL",
                  delta_color="inverse" if dp_torre > 40.0 else "normal")
    
    if sis_tripped:
        col_m4.metric("Estado Quemador", "❌ SHUTDOWN", delta="SIS: TRIPPED (>204°C)", delta_color="inverse")
    else:
        col_m4.metric("Estado Quemador", "🔥 ACTIVO", delta=f"TIC Set: {sp_reboiler}°C")

    # --- ALERTAS DINÁMICAS (LÓGICA COGNITIVA) ---
    if sis_tripped:
        st.error("🚨 **INTERLOCK ACTIVADO (NAG-125):** El transmisor de temperatura (TT) del reboiler superó el límite crítico de degradación térmica del TEG ($204^\\circ\\text{C}$). El PLC de seguridad cerró la válvula solenoide (XV) de gas combustible. La planta ya no deshidrata eficientemente.")
    
    if foaming_activo:
        st.warning("⚠️ **ANOMALÍA DETECTADA - ESPUMADO EN CURSO:** La alta presión diferencial ($\Delta P$) combinada con la pérdida súbita de calidad de gas confirma la presencia de espuma en los platos. *Acción requerida:* Dosificar antiespumante siliconado inmediatamente.")

    # --- PANEL GRÁFICO: SENSIBILIDAD DE LA TASA DE INYECCIÓN ---
    st.markdown("### 📈 Curva de Operación: Humedad vs Inyección")
    
    tasas_eje = np.linspace(1.2, 4.8, 50)
    if sis_tripped:
        humedades_eje = [float(humedad_calculada)] * len(tasas_eje)
    else:
        factor_foaming = 4.5 if foaming_activo else 1.0
        humedades_eje = [float((110.0 / (t * (pureza_teg - 97.0))) * factor_foaming * (1.0 + (t_entrada - 20.0) * 0.03)) for t in tasas_eje]

    fig_teg = go.Figure()
    fig_teg.add_trace(go.Scatter(x=[float(t) for t in tasas_eje], y=humedades_eje, mode='lines', name='Respuesta de Planta', line=dict(color='#00CC96', width=3)))
    fig_teg.add_trace(go.Scatter(x=[float(tasa_circ)], y=[float(humedad_calculada)], mode='markers', name='Punto Operativo Actual', marker=dict(color='white', size=12, symbol='square')))
    # Línea límite normativa de transporte (64 mg/m³)
    fig_teg.add_trace(go.Scatter(x=[1.2, 4.8], y=[64.0, 64.0], mode='lines', name='Límite NAG (64 mg/m³)', line=dict(color='red', dash='dash')))

    fig_teg.update_layout(
        xaxis_title="Tasa de Inyección (gal/lb)", yaxis_title="Humedad Residual (mg/m³)",
        template="plotly_dark", height=300, margin=dict(l=20, r=20, t=20, b=20)
    )
    st.plotly_chart(fig_teg, use_container_width=True)

    # Retornamos las variables críticas modificadas para actualizar la app.py global
    return float(humedad_calculada), float(t_reboiler_real)
