# modulos/manual_digital.py
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import config as cfg

def render_manual():
    st.header("📚 Pilar 1: Manual Técnico Digital de Operaciones de Planta")
    st.caption("Enciclopedia avanzada de ingeniería de procesos, termodinámica de hidrocarburos y filosofías instrumentadas de seguridad.")
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
        * **Parámetro $a(T)$:** Representa las fuerzas de atracción intermoleculares de la mezcla.
        * **Parámetro $b$:** Representa el **co-volumen molecular**, que es el espacio físico mínimo e infranqueable ocupado por las propias moléculas de gas real, restándoselo al espacio libre disponible.
        
        A partir de estas ecuaciones se calcula el **Factor de Compresibilidad ($Z$)**: $P \cdot V = Z \cdot n \cdot R \cdot T$. Cuando las fuerzas de atracción molecular predominan, el factor Z cae por debajo de 1.0 ($Z < 1$), facilitando la compresión del gas. A presiones extremas (superiores a 7000 kPa), la precisión de las EOS cúbicas disminuye, prefiriéndose para transferencias de custodia el modelo de coeficientes de virial extendido **AGA8**.
        
        Adicionalmente, la presencia de componentes intermedios y pesados ($C_3, C_4$) expande considerablemente la envolvente de fases de la mezcla, desplazando la **cricondembara** y la región de dos fases hacia valores de presión y temperatura sustancialmente más elevados.
        """)
        
        # Gráfica interactiva: Factor Z vs Presión
        st.markdown("#### 📈 Panel Interactivo: Factor de Compresibilidad $Z$")
        st.caption("Simulación de la desviación del gas ideal según la presión operativa a temperatura de colector.")
        
        p_rango = np.linspace(100, 10000, 100) # kPa
        z_rango = 1.0 - (p_rango * 0.00004) + (p_rango**2 * 2.5e-9)
        
        # Sanitización explícita para evitar ValueErrors en Plotly
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
        
        st.subheader("1.2 Mecanismo de Formación e Inhibición de Hidratos")
        st.write("""
        Los hidratos de gas son clatratos cristalinos estables. No se trata de la congelación del agua, sino de un cambio de fase termodinámico donde el agua actúa como "jaula" (huésped) reteniendo hidrocarburos livianos. 
        
        **Efecto de la Presión:** El aumento de presión en el Colector de Entrada eleva la temperatura de formación de hidratos, desplazando el equilibrio operativo hacia la zona de riesgo. 
        
        **Estrategias de Mitigación:**
        * **Inhibidores Termodinámicos (Metanol / MEG):** Rompen los puentes de hidrógeno del agua líquida, desplazando de raíz la curva de equilibrio hacia temperaturas mucho más frías (zonas seguras).
        * **Inhibidores Cinéticos (KHI):** Polímeros que no alteran la termodinámica, sino que se adhieren a los microcristales retardando significativamente su nucleación y crecimiento mecánico.
        """)

    # =========================================================================
    # MÓDULO II: HIDRÁULICA DE SEPARACIÓN Y GESTIÓN DE SLUGS
    # =========================================================================
    elif "Módulo II" in capitulo:
        st.subheader("2.1 Diseño Hidráulico y Fenómenos de Arrastre")
        st.write("""
        La separación primaria en los recipientes mecánicos o en los **Slug Catchers tipo 'Finger' (de dedos)** aprovecha la segregación gravitatoria a lo largo de cañerías paralelas con pendiente descendente. El criterio estructural e hidráulico para evitar fallas críticas se rige por la **Ecuación de Souders-Brown**, que calcula la velocidad máxima permitida del gas ($v_{max}$) para evitar el arrastre por cabeza (*Carry-over*):
        """)
        st.latex(r"v_{max} = K \cdot \sqrt{\frac{\rho_l - \rho_g}{\rho_g}}")
        st.write("""
        * **Efecto de una Sobrepresión:** Si la presión en la línea se eleva, la densidad del gas ($\rho_g$) aumenta, disminuyendo la diferencia $(\rho_l - \rho_g)$. Esto reduce la velocidad límite permitida ($v_{max}$) y exige regular el caudal total de entrada para mantener la eficiencia de separación.
        
        **Fenómenos Críticos de Operación:**
        * **Carry-over (Arrastre por cabeza):** Gotas líquidas suspendidas escapan por el tope de gas, saturando la malla desnebulizadora (*Demister Pad*). Si el demister se obstruye por sales o parafinas, la presión diferencial ($\Delta P$) medida entre la entrada y salida subirá drásticamente.
        * **Carry-under (Arrastre por fondo):** Burbujas de gas quedan atrapadas e inundan la fase líquida saliente. Ocurre por un bajo tiempo de residencia o niveles operativos deficientes en el fondo del separador.
        * **Deflector de Entrada (Inlet Deflector):** Dispositivo mecánico encargado de reducir bruscamente el momento lineal del fluido multifásico entrante, logrando una pre-separación gruesa y direccionando los líquidos hacia el fondo de acumulación de forma balanceada.
        """)
        
        st.markdown("#### 📈 Gráfica de Control: Velocidad Crítica de Souders-Brown")
        pressures = np.linspace(1000, 7000, 50)
        rho_g = pressures / (8.314 * 293) * 16  
        rho_l = 750.0  
        k_factor = 0.11  
        v_critica = k_factor * np.sqrt((rho_l - rho_g) / rho_g)
        
        df_v = pd.DataFrame({
            "Presión Colector (kPa)": pressures,
            "Velocidad Límite del Gas (m/s)": v_critica
        }).set_index("Presión Colector (kPa)")
        
        st.line_chart(df_v)
        st.caption("A mayor presión de operación, la densidad del gas aumenta, disminuyendo la velocidad límite permitida dentro del separador para evitar el arrastre.")

    # =========================================================================
    # MÓDULO III: TRANSFERENCIA DE MASA EN TORRES DE TEG
    # =========================================================================
    elif "Módulo III" in capitulo:
        st.subheader("3.1 Cinética de la Deshidratación por Trietilenglicol (TEG)")
        st.write("""
        La absorción del vapor de agua en el TEG es un proceso de transferencia de masa interfacial no reactivo. La tasa de transferencia normalizada exige una tasa de circulación equilibrada (típicamente **de 1.5 a 3.0 galones de TEG por cada libra de agua a remover**). 
        
        Una tasa de circulación excesiva ($> 4.5\\text{ gal/lb }H_2O$) causa una severa sobrecarga térmica en el reboiler, aumenta el consumo de combustible y eleva el arrastre perjudicial de compuestos orgánicos volátiles (VOCs) en las líneas de venteo.
        
        **Dinámica de Equipos del Lazo:**
        1. **Torre Contactora:** El gas húmedo fluye en contracorriente con el glicol pobre. La temperatura del glicol de entrada debe mantenerse estrictamente **entre 3 °C y 5 °C por encima de la temperatura del gas**. Si entra más frío, inducirá la condensación indeseada de hidrocarburos gaseosos, provocando el fenómeno de **espumado (foaming)**.
        2. **Flash Drum (Tanque de Flasheo):** Opera a baja presión (300-500 kPa) retirando por descompresión los hidrocarburos gaseosos disueltos en el glicol rico antes de que ingresen al tren térmico.
        3. **Reboiler y Columna de Regeneración:** El reboiler debe operar en un rango estricto de **195 °C a 202 °C**. Superar los $204^\\circ\\text{C}$ destruye térmicamente la molécula de TEG. Para alcanzar purezas superiores al 99.5%, se inyecta **Stripping Gas** en la base de la columna para reducir la presión parcial del vapor de agua y forzar el despojamiento molecular definitivo.
        """)
        
        st.markdown("#### 📈 Simulador de Sensibilidad: Tasa de Inyección de TEG")
        tasa_circ = st.slider("Tasa de Inyección de TEG (Galones/lb H2O):", 1.0, 4.0, 2.0, step=0.5)
        h_salida_sim = 120.0 / (tasa_circ * 1.8)
        limite_h = float(getattr(cfg, "LIMITE_HUMEDAD", 64.0))
        
        st.metric("Humedad Estimada de Salida", f"{h_salida_sim:.1f} mg/m³", 
                  delta="DENTRO DE NORMA" if h_salida_sim <= limite_h else "FUERA DE ESPECIFICACIÓN",
                  delta_color="normal" if h_salida_sim <= limite_h else "inverse")

        st.subheader("3.2 Resolución de Anomalías de Proceso (Troubleshooting)")
        st.write("""
        * **Fenómeno de Espumado (Foaming):** Causado por el ingreso de hidrocarburos líquidos pesados, condensados o químicos de pozo que alteran la tensión interfacial del solvente. Eleva bruscamente la $\\Delta P$ de la torre y genera un masivo arrastre por cabeza. *Acción operativa:* Inyectar dosificador antiespumante siliconado a la succión.
        * **Falla de Bomba Kimray:** Las impurezas mecánicas o la obstrucción en los filtros de partículas de la succión traban las agujas y sellos internos del bloque piloto de las bombas Kimray (accionadas por el propio glicol rico), deteniendo el ciclo hidráulico por completo.
        """)

    # =========================================================================
    # MÓDULO IV: CRIOGENIA AVANZADA Y TURBOEXPANSIÓN
    # =========================================================================
    elif "Módulo IV" in capitulo:
        st.subheader("4.1 Balances Térmicos y Expansión Isentrópica")
        st.write("""
        La turboexpansión representa el núcleo del proceso de extracción profunda de Líquidos del Gas Natural (LGN). A diferencia de una válvula Joule-Thomson (JT), que realiza una expansión isentálpica irreversible (sin extracción de trabajo), el turboexpansor ejecuta una **expansión isentrópica con extracción de trabajo útil**. El balance de energía bajo flujo estacionario responde a:
        """)
        st.latex(r"\Delta H_{real} = \eta_{isentropica} \cdot (H_{entrada} - H_{salida, ideal})")
        st.write("""
        Si el operador reduce la eficiencia isentrópica cerrando parcialmente los álabes (toberas de entrada), se genera entropía y el gas retiene calor latente, haciendo que la temperatura resultante sea más alta de lo planificado y limitando drásticamente la recuperación de propano y butano.
        
        **Requisitos Críticos del Gas de Entrada:**
        * **Límite Extremo de Humedad:** El gas debe ser deshidratado en camas fijas de **Tamices Moleculares (Zeolita 4A)** hasta valores menores a **1 ppm de agua** (Punto de rocío $< -100^\\circ\\text{C}$). Una planta de TEG convencional solo llega a $\\sim 64\\text{ mg/m}^3$ ($-15^\\circ\\text{C}$), lo que causaría el bloqueo total por hielo de los canales del intercambiador compacto.
        * **Especificación de CO2:** La concentración de CO2 molar debe ser estrictamente regulada ($< 0.5\\%-1.0\\%$). A temperaturas criogénicas inferiores a $-60^\\circ\\text{C}$, el CO2 supera su límite de solubilidad y **sublima formando hielo seco**, taponando los canales del **Cold Box**.
        * **Hidrocarburos Pesados ($C_6+$):** Su presencia en el gas genera la solidificación y formación de geles cerosos a temperaturas frías, inhabilitando las mallas coalescedoras de los separadores criogénicos.
        
        **Intercambiadores Cold Box y Booster:** Se emplean bloques compactos de aluminio soldado por su masiva densidad de área de transferencia y aproximaciones térmicas estrechas ($< 2^\\circ\\text{C}$). El trabajo del eje se acopla rígidamente a un compresor **Booster** que pre-comprime el gas residual saliente de la Demetinizadora, optimizando la eficiencia de la planta.
        """)
        
        st.markdown("#### 📈 Simulador de Caída de Temperatura Criogénica")
        eff_exp = st.slider("Eficiencia Isentrópica del Turboexpansor (%):", 65, 95, 85)
        p_in = 6000.0  
        p_out = np.linspace(1500, 4000, 50)
        t_out = 20.0 - (((p_in - p_out) / p_in) * 120.0 * (eff_exp / 100.0))
        
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
        st.subheader("5.1 Fenómenos de Inestabilidad Aerodinámica: Surge y Choke")
        st.write("""
        Las turbocompresoras instaladas en las redes de transporte están sujetas a límites hidrodinámicos estrictos descritos en sus mapas de performance:
        
        * **Fenómeno de Surge (Bombeo):** Ocurre si el punto operativo cruza a la izquierda de la **Línea de Límite de Surge (SLL)** por falta de caudal volumétrico. La contrapresión del gasoducto vence el empuje de los álabes del rodete y el flujo de gas se invierte instantáneamente circulando de forma retrógrada. Esto produce fluctuaciones violentas y oscilaciones cíclicas que inducen un severo **desplazamiento microscópico del eje (vibración axial)**, destruyendo los cojinetes de empuje (*Tilting Pad Bearings*) y los sellos de gas seco en segundos.
        * **Fenómeno de Choke (Stone Wall):** Representa el punto de caudal máximo admisible a la derecha de la curva, donde la velocidad del gas en el ojo del impulsor alcanza la velocidad del sonido (**Mach 1**), provocando ondas de choque internas y la caída vertical de la eficiencia.
        
        **Filosofía de Control e Instrumentación de Soporte:**
        * **Lazo Anti-Surge:** Regula la apertura automatizada y ultrarrápida de la Válvula de Reciclo Rápido ($ASV$) para reinyectar gas de la descarga caliente (previa refrigeración) hacia la succión, forzando un aumento del caudal real por encima del límite crítico.
        * **Separador de Succión (Scrubber):** Equipo mandatorio instalado aguas arriba de la succión. Elimina cualquier bache o traza de líquido libre. Al ser los líquidos fluidos incompresibles, el impacto de una gota contra un impulsor girando a miles de RPM causa erosión inmediata y la destrucción mecánica total del rodete por desbalance dinámico.
        * **Sellos de Gas Seco (Dry Gas Seals):** Actúan como barreras de contención entre el eje rotante y la carcasa presurada utilizando gas de proceso ultrafiltrado de alta pureza. Operan por ranuras dinámicas sin contacto físico, evitando fugas de hidrocarburos a la atmósfera o contaminación con el aceite de lubricación.
        * **Aeroenfriadores Interetapa (Intercoolers):** El proceso de compresión eleva fuertemente la temperatura por trabajo termodinámico. El enfriamiento interetapa reduce el volumen específico del gas, minimizando la potencia requerida para la siguiente etapa de compresión en serie y resguardando los límites mecánicos de los materiales.
        """)

    # =========================================================================
    # MÓDULO VI: FILOSOFÍA DE PROTECCIONES Y NORMA NAG-125
    # =========================================================================
    elif "Módulo VI" in capitulo:
        st.subheader("6.1 Arquitectura SIS y Filosofía de Diseño Fail-Safe")
        st.write("""
        Bajo las exigencias dictaminadas por la norma nacional **NAG-125**, los esquemas de protección automatizada de planta deben responder a directrices internacionales de alta disponibilidad:
        
        * **Independencia de Sistemas:** El **Sistema Instrumentado de Seguridad (SIS)** debe estar lógica y físicamente desacoplado del Sistema de Control de Procesos Distribuido ($DCS$). Utiliza hardware dedicado y certificado (PLC de Seguridad con niveles de confianza *SIL 2* o *SIL 3*) asegurando que los lazos de parada actúen de manera autónoma e infalible aunque falle el control diario de pantallas en la sala de operaciones.
        * **Lógica del Desenergizar para Disparar (Fail-Safe):** Todos los lazos operan bajo el principio de seguridad inherente. Si hay pérdida total de energía eléctrica o aire de instrumentos en la planta, los actuadores de resorte mecánico forzarán de inmediato el posicionamiento seguro de los activos: las **Válvulas de Bloqueo de Frontera ($SDV$)** cerrarán herméticamente (*Fail-Close*) para confinar áreas operativas, mientras que las **Válvulas de Despresurización ($BDV$)** abrirán por completo (*Fail-Open*) para aliviar y derivar los inventarios de gas retenidos hacia la antorcha en menos de 5 minutos.
        * **Lógica de Votación Coincidente (2oo3):** Los instrumentos de variables críticas de proceso (como transmisores de presión o nivel) se instalan por triplicado. El PLC de seguridad ejecutará el disparo de emergencia solo si al menos dos de los tres sensores independientes validan de forma simultánea la condición de alarma, equilibrando la mitigación de riesgos con la prevención de paradas espurias.
        * **Pruebas de Recorrido Parcial (Partial Stroke Testing - PST):** Práctica que permite mover una válvula de corte crítico ($SDV$) una fracción pequeña de su carrera (ej. 10%-15%) durante la operación normal de planta. Esto verifica que el actuador y el vástago no estén bloqueados o agarrotados mecánicamente, incrementando la disponibilidad del lazo sin interrumpir la producción de gas.
        
        **Protocolo de Parada de Emergencia Nivel 1 (ESD Nivel 1):** Es la máxima acción de resguardo operativo ante catástrofes. Involucra el bloqueo automático y estanco de las fronteras de ingreso de yacimientos, parada instantánea de todas las unidades de compresión y trenes de proceso, seguido de la apertura masiva de las $BDV$ para vaciar de forma segura y controlada la energía acumulada en las instalaciones de la planta.
        """)
