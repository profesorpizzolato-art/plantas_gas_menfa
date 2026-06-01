# modulos/transporte.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render_transporte():
    st.header("🌀 Módulo de Proceso: Estaciones de Turbocompresión y Despacho")
    st.caption("Simulación hidrodinámica de compresión centrífuga y control de entrega a gasoductos troncales.")
    st.markdown("---")

    # Tomamos la presión de la planta para que interactúe con el resto del sistema
    p_succion_sistema = st.session_state.p_entrada  # kPa

    # --- PANEL DE CONTROL DE OPERACIONES (CONTROLES DEL ALUMNO) ---
    col_c1, col_c2, col_c3 = st.columns(3)
    
    with col_c1:
        st.markdown("##### ⚙️ Parámetros de la Máquina")
        rpm_solicitadas = st.slider("Velocidad de la Turbina (RPM):", 6000, 12000, 9500, step=100)
        caudal_solicitado = st.slider("Caudal de Despacho Solicitado (m³/h):", 1500, 8500, 5000, step=100)
        
    with col_c2:
        st.markdown("##### ❄️ Auxiliares e Intercoolers")
        t_succion_manual = st.slider("Temperatura Succión Gas (°C):", 15.0, 65.0, 28.0, step=1.0,
                                     help="Regulada por los aeroenfriadores de entrada. Afecta directamente la densidad del gas.")
        lazo_antisurge = st.toggle("Habilitar Lazo de Control Anti-Surge", value=False,
                                   help="Lazo automático que abre la válvula de reciclo (ASV) para proteger el rodete.")

    with col_c3:
        st.markdown("##### 🚧 Restricciones de Cañería")
        p_backpressure = st.slider("Contrapresión del Gasoducto Comercial (kPa):", 5500, 7800, 6200, step=50,
                                   help="Presión aguas abajo impuesta por la línea troncal de transporte.")

    st.markdown("---")

    # --- MOTOR MATEMÁTICO DE COMPRESIÓN CENTRÍFUGA (PLANTAS COMPRESORAS) ---
    
    # Si el lazo anti-surge está activo y estamos en zona de bajo caudal, abre la ASV
    apertura_asv = 0.0
    caudal_efectivo_rodete = float(caudal_solicitado)
    
    if lazo_antisurge and caudal_solicitado < 3000:
        # Abre la válvula proporcionalmente para sostener un caudal mínimo seguro en el rodete
        apertura_asv = float(((3000 - caudal_solicitado) / 1500) * 100)
        apertura_asv = min(apertura_asv, 100.0)
        caudal_efectivo_rodete += (apertura_asv * 20.0)  # Gas reciclado inyectado

    # Cálculo de la Relación de Compresión (Rc) teórica basada en RPM
    # Rc = P_descarga / P_succion
    rc_base = 1.1 + ((rpm_solicitadas - 6000) * 0.0002)
    # Pérdida por exceso de caudal (efecto Choke / Stone Wall)
    if caudal_efectivo_rodete > 7500:
        rc_base -= ((caudal_efectivo_rodete - 7500) * 0.00015)
        
    p_descarga_calculada = p_succion_sistema * rc_base

    # Influencia de la contrapresión del gasoducto comercial
    if p_descarga_calculada < p_backpressure:
        # El compresor no tiene fuerza para empujar, el gas se frena (Camino directo al Surge)
        p_descarga_real = p_backpressure
        vibracion_surge_factor = (p_backpressure - p_descarga_calculada) * 0.08
    else:
        p_descarga_real = p_descarga_calculada
        vibracion_surge_factor = 0.0

    # Modelado de Vibración Axial del Eje (Milésimas de pulgada - mils)
    vibracion_base = 0.8 + (rpm_solicitadas / 12000) * 0.5
    # Incremento violento si el caudal en el rodete cae por debajo del límite hidrodinámico
    if caudal_efectivo_rodete < 2800:
        vibracion_base += ((2800 - caudal_efectivo_rodete) * 0.0025) ** 2
    vibracion_axial = float(vibracion_base + vibracion_surge_factor)

    # Cálculo Termodinámico de la Potencia Requerida (BHP)
    # A mayor temperatura de succión, el gas es menos denso, requiere más energía para comprimirse
    factor_temperatura = 1.0 + ((t_succion_manual - 20.0) * 0.006)
    potencia_bhp = (caudal_efectivo_rodete * (rc_base - 1) * 0.45) * factor_temperatura
    if lazo_antisurge:
        potencia_bhp += (apertura_asv * 5.0) # El reciclo consume potencia extra de arrastre

    # Lógica de Disparo SIS (Trip de Turbina) por Vibración Crítica
    turbina_tripped = vibracion_axial >= 4.5
    if turbina_tripped:
        p_descarga_real = p_succion_sistema  # Al apagarse, las presiones se igualan a través de las líneas
        potencia_bhp = 0.0
        vibracion_axial = 0.2

    # --- VISUALIZACIÓN DE MÉTRICAS (CONSOLA DE INSTRUMENTACIÓN) ---
    st.subheader("📊 Consola de Medición y Control de la Estación")
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    
    col_m1.metric("Presión de Despacho", f"{p_descarga_real:.1f} kPa", 
                  delta=f"Rc: {rc_base:.2f}", delta_color="normal" if not turbina_tripped else "off")
    
    col_m2.metric("Potencia Absorbida", f"{potencia_bhp:.1f} BHP",
                  delta=f"Efecto T_in: +{((factor_temperatura-1)*100):.1f}%" if potencia_bhp > 0 else "APAGADO",
                  delta_color="inverse")
    
    col_m3.metric("Vibración Axial Eje", f"{vibracion_axial:.2f} mils",
                  delta="CRÍTICA (TRIP)" if vibracion_axial > 4.0 else "DENTRO DE LÍMITES",
                  delta_color="inverse" if vibracion_axial > 3.0 else "normal")
    
    if lazo_antisurge:
        col_m4.metric("Válvula Anti-Surge (ASV)", f"{apertura_asv:.1f} %", delta="BYPASS ACTIVO" if apertura_asv > 0 else "CERRADA")
    else:
        col_m4.metric("Lazo Anti-Surge", "❌ DESACTIVADO", delta="RIESGO DE BOMBEO", delta_color="inverse")

    # --- ALERTAS COGNITIVAS OPERATIVAS ---
    if turbina_tripped:
        st.error("🚨 **TRIP DE TURBOCOMPRESOR (NAG-125):** Se detectó un valor de vibración axial destructivo ($>4.5\\text{ mils}$). El lazo instrumentado de seguridad ejecutó un enclavamiento de emergencia deteniendo el motor principal para evitar el rozamiento mecánico de los álabes contra la carcasa.")
    elif vibracion_axial >= 3.2:
        st.warning("⚠️ **PRE-ALARMA DE SURGE (BOMBEO AERODINÁMICO):** El compresor se encuentra operando muy cerca de su límite izquierdo. El caudal es insuficiente para vencer la contrapresión del gasoducto. *Acción sugerida:* Suba las RPM o active el Lazo Anti-Surge.")

    if t_succion_manual > 45.0 and not turbina_tripped:
        st.info("💡 **Lección de Eficiencia Térmica:** Note cómo al ingresar el gas caliente ($>45^\\circ\\text{C}$), la potencia requerida se dispara. Esto ocurre porque el fluido se expande y el compresor debe realizar mucho más trabajo mecánico para desplazar la misma masa de gas.")

    # --- MAPA DINÁMICO DE PERFORMANCE INTERACTIVO ---
    st.markdown("### 📈 Mapa de Performance del Turbocompresor en Tiempo Real")
    
    flow_axis = np.linspace(1500, 8500, 100)
    # Generamos la curva característica real de la máquina según las RPM elegidas
    rc_curve = 1.1 + ((rpm_solicitadas - 6000) * 0.0002) - ((flow_axis - 4000)**2 / 12000000)
    
    fig_transporte = go.Figure()
    # Zona de Surge Fija
    fig_transporte.add_trace(go.Scatter(x=[2800, 2800], y=[1.0, 2.5], mode='lines', name='Límite de Surge', line=dict(color='red', width=3, dash='dash')))
    # Curva de comportamiento dinámica
    fig_transporte.add_trace(go.Scatter(x=[float(f) for f in flow_axis], y=[float(r) for r in rc_curve], mode='lines', name=f'Curva de Trabajo a {rpm_solicitadas} RPM', line=dict(color='#00CC96', width=3)))
    
    # Punto operativo real del rodete
    if not turbina_tripped:
        rc_actual = float(p_descarga_real / p_succion_sistema)
        fig_transporte.add_trace(go.Scatter(x=[float(caudal_efectivo_rodete)], y=[rc_actual], mode='markers', name='Punto Operativo Actual', marker=dict(color='white', size=14, symbol='diamond')))

    fig_transporte.update_layout(
        xaxis_title="Caudal en el Rodete (m³/h)", yaxis_title="Relación de Compresión (Rc)",
        template="plotly_dark", height=320, margin=dict(l=20, r=20, t=20, b=20)
    )
    st.plotly_chart(fig_transporte, use_container_width=True)

    # Retornamos la presión de descarga calculada para actualizar la sesión global de app.py
    return float(p_descarga_real)
