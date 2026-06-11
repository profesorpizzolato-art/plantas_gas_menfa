# modulos/manual_digital.py
import streamlit as st

def render_manual():
    st.title("📘 Manual Técnico de Procesos y Programa de Estudio")
    st.caption("Guía de ingeniería interactiva para el operador de plantas de tratamiento de gas.")
    st.markdown("---")

    unidades_programa = [
        "Capítulo 1: Introducción y Perfil del Operador",
        "Capítulo 2: Flujo de Fluidos e Hidráulica",
        "Capítulo 3: Fases y Composición de la Industria del Gas",
        "Capítulo 4: Sistemas de Separación Mecánica de Fases",
        "Capítulo 5: Extracción de Líquidos (Control de Dew Point)",
        "Capítulo 6: Fraccionamiento del Gas Natural",
        "Capítulo 7: Turbinas y Compresión de Despacho",
        "Capítulo 8: Seguridad Operacional, Riesgos y EPP"
    ]
    
    capitulo = st.selectbox("Seleccione el capítulo del Manual a estudiar:", unidades_programa)
    st.markdown(f"## {capitulo}")
    st.markdown("---")

    if "Capítulo 1" in capitulo:
        st.write("""
        ### 1.1 Explicación del curso dirigido al operador
        Este manual técnico interactivo constituye la base del conocimiento operativo de la **Suite MENFA**. 
        El fin último de este entrenamiento es comprender las leyes de la física y la termodinámica para operarlas de forma segura y eficiente desde la consola de control.
        """)
        st.info("💡 **Aprender haciendo:** Cada decisión de diseño tomada en este manual alterará de forma inmediata las lecturas analógicas del SCADA.")

    elif "Capítulo 2" in capitulo:
        st.write("""
        ### 2.1 Fundamentos de Hidráulica de Fluidos
        * **Estados de la materia:** Transiciones críticas gas-líquido y el riesgo de congelamiento latente por hidratos de carbono.
        * **Peso y Gravedad Específica:** Relación de densidades respecto a fluidos de referencia en condiciones estándar de presión y temperatura.
        * **Presión Hidrostática:** La presión ejercida por una columna estática de líquido está definida por la ecuación fundamental:
        """)
        st.latex(r"P_{hidro} = \rho \cdot g \cdot h")
        
        st.markdown("#### 🔬 Laboratorio en Vivo: Simulación de Transmisor de Nivel por ΔP")
        h_manual = st.slider("Ajustar nivel físico del tanque de almacenamiento (m):", 0.0, 10.0, 4.5)
        densidad_manual = st.number_input("Densidad del Hidrocarburo Líquido Estabilizado (kg/m³):", value=750)
        
        # Cálculo dinámico directo
        p_calc = (densidad_manual * 9.81 * h_manual) / 1000.0
        st.metric("Presión medida en la celda de fondo del tanque:", f"{p_calc:.2f} kPa")
        
        # Guardamos en la memoria global para que impacte en los módulos de nivel
        st.session_state['nivel_liquido'] = (h_manual / 10.0) * 100.0

    elif "Capítulo 3" in capitulo:
        st.write("""
        ### 3.1 Fases de la Industria del Gas Natural
        * **Definición de Gas Natural:** Mezcla gaseosa rica en metano ($CH_4$), clasificada comercialmente como gas dulce o agrio, seco o húmedo según la presencia de contaminantes e hidrocarburos pesados.
        * **Historia:** Evolución del procesamiento del gas desde simples purgas mecánicas hasta las complejas técnicas de fraccionamiento molecular actuales.
        """)

    elif "Capítulo 4" in capitulo:
        st.write("""
        ### 4.1 Condiciones y Componentes de un Separador (V-101)
        Para evitar el arrastre de líquido (*Carry-over*) hacia las plantas de endulzamiento y deshidratación, el gas debe mantener una velocidad menor a la velocidad de asentamiento por gravedad.
        """)
        st.markdown("**Componentes internos analizados:**\n1. Deflector de entrada\n2. Placas coalescentes\n3. Extractor de niebla (*Demister*)")
        
        st.markdown("#### 🛠️ Inyección de Carga Operativa a Planta")
        # El manual le permite al alumno alterar las variables duras de entrada de la planta
        st.session_state['caudal_gas'] = st.slider("Fijar Caudal del Gas de Yacimiento (MMm³/día):", 1.0, 15.0, float(st.session_state['caudal_gas']))

    elif "Capítulo 5" in capitulo:
        st.write("""
        ### 5.1 Extracción de Líquidos del Gas Natural
        El acondicionamiento del gas para transporte exige controlar el punto de rocío de hidrocarburos (*Dew Point*) y agua. Esto se logra disminuyendo drásticamente la temperatura en el Chiller mediante refrigeración mecánica o expansión Joule-Thomson.
        """)
        
        st.markdown("#### ❄️ Inyección de Falla Térmica")
        if st.button("🚨 Provocar Falla en Sistema de Inyección de Glicol (Simular Tapón por Hidratos)"):
            st.session_state['falla_hidratos_activa'] = True
            st.session_state['humedad_salida'] = 95.0
            st.warning("Escenario crítico inyectado. La humedad en la salida se disparará por congelamiento del intercambiador.")

    elif "Capítulo 6" in capitulo:
        st.write("""
        ### 6.1 Procesos de Fraccionamiento de LGN
        Las columnas de destilación fraccionan el condensado aprovechando las diferencias en los puntos de ebullición de los componentes ($C_2$, $C_3$, $C_4$).
        """)
        st.markdown("#### 🗼 Alteración de la Pureza de Fondo desde el Manual")
        st.session_state['c2_en_glp'] = st.slider("Fijar concentración de etano retenido en fondo de torre (% mol):", 0.1, 5.0, float(st.session_state['c2_en_glp']))

    elif "Capítulo 7" in capitulo:
        st.write("""
        ### 7.1 Turbinas y Compresión Centrífuga
        Las turbinas de gas aportan la potencia necesaria en el eje para acoplar compresores de despacho de alta presión, requiriendo el monitoreo permanente de la línea de control anti-surge.
        """)
        st.markdown("#### ⚙️ Inyección de Contingencia Mecánica")
        if st.button("💥 Forzar Caída Súbita de Presión en Línea Troncal (Inyectar Surge)"):
            st.session_state['falla_surge_activa'] = True
            st.session_state['p_descarga_gasoducto'] = 4200.0

    elif "Capítulo 8" in capitulo:
        st.write("""
        ### 8.1 Seguridad Operacional y Factores de Riesgo en Plantas de Gas
        Análisis de riesgos asociados a altas presiones, atmósferas explosivas (ATEX) y gases altamente tóxicos.
        """)
        st.markdown("**EPP Requerido:** Ropa ignífuga, protectores auditivos, calzado de seguridad con puntera compuesta y detector multigas portátil.")
