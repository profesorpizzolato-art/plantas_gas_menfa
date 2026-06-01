# app.py
import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Suite MENFA - Simulador de Producción y Plantas de Gas",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INICIALIZACIÓN DEL ESTADO GLOBAL (MEMORIA DINÁMICA DE LA PLANTA) ---
if 'p_entrada' not in st.session_state:
    st.session_state['p_entrada'] = 3500.0  # kPa
if 't_entrada' not in st.session_state:
    st.session_state['t_entrada'] = 22.0    # °C
if 'nivel_liquido' not in st.session_state:
    st.session_state['nivel_liquido'] = 45.0 # %
if 'humedad_salida' not in st.session_state:
    st.session_state['humedad_salida'] = 24.5 # mg/m³
if 'p_descarga_gasoducto' not in st.session_state:
    st.session_state['p_descarga_gasoducto'] = 6100.0 # kPa

# --- IMPORTACIÓN SEGURA DE MÓDULOS DE INGENIERÍA ---
try:
    from modulos.separacion import render_separacion
    from modulos.procesamiento import render_procesamiento
    from modulos.calidad_medicion import render_calidad_medicion
    from modulos.servicios_auxiliares import render_servicios
    from modulos.guias_rapidas import render_guias_rapidas
    from modulos.evaluacion import render_evaluacion
except ImportError as e:
    st.error(f"⚠️ Error de consistencia en arquitectura modular: {e}")
    st.stop()
    # --- MENÚ LATERAL CON IDENTIDAD CORPORATIVA MENFA ---
st.sidebar.image("logo_menfa.png", use_container_width=True)
st.sidebar.title("🎛️ Matriz Operativa")

# Diccionario para agrupar visualmente en el Selectbox
opciones_menu = {
    "🏭 MÓDULOS DE PROCESO Y PLANTA": [
        "Panel Control General",
        "Separación de Entrada",
        "Planta Criogénica y LGN",
        "Calidad y Medición (ENARGAS)",
        "Servicios Auxiliares & IIoT"
    ],
    "📘 SOPORTE Y ENTRENAMIENTO ACADÉMICO": [
        "1. Manual Técnico Digital",
        "2. Guías Rápidas de Campo",      
        "3. Sistema de Evaluación",
        "4. Entrenamiento Normativo",
        "5. Entrenamiento Cognitivo"
    ]
}

# Planificar la lista plana para el selectbox manteniendo los encabezados
lista_desplegable = []
for categoria, subitems in opciones_menu.items():
    lista_desplegable.append(f"--- {categoria} ---")
    lista_desplegable.extend(subitems)

# Render del Selectbox único
seleccion_cruda = st.sidebar.selectbox("Seleccione el Entorno de Trabajo:", lista_desplegable)

# Lógica de bloqueo: si eligen un encabezado decorativo, por defecto va al Panel General
if seleccion_cruda.startswith("---"):
    seccion = "Panel Control General"
else:
    seccion = seleccion_cruda

st.sidebar.markdown("---")
st.sidebar.info("📌 **Control de Gestión:** Suite MENFA parametrizada bajo normas de transporte y seguridad industrial argentina (ENARGAS).")
# =====================================================================
# --- RUTEO LOGÍSTICO Y DESPLIEGUE DE PESTAÑAS ---
# =====================================================================

if seccion == "Panel Control General":
    st.title("🖥️ Consola Central SCADA - Suite MENFA")
    st.caption("Resumen ejecutivo del estado de las variables de proceso y lazos cerrados de control de la planta.")
    st.markdown("---")
    
    # Matriz de KPI en tiempo real
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Presión de Entrada (V-101)", f"{st.session_state['p_entrada']:.1f} kPa")
    col2.metric("Nivel Domo Líquidos", f"{st.session_state['nivel_liquido']:.1f} %")
    col3.metric("Humedad Control ENARGAS", f"{st.session_state['humedad_salida']:.1f} mg/m³")
    col4.metric("Presión Despacho Troncal", f"{st.session_state['p_descarga_gasoducto']:.1f} kPa")
    
    st.markdown("### 🗺️ Diagrama de Flujo de Procesos (PFD)")
    st.info("💡 **Indicación al Operador:** Seleccione un módulo de la barra lateral para intervenir las variables analógicas o gestionar los escenarios de contingencia de las cuencas.")

elif seccion == "Separación de Entrada":
    p_op, t_op, niv_op = render_separacion()
    st.session_state['p_entrada'] = p_op
    st.session_state['t_entrada'] = t_op
    st.session_state['nivel_liquido'] = niv_op

elif seccion == "Planta Criogénica y LGN":
    render_procesamiento(st.session_state['p_entrada'], st.session_state['t_entrada'])

elif seccion == "Calidad y Medición (ENARGAS)":
    render_calidad_medicion()

elif seccion == "Servicios Auxiliares & IIoT":
    render_servicios()

# =====================================================================
# --- MANUAL TÉCNICO DIGITAL EXHAUSTIVO DE PROCESOS ---
# =====================================================================
elif seccion == "1. Manual Técnico Digital":
    st.title("📘 Manual Técnico de Ingeniería de Procesos y Operaciones")
    st.caption("Documentación oficial de diseño, ecuaciones fundamentales de control y matrices de enclavamiento de la Suite MENFA.")
    st.markdown("---")
    
    # Índice modularizado de alta densidad teórica
    m_tabs = st.tabs([
        "🛢️ Cap. 1: Separación Primaria", 
        "💧 Cap. 2: Absorción y Deshidratación", 
        "❄️ Cap. 3: Termodinámica Criogénica", 
        "🌀 Cap. 4: Turbocompresión y Dinámica",
        "🛡️ Cap. 5: Protocolos de Custodia ENARGAS"
    ])
    
    # --- CAPÍTULO 1 ---
    with m_tabs[0]:
        st.header("Capítulo 1: Separación de Entrada y Dinámica del Subsuelo")
        st.markdown("""
        El comportamiento hidrodinámico del separador horizontal primario (V-101) responde directamente a la caracterización física y energética del subsuelo según los lineamientos de *El Pozo Ilustrado*. 
        """)
        
        col_c1_1, col_c1_2 = st.columns(2)
        with col_c1_1:
            st.subheader("1.1 Parámetros de Diseño y Leyes de Asentamiento")
            st.markdown("""
            El volumen útil está dimensionado para garantizar un **tiempo de residencia mínimo ($\tau$) de 3 a 5 minutos**, permitiendo que la diferencia de densidades segregue las fases y evitando el fenómeno de arrastre de líquido en la corriente de gas (*Carry-over*).
            
            La velocidad de diseño del gas para impedir que gotas de líquido mayores a 150 micrones alcancen el tope del recipiente se rige por la ecuación de Saunders-Brown:
            """)
            st.latex(r"V_c = K \cdot \sqrt{\frac{\rho_L - \rho_G}{\rho_G}}")
            st.caption("Donde $K$ representa el factor empírico del extractor de niebla (*mist extractor*), y $\rho_L, \rho_G$ son las densidades de las fases líquida y gaseosa.")
            
        with col_c1_2:
            st.subheader("1.2 Mecanismos de Empuje y Modos de Falla")
            st.markdown("""
            * **Empuje Hidráulico Activo (*Water Drive*):** Provoca un incremento severo y progresivo del *BS&W* (Corte de agua y sedimentos), pudiendo superar la capacidad nominal de descarga de la válvula de fondo (LCV-101) e inundar el equipo.
            * **Cizallamiento Mecánico y Emulsiones:** La restricción brusca en la *Choke Valve* de entrada genera una caída entálpica. Si la temperatura decae por debajo del punto de escurrimiento de parafinas (**< 20°C**), se forma una emulsión agua-en-petróleo ($W/O$) altamente estable.
            * **Mitigación Operativa:** Requiere la dosificación controlada de agentes desemulsificantes (*Demulsifiers*) para alterar la tensión interfacial y forzar la coalescencia acelerada.
            """)
            
        st.markdown("---")
        st.subheader("📋 Matriz de Causa y Efecto - Enclavamientos de Entrada (ESD-101)")
        st.table({
            "Instrumento / Lazo": ["LSHH-101 (Nivel Muy Alto)", "LSLL-101 (Nivel Muy Bajo)", "PSHH-101 (Presión Muy Alta)"],
            "Umbral Crítico": ["> 85 % del volumen útil", "< 15 % del volumen útil", "> 5500 kPa"],
            "Acción de Seguridad Automatizada": [
                "Cierre mandatorio de la SDV (Válvula de Bloqueo de Emergencia) de entrada a planta para evitar la destrucción hidrodinámica de los compresores por arrastre de líquido.",
                "Cierre de la LCV de fondo para evitar que el gas escape por la línea de líquidos hacia los tanques atmosféricos (Gas Blowby).",
                "Apertura secuencial de la BDV (Blowdown Valve) de alivio térmico hacia la antorcha (Flare) y parada de emergencia de los pozos aportantes."
            ]
        })

    # --- CAPÍTULO 2 ---
    with m_tabs[1]:
        st.header("Capítulo 2: Deshidratación de Gas Natural por Absorción (TEG)")
        st.markdown("""
        La remoción de vapor de agua en fase gaseosa se fundamenta en los perfiles de transferencia de masa de columnas de platos de copas de burbujeo (*Bubble Cap Trays*) analizados en los compendios de deshidratación de *Dialnet*.
        """)
        
        col_c2_1, col_c2_2 = st.columns(2)
        with col_c2_1:
            st.subheader("2.1 Operación de la Torre Contactora")
            st.markdown("""
            El gas húmedo asciende desde el fondo entrando en íntimo contacto a contracorriente con el Trietilanglicol (TEG) pobre dosificado por el tope con una pureza inicial mínima del **99.0%**.
            
            * **Tasa de Circulación Estándar:** Regulada entre **1.5 y 3.0 galones de TEG por cada libra de agua** extraída. Un caudal bajo satura el glicol y saca al gas de especificación; un exceso provoca inundación mecánica de platos.
            * **Presión Diferencial ($\Delta P$):** Rango normal de operación de **5 a 15 kPa**. Un incremento súbito es indicativo crítico de **Foaming (Espumado del solvente)** por arrastre de hidrocarburos pesados o degradación química de la solución.
            """)
            
        with col_c2_2:
            st.subheader("2.2 Unidad de Regeneración Térmica (Reboiler)")
            st.markdown("""
            La reconcentración del glicol rico se realiza por adición de energía térmica, aprovechando que el agua evapora a $100^\circ\text{C}$ y el TEG puro a $285^\circ\text{C}$.
            
            * **Punto de Consigna Térmico:** Fijado estrictamente en **$200^\circ\text{C}$**.
            * **Límite de Degradación Estructural:** Si el lazo de control falla y supera los **$204^\circ\text{C}$**, se produce el craqueo térmico (*Thermal Cracking*) del glicol, generando subproductos ácidos corrosivos y polímeros carbonosos que arruinan la capacidad de absorción.
            * **Stripping Gas:** Inyección de gas seco de agotamiento en la base de la columna de regeneración para abatir la presión parcial del vapor de agua, posibilitando purezas de TEG ultra-pobres del **99.9%**.
            """)

    # --- CAPÍTULO 3 ---
    with m_tabs[2]:
        st.header("Capítulo 3: Procesamiento Criogénico y Fraccionamiento de Líquidos (LGN)")
        st.markdown("""
        El ajuste fino del Punto de Rocío de Hidrocarburos (*Cricondenterm*) y la obtención de subproductos comerciales ligeros se rige por las especificaciones termodinámicas industriales compiladas por *Techint*.
        """)
        
        st.subheader("3.1 Expansión Isentrópica mediante Turboexpander")
        st.markdown("""
        Para forzar temperaturas criogénicas inferiores a los **-40°C**, el simulador modela una transformación isentrópica (entropía constante) donde el gas realiza un trabajo mecánico de expansión sobre los álabes de una turbina de expansión radial, cediendo calor latente en el proceso:
        """)
        st.latex(r"\Delta T_{real} = T_1 \cdot \left[1 - \left(\frac{P_2}{P_1}\right)^{\frac{\gamma - 1}{\gamma}}\right] \cdot \eta_{tx}")
        st.caption("Donde $P_1, T_1$ representan las condiciones operativas de succión, $P_2$ la presión en el separador frío, $\gamma$ el coeficiente adiabático y $\eta_{tx}$ la eficiencia mecánica del rodete.")
        
        col_c3_1, col_c3_2 = st.columns(2)
        with col_c3_1:
            st.markdown("##### Desviación de Rutas Termodinámicas:")
            st.markdown("""
            * **Modo Turboexpander (Eficiencia Nominal):** Máxima transferencia de energía. El gas licúa de forma masiva las fracciones pesadas, logrando recuperaciones de etano/propano de hasta el **95-98%**. El gas de cabeza resultante es metano puro ($C_1$) de alta calidad.
            * **Modo Válvula Joule-Thomson (Contingencia/Trip):** Expansión isoentálpica (entalpía constante) simple sin extracción de trabajo. La caída de temperatura es mucho menor. La planta pierde un 60% de su capacidad de recuperación de líquidos, dejando pasar hidrocarburos ricos no acondicionados al gasoducto troncal.
            """)
            
        with col_c3_2:
            st.subheader("3.2 Tren de Destilación Fraccionada")
            st.markdown("""
            Los condensados obtenidos en el separador de baja temperatura (LTS) se procesan en torres de fraccionamiento acopladas:
            * **Torre Deetandizadora (*Deethanizer*):** El reboiler opera en la banda de **82°C a 95°C** para rechazar por cabeza el Metano y Etano excedentes. Si la temperatura cae, el etano permanece retenido en el fondo, contaminando el lote y violando la especificación comercial de presión de vapor de los productos subsiguientes.
            * **Torre Debutanizadora (*Debutanizer*):** Regula los perfiles térmicos y la tasa de reflujo para separar de forma limpia el **GLP** comercial (mezcla normalizada de Propano y Butano de acuerdo al glosario técnico de *Weatherford*).
            """)

    # --- CAPÍTULO 4 ---
    with m_tabs[3]:
        st.header("Capítulo 4: Turbocompresión Dinámica y Control del Surge")
        st.markdown("""
        La restitución energética para el transporte a grandes distancias emplea modelos de compresión centrífuga regulados bajo las especificaciones de diseño mecánico de *Plantas Compresoras*.
        """)
        
        col_c4_1, col_c4_2 = st.columns(2)
        with col_c4_1:
            st.subheader("4.1 Aerodinámica del Impulsor y Densidad de Succión")
            st.markdown("""
            El rodete centrífugo entrega energía cinética al fluido, la cual es transformada en energía de presión estática en el difusor. La potencia requerida en el eje ($BHP$) depende de la masa compactada.
            
            * **Falla de Aeroenfriadores (*Aftercoolers/Intercoolers*):** Si los ventiladores fallan y la temperatura del gas de succión se eleva, el fluido se expande volumétricamente perdiendo densidad. La máquina se ve exigida a absorber una mayor potencia mecánica ($BHP$) para intentar mantener la relación de compresión, provocando sobrecalentamiento axial y fatiga de cojinetes.
            """)
            
        with col_c4_2:
            st.subheader("4.2 El Fenómeno del Surge (Bombeo Aerodinámico)")
            st.markdown("""
            El **Surge** es la condición inestable más destructiva en máquinas dinámicas. Ocurre si el caudal de entrada cae por debajo del límite aerodinámico requerido para contrarrestar la presión de descarga.
            
            Al perderse el flujo mínimo, la contrapresión del gasoducto vence la fuerza del impulsor, provocando la **inversión violenta del flujo de gas** en dirección a la succión. Esto desata oscilaciones cíclicas extremas de presión, caídas bruscas de RPM y una **vibración axial severa** que destruye los laberintos, álabes y sellos de gas seco.
            
            * **Válvula Anti-Surge (ASV):** Lazo de control automático instrumentado *Fail-Open*. Calcula en tiempo real la proximidad a la línea de bombeo y, ante un desvío, abre la ASV para reciclar gas caliente de la descarga hacia la succión, restituyendo de inmediato la masa en el rodete.
            """)

    # --- CAPÍTULO 5 ---
    with m_tabs[4]:
        st.header("Capítulo 5: Especificaciones Fiscales y Transferencia de Custodia (ENARGAS)")
        st.markdown("""
        Los parámetros de despacho de gas procesado en la República Argentina están estrictamente regulados por el marco legal y las especificaciones de calidad del **ENARGAS**.
        """)
        
        st.subheader("5.1 Tabla de Parámetros de Calidad Obligatorios")
        st.markdown("""
        Cualquier lectura por fuera de los rangos habilitados faculta al centro de despacho nacional a emitir un **Acta de Rechazo Inyección Comercial**, obligando a la clausura neumática de la planta y la aplicación de penalizaciones contractuales.
        """)
        
        st.table({
            "Parámetro Controlado": ["Humedad Remanente (Vapor de Agua)", "Cricondenterm (Punto de Rocío HC)", "Poder Calorífico Superior (PCS)", "Inertes Totales (CO₂ + N₂)"],
            "Límite Legal Exigido": ["<= 65 mg/m³", "<= -2 °C a presión de operación", "8850 a 10200 kcal/m³", "<= 3.5 % molar"],
            "Fundamento de Ingeniería de la Norma": [
                "Evitar la precipitación de agua libre y la consecuente solidificación de hidratos de gas que obstruyen las cañerías, así como prevenir la corrosión ácida por $CO_2$.",
                "Garantizar que no existan condensaciones de hidrocarburos líquidos en fase gaseosa dentro de las líneas de transporte troncales, suprimiendo golpes de líquido en compresores de ruta.",
                "Estabilizar el valor calórico neto transferido para asegurar una combustión controlada en la red de distribución urbana y residencial.",
                "Optimizar y resguardar la capacidad útil disponible de transporte de masa real dentro del sistema interconectado."
            ]
        })
        
        st.subheader("5.2 Escenarios Geográficos y Operación de Gasoductos Troncales")
        st.markdown("""
        * **Gasoducto Néstor Kirchner (GPNK - Vaca Muerta):** Operación en presiones hidrodinámicas extremas en cabecera (**$8200 - 9500\text{ kPa}$**). Al transportar gas asociado rico de la *Cuenca Neuquina*, la planta criogénica debe sostener una máxima remoción de pesados para evitar la condensación retrógrada en la línea.
        * **Gasoducto San Martín (TGS - Cuenca Austral):** Atraviesa geografías hostiles con temperaturas de suelo patagónico promedio de **4°C**. Si la humedad saliente de la torre contactora supera los $65\text{ mg/m}^3$, el gasoducto sufrirá taponamiento físico por congelamiento e hidratos en los cruces de cuenca.
        * **Estacionalidad de Demanda Invernal:** Ante el "Pico de Invierno", el despacho nacional prioriza de manera absoluta la inyección volumétrica bruta para el consumo prioritario domiciliario. Se penalizan severamente las paradas imprevistas y se flexibiliza marginalmente la extracción de licuables para favorecer el empuje de gas hacia los centros urbanos.
        """)

# --- CONTINUACIÓN DEL BLOQUE PEDAGÓGICO ---

elif seccion == "2. Guías Rápidas de Campo":
    render_guias_rapidas()

elif seccion == "3. Sistema de Evaluación":
    render_evaluacion()

elif seccion == "4. Entrenamiento Normativo":
    st.title("📜 4. Entrenamiento Normativo & Regulatorio")
    st.caption("Módulo de adiestramiento en legislación técnica y resoluciones del ENARGAS.")
    st.markdown("---")
    st.info("💡 **Marco de Aplicación Nacional:** En este espacio los alumnos se entrenan bajo las especificaciones de calidad de la NAG-100 y resoluciones vigentes para la entrega conforme de gas natural a los gasoductos de transporte interconectados.")

elif seccion == "5. Entrenamiento Cognitivo":
    st.title("🧠 5. Entrenamiento Cognitivo y Análisis de Fallas")
    st.caption("Simulación de escenarios complejos ocultos para el desarrollo del criterio operativo.")
    st.markdown("---")
    st.warning("⚠️ **Módulo Avanzado:** Espacio diseñado para inyectar fallas encadenadas en la planta (ej: pérdida de señal de telemetría IIoT coincidente con un golpe de bomba en el Upstream), obligando al operador a diagnosticar la raíz del problema mediante telemetría desactualizada.")
