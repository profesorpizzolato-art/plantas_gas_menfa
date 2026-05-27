# modulos/tratamiento.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import config as cfg 
# NOTA: Importamos 'config as cfg' de forma directa para usar 'cfg.LIMITE_HUMEDAD' 
# Esto es más limpio y evita tener que importar variables una por una.

def render_treatment(p_entrada, t_entrada):
    # (Mantenemos la firma de la función como la llama app.py)
    return render_tratamiento(p_entrada, t_entrada)

def render_tratamiento(p_entrada, t_entrada):
    st.header("💧 Sistema de Deshidratación por Glicol (TEG)")
    col1, col2 = st.columns([1, 2])
    with col1:
        eficiencia_teg = st.slider("Eficiencia del Contactor (%)", 80.0, 99.5, 95.0)
        temp_reboiler = st.slider("Temperatura del Reboiler (°C)", 140, 220, int(st.session_state.temp_reboiler))
    with col2:
        # Fórmulas de aproximación de saturación física basadas en el manual
        humedad_saturacion = (10 ** (0.02 * t_entrada + 2.5)) / (p_entrada / 1000)
        humedad_salida = humedad_saturacion * (1 - (eficiencia_teg / 100))
        
        temps = np.linspace(-10, 40, 20)
        curva = ((10 ** (0.02 * temps + 2.5)) / (p_entrada / 1000)) * (1 - (eficiencia_teg / 100))
        
        # Gráfico interactivo de Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=temps, y=curva, mode='lines', name='Humedad Salida', line=dict(color='#00CC96')))
        
        # CORRECCIÓN AQUÍ: Se cambió cfg.LIMITE_HUMEDAD_M3 por cfg.LIMITE_HUMEDAD
        fig.add_trace(go.Scatter(x=temps, y=[cfg.LIMITE_HUMEDAD]*20, mode='lines', name='Límite de Red', line=dict(color='red', dash='dash')))
        
        fig.update_layout(title="Sensibilidad: Temperatura vs Humedad Salida", template="plotly_dark", height=280)
        st.plotly_chart(fig, use_container_width=True)
        
    return humedad_salida, temp_reboiler
