import streamlit as st

def render_separacion():
    st.header("🛢️ Sistema de Separación de Entrada")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Controles del Operador")
        p_entrada = st.slider("Presión de Entrada (kPa)", 700, 7000, 3500, step=100)
        t_entrada = st.slider("Temperatura de Entrada (°C)", -20, 40, 20)
        nivel_liquido = st.slider("Nivel de Líquidos en Tanque (%)", 0, 100, 45)
    
    with col2:
        st.subheader("Estado Mecánico del Separador")
        # Simulación de estados
        st.info(f"Presión del Colector: **{p_entrada} kPa** | Temperatura: **{t_entrada} °C**")
        
        # Lógica de progreso visual del nivel del tanque (Slug Catcher / Separador)
        st.progress(nivel_liquido / 100.0)
        st.caption(f"Capacidad actual del acumulador de líquidos: {nivel_liquido}%")
        
    return p_entrada, t_entrada, nivel_liquido
