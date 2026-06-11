# modulos/tratamiento.py
import streamlit as st

def render_tratamiento():
    st.title("🧪 Planta de Tratamiento de Gas: Endulzamiento por Aminas")
    st.caption("Remoción selectiva de componentes contaminantes ácidos ($CO_2 / H_2S$) mediante absorción química.")
    st.markdown("---")
    
    st.subheader("Consola de Monitoreo de la Torre Absorbedora")
    
    caudal_amina = st.slider("Caudal de circulación de Amina Pobre (m³/h):", 10, 150, 80)
    
    # Simulación del comportamiento químico del proceso de endulzamiento
    co2_calculado = max(0.05, 4.0 - (caudal_amina * 0.04))
    st.session_state['co2_salida'] = co2_calculado
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Circulación de Amina", f"{caudal_amina} m³/h")
    with col2:
        st.metric("Concentración de CO2 en Gas Dulce de Salida", f"{co2_calculado:.2f} % mol")
        
    if co2_calculado > 2.0:
        st.error("🚨 **GAS FUERA DE ESPECIFICACIÓN TRANSPORTE:** Supera el límite de 2.0% mol admisible por la norma de transporte de gas.")
    else:
        st.success("✅ **Calidad Química Óptima:** Gas acondicionado para envío seguro a etapa criogénica.")
