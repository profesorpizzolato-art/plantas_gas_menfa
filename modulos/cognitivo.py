# modulos/cognitivo.py
import streamlit as st
import config as cfg

def render_cognitivo():
    st.header("🧠 Pilar 4: Entrenamiento Cognitivo Operacional")
    st.caption("Consola viva de simulación de contingencias y toma de decisiones críticas.")
    
    escenario = st.selectbox("Seleccione el escenario operativo a enfrentar:", [
        "A: Planta Estable en Régimen Nominal",
        "B: Arrastre Masivo de Líquidos (Tapón en Gasoducto)",
        "C: Descontrol Térmico en Reboiler de Regeneración"
    ])
    
    # --- INICIALIZACIÓN DE VARIABLES DINÁMICAS ---
    # Valores base nominales
    presion = 3200.0
    nivel_sep = 42.0
    temp_reboiler = 182.0
    calidad_gas = 24.5
    
    st.markdown("---")
    
    # --- MODIFICACIÓN DE VARIABLES SEGÚN CONTINGENCIA ---
    if escenario == "B: Arrastre Masivo de Líquidos (Tapón en Gasoducto)":
        presion = 6100.0
        nivel_sep = 94.5
        calidad_gas = 98.0
        st.error("🚨 ¡EMERGENCIA DE PROCESO! El Slug Catcher de entrada reporta inundación por bache de condensado de alta velocidad. Presión en alza.")
        
    elif escenario == "C: Descontrol Térmico en Reboiler de Regeneración":
        temp_reboiler = 215.0
        calidad_gas = 135.0
        st.error("🚨 ¡ALERTA OPERATIVA! El lazo de control de gas al quemador del reboiler quedó trabado al 100%. Temperatura fuera de control térmico.")
        
    else:
        st.success("🟢 Planta operando en condiciones estables. Monitoreo rutinario en curso.")

    # --- MATRIZ COGNITIVA DE TOMA DE DECISIONES (Evaluada antes de los indicadores para feedback dinámico) ---
    decision = None
    if escenario != "A: Planta Estable en Régimen Nominal":
        st.subheader("🤔 Diagnóstico de Contingencia y Acción Operativa")
        
        # Usamos una clave única (key) basada en el escenario para evitar conflictos de renderizado
        decision = st.radio(
            "Como operador a cargo del panel de control, ¿cuál es su acción inmediata?", 
            [
                "Monitorear las tendencias gráficas por 15 minutos para confirmar el error del sensor.",
                "Ejecutar el Cierre de Emergencia Manual (ESD/CDE) desde la consola para bloquear la planta y aislar los equipos del peligro.",
                "Puentear (Bypassear) la alarma de nivel del separador para evitar la parada total de la producción comercial."
            ], 
            index=None,
            key=f"radio_{escenario}"
        )
        
        # REACCIÓN EN TIEMPO REAL: Si el operador presiona CDE, alteramos las variables simuladas antes de que se muestren
        if decision and "Cierre de Emergencia Manual" in decision:
            if escenario == "B: Arrastre Masivo de Líquidos (Tapón en Gasoducto)":
                presion = 1200.0   # Bajó por despresurización de emergencia (Vent)
                nivel_sep = 94.5   # El líquido quedó retenido y contenido
            elif escenario == "C: Descontrol Térmico en Reboiler de Regeneración":
                temp_reboiler = 140.0 # El corte de gas de emergencia apagó el reboiler y empieza a enfriar

    st.markdown("---")
    
    # --- PANEL DE INDICADORES DIGITALES (Muestra el estado modificado por la acción) ---
    st.subheader("🎛️ Panel de Indicadores Digitales de Planta")
    col1, col2, col3, col4 = st.columns(4)
    
    # Lógicas dinámicas de las etiquetas Delta
    col1.metric("Presión Colector", f"{presion:.1f} kPa", 
              delta="SEGURO (VENT)" if (decision and "Cierre" in str(decision) and escenario == "B") else ("CRÍTICO" if presion >= cfg.PRESION_MAX_PLANTA else "Estable"))
    
    col2.metric("Nivel Separador", f"{nivel_sep:.1f} %", 
              delta="CONTENIDO (ESD)" if (decision and "Cierre" in str(decision) and escenario == "B") else ("DISPARO ESD" if nivel_sep >= cfg.NIVEL_MAX_SEPARADOR else "Normal"))
    
    col3.metric("Temperatura Reboiler", f"{temp_reboiler:.1f} °C", 
              delta="EN ENFRIAMIENTO" if (decision and "Cierre" in str(decision) and escenario == "C") else ("DEGRADACIÓN TEG" if temp_reboiler >= cfg.TEMP_MAX_REBOILER else "Normal"))
    
    col4.metric("Calidad Gas (Humedad)", f"{calidad_gas:.1f} mg/m³", 
              delta="FUERA DE ESPECIFICACIÓN" if calidad_gas > cfg.LIMITE_HUMEDAD else "OK")

    # --- MENSAJES DE FEEDBACK PEDAGÓGICO ---
    if decision:
        st.markdown("---")
        if "Cierre de Emergencia Manual" in decision:
            st.success("🎯 **Excelente resolución cognitiva.** De acuerdo con los manuales de seguridad operativa y la NAG-125, ante la inminencia de un daño mecánico catastrófico, la prioridad mandatoria es detener la planta en forma segura. *Observe en el panel superior cómo se estabilizaron los indicadores.*")
        else:
            st.error("❌ **Decisión Crítica Incorrecta.** Esa acción incrementará drásticamente la probabilidad de una ruptura de cañerías, explosión o destrucción mecánica de compresores. Las variables en el panel siguen en estado de peligro térmico o mecánico.")
