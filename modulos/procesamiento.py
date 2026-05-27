# modulos/procesamiento.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def render_procesamiento(p_entrada, t_entrada):
    st.header("❄️ Planta Criogénica y Extracción de Licuables")
    st.subheader("Simulación basada en el proceso de Turboexpansión")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("**Controles del Turboexpansor**")
        eficiencia_exp = st.slider("Eficiencia Isentrópica del Expansor (%)", 70.0, 95.0, 85.0)
        p_salida_criog = st.slider("Presión de Salida (kPa)", 1000, 3000, 1800, step=100)
        
    with col2:
        # Caída de temperatura Joule-Thomson + Expansión Dinámica simplificada
        caida_p_relativa = (p_entrada - p_salida_criog) / p_entrada
        t_salida_criog = t_entrada - (caida_p_relativa * 110 * (eficiencia_exp / 100))
        
        # Rendimientos estimados de Líquidos del Gas Natural (LGN)
        rendimiento_lgn = max(0.0, float(caida_p_relativa * 4.5 * (eficiencia_exp / 85)))
        
        st.metric("Temperatura en Demetinizadora", f"{t_salida_criog:.1f} °C", 
                  delta="Riesgo de congelamiento" if t_salida_criog < -100 else "Rango Óptimo")
        st.metric("Producción Estimada de LGN", f"{rendimiento_lgn:.2f} m³/MMSCF")
        
        # Gráfico de destilación conceptual / separación
        fig = go.Figure(go.Bar(
            x=['Etano (C2)', 'Propano (C3)', 'Butano (C4+)', 'Gas Residual'],
            y=[rendimiento_lgn*0.4, rendimiento_lgn*0.35, rendimiento_lgn*0.25, 100 - rendimiento_lgn],
            marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
        ))
        fig.update_layout(title="Fraccionamiento de Componentes en Planta", template="plotly_dark", height=250)
        st.plotly_chart(fig, use_container_width=True)
        
    return t_salida_criog
