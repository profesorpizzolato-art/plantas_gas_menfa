# modulos/guias_rapidas.py
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def render_guias_rapidas():
    st.header("⚡ Guías Rápidas de Operación y Despacho")
    st.caption("Fichas de campo dinámicas, fáciles de interpretar y de alta fidelidad para personal de planta.")
    st.markdown("---")
    
    # Selector de Fichas de Campo
    opcion_guia = st.radio(
        "Seleccione la Guía de Campo que desea visualizar:",
        ["🌀 Compresión de Gas (Surge vs Choke)", "📜 Normativas y Especificación de Gasoductos", "❄️ Plantas de Licuefacción (GNL)"],
        horizontal=True
    )
    
    st.markdown("---")
    
    # =========================================================================
    # FICHA 1: COMPRESIÓN DE GAS
    # =========================================================================
    if "Compresión" in opcion_guia:
        st.subheader("🌀 Ficha Operativa: Compresión de Gas de Forma Sencilla")
        st.write("""
        Imaginá un compresor centrífugo como un ventilador industrial de velocidad extrema. Su trabajo no es empujar el gas en línea recta, sino **tomarlo por el centro (ojo del impulsor) y revolearlo hacia afuera a miles de RPM** utilizando la fuerza centrífuga para aumentar radicalmente su presión y velocidad.
        """)
        
        # Gráfico dinámico interactivo: Mapa de Performance Simplificado
        st.markdown("#### 📈 Mapa Interactivo de Operación (Ventana Segura)")
        st.caption("Mueva el deslizador para ver cómo cambia el punto de operación respecto a las zonas de peligro de la turbocompresora.")
        
        # Control del alumno
        caudal_operativo = st.slider("Caudal Volumétrico de Entrada (m³/h):", 1000, 9000, 5000, step=500)
        
        # Curvas base fijas del compresor
        flow_axis = np.linspace(1500, 8500, 100)
        head_surge_line = 4000 + (flow_axis - 1500) * 0.2  # Límite izquierdo
        head_performance = 5500 - ((flow_axis - 4000)**2 / 3500) # Curva de trabajo real
        
        # Punto actual del simulador
        current_head = float(5500 - ((caudal_operativo - 4000)**2 / 3500))
        
        fig_mapa = go.Figure()
        # Línea de Surge
        fig_mapa.add_trace(go.Scatter(x=[2000, 2000], y=[2500, 6000], mode='lines', name='Línea de Surge (Peligro Izquierdo)', line=dict(color='red', width=3, dash='dash')))
        # Línea de Choke
        fig_mapa.add_trace(go.Scatter(x=[8000, 8000], y=[2500, 6000], mode='lines', name='Línea de Choke (Peligro Derecho)', line=dict(color='yellow', width=3, dash='dash')))
        # Curva de Performance
        fig_mapa.add_trace(go.Scatter(x=[float(f) for f in flow_axis], y=[float(h) for h in head_performance], mode='lines', name='Curva de Eficiencia del Rodete', line=dict(color='#00CC96', width=2)))
        # Punto Operativo Actual
        fig_mapa.add_trace(go.Scatter(x=[caudal_operativo], y=[current_head], mode='markers+text', name='Punto Operativo Actual', marker=dict(color='white', size=12, symbol='diamond'), text=["📍 Operación"], textposition="top center"))
        
        fig_mapa.update_layout(
            xaxis_title="Caudal de Gas (m³/h)", yaxis_title="Presión de Descarga (Head - m)",
            template="plotly_dark", height=320, margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig_mapa, use_container_width=True)
        
        # Diagnóstico automático basado en el simulador
        if caudal_operativo <= 2000:
            st.error("🚨 **ALERTA DE SURGE (BOMBEO):** El caudal es extremadamente bajo. El gas se va a invertir de dirección hacia la succión, generando fuerzas y vibraciones axiales destructivas. ¡Active el lazo Anti-Surge para abrir la ASV y reciclar gas!")
        elif caudal_operativo >= 8000:
            st.warning("⚠️ **ALERTA DE CHOKE (STONE WALL):** El gas alcanzó la velocidad del sonido (Mach 1) en los álabes. Se formó una barrera sónica invisible; el caudal no aumentará más y la eficiencia cayó a cero.")
        else:
            st.success("🟢 **ZONA DE OPERACIÓN SEGURA:** El equilibrio hidrodinámico es correcto. Los cojinetes y sellos operan bajo parámetros estables.")
            
        st.markdown("---")
        st.markdown("### 🛡️ Los Tres Guardianes del Compresor")
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            st.markdown("**1. El Scrubber**")
            st.caption("Es el escudo mecánico. Como los líquidos no se pueden comprimir, una sola gota golpeando un álabe a 10.000 RPM actúa como una bala. El Scrubber la frena antes de la succión.")
        with col_c2:
            st.markdown("**2. Los Intercoolers**")
            st.caption("Al comprimir el gas, este se calienta. El gas caliente se expande y exige más potencia para seguir comprimiéndose. Los aeroenfriadores lo achican entre etapas para ahorrar energía.")
        with col_c3:
            st.markdown("**3. Los Dry Gas Seals**")
            st.caption("Son colchones de gas microscópicos de alta pureza que sellan el eje rotativo. Evitan que el gas de proceso se escape a la atmósfera o que se contamine con el aceite lubricante.")

    # =========================================================================
    # FICHA 2: NORMATIVAS DE GASODUCTOS
    # =========================================================================
    elif "Normativas" in opcion_guia:
        st.subheader("📜 Ficha Operativa: Normativas de Gasoductos y Despacho Seguro")
        st.write("""
        Para inyectar gas en un sistema de transporte troncal (como las redes comerciales), el gas debe cumplir de manera estricta con una 'partida de nacimiento' de calidad para proteger la integridad del caño de acero.
        """)
        
        
        
        st.markdown("### 📋 Las 4 Reglas de Oro Técnicas")
        
        t1, t2, t3, t4 = st.tabs(["💧 Humedad (64 mg/m³)", "🌡️ Punto de Rocío", "☣️ Corrosión (H2S/CO2)", "🔥 Combustión (Wobbe)"])
        
        with t1:
            st.markdown("#### Límite Estricto de Humedad: Máximo 64 mg/m³")
            st.write("""
            * **El Riesgo Real:** El agua libre combinada con el metano a alta presión forma **hidratos** (bloques de clatratos con aspecto de hielo que bloquean por completo el flujo de la cañería).
            * **La Solución:** Las plantas de deshidratación por glicol (TEG) absorben esta humedad, asegurando que el gas viaje seco.
            """)
        with t2:
            st.markdown("#### Punto de Rocío de Hidrocarburos (Dew Point)")
            st.write("""
            * **El Riesgo Real:** Si la temperatura ambiental en el trayecto del gasoducto baja y el gas contiene muchos componentes pesados ($C_3, C_4, C_5+$), estos pasarán a estado líquido dentro del caño. Esto genera baches de líquido, caídas de presión drásticas y golpes de ariete destructivos.
            """)
        with t3:
            st.markdown("#### Control de Gases Ácidos")
            st.write("""
            * **H2S (Sulfuro de Hidrógeno):** Es altamente tóxico y letal. Las normas exigen un máximo estricto de 5 mg/m³ para proteger la vida humana.
            * **CO2 (Dióxido de Carbono):** Si se junta con trazas de agua, forma ácido carbónico, el cual devora el acero del gasoducto generando corrosión alveolar severa desde el interior.
            """)
        with t4:
            st.markdown("#### Índice de Wobbe y Homogeneidad")
            st.write("""
            * **El Riesgo Real:** Los quemadores domésticos e industriales en las ciudades necesitan recibir una energía constante. El Índice de Wobbe mide esta intercambiabilidad. Si el gas va muy cargado de pesados o con exceso de nitrógeno (inerte), las llamas de destino pueden apagarse o generar monóxido de carbono por mala combustión.
            """)

    # =========================================================================
    # FICHA 3: PLANTAS DE LICUEFACCIÓN (GNL)
    # =========================================================================
    elif "Licuefacción" in opcion_guia:
        st.subheader("❄️ Ficha Operativa: Plantas de Licuefacción y Frontera del GNL")
        st.write("""
        Cuando los gasoductos terrestres no son viables (por ejemplo, para exportar gas a otros continentes), se recurre al **GNL (Gas Natural Licuado)** para cargarlo en barcos metaneros.
        """)
        
        st.info("💡 **El Gran Truco Físico del GNL:** Al enfriar el metano hasta **-162 °C** a presión atmosférica, este cambia de estado gaseoso a líquido, **reduciendo su volumen 600 veces**. ¡Es como meter todo el gas de una habitación entera dentro de un bidón de agua de 5 litros!")
        
        st.markdown("### 🏗️ El Riguroso Camino del Gas hacia los -162 °C")
        st.write("""
        El frío criogénico extremo no perdona impurezas. Una planta de licuefacción requiere un pre-tratamiento absoluto antes de congelar:
        
        1. **Endulzamiento Total ($CO_2 < 50$ ppm):** Si el gas entra con dióxido de carbono común, al cruzar los $-60^\circ\text{C}$ el CO2 va a **sublimar** (pasa directo de gas a sólido), formando bloques de hielo seco que taponan instantáneamente las placas de aluminio del intercambiador principal.
        2. **Deshidratación de Extrema Pureza ($H_2O < 0.1$ ppm):** Las plantas de TEG no alcanzan para el GNL. Se requiere obligatoriamente pasar el gas por lechos secos de **Tamices Moleculares (Zeolita 4A)** para remover la humedad a nivel de trazas moleculares absolutas y evitar congelamientos.
        3. **Remoción de Mercurio:** El mercurio destruye el aluminio de los intercambiadores compactos (*Cold Box*) mediante un ataque químico llamado amalgama de metal líquido. Se elimina por completo usando filtros de carbón activado reactivo.
        4. **El Lazo Criogénico (MCR):** Una vez purificado, el gas ingresa al intercambiador principal, donde cede su calor contra un circuito cerrado de refrigerantes mixtos (mezclas de nitrógeno, propano y etano) que se evaporan a temperaturas ultra-frías, forzando la licuación segura del metano.
        """)
        
        # Comparador visual de volumen
        st.markdown("#### 📊 Reducción Exponencial de Espacio")
        datos_vol = pd.DataFrame({
            "Metros Cúbicos Equivalentes": [600, 1]
        }, index=["Estado Gaseoso Comercial", "Estado Líquido Criogénico (GNL)"])
        st.bar_chart(datos_vol)
