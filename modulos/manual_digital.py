# modulos/manual_digital.py
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import config as cfg

def render_manual():
    st.header("📚 Pilar 1: Manual Técnico Digital de Operaciones de Planta")
    st.caption("Enciclopedia avanzada de ingeniería de procesos, termodinámica y procedimientos operativos estándar.")
    st.markdown("---")
    
    capitulo = st.selectbox("Seleccione el módulo de ingeniería de detalle a estudiar:", [
        "Módulo I: Termodinámica del Gas, Hidratos y Ecuaciones de Estado",
        "Módulo II: Hidráulica de Separación de Entrada y Gestión Dinámica de Slugs",
        "Módulo III: Transferencia de Masa en Torres de TEG y Fenómenos Interfaciales",
        "Módulo IV: Criogenia Avanzada, Balances de Energía y Turboexpansión",
        "Módulo V: Dinámica de la Compresión, Curvas de Surge y Redes de Transporte",
        "Módulo VI: Filosofía de Protecciones, Lazos de Interlock y Norma NAG-125"
    ])
    
    st.markdown("---")
    
    # =========================================================================
    # MÓDULO I: TERMODINÁMICA, HIDRATOS Y ECUACIONES DE ESTADO
    # =========================================================================
    if "Módulo I" in capitulo:
        st.subheader("1.1 Ecuaciones de Estado (EOS) aplicadas al Gas Natural")
        st.write("""
        El comportamiento P-V-T (Presión, Volumen, Temperatura) del gas natural real se desvía de la ley de los gases ideales a presiones elevadas debido a las fuerzas de atracción y repulsión intermoleculares y al volumen propio de las moléculas. Para el modelado de plantas de gas y transporte, la industria emplea ecuaciones cúbicas de estado, siendo **Peng-Robinson (PR)** y **Soave-Redlich-Kwong (SRK)** las estándares.
        
        La ecuación cúbica de Peng-Robinson se expresa como:
        """)
        st.latex(r"P = \frac{R \cdot T}{V - b} - \frac{a(T)}{V \cdot (V + b) + b \cdot (V - b)}")
        st.write("""
        Donde $a(T)$ representa las fuerzas de atracción intermoleculares y $b$ es el co-volumen molecular. A partir de estas ecuaciones se calcula el **Factor de Compresibilidad ($Z$)**, crucial para la determinación del volumen real de despacho: $P \cdot V = Z \cdot n \cdot R \cdot T$.
        """)
        
        # Gráfica interactiva de código: Factor Z vs Presión
        st.markdown("#### 📈 Panel Interactivo: Factor de Compresibilidad $Z$")
        st.caption("Simulación del comportamiento de la desviación del gas ideal según la presión operativa a temperatura de colector.")
        
        p_rango = np.linspace(100, 10000, 100) # kPa
        z_rango = 1.0 - (p_rango * 0.00004) + (p_rango**2 * 2.5e-9)
        
        # Sanitización de datos para Plotly
        x_p = [float(p) for p in p_rango]
        y_z = [float(z) for z in z_rango]
        y_ideal = [1.0] * len(x_p)
        
        fig_z = go.Figure()
        fig_z.add_trace(go.Scatter(x=x_p, y=y_z, mode='lines', name='Gas Real (Predicción PR)', line=dict(color='#00CC96', width=3)))
        fig_z.add_trace(go.Scatter(x=x_p, y=y_ideal, mode='lines', name='Gas Ideal (Z=1)', line=dict(color='white', dash='dash')))
        fig_z.update_layout(
            title="Desviación de Compresibilidad (Factor Z) vs Presión", 
            xaxis_title="Presión Operativa (kPa)", 
            yaxis_title="Factor Z", 
            template="plotly_dark", 
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_z, use_container_width=True)
        
        st.subheader("1.2 Mecanismo de Formación y Disociación de Hidratos")
        st.write("""
        Los hidratos de gas son clatratos cristalinos estables. No se trata de la congelación del agua, sino de un cambio de fase termodinámico donde el agua actúa como "jaula" (huésped) reteniendo hidrocarburos livianos. 
        
        **Límites de Operación Segura:** Si el gas opera en el área derecha de la curva de equilibrio (Alta temperatura, baja presión), el agua libre permanece líquida y puede ser drenada. Si cruza a la izquierda, la cristalización obstruirá válvulas de control y cañerías de forma irreversible.
        """)

    # =========================================================================
    # MÓDULO II: HIDRÁULICA DE SEPARACIÓN Y GESTIÓN DE SLUGS
    # =========================================================================
    elif "Módulo II" in capitulo:
        st.subheader("2.1 Diseño Hidráulico y Tiempo de Residencia en Slug Catchers")
        st.write("""
        El diseño de un separador de entrada o Slug Catcher de tipo de dedos (Finger Type) o de recipiente horizontal responde a la capacidad de disipar la energía cinética del fluido multifásico entrante. 
        La separación de la fase líquida pesada se rige por el desprendimiento gravitacional. El criterio fundamental de diseño estructural es la **Ecuación de Souders-Brown**, que define la velocidad máxima permitida del gas para evitar el arrastre por cabeza (*Carry-over*):
        """)
        st.latex(r"v_{max} = K \cdot \sqrt{\frac{\rho_l - \rho_g}{\rho_g}}")
        st.write("""
        Donde $K$ es un factor empírico de diseño mecánico dependiente de la geometría interna y el uso de mallas desnebulizadoras (*Demister pads*).
        
        **Tiempo de Residencia:** El volumen de líquidos debe dimensionarse para retener el bache el tiempo suficiente para que las burbujas de gas atrapadas en el líquido migren hacia arriba (*Carry-under*), típicamente entre 5 y 10 minutos.
        """)
        
        st.markdown("#### 📈 Gráfica de Control: Velocidad Crítica de Souders-Brown")
        pressures = np.linspace(1000, 7000, 50)
        rho_g = pressures / (8.314 * 293) * 16  
        rho_l = 750.0  
        k_factor = 0.11  
        v_critica = k_factor * np.sqrt((rho_l - rho_g) / rho_g)
        
        # DataFrame limpio y estructurado para Streamlit nativo
        df_v = pd.DataFrame({
            "Presión Colector (kPa)": pressures,
            "Velocidad Límite del Gas (m/s)": v_critica
        }).set_index("Presión Colector (kPa)")
        
        st.line_chart(df_v)
        st.caption("A mayor presión de operación, la densidad del gas aumenta, disminuyendo la velocidad límite permitida dentro del separador para evitar el arrastre.")

        st.subheader("2.2 Procedimiento Operativo Estándar (SOP): Limpieza de Gasoductos (Scraping)")
        st.write("""
        Ante una corrida programada de un *scraper* (chancho de limpieza) en el gasoducto de alimentación, el operador de panel debe ejecutar el siguiente protocolo estricto:
        1. **Verificación de Inventario:** Deprimir el nivel operativo del slug catcher al mínimo técnico posible (ej. 15%-20%) para maximizar el volumen de amortiguación disponible.
        2. **Monitoreo de Presión Diferencial:** Observar el incremento de $\Delta P$ en el receptor de chanchos.
        3. **Control de Drenaje:** Seteo del lazo de control de nivel ($LIC$) en modo automático-asistido o manual al 80% de apertura de la $LCV$ de fondo para derivar el condensado hacia los tanques de estabilización en cuanto impacte el frente líquido.
        """)

    # =========================================================================
    # MÓDULO III: TRANSFERENCIA DE MASA EN TORRES DE TEG
    # =========================================================================
    elif "Módulo III" in capitulo:
        st.subheader("3.1 Cinética de Transferencia de Masa e Hidrodinámica")
        st.write("""
        La absorción del vapor de agua en el Trietilenglicol (TEG) es un proceso de transferencia de masa interfacil no reactivo. La tasa de transferencia está determinada por la ley de difusión y el número de platos teóricos de equilibrio (comúnmente entre 4 y 6 platos reales).
        
        La eficiencia de remoción de agua es directamente proporcional a la tasa de circulación del glicol pobre (típicamente de **1.5 a 3.0 galones de TEG por cada libra de agua a remover**) y a la pureza del glicol regenerado.
        """)
        
        st.markdown("#### 📈 Simulador de Sensibilidad: Tasa de Inyección de TEG")
        tasa_circ = st.slider("Tasa de Inyección de TEG (Galones/lb H2O):", 1.0, 4.0, 2.0, step=0.5)
        
        h_salida_sim = 120.0 / (tasa_circ * 1.8)
        
        # Protección ante configuraciones faltantes en config.py
        limite_h = getattr(cfg, "LIMITE_HUMEDAD", 64.0)
        
        st.metric("Humedad Estimada de Salida", f"{h_salida_sim:.1f} mg/m³", 
                  delta="DENTRO DE NORMA" if h_salida_sim <= limite_h else "FUERA DE ESPECIFICACIÓN",
                  delta_color="normal" if h_salida_sim <= limite_h else "inverse")

        st.subheader("3.2 Guía de Resolución de Fallas Críticas (Troubleshooting)")
        st.write("""
        * **Síntoma: Incremento repentino de la Humedad en el Gas de Venta ($>64 \\text{ mg/m}^3$)**
          1. *Causa:* Tasa de circulación de glicol insuficiente. *Acción:* Verificar amperaje y carrera de las bombas operativas (Kimray o eléctricas).
          2. *Causa:* Pérdida de eficiencia en el reboiler por ensuciamiento o baja temperatura. *Acción:* Comprobar que el set-point del quemador se ubique por encima de los $195^\\circ\\text{C}$ sin violar el límite de degradación de $204^\\circ\\text{C}$.
          3. *Causa:* Fenómeno de espumado en desarrollo. *Acción:* Monitorear la $\Delta P$ de la torre contactora. Si registra valores superiores a los de régimen nominal, inyectar dosificador antiespumante (tipo siliconado) a través del lazo de succión de la bomba.
        """)

    # =========================================================================
    # MÓDULO IV: CRIOGENIA AVANZADA Y TURBOEXPANSIÓN
    # =========================================================================
    elif "Módulo IV" in capitulo:
        st.subheader("4.1 Balance de Energía en Sistemas de Expansión Trabajo-Eje")
        st.write("""
        En las plantas criogénicas de extracción del Complejo Cerri, la turboexpansión representa el núcleo del proceso de fraccionamiento profundo. El balance de energía bajo flujo estacionario para el expansor operando de manera adiabática reversible (isentrópica) se modela mediante el salto de entalpía real:
        """)
        st.latex(r"\Delta H_{real} = \eta_{isentropica} \cdot (H_{entrada} - H_{salida, ideal})")
        st.write("""
        El trabajo mecánico extraído es transmitido rígiramente por un eje común hacia el compresor de carga (booster), el cual realiza una pre-compresión del gas residual de la torre demetinizadora, optimizando la eficiencia térmica global del sistema.
        """)
        
        st.markdown("#### 📈 Simulador de Caída de Temperatura Criogénica")
        eff_exp = st.slider("Eficiencia Isentrópica del Turboexpansor (%):", 65, 95, 85)
        
        p_in = 6000.0  
        p_out = np.linspace(1500, 4000, 50)
        t_out = 20.0 - (((p_in - p_out) / p_in) * 120.0 * (eff_exp / 100.0))
        
        # Conversión explícita a flotantes nativos para evitar ValueErrors en gráficos
        x_p_out = [float(p) for p in p_out]
        y_t_out = [float(t) for t in t_out]
        temp_critica = float(getattr(cfg, "TEMP_CRITICA_TURBOEXP", -100.0))
        y_limite = [temp_critica] * len(x_p_out)
        
        fig_criog = go.Figure()
        fig_criog.add_trace(go.Scatter(x=x_p_out, y=y_t_out, mode='lines', name='Temperatura Demetinizadora', line=dict(color='#1f77b4', width=3)))
        fig_criog.add_trace(go.Scatter(x=x_p_out, y=y_limite, mode='lines', name='Límite de Diseño de Materiales', line=dict(color='red', dash='dash')))
        fig_criog.update_layout(
            title="Temperatura Resultante vs Presión de Salida", 
            xaxis_title="Presión de Salida de Expansor (kPa)", 
            yaxis_title="Temperatura (°C)", 
            template="plotly_dark", 
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_criog, use_container_width=True)

    # =========================================================================
    # MÓDULO V: DINÁMICA DE LA COMPRESIÓN Y REDES DE TRANSPORTE
    # =========================================================================
    elif "Módulo V" in capitulo:
        st.subheader("5.1 Fenómeno de Surge (Bombeo) en Compresores Centrífugos")
        st.write("""
        El **Surge o Bombeo** es la inestabilidad aerodinámica más destructiva que puede sufrir un compresor centrífugo de gas. Ocurre cuando el caudal volumétrico de entrada cae por debajo de un valor crítico para una velocidad de rotación determinada, provocando que la contrapresión del gasoducto venza la fuerza de empuje de los álabes del rodete.
        
        El flujo de gas se invierte instantáneamente, circulando en sentido retrógrado (desde la descarga hacia la succión). Esto genera fluctuaciones violentas de presión, vibraciones axiales extremas, sobrecalentamiento de cojinetes y la destrucción mecánica total de los sellos de gas seco y álabes en cuestión de segundos.
        """)
        
        st.subheader("5.2 Filosofía del Lazo Anti-Surge y Válvula de Reciclo")
        st.write("""
        Para mitigar este riesgo, las estaciones compresoras cuentan con una línea de reciclo rápido equipada con una válvula de control de apertura ultrarrápida ($ASV$). El controlador anti-surge mide continuamente el caudal y la relación de presiones, manteniendo el punto de operación a la derecha de la **Línea de Límite de Surge (SLL)** mediante la apertura preventiva de la válvula para reinyectar gas de la descarga hacia la succión.
        """)

    # =========================================================================
    # MÓDULO VI: FILOSOFÍA DE PROTECCIONES Y NORMA NAG-125
    # =========================================================================
    elif "Módulo VI" in capitulo:
        st.subheader("6.1 Arquitectura del Sistema Instrumentado de Seguridad (SIS)")
        st.write("""
        De acuerdo con las exigencias legales dictaminadas por la norma **NAG-125**, las funciones instrumentadas de seguridad deben estar lógicamente desacopladas del Sistema de Control de Procesos Distribuido ($DCS$). Esto garantiza que ante una falla general de las pantallas de control o del procesador central, el PLC de seguridad (certificado bajo normas internacionales *SIL 2* o *SIL 3*) actúe de manera autónoma.
        
        **Lógica del Desenergizar para Disparar (Fail-Safe):** Todos los lazos de las válvulas de cierre de emergencia de planta ($SDV$) operan bajo el principio de seguridad inherente: si el sistema pierde alimentación eléctrica o presión de aire de instrumentos, los actuadores de resorte forzarán inmediatamente el cierre estanco de las válvulas para aislar la planta.
        """)
        
        st.subheader("6.2 Protocolos de Emergencia Operativa (ESD) ante Incidentes de Proceso")
        st.write("""
        * **Nivel Operacional de Parada 1 (ESD Total de Planta):** Bloqueo total de fronteras mediante el cierre inmediato de las $SDV$ de entrada de yacimientos y de despacho a gasoductos troncales. Desconexión instantánea de todas las unidades de compresión y apertura manual o automática de las $BDV$ (Blowdown valves) para despresurizar el inventario de gas retenido hacia la antorcha de forma segura en menos de 5 minutos.
        * **Nivel Operacional de Parada 2 (Aislamiento de Unidad):** Parada localizada de un compresor o tren térmico sin necesidad de despresurizar o aislar los módulos remotos de la planta.
        """)
