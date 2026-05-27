# modulos/seguridad.py
import streamlit as st
import config as cfg

def procesar_matriz_seguridad():
    st.header("🛡️ Matriz de Interlocks y Paradas de Emergencia (ESD / CDE)")
    
    cde_activado = False
    causas = []
    
    # Comprobación de condiciones críticas guardadas en el session_state
    if st.session_state.get('nivel_liquido', 0) >= cfg.NIVEL_LIQUIDO_CRITICO:
        cde_activado = True
        causas.append(f"Nivel de líquido en separador superior al límite ({st.session_state.nivel_liquido}% >= {cfg.NIVEL_LIQUIDO_CRITICO}%)")
        
    if st.session_state.get('p_entrada', 0) >= cfg.PRESION_MAX_COLECTOR:
        cde_activado = True
        causas.append(f"Sobrepresión en Colector de Entrada ({st.session_state.p_entrada} kPa >= {cfg.PRESION_MAX_COLECTOR} kPa)")
        
    if st.session_state.get('p_descarga_gasoducto', 0) >= cfg.PRESION_MAX_GASODUCTO:
        cde_activado = True
        causas.append(f"Sobrepresión en línea de Despacho / Gasoducto ({st.session_state.p_descarga_gasoducto} kPa >= {cfg.PRESION_MAX_GASODUCTO} kPa)")

    if cde_activado:
        st.error("🚨 SINOPSIS DE DISPARO: CIERRE DE EMERGENCIA DE PLANTA ACTIVADO")
        for causa in causas:
            st.write(f"❌ **Causa:** {causa}")
        st.markdown("---")
        st.warning("⚠️ **Acciones automáticas según NAG-125:** Cierre de válvulas de bloqueo de entrada/salida, despresurización manual de emergencia (Vent) y parada de unidades compresoras.")
    else:
        st.success("🟢 SISTEMA DE ENCLAVAMIENTO DE SEGURIDAD EN LÍNEA - SIN ALARMAS ACTIVAS")
        
    # Elementos de protección fija contra incendios según norma
    with st.expander("Verificación de Sistemas Fijos Contra Incendios"):
        st.info("Monitoreo de tanques de espumígeno, redes de agua y válvulas de diluvio en zona de almacenamiento de licuables.")
