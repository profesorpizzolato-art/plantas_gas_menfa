# modulos/separacion.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render_separacion():
    st.header("🛢️ Módulo de Entrada: Recepción de Fluidos y Separación Bifásica/Trifásica")
    st.caption("Simulación de las condiciones de producción del Upstream y control de estabilidad del Separador de Primera Etapa (V-101).")
    st.markdown("---")

    # --- PANEL DE CONTROL (ENTRADA DESDE EL YACIMIENTO) ---
    col_pozo, col_vessel, col_quimica = st.columns(3)

    with col_pozo:
        st.markdown("##### 🕳️ Dinámica del Yacimiento")
        mecanismo_empuje = st.selectbox(
            "Mecanismo de Empuje Natural (Subsuelo):",
            ["Empuje por Capa de Gas", "Empuje Hidráulico (Acuífero Activo)", "Gas Disuelto (Depleción)"],
            help="Determina la firma de fluidos y presiones que entrega el yacimiento según 'El Pozo Ilustrado'."
        )
        t_linea_entrada = st.slider("Temperatura de Línea de Producción (°C):", 10.0, 50.0, 22.0, step=1.0)

    with col_vessel:
        st.markdown("##### 🎛️ Control de Presión y Nivel")
        apertura_pcv = st.slider("Apertura Válvula Control Presión (PCV-101) %:", 10.0, 100.0, 55.0, step=0.5,
                                help="Controla la contrapresión interna del recipiente liberando gas hacia tratamiento.")
        apertura_lcv = st.slider("Apertura Válvula Control Líquido (LCV-101) %:", 10.0, 100.0, 48.0, step=0.5,
                                help="Controla el drenaje de líquidos del fondo hacia los tanques de almacenamiento.")

    with col_quimica:
        st.markdown("##### 🧪 Inyección de Tensoactivos")
        quimica_ppm = st.slider("Dosificación de Desemulsificante (ppm):", 0, 50, 0, step=5,
                               help="Química dosificada en la cabeza del separador para romper la tensión interfacial agua-petróleo.")

    st.markdown("---")

    # --- MOTOR HIDRODINÁMICO DEL SEPARADOR (EL POZO ILUSTRADO) ---
    
    # 1. Definición del perfil de fluidos entrantes según el tipo de empuje
    if mecanismo_empuje == "Empuje por Capa de Gas":
        p_llegada_teorica = 4200.0  # kPa
        caudal_gas_in = 8500.0      # m³/h
        caudal_liq_in = 15.0        # m³/h (Predomina gas libre)
        bsw = 5.0                   # % de agua en el líquido
    elif mecanismo_empuje == "Empuje Hidráulico (Acuífero Activo)":
        p_llegada_teorica = 3600.0
        caudal_gas_in = 3800.0
        caudal_liq_in = 55.0        # Gran volumen de líquido aportado por el acuífero
        bsw = 65.0                  # Alto corte de agua
    else:  # Gas Disuelto
        p_llegada_teorica = 2800.0
        caudal_gas_in = 2200.0
        caudal_liq_in = 20.0
        bsw = 12.0

    # 2. Modelado del Fenómeno de Emulsión (Viscosidad y Temperatura)
    # A bajas temperaturas (<20°C) y alto BSW, las emulsiones mecánicas son altamente estables
    emulsión_critica = t_linea_entrada < 20.0 and bsw > 30.0
    
    # Eficiencia de separación afectada por la emulsión y ayudada por la química
    eficiencia_rompimiento = min((quimica_ppm * 2.5) if quimica_ppm > 0 else 0.0, 100.0)
    
    if emulsión_critica and eficiencia_rompimiento < 75.0:
        eficiencia_separacion_fases = 0.4  # Las fases no se separan bien, el agua queda atrapada en el crudo
        viscosidad_aparente = "ALTA (Emulsionado)"
    else:
        eficiencia_separacion_fases = 1.0
        viscosidad_aparente = "NORMAL"

    # 3. Balance de Masa y Dinámica de Presión de Operación
    # Presión = f(Gas de entrada, Gas liberado por la PCV)
    p_operacion = p_llegada_teorica * (caudal_gas_in / 5000.0) * (100.0 / apertura_pcv) * 0.5
    p_operacion = float(np.clip(p_operacion, 800.0, 6500.0))

    # 4. Dinámica del Nivel de Líquido acumulado en el domo inferior
    # Nivel = f(Líquidos que entran, Líquidos drenados por LCV, Pérdida por emulsión)
    nivel_teorico = 45.0 + (caudal_liq_in * 0.8 / eficiencia_separacion_fases) - (apertura_lcv * 0.7)
    nivel_actual = float(np.clip(nivel_teorico, 0.0, 100.0))

    # --- EXPOSICIÓN DE RESULTADOS EN CONSOLA (METRICS) ---
    st.subheader("📊 Panel de Instrumentación del Separador V-101")
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    
    col_m1.metric("Presión Interna Vessel", f"{p_operacion:.1f} kPa", 
                  delta="SOPREPRESIÓN" if p_operacion > 4000.0 else "NORMAL",
                  delta_color="inverse" if p_operacion > 4000.0 else "normal")
    
    col_m2.metric("Nivel de Líquido", f"{nivel_actual:.1f} %",
                  delta="INUNDACIÓN / ALTO ARRASTRE" if nivel_actual > 80.0 else "NORMAL",
                  delta_color="inverse" if nivel_actual > 80.0 else "normal")
    
    col_m3.metric("Viscosidad del Fluido", viscosidad_aparente, 
                  delta=f"BSW Yacimiento: {bsw}%", delta_color="off")
    
    col_m4.metric("Gas Enviado a Planta", f"{(caudal_gas_in * (apertura_pcv/100)):.1f} m³/h")

    # --- ALERTAS OPERATIVAS Y PEDAGÓGICAS ---
    if nivel_actual > 80.0:
        st.error("🚨 **ALTO NIVEL EN SEPARADOR (ESD Nivel 2):** El nivel de líquido superó el límite crítico del 80%. El crudo negro y el agua libre están sufriendo arrastre mecánico superior (*Carry-over*) directo hacia la planta de gas. Esto contaminará fatalmente las torres de glicol en el módulo de Tratamiento.")
    elif emulsión_critica and eficiencia_rompimiento < 75.0:
        st.warning("⚠️ **ANOMALÍA UPSTREAM - EMULSIÓN AGUA-ACEITE DETECTADA:** La baja temperatura de línea ($<20^\\circ\\text{C}$) combinada con el cizallamiento en el choke formó una emulsión estable. Las fases no logran decantar por gravedad. *Acción del operador:* Incremente la dosificación de Desemulsificante de inmediato para romper la tensión superficial.")

    if mecanismo_empuje == "Empuje Hidráulico (Acuífero Activo)":
        st.info("💡 **Lección de Campo (El Pozo Ilustrado):** Al estar conectado a un yacimiento con empuje hidráulico, el pozo produce un volumen de agua libre masivo ($BSW = 65\%$). Esto exige que mantenga la válvula de drenaje (LCV) con mayor apertura para evitar inundar las placas coalescentes.")

    # --- GRÁFICO DINÁMICO: PERFIL DE INTERFAZ DENTRO DEL RECIPIENTE ---
    st.markdown("### 📈 Visualización del Domo Interno y Niveles de Fases")
    
    # Simulación gráfica de los niveles internos (Agua decantada vs Petróleo)
    altura_agua = nivel_actual * (bsw / 100.0) * eficiencia_separacion_fases
    altura_crudo = nivel_actual - altura_agua

    fig_vessel = go.Figure()
    # Fase Agua (Fondo)
    fig_vessel.add_trace(go.Bar(name='Fase Agua Libre (Fondo)', x=['Separador V-101'], y=[float(altura_agua)], marker_color='#1f77b4'))
    # Fase Petróleo/Emulsión (Intermedia)
    fig_vessel.add_trace(go.Bar(name='Fase Petróleo / Emulsión', x=['Separador V-101'], y=[float(altura_crudo)], base=[float(altura_agua)], marker_color='#8c564b'))
    # Espacio libre para gas
    fig_vessel.add_trace(go.Bar(name='Cámara Superior de Gas', x=['Separador V-101'], y=[float(100.0 - nivel_actual)], base=[float(nivel_actual)], marker_color='#2ca02c'))

    fig_vessel.update_layout(
        barmode='stack', yaxis=dict(title='Capacidad Volumétrica Total (%)', range=[0, 100]),
        template="plotly_dark", height=300, margin=dict(l=20, r=20, t=20, b=20),
        showlegend=True
    )
    st.plotly_chart(fig_vessel, use_container_width=True)

    # Retornamos los valores actualizados para el lazo cerrado de control global de app.py
    return float(p_operacion), float(t_linea_entrada), float(nivel_actual)
