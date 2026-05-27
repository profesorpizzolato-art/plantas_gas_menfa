# modulos/procesamiento.py
import streamlit as st
import plotly.graph_objects as go

def render_procesamiento(p_entrada, t_entrada):
    st.header("❄️ Planta Criogénica y Extracción de Líquidos (Complejo Cerri)")
    col1, col2 = st.columns([1, 2])
    with col1:
        eficiencia_exp = st.slider("Eficiencia Isentrópica del Expansor (%)", 70.0, 95.0, 85.0)
        p_salida = st.slider("Presión de Salida de Expansor (kPa)", 1000, 3000, 1800)
    with col2:
        caida_p = (p_entrada - p_salida) / p_entrada
        t_demetinizadora = t_entrada - (caida_p * 110 * (eficiencia_exp / 100))
        rendimiento_lgn = max(0.0, float(caida_p * 4.5 * (eficiencia_exp / 85)))
        
        st.metric("Temperatura en Demetinizadora", f"{t_demetinizadora:.1f} °C")
        
        fig = go.Figure(go.Bar(
            x=['Etano', 'Propano', 'Butano', 'Gasolina', 'Gas Residual'],
            y=[rendimiento_lgn*0.4, rendimiento_lgn*0.35, rendimiento_lgn*0.15, rendimiento_lgn*0.1, 100-rendimiento_lgn],
            marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd', '#d62728']
        ))
        fig.update_layout(title="Perfil de Productos Extraídos (m³/MMSCF)", template="plotly_dark", height=250)
        st.plotly_chart(fig, use_container_width=True)
