# modulos/separacion.py
import streamlit as st

def render_separacion():
    st.title("🛢️ Operación: Separación de Entrada (V-101)")
    st.markdown("---")
    
    caudal = st.session_state['caudal_gas']
    nivel = st.session_state['nivel_liquido']
    
    st.subheader("Estado Operativo del Separador Primario")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Caudal Alimentado (Manual)", f"{caudal:.1f} MMm³/día")
        st.metric("Nivel Hidrostático del Domo", f"{nivel:.1f} %")
        
    with col2:
        # Relación física de arrastre basada en velocidad de arrastre cinemático
        velocidad_gas = caudal * 1.3
        st.write(f"Velocidad de paso calculada: **{velocidad_gas:.2f} m/s**")
        
        if nivel > 80.0 and velocidad_gas > 10.0:
            st.error("🚨 **CRÍTICO: CARRY-OVER DETECTADO.** Arrastre masivo de hidrocarburos líquidos hacia la sección de tratamiento debido a velocidad de gas excesiva con alto nivel.")
        elif nivel > 70.0:
            st.warning("⚠️ **Alerta de Alto Nivel:** Margen seguro de separación de fases comprometido.")
        else:
            st.success("✅ **Operación Nominal:** Separación mecánica por gravedad y demister funcionando correctamente.")
            
    st.markdown("---")
    st.subheader("Controles de Campo por el Operador")
    apertura_valve = st.slider("Apertura de la válvula automática de control de nivel de líquidos (LV-101) %:", 0, 100, 45)
    
    # Recalculamos el nivel y modificamos el estado dinámico global de la planta
    st.session_state['nivel_liquido'] = max(5.0, nivel - (apertura_valve * 0.5) + (caudal * 0.4))
