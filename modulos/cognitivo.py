# modulos/cognitivo.py
import streamlit as st
import config as cfg

def render_cognitivo():
    st.header("🧠 Entrenamiento Cognitivo Operacional")
    st.caption("Simulación de toma de decisiones críticas frente a contingencias en vivo.")
    
    # Selección de Escenario de Falla por parte del Instructor o Alumno
    escenario = st.selectbox("Seleccione el Escenario de Contingencia a Resolver:", [
        "Condición Normal de Operación",
        "Arrastre Severo de Líquido en Gasoducto (Slug de Entrada)",
        "Pérdida de Llama / Falla de Fuego en Reboiler de TEG"
    ])
    
    # Variables base mutables por la contingencia
    p_entrada = 3500.0
    nivel_sep = 45.0
    temp_reboiler = 180.0
    humedad_salida = 22.0
    
    if escenario == "Arrastre Severo de Líquido en Gasoducto (Slug de Entrada)":
        nivel_sep = 92.0  # Dispara alarma
        humedad_salida = 75.0 # Sube la humedad por contaminación de la torre
        st.critical("🚨 ¡ALERTA COGNITIVA! El nivel del separador sube rápidamente y el gas de venta se está saliendo de especificación comercial.")
        
    elif escenario == "Pérdida de Llama / Falla de Fuego en Reboiler de TEG":
        temp_reboiler = 85.0  # El glicol se enfría
        humedad_salida = 110.0 # El glicol frío no absorbe agua, se dispara la humedad
        st.critical("🚨 ¡ALERTA COGNITIVA! Falla en quemador del reboiler. Temperatura en descenso continuo.")

    # Visualización de las variables afectadas por la falla
    st.subheader("🎛️ Consola de Instrumentación del Operador")
    col1, col2, col3 = st.columns(3)
    col1.metric("Nivel del Separador", f"{nivel_sep} %", delta="CRÍTICO" if nivel_sep >= cfg.NIVEL_LIQUIDO_CRITICO else "OK")
    col2.metric("Temp. Reboiler TEG", f"{temp_reboiler} °C", delta="DESCENSO" if temp_reboiler < 140 else "OK")
    col3.metric("Humedad Gas de Venta", f"{humedad_salida} mg/m³", delta="FUERA DE NORMA" if humedad_salida > cfg.LIMITE_HUMEDAD else "OK")
    
    # Espacio para la acción del operador (Toma de decisiones cognitivas)
    st.markdown("---")
    st.subheader("💡 Diagnóstico Operativo y Acción Requerida")
    
    if escenario != "Condición Normal de Operación":
        accion = st.radio("¿Qué acción operativa inmediata ejecuta usted según los procedimientos?", [
            "No hacer nada y esperar a que la variable se estabilice sola.",
            "Accionar manualmente el pulsador de Cierre de Emergencia (CDE) de planta para aislar la instalación y proteger los activos.",
            "Aumentar el caudal de gas de entrada para tratar de empujar el problema."
        ], index=None)
        
        if accion:
            if "Cierre de Emergencia" in accion:
                st.success("🎯 **Excelente decisión operativa.** El resguardo de la integridad física y mecánica de la planta ante una contingencia incontrolable es la prioridad número uno según la NAG-125.")
            else:
                st.error("❌ **Decisión incorrecta / Riesgosa.** Esa acción agravará la falla, pudiendo causar daños catastróficos a los equipos aguas abajo (ej. rotura de compresores por líquido).")
