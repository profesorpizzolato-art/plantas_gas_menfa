# modulos/cognitivo.py
import streamlit as st

def render_cognitivo():
    st.title("🧠 Aula Virtual de Entrenamiento Cognitivo")
    st.caption("Resolución de fallas en cascada y toma de decisiones industriales críticas.")
    st.markdown("---")

    # Lectura automática del estado en tiempo real de la simulación
    hidratos = st.session_state.get('falla_hidratos_activa', False)
    surge = st.session_state.get('falla_surge_activa', False)

    st.subheader("📋 Matriz de Diagnóstico de Incidentes Activos")

    if hidratos:
        st.error("🚨 **INCIDENTE REPORTADO:** Caída de presión y taponamiento térmico por formación de hidratos sólidos detectada en el Chiller.")
        st.markdown("**Desafío Operativo:** ¿Qué acción inmediata mitiga la cristalización en los intercambiadores criogénicos?")
        
        respuesta = st.radio("Acción correctiva propuesta:", [
            "Aumentar la presión de entrada para empujar mecánicamente el bloque sólido.",
            "Iniciar de inmediato la inyección forzada de Monoetilanglicol (MEG) o Metanol al sistema como inhibidor termodinámico.",
            "Cerrar la válvula de venteo general y aislar los transmisores de temperatura."
        ])
        
        if st.button("Validar Plan de Mitigación"):
            if "Monoetilanglicol" in respuesta:
                st.success("🎯 **Excelente Criterio Técnico:** El MEG deprime el punto de congelamiento del agua libre disolviendo el hidrato de forma segura.")
                st.session_state['falla_hidratos_activa'] = False
                st.session_state['humedad_salida'] = 24.5
            else:
                st.error("💥 **Acción de Alto Riesgo:** Intentar presurizar contra una cañería obstruida por sólidos puede provocar una falla catastrófica del material.")

    elif surge:
        st.error("🚨 **INCIDENTE REPORTADO:** Turbocompresor operando al límite izquierdo de su curva de diseño (Condición de Surge inminente).")
        st.markdown("**Desafío Operativo:** ¿Cómo resguarda la integridad de los álabes de la turbomaquinaria?")
        
        respuesta = st.radio("Acción correctiva propuesta:", [
            "Abrir de forma manual o automática la válvula de reciclaje Anti-Surge (Blow-off) para aumentar el caudal circulante.",
            "Bajar drásticamente las RPM de la máquina sin despresurizar el tramo.",
            "Estrangular por completo la válvula de descarga para contener el flujo reverso."
        ])
        
        if st.button("Validar Plan de Mitigación"):
            if "válvula de reciclaje" in respuesta:
                st.success("🎯 **Respuesta Correcta:** Al abrir el lazo de reciclaje se desplaza el punto operativo a la derecha de la envolvente, estabilizando la máquina.")
                st.session_state['falla_surge_activa'] = False
                st.session_state['p_descarga_gasoducto'] = 6100.0
            else:
                st.error("💥 **Falla Mecánica Simulada:** Vibraciones radiales severas. Daño crítico en sellos secos y cojinetes de empuje.")

    else:
        st.success("🟢 **Consola Limpia:** No hay incidentes dinámicos inyectados en este momento. Diríjase al **Manual Técnico (Capítulos 5 u 7)** para disparar fallas físicas simuladas.")
