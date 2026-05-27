import streamlit as st
import numpy as np
import plotly.graph_objects as go
from config import LIMITE_HUMEDAD_M3

def render_tratamiento(p_entrada, t_entrada):
    st.header("💧 Sistema de Deshidratación y Tratamiento (TEG)")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Variables del Contactor")
        eficiencia_teg = st.slider("Eficiencia de Absorción del Contactor (%)", 80.0, 99.5, 95.0)
        temp_recalentador = st.slider("Temperatura del Reboiler (°C)", 150, 210, 180)
    
    with col2:
        st.subheader("Cálculo de Desempeño Térmico")
        
        # Simulación física de humedad de saturación
        humedad_saturacion = (10 ** (0.02 * t_entrada + 2.5)) / (p_entrada / 1000)
        humedad_salida = humedad_saturacion * (1 - (eficiencia_teg / 100))
        
        # Gráfico dinámico de sensibilidad de temperatura vs humedad
        temps_ejemplo = np.linspace(-10, 30, 20)
        curva_saturacion = (10 ** (0.02 * temps_ejemplo + 2.5)) / (p_entrada / 1000)
        curva_salida_real = curva_saturacion * (1 - (eficiencia_teg / 100))

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=temps_ejemplo, y=curva_salida_real, mode='lines', 
                                 name='Humedad Salida (mg/m³)', line=dict(color='#00CC96', width=3)))
        fig.add_trace(go.Scatter(x=temps_ejemplo, y=[LIMITE_HUMEDAD_M3]*20, mode='lines', 
                                 name='Límite de Red Gas', line=dict(color='red', dash='dash')))

        fig.update_layout(
            title=f"Humedad del Gas de Salida vs Temperatura Operativa",
            xaxis_title="Temperatura (°C)",
            yaxis_title="Contenido de Humedad (mg/m³)",
            template="plotly_dark",
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
        
    return humedad_salida, temp_recalentador
