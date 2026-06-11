import streamlit as st

def render_manual():
    st.title("📘 Programa Académico y Manual del Operador")
    st.caption("Estructura curricular oficial del curso de formación para Operadores de Plantas de Tratamiento de Gas.")
    st.markdown("---")
    
    # Barra de progreso pedagógico basada en las unidades
    st.sidebar.markdown("### 🎓 Progreso del Curso")
    progreso = st.sidebar.slider("Unidades completadas:", 0, 8, 0)
    st.sidebar.progress(progreso / 8)
    
    st.subheader("📋 Contenido Curricular y Material de Soporte")
    st.write("Despliegue cada unidad para acceder al temario técnico y las referencias operativas.")
    
    # --- UNIDAD 1 ---
    with st.expander("1️⃣ Unidad 1: Introducción al Perfil Operativo", expanded=True):
        st.markdown("### 🎯 Explicación del curso dirigido al operador")
        st.write("""
        Este programa está diseñado para dotar al personal de planta de las competencias críticas necesarias para la toma de decisiones seguras y eficientes. 
        El objetivo es cerrar la brecha entre la teoría termodinámica y la intervención real en la consola SCADA.
        """)
        st.info("💡 **Conexión con el Simulador:** Utilice el *Panel de Control General* para familiarizarse con las variables analógicas de la planta antes de avanzar.")

    # --- UNIDAD 2 ---
    with st.expander("2️⃣ Unidad 2: Fundamentos del Flujo de Fluidos"):
        st.markdown("### 🧪 Conceptos Hidráulicos de Base")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Temario Teórico:**")
            st.markdown("""
            * **a) Estados de la materia:** Transiciones de fase gas, líquido y sólido (formación de hidratos).
            * **b) Peso específico:** Relación entre el peso de un volumen de fluido y su volumen unitario.
            * **c) Gravedad específica:** Densidad del gas/líquido respecto al aire/agua en condiciones estándar.
            """)
        with col2:
            st.markdown("**Aplicaciones y Presión Hidrostática:**")
            st.markdown("""
            * **d) Presión hidrostática:** $P = \rho \cdot g \cdot h$. Fundamental para entender el comportamiento y calibración de los transmisores de nivel por presión diferencial ($\Delta P$).
            * **e) Aplicaciones prácticas:** Pérdidas de carga en cañerías, cálculo de inventario en tanques y cabezales de succión.
            """)
            
        # Pequeña calculadora interactiva para fijar el concepto analítico de la unidad
        st.markdown("---")
        st.caption("🧮 **Mini-Laboratorio de la Unidad:** Cálculo de Presión Hidrostática en Domo de Líquidos")
        h = st.slider("Altura del líquido (m):", 0.5, 10.0, 3.0, step=0.5)
        densidad_liq = st.number_input("Densidad del condensado/agua (kg/m³):", value=800)
        p_hidro = (densidad_liq * 9.81 * h) / 1000 # Resultado en kPa
        st.metric("Presión Hidrostática Resultante en la Base:", f"{p_hidro:.2f} kPa")

    # --- UNIDAD 3 ---
    with st.expander("3️⃣ Unidad 3: Fases de la Industria del Gas Natural"):
        st.markdown("""
        ### 🌐 Contexto del Negocio del Gas
        * **a) Definición de gas natural:** Mezcla rica de hidrocarburos gaseosos (predominantemente Metano, $CH_4$) con presencia de impurezas ($CO_2$, $H_2S$, $N_2$ y agua).
        * **b) Historia de la industria:** Evolución tecnológica desde el venteo sistemático hasta la optimización moderna mediante plantas criogénicas de extracción de Líquidos del Gas Natural (LGN) y sistemas de transporte troncal integrados.
        """)

    # --- UNIDAD 4 ---
    with st.expander("4️⃣ Unidad 4: Separación de Fases (Separadores)"):
        st.markdown("### 🛢️ Operaciones Unitarias: Separadores Mecánicos")
        st.markdown("""
        * **a) Condiciones de operación:** Límites de presión y temperatura para evitar el arrastre de líquido (*carry-over*) o gasificación del líquido (*gas-coning*).
        * **b) Aplicaciones en planta:** Separadores de entrada (V-101), separadores bifásicos y trifásicos, filtros coalescentes de alta eficiencia.
        * **c) Componentes internos críticos:**
            * Deflector de entrada (*Slug catcher* o placas de choque).
            * Extractores de niebla (*Demisters* o mallas coalescentes).
            * Rompedores de vórtice en las salidas de líquido.
        """)
        st.warning("🔗 **Práctica en Simulador:** Modifique las variables del módulo **'Separación de Entrada'** para observar cómo impacta el nivel del domo en la estabilidad del proceso downstream.")

    # --- UNIDAD 5 ---
    with st.expander("5️⃣ Unidad 5: Extracción de Líquidos del Gas Natural"):
        st.markdown("### ❄️ Control de Punto de Rocío (Dew Point) y Acondicionamiento")
        st.markdown("""
        * **a) Condiciones del proceso:** Control de temperatura mediante refrigeración mecánica (propano) o caídas auto-refrigerantes (Efecto Joule-Thomson / Turboexpansores).
        * **b) Aplicación industrial:** Ajuste de poder calorífico e índice de Wobbe para cumplir las normativas de transporte, y maximización de la recuperación de etano, propano y butano comercial.
        * **c) Componentes del sistema:** Intercambiadores de tubo y coraza (Gas/Gas, Gas/Líquido), Chiller de propano y separador frío.
        """)

    # --- UNIDAD 6 ---
    with st.expander("6️⃣ Unidad 6: Fraccionamiento del Gas Natural"):
        st.markdown("### 🗼 Columnas de Destilación")
        st.markdown("""
        * **a) Procesos de fraccionamiento:** Separación de los componentes de la mezcla de LGN por diferencias en sus puntos de ebullición bajo presión.
        * **Torres en serie:**
            * **Deetanizadora:** Separa el $C_2$ (Etano) por el tope.
            * **Depropanizadora:** Separa el $C_3$ (Propano).
            * **Debutanizadora:** Separa el $C_4$ (Butano) dejando gasolina natural por el fondo.
        """)

    # --- UNIDAD 7 ---
    with st.expander("7️⃣ Unidad 7: Sistemas de Compresión y Turbinas"):
        st.markdown("### ⚙️ Turbomaquinaria y Potencia de Planta")
        st.markdown("""
        * **a) Componentes principales:** Compresores centrífugos, álabes de la turbina de gas (generador de gas y turbina de potencia), sistema de combustible, lazos de control anti-surge.
        * **b) Aplicaciones críticas:** Re-compresión de gas residual para inyección directa a gasoductos troncales de despacho de alta presión.
        """)

    # --- UNIDAD 8 ---
    with st.expander("8️⃣ Unidad 8: Seguridad Operacional e Industrial"):
        st.markdown("### 🛡️ Preservación de la Integridad Física y de Planta")
        st.markdown("""
        * **a) Factores de riesgo:** Presencia de atmósferas explosivas (ATEX), toxicidad por gas ácido ($H_2S$), sobrepresiones catastróficas, radiación térmica en antorcha.
        * **b) Equipos de Protección Personal (EPP):** Uso obligatorio de ropa ignífuga, calzado dieléctrico/antideslizante, protección auditiva de alta atenuación, detectores portátiles multigas ($LEL / O_2 / CO / H_2S$) y equipos de respiración autónoma (ERA) para contingencias en áreas confinadas.
        """)
        st.error("🚨 **Criterio de Aprobación:** Es mandatorio que el operador domine los procedimientos de parada de emergencia (ESD) disponibles en los sistemas IIoT.")
