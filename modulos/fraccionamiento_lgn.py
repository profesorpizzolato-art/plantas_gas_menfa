# modulos/fraccionamiento_lgn.py
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def render_fraccionamiento():
    st.header("🔮 Unidad de Fraccionamiento de Líquidos (LGN)")
    st.caption("Simulador interactivo de torres de destilación fraccionada para la obtención de productos comerciales (C2, C3, C4 y C5+).")
    
    # --- PESTAÑAS DE TORRES ---
    tab1, tab2 = st.tabs(["🗼 Torre Deetanizadora (C2 Out)", "🗼 Torre Depropanizadora (C3/C4 Split)"])
    
    # ==========================================
    # PESTAÑA 1: TORRE DEETANIZADORA
    # ==========================================
    with tab1:
        st.subheader("Control Operativo de la Deetanizadora")
        st.markdown("""
        Esta torre recibe el líquido criogénico de fondo de la Demetinizadora. Su objetivo es separar el **Etano ($C_2$)** por el tope como gas residual o petroquímico, dejando las fracciones pesadas ($C_3+$) en el fondo.
        """)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("### 🎛️ Variables de Proceso")
            p_deet = st.slider("Presión de la Torre (kPa)", 1800, 2600, 2200, key="p_deet")
            t_reb_deet = st.slider("Temperatura del Reboiler (°C)", 75, 115, 95, key="t_reb_deet")
            r_ratio_deet = st.slider("Relación de Reflujo (L/D)", 1.0, 3.5, 2.1, step=0.1, key="r_ratio_deet")
            
        with col2:
            st.markdown("### 📊 Perfil de Composición y Eficiencia")
            
            # Modelo matemático simplificado de perfil de platos (20 platos)
            platos = np.arange(1, 21)
            # Simulación de curvas de fracción molar según variables
            factor_separacion = (t_reb_deet / 95.0) * (r_ratio_deet / 2.1) / (p_deet / 2200.0)
            
            c2_profile = 1.0 / (1.0 + np.exp((platos - 10) * 0.4 * factor_separacion))
            c3_profile = 1.0 - c2_profile
            
            # Gráfico de Plotly para el perfil de la torre
            fig_deet = go.Figure()
            fig_deet.add_trace(go.Scatter(x=c2_profile, y=platos, mode='lines+markers', name='Etano (C2)', line=dict(color='#00CC96', width=3)))
            fig_deet.add_trace(go.Scatter(x=c3_profile, y=platos, mode='lines+markers', name='Propano+ (C3+)', line=dict(color='#AB63FA', width=3)))
            
            fig_deet.update_layout(
                title="Perfil de Concentración Molar por Plato",
                xaxis_title="Fracción Molar en Fase Líquida (x)",
                yaxis_title="Número de Plato (Fondo a Tope)",
                template="plotly_dark",
                height=320,
                margin=dict(l=20, r=20, t=40, b=20)
            )
            # SOLUCCIÓN AL VALUEERROR: Inversión del eje de manera explícita y segura
            fig_deet.update_yaxes(autorange="reverse")
            st.plotly_chart(fig_deet, use_container_width=True)
            
        # Indicadores de calidad comerciales
        pureza_tope = c2_profile[0] * 100
        contaminacion_fondo = (1.0 - c3_profile[-1]) * 100
        
        st.markdown("#### 🔍 Análisis de Producto de Salida")
        c_col1, c_col2 = st.columns(2)
        c_col1.metric("Pureza de Etano en Tope", f"{pureza_tope:.2f} %", 
                      delta="ÓPTIMA" if pureza_tope >= 95.0 else "FUERA DE ESPECIFICACIÓN (Bajo Reflujo)",
                      delta_color="normal" if pureza_tope >= 95.0 else "inverse")
        
        c_col2.metric("Remanente de C2 en Fondo (Especificación vapor)", f"{contaminacion_fondo:.2f} %",
                      delta="BAJO CONTROL" if contaminacion_fondo <= 2.0 else "ALTA PRESIÓN DE VAPOR (Subir T Reboiler)",
                      delta_color="normal" if contaminacion_fondo <= 2.0 else "inverse")

    # ==========================================
    # PESTAÑA 2: TORRE DEPROPANIZADORA
    # ==========================================
    with tab2:
        st.subheader("Control Operativo de la Depropanizadora")
        st.markdown("""
        El producto de fondo de la Deetanizadora ($C_3+$) se alimenta a esta columna. Aquí aislamos el **Propano ($C_3$)** comercial por el tope para la producción de GLP, despachando el **Butano y las Gasolinas ($C_4+$)** por el fondo.
        """)
        
        col3, col4 = st.columns([1, 2])
        
        with col3:
            st.markdown("### 🎛️ Variables de Proceso")
            p_deprop = st.slider("Presión de la Torre (kPa)", 1400, 2000, 1700, key="p_deprop")
            t_reb_deprop = st.slider("Temperatura del Reboiler (°C)", 110, 150, 130, key="t_reb_deprop")
            r_ratio_deprop = st.slider("Relación de Reflujo (L/D)", 1.5, 4.0, 2.5, step=0.1, key="r_ratio_deprop")
            
        with col4:
            st.markdown("### 📊 Perfil de Composición y Eficiencia")
            
            # Modelo matemático para depropanizadora (24 platos)
            platos_dep = np.arange(1, 25)
            factor_sep_dep = (t_reb_deprop / 130.0) * (r_ratio_deprop / 2.5) / (p_deprop / 1700.0)
            
            c3_profile = 1.0 / (1.0 + np.exp((platos_dep - 12) * 0.35 * factor_sep_dep))
            c4_profile = 1.0 - c3_profile
            
            fig_deprop = go.Figure()
            fig_deprop.add_trace(go.Scatter(x=c3_profile, y=platos_dep, mode='lines+markers', name='Propano (C3)', line=dict(color='#FFA15A', width=3)))
            fig_deprop.add_trace(go.Scatter(x=c4_profile, y=platos_dep, mode='lines+markers', name='Butano+ (C4+)', line=dict(color='#19D3F3', width=3)))
            
            fig_deprop.update_layout(
                title="Perfil de Concentración Molar por Plato",
                xaxis_title="Fracción Molar en Fase Líquida (x)",
                yaxis_title="Número de Plato (Fondo a Tope)",
                template="plotly_dark",
                height=320,
                margin=dict(l=20, r=20, t=40, b=20)
            )
            # SOLUCCIÓN AL VALUEERROR: Inversión del eje de manera explícita y segura
            fig_deprop.update_yaxes(autorange="reverse")
            st.plotly_chart(fig_deprop, use_container_width=True)
            
        pureza_c3_tope = c3_profile[0] * 100
        contaminacion_c3_fondo = (1.0 - c4_profile[-1]) * 100
        
        st.markdown("#### 🔍 Análisis de Producto Comercial")
        c_col3, c_col4 = st.columns(2)
        c_col3.metric("Pureza de Propano Comercial (GLP)", f"{pureza_c3_tope:.2f} %",
                      delta="CALIDAD COMERCIAL" if pureza_c3_tope >= 96.0 else "RECHAZO DE DESPACHO",
                      delta_color="normal" if pureza_c3_tope >= 96.0 else "inverse")
        
        c_col4.metric("Pérdida de C3 en Corriente de Fondo", f"{contaminacion_c3_fondo:.2f} %",
                      delta="MÍNIMA PÉRDIDA" if contaminacion_c3_fondo <= 1.5 else "PÉRDIDA ECONÓMICA (Subir Fuego)",
                      delta_color="normal" if contaminacion_c3_fondo <= 1.5 else "inverse")
