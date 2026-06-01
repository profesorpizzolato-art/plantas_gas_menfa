# modulos/guias_rapidas.py
import streamlit as st

def render_guias_rapidas():
    st.header("📖 Guías Rápidas de Campo y Glosario Técnico Bilingüe")
    st.caption("Fichas de consulta operativa basadas en la terminología estandarizada de la industria (English / Español).")
    st.markdown("---")

    # --- BUSCADOR / SELECTOR DE EQUIPOS PRINCIPALES ---
    st.subheader("🔍 Fichas Técnicas de Equipos e Instrumentación")
    
    categoria = st.tabs(["🛢️ Upstream & Separación", "💧 Tratamiento & Procesos", "🌀 Compresión & Bombas"])
    
    with categoria[0]:
        st.markdown("##### Glosario Crítico de Entrada")
        equipo_up = st.selectbox("Seleccione el componente a revisar (Upstream):", [
            "Production Separator (Separador de Producción)",
            "Choke Valve (Válvula de Estrangulamiento / Estricción)",
            "Basic Sediment and Water - BS&W (Corte de Agua y Sedimentos)",
            "Emulsion Breaker / Demulsifier (Desemulsificante)"
        ])
        
        if "Production Separator" in equipo_up:
            st.info("**Terminología:** *Production Separator* ➡️ Separador de Producción (V-101).")
            st.markdown("""
            * **Función Operativa:** Recipiente de presión horizontal o vertical diseñado para segregar los fluidos del pozo en fases (Gas, Petróleo, Agua) por diferencia de densidades y gravedad.
            * **Parámetro Clave:** Controlar el tiempo de residencia. Un nivel excesivo provoca *Carry-over* (arrastre de líquido al gas).
            """)
        elif "Choke Valve" in equipo_up:
            st.info("**Terminología:** *Choke Valve* ➡️ Válvula de estrangulamiento, estricción o 'estrangulador'.")
            st.markdown("""
            * **Función Operativa:** Restringe el paso del fluido en la cabeza del pozo o línea de entrada para controlar el caudal de producción y reducir la presión del yacimiento a la presión segura de la planta.
            * **Efecto de Campo:** Alta restricción genera cizallamiento severo, favoreciendo la formación de emulsiones mecánicas estables si hay baja temperatura.
            """)
        elif "BS&W" in equipo_up:
            st.info("**Terminología:** *BS&W (Basic Sediment and Water)* ➡️ Porcentaje de agua libre y sedimentos suspendidos en el crudo.")
            st.markdown("""
            * **Importancia:** Define el tratamiento necesario en los separadores trifásicos. Un BS&W elevado (como en campos con empuje hidráulico activo) satura la capacidad de drenaje del fondo del vessel.
            """)
        elif "Demulsifier" in equipo_up:
            st.info("**Terminología:** *Demulsifier / Emulsion Breaker* ➡️ Desemulsificante / Rompedor de Emulsión.")
            st.markdown("""
            * **Función Operativa:** Agente químico tensoactivo que se dosifica aguas arriba del separador. Debilita la película interfacial de las gotas de agua dispersas en el petróleo, acelerando la coalescencia y decantación rápida del agua libre.
            """)

    with categoria[1]:
        st.markdown("##### Glosario de Plantas de Gas")
        equipo_proc = st.selectbox("Seleccione el componente a revisar (Procesos):", [
            "Contactor Tower / Absorber (Torre Contactora / Absorbedora)",
            "Reboiler (Rehervidor / Calentador)",
            "Stripping Gas (Gas de Despojamiento)",
            "Foaming (Espumado del Solvente)"
        ])
        
        if "Contactor Tower" in equipo_proc:
            st.info("**Terminología:** *Contactor Tower / Glycol Absorber* ➡️ Torre Contactora o Absorbedora de Glicol.")
            st.markdown("""
            * **Función Operativa:** Recipiente vertical de platos o empaque donde el gas húmedo fluye en contracorriente ascendente y entra en contacto íntimo con el TEG pobre descendente, que absorbe el vapor de agua.
            """)
        elif "Reboiler" in equipo_proc:
            st.info("**Terminología:** *Reboiler* ➡️ Rehervidor.")
            st.markdown("""
            * **Función Operativa:** Unidad térmica de regeneración. Suministra calor al glicol rico (cargado de agua) para evaporar el agua residual a base de sus diferentes puntos de ebullición, devolviendo el TEG a concentraciones superiores al 98%.
            """)
        elif "Stripping Gas" in equipo_proc:
            st.info("**Terminología:** *Stripping Gas* ➡️ Gas de despojamiento o agotamiento.")
            st.markdown("""
            * **Función Operativa:** Gas seco inyectado en el fondo del reboiler para reducir la presión parcial del vapor de agua, permitiendo sobrepasar el equilibrio termodinámico térmico ordinario y obtener glicol ultra-puro (hasta 99.9%).
            """)
        elif "Foaming" in equipo_proc:
            st.info("**Terminología:** *Foaming* ➡️ Espumado.")
            st.markdown("""
            * **Condición de Falla:** Expansión e incremento volumétrico anómalo del glicol dentro de la torre por contaminación (sal, crudo, compuestos químicos). Provoca una pérdida súbita de transferencia de masa y un disparo severo de la presión diferencial ($\Delta P$).
            """)

    with categoria[2]:
        st.markdown("##### Glosario de Sistemas Mecánicos")
        equipo_comp = st.selectbox("Seleccione el componente a revisar (Compresión):", [
            "Centrifugal Compressor (Compresor Centrífugo)",
            "Surge / Compressor Impeller (Bombeo Aerodinámico / Rodete)",
            "Anti-Surge Valve - ASV (Válvula Anti-Surge)",
            "Intercooler / Aftercooler (Aeroenfriador Interetapa o Descarga)"
        ])
        
        if "Centrifugal Compressor" in equipo_comp:
            st.info("**Terminología:** *Centrifugal Compressor* ➡️ Compresor Centrífugo.")
            st.markdown("""
            * **Función Operativa:** Máquina rotativa dinámica que transfiere energía cinética al gas mediante álabes en movimiento, transformándola en energía de presión estática al pasar por el difusor.
            """)
        elif "Surge" in equipo_comp:
            st.info("**Terminología:** *Surge (Compressor Surge)* ➡️ Bombeo aerodinámico / Inestabilidad de flujo inverso.")
            st.markdown("""
            * **Fenómeno Crítico:** Fenómeno altamente destructivo que ocurre cuando el caudal disminuye excesivamente o la contrapresión supera la fuerza de empuje del rodete (*impeller*), provocando el retroceso violento del gas y oscilaciones de vibración axial severas en el eje.
            """)
        elif "Anti-Surge Valve" in equipo_comp:
            st.info("**Terminología:** *Anti-Surge Valve (ASV)* ➡️ Válvula de control anti-bombeo / Reciclo rápido.")
            st.markdown("""
            * **Lazo Instrumentado:** Lazo automático de protección *Fail-Open*. Ante la proximidad al límite de Surge, abre la ASV para reciclar gas desde la descarga hacia la succión, incrementando la masa en el rodete para mantener al equipo en zona segura.
            """)
        elif "Intercooler" in equipo_comp:
            st.info("**Terminología:** *Intercooler / Aeroenfriador* ➡️ Intercambiador de calor de tubos y aletas.")
            st.markdown("""
            * **Propósito Térmico:** Enfría el gas entre etapas de compresión. Reduce la temperatura para contraer el volumen específico del fluido, optimizando la densidad del gas y disminuyendo drásticamente la potencia mecánica absorbida ($BHP$) requerida por el impulsor.
            """)

    st.markdown("---")
    
    # --- SECCIÓN DE ENLACE PEDAGÓGICO ---
    st.subheader("💡 Tips para la Evaluación de Alumnos")
    st.markdown("""
    Cuando evalúes las maniobras en el simulador, recordá exigirles que justifiquen sus decisiones usando los nombres normalizados:
    1. Que no digan "la válvula de desvío", que identifiquen la **ASV (Anti-Surge Valve)**.
    2. Que correlacionen el aumento de la **$\Delta P$ (Differential Pressure)** en la contactora con el fenómeno de **Foaming**.
    3. Que monitoreen las condiciones del **Vessel (Recipiente)** de entrada ante variaciones bruscas del **BS&W**.
    """)
