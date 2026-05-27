# modulos/transporte.py
import streamlit as st
import numpy as np
import pandas as pd  # <--- CORRECCIÓN: Agregada la importación que faltaba

def render_transporte():
    st.header("🚀 Estación Compresora y Despacho a Gasoducto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Parámetros de Succión y Descarga")
        p_succion = st.slider("Presión de Succión (kPa)", 2000, 4500, 3200)
        p_descarga = st.slider("Presión de Descarga (kPa)", 4500, 8000, 6100)
        tipo_compresor = st.selectbox("Tipo de Unidad Compresora", ["Centrífugo (Turbocompresor)", "Alternativo (Desplazamiento Positivo)"])
        
    with col2:
        st.subheader("Cálculos de Operación")
        # Relación de compresión (Rc = Pd_abs / Ps_abs)
        rc = (p_descarga + 101.3) / (p_succion + 101.3)
        st.metric("Relación de Compresión (Rc)", f"{rc:.2f}")
        
        # Alerta de temperatura o límite por Rc elevado
        if rc > 3.0:
            st.warning("⚠️ Rc elevada: Alta temperatura de descarga esperada. Requiere postenfriamiento.")
            
        # Pérdida de carga simulada a lo largo del gasoducto (Ecuación de caída lineal para visualización)
        distancia = np.linspace(0, 100, 50)
        presion_linea = p_descarga - (distancia * 12)  # Simulación de pérdida de carga por fricción
        
        # Crear el DataFrame correctamente con la librería importada
        df_grafico = pd.DataFrame({"Presión en Gasoducto (kPa)": presion_linea}, index=distancia)
        
        st.line_chart(df_grafico)
        st.caption("Perfil de presión estimado a lo largo de 100 km de gasoducto (Simulación de fricción).")
        
    return p_descarga
