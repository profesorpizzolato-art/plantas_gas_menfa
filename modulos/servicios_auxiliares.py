# modulos/servicios_auxiliares.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render_servicios():
    st.header("⚡ Servicios Auxiliares de Planta (Utilities)")
    st.caption("Consola de control y monitoreo de los sistemas de soporte crítico: Aceite Térmico (Hot Oil) y Aire de Instrumentos.")
    
    tab1, tab2 = st.tabs(["🔥 Sistema de Aceite Térmico", "💨 Red de Aire de Instrumentos"])
    
    # ==========================================
    # PESTAÑA 1: ACEITE TÉRMICO (HOT OIL)
    # ==========================================
    with tab1:
        st.subheader("Circuito de Calentamiento por Aceite Térmico")
        st.markdown("""
        El sistema de *Hot Oil* utiliza un fluido caloportador sintético bombeado a través de un horno de proceso para suministrar energía térmica regulada a los reboilers de fraccionamiento y de regeneración de glicol, evitando los puntos calientes que degradarían los productos.
        """)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("### 🎛️ Control del Horno")
            caudal_aceite = st.slider("Caudal de Circulación (m³/h)", 40.0, 120.0, 85.0, key="caudal_aceite")
            potencia_quemador = st.slider("Potencia del Quemador (%)", 10, 100, 65, key="potencia_quemador")
            
        with col2:
            st.markdown("### 📊 Balance Térmico del Fluido")
            
            # Lógica física simulada del circuito de calor
            t_retorno = 140.0  # °C constante de retorno de planta
            # La temperatura de salida sube con la potencia y baja con el caudal
            t_salida = t_retorno + (potencia_quemador * 2.2) - ((caudal_aceite - 85) * 0.4)
            
            # Gráfico de eficiencia térmica
            fig_oil = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = t_salida,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Temperatura de Salida del Horno (°C)"},
                gauge = {
                    'axis': {'range': [100, 300]},
                    'bar': {'color': "#FF4B4B"},
                    'steps': [
                        {'range': [100, 180], 'color': "#1f77b4"},
                        {'range': [180, 260], 'color': "#00CC96"},
                        {'range': [260, 300], 'color': "#FF9700"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 280.0
                    }
                }
            ))
            fig_oil.update_layout(template="plotly_dark", height=250, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig_oil, use_container_width=True)
            
        st.markdown("#### 🔍 Estado de Entrega Térmica")
        o_col1, o_col2 = st.columns(2)
        o_col1.metric("Temperatura de Suministro", f"{t_salida:.1f} °C",
                      delta="TEMPERATURA EFICIENTE" if 190 <= t_salida <= 250 else "RIESGO DE CRACKEO O BAJO CALOR",
                      delta_color="normal" if 190 <= t_salida <= 250 else "inverse")
        
        eficiencia_horno = (100 - (caudal_aceite * 0.1) - (100 - potencia_quemador) * 0.2)
        o_col2.metric("Eficiencia Térmica Estimada", f"{eficiencia_horno:.1f} %")

    # ==========================================
    # PESTAÑA 2: AIRE DE INSTRUMENTOS
    # ==========================================
    with tab2:
        st.subheader("Sistema de Compresión y Secado de Aire de Control")
        st.markdown("""
        Este sistema alimenta los actuadores neumáticos de las válvulas de control ($FCV$, $LCV$, $PCV$) y de bloqueo ($SDV$). Una pérdida de presión aquí fuerza a las válvulas a adoptar sus posiciones seguras de falla (*Fail-Safe*).
        """)
        
        col3, col4 = st.columns([1, 2])
        
        with col3:
            st.markdown("### 🎛️ Operación de Compresores de Aire")
            compresores_on = st.number_input("Compresores en Marcha", min_value=0, max_value=2, value=1, key="comp_on")
            
            st.markdown("---")
            # Botón de contingencia cognitiva
            st.error("🚨 Simular Contingencia Crítica")
            fuga_aire = st.checkbox("Simular Fuga Masiva en Troncal de Aire", value=False, key="fuga_aire")
            
        with col4:
            st.markdown("### 📊 Presión de la Red Neumática")
            
            # Simulación de presión según compresores y fuga
            if fuga_aire:
                p_aire = 250.0 + (compresores_on * 100.0) # Cae drásticamente
            else:
                if compresores_on == 0: p_aire = 0.0
                elif compresores_on == 1: p_aire = 720.0 # Presión nominal en kPa (aprox 100 psi)
                else: p_aire = 850.0 # Sobresaturación
                
            fig_air = go.Figure()
            fig_air.add_trace(go.Scatter(x=[0, 1, 2, 3, 4, 5], y=[p_aire]*6, mode='lines+markers', name='Presión Red (kPa)', line=dict(color='#19D3F3', width=4)))
            fig_air.add_trace(go.Scatter(x=[0, 5], y=[550.0, 550.0], mode='lines', name='Límite Crítico de Falla', line=dict(color='red', dash='dash')))
            
            fig_air.update_layout(
                title="Tendencia de Presión de Aire de Instrumentos",
                xaxis_title="Tiempo de Muestreo (min)",
                yaxis_title="Presión (kPa)",
                yaxis=dict(range=[0, 1000]),
                template="plotly_dark",
                height=240,
                margin=dict(l=20, r=20, t=40, b=20)
            )
            st.plotly_chart(fig_air, use_container_width=True)
            
        st.markdown("#### 🔍 Estado de Instrumentación Neumática")
        if p_aire < 550.0:
            st.error(f"🚨 **ALERTA CRÍTICA DE AIRE ({p_aire:.0f} kPa):** Presión por debajo del límite operativo. Las válvulas de control de la planta se han bloqueado en posición de falla (FO/FC). El lazo general de seguridad ESD se activará por hardware de campo de forma inminente.")
        else:
            st.success(f"✅ **SISTEMA DE AIRE OPERATIVO ({p_aire:.0f} kPa):** Presión estable en anillo de distribución. Actuadores respondiendo normalmente a las señales del DCS.")
