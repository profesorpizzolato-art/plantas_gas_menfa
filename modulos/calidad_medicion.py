# modulos/calidad_medicion.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render_calidad_medicion():
    st.header("🛡️ Estación de Medición Fiscal y Control de Calidad (ENARGAS)")
    st.caption("Validación regulatoria de parámetros de transferencia de custodia e inyección a sistemas de transporte troncal.")
    st.markdown("---")

    # Recorremos variables del st.session_state global para evaluar la planta en vivo
    humedad_actual = st.session_state.get('humedad_salida', 24.5)  # mg/m³
    p_despacho = st.session_state.get('p_descarga_gasoducto', 6100.0) # kPa

    # --- PANEL DE CONFIGURACIÓN DEL CONTEXTO ARGENTINO ---
    col_arg1, col_arg2, col_arg3 = st.columns(3)

    with col_arg1:
        st.markdown("##### 🗺️ Procedencia de Inyección")
        cuenca = st.selectbox(
            "Seleccione Cuenca Productora (Firma de Inertes):",
            ["Cuenca Neuquina (Vaca Muerta - Rico)", "Cuenca Austral (Gas de Estrecho)", "Cuenca Noroeste (Alto CO₂ / Inertes)"],
            help="Cada cuenca aporta una composición base de hidrocarburos e inertes que altera el Poder Calorífico."
        )

    with col_arg2:
        st.markdown("##### 🚛 Destino de Transporte")
        gasoducto_destino = st.selectbox(
            "Gasoducto Troncal de Entrega:",
            ["GPNK (Néstor Kirchner - Cabecera Tratayén)", "Gasoducto San Martín (TGS - Sur)", "Gasoducto Norte (TGN - Reversión)"],
            help="Define la presión hidrodinámica obligatoria impuesta por el sistema nacional."
        )

    with col_arg3:
        st.markdown("##### ❄️ Estacionalidad Local")
        estacion = st.radio(
            "Escenario de Demanda Nacional:",
            ["Pico de Invierno (Máximo Caudal / Gas Domiciliario)", "Periodo Estival / Verano (Máxima Extracción de LGN)"],
            help="Altera el foco comercial y las exigencias de volumen sobre la planta."
        )

    st.markdown("---")

    # --- MOTOR MATEMÁTICO DE CALIDAD REGULATORIA ARGENTINA ---
    
    # 1. Definición del Poder Calorífico Superior (PCS) según la Cuenca
    # El gas normado por ENARGAS debe estar entre 8850 y 10200 kcal/m³
    if cuenca == "Cuenca Neuquina (Vaca Muerta - Rico)":
        pcs_base = 9850.0  # Gas rico en etano y propano
        co2_pct = 0.8
    elif cuenca == "Cuenca Austral (Gas de Estrecho)":
        pcs_base = 9400.0
        co2_pct = 1.2
    else:  # Noroeste
        pcs_base = 8650.0  # Fuera de norma inferior si no se trata el CO2/N2
        co2_pct = 4.5      # Alto contenido de inertes

    # 2. Definición del Punto de Rocío de Hidrocarburos (Cricondenterm)
    # Normativa ENARGAS: Máximo -2°C para evitar condensación líquida en la cañería
    # Si la presión del gasoducto es muy alta y no se pasaron los pesados por la Criogénica, condensa
    if p_despacho > 7500.0 and cuenca == "Cuenca Neuquina (Vaca Muerta - Rico)":
        cricondenterm = 1.5  # Condensa hidrocarburos a temperatura de cañería (PELIGRO)
    else:
        cricondenterm = -4.2  # Gas seco y conforme

    # 3. Restricciones Hidrodinámicas por Gasoducto
    if gasoducto_destino == "GPNK (Néstor Kirchner - Cabecera Tratayén)":
        p_requerida_min = 8200.0  # kPa (Línea de alta presión)
        temp_suelo = 12.0
    elif gasoducto_destino == "Gasoducto San Martín (TGS - Sur)":
        p_requerida_min = 5800.0
        temp_suelo = 4.0          # Clima Patagónico extremo
    else: # Norte
        p_requerida_min = 4500.0
        temp_suelo = 20.0

    # --- VALIDACIÓN DE RECHAZOS (EL JUEZ REGULATORIO) ---
    gas_rechazado = False
    motivos_rechazo = []

    # Control de Humedad ENARGAS (Límite: 65 mg/m³)
    if humedad_actual > 65.0:
        gas_rechazado = True
        motivos_rechazo.append(f"❌ CONTENIDO DE AGUA EXCESIVO: Registrado {humedad_actual:.1f} mg/m³ (Límite ENARGAS: 65 mg/m³).")

    # Control de Inyección por Presión de Cabecera
    if p_despacho < p_requerida_min:
        gas_rechazado = True
        motivos_rechazo.append(f"❌ COMPRESIÓN INSUFICIENTE: Presión de planta ({p_despacho:.1f} kPa) no vence la línea del {gasoducto_destino} (Mínimo: {p_requerida_min} kPa).")

    # Control de Calidad Térmica (PCS)
    if pcs_base < 8850.0 or pcs_base > 10200.0:
        gas_rechazado = True
        motivos_rechazo.append(f"❌ PODER CALORÍFICO FUERA DE ESPECIFICACIÓN: {pcs_base:.0f} kcal/m³ (Rango legal: 8850 - 10200).")

    # Control de Hidratos por Punto de Rocío
    if cricondenterm > -2.0:
        gas_rechazado = True
        motivos_rechazo.append(f"❌ PUNTO DE ROCÍO CRÍTICO: Cricondenterm en {cricondenterm}°C (Máximo permitido: -2°C). Riesgo de arrastre líquido en línea.")

    # --- EXPOSICIÓN DE RESULTADOS (CROMATOGRAFÍA Y FISCALIZACIÓN) ---
    st.subheader("📊 Monitoreo del Puente de Medición e Inyección")
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    
    col_m1.metric("Poder Calorífico (PCS)", f"{pcs_base:.0f} kcal/m³", 
                  delta="CONFORME" if (8850 <= pcs_base <= 10200) else "FUERA DE RANGO",
                  delta_color="normal" if (8850 <= pcs_base <= 10200) else "inverse")
    
    col_m2.metric("Punto de Rocío (HC)", f"{cricondenterm:.1f} °C",
                  delta="FUERA DE NORMA" if cricondenterm > -2.0 else "OK",
                  delta_color="inverse" if cricondenterm > -2.0 else "normal")
    
    col_m3.metric("Contenido de Inertes (CO₂)", f"{co2_pct:.1f} %",
                  delta="ALTO" if co2_pct > 2.0 else "BAJO", delta_color="inverse" if co2_pct > 2.0 else "normal")
    
    status_comercial = "🔴 RECHAZADO / CLAUSURADO" if gas_rechazado else "🟢 INYECTANDO A LA RED"
    col_m4.metric("Estatus Comercial ENARGAS", status_comercial)

    # --- CUADRO DE DICTAMEN EMITIDO ---
    if gas_rechazado:
        st.error("### 🚫 ACTA DE RECHAZO DE INYECCIÓN COMERCIAL")
        for motivo in motivos_rechazo:
            st.markdown(motivo)
        st.caption("El centro de despacho nacional (DESNCS) ordenó el cierre de la válvula de bloqueo de cabecera de la planta. Deberá estabilizar el proceso químico o subir las RPM de los turbocompresores para reestablecer la entrega comercial.")
    else:
        st.success(f"### 🤝 GAS CONFORME EN TRANSFERENCIA DE CUSTODIA ({gasoducto_destino})")
        st.markdown(f"La planta se encuentra entregando fluido en especificación comercial bajo las condiciones de **{estacion}**. Todo el volumen despachado está siendo computado para la venta mayorista al sistema interconectado.")

    if estacion == "Pico de Invierno (Máximo Caudal / Gas Domiciliario)":
        st.warning("⚠️ **ALERTA DE CONTEXTO - OPERACIÓN EN PICO DE INVIERNO:** El sistema de transporte nacional está saturado. Se prioriza bombear metros cúbicos brutos para consumo de calefacción domiciliaria. Está prohibido realizar paradas de mantenimiento no programadas.")
    else:
        st.info("💡 **LECCIÓN DE GESTIÓN INDUSTRIAL EN VERANO:** Con el consumo domiciliario en baja, aproveche el espacio sobrante en el gasoducto para forzar al máximo el tren criogénico y optimizar los ingresos mediante la venta de Garrafas de GLP (Propano/Butano).")

    # --- GRÁFICO COMPARATIVO REGULATORIO ---
    st.markdown("### 📈 Gráfico de Control: Humedad vs. Límite Legal ENARGAS")
    
    fig_calidad = go.Figure()
    # Línea límite ENARGAS
    fig_calidad.add_trace(go.Scatter(x=[0, 24], y=[65, 65], mode='lines', name='Límite Máximo ENARGAS (65 mg/m³)', line=dict(color='red', width=3, dash='dash')))
    # Historial de humedad (simulado dinámico a partir de la humedad de la sesión)
    horas = list(range(25))
    historial_humedad = [float(humedad_actual + np.sin(h)*1.5) for h in horas]
    fig_calidad.add_trace(go.Scatter(x=horas, y=historial_humedad, mode='lines+markers', name='Humedad Registrada Planta MENFA', line=dict(color='#00CC96', width=2)))

    fig_calidad.update_layout(
        xaxis_title="Últimas 24 Horas de Marcha (h)", yaxis_title="Humedad del Gas (mg/m³)",
        template="plotly_dark", height=280, margin=dict(l=20, r=20, t=20, b=20)
    )
    st.plotly_chart(fig_calidad, use_container_width=True)
