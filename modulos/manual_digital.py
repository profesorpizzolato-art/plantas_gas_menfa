import streamlit as st
import numpy as np

def render_manual():
    st.title("🎓 Programa Analítico Interactivo: Aprender Haciendo")
    st.caption("Interactúe con los parámetros físicos de cada unidad temática para comprender el comportamiento real de la planta.")
    st.markdown("---")

    # --- CONTROL DE PROGRESO PEDAGÓGICO ---
    if 'unidad_actual' not in st.session_state:
        st.session_state['unidad_actual'] = "1. Introducción"

    st.sidebar.markdown("### 🗺️ Hoja de Ruta del Operador")
    unidades = [
        "1. Introducción", "2. Flujo de Fluidos", "3. Fases de la Industria",
        "4. Separadores", "5. Extracción de Líquidos", "6. Fraccionamiento",
        "7. Turbocompresión", "8. Seguridad Operacional"
    ]
    
    idx_actual = unidades.index(st.session_state['unidad_actual'])
    unidad_sel = st.sidebar.radio("Ir a la Unidad:", unidades, index=idx_actual)
    st.session_state['unidad_actual'] = unidad_sel
    
    st.sidebar.progress((unidades.index(unidad_sel) + 1) / len(unidades))

    # =========================================================================
    # UNIDAD 1: INTRODUCCIÓN
    # =========================================================================
    if unidad_sel == "1. Introducción":
        st.header("1️⃣ Unidad 1: El Rol del Operador de Planta de Gas")
        st.markdown("""
        El operador no es un mero observador del SCADA; es quien gestiona la energía y la seguridad del sistema. 
        En este simulador, cada acción que tome en las pestañas teóricas afectará las variables globales de la planta.
        """)
        
        st.subheader("🚀 Ejercicio de Inducción: Reconocimiento del SCADA")
        st.write("Modifique las variables iniciales de la planta para verificar la respuesta del sistema:")
        
        col1, col2 = st.columns(2)
        with col1:
            p_init = st.slider("Presión de Entrada General (kPa):", 2000.0, 5000.0, float(st.session_state['p_entrada']), step=100.0)
            st.session_state['p_entrada'] = p_init
        with col2:
            t_init = st.slider("Temperatura de Entrada General (°C):", 10.0, 50.0, float(st.session_state['t_entrada']), step=1.0)
            st.session_state['t_entrada'] = t_init

        st.info("📊 **Efecto en Planta:** Si va ahora a la *Consola Central SCADA*, verá que los indicadores principales cambiaron según los valores que acaba de setear.")

    # =========================================================================
    # UNIDAD 2: FLUJO DE FLUIDOS
    # =========================================================================
    elif unidad_sel == "2. Flujo de Fluidos":
        st.header("2️⃣ Unidad 2: Fundamentos Físicos y Presión Hidrostática")
        st.write("Aprenda cómo la densidad y la altura generan presión hidrostática, el principio clave para medir niveles en los tanques de la planta.")
        
        st.markdown("### 🧮 Laboratorio Hidráulico: Calibración de Transmisor de Nivel (LT)")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            temperatura_fluido = st.slider("Temperatura del Fluido (°C):", 10, 60, 25)
            # Simulación del cambio de densidad del agua/condensado con la temperatura
            densidad_base = 800.0 - (temperatura_fluido - 15) * 0.8 
            st.metric("Densidad Calculada (ρ)", f"{densidad_base:.1f} kg/m³")
            
            altura_m = st.slider("Altura real del nivel (metros):", 0.0, 6.0, 3.0, step=0.1)
        
        with col2:
            # Fórmula física de presión hidrostática: P = rho * g * h
            presion_hidro_kPa = (densidad_base * 9.81 * altura_m) / 1000.0
            
            st.markdown("**Cálculo Analítico en Tiempo Real:**")
            st.latex(r"P_{hidrost\acute{a}tica} = \rho \cdot g \cdot h")
            st.latex(f"{presion_hidro_kPa:.2f} \\text{{ kPa}} = {densidad_base:.1f} \\text{{ kg/m³}} \\cdot 9.81 \\text{{ m/s²}} \\cdot {altura_m:.1f} \\text{{ m}}")
            
            # Sincronizar el nivel porcentual con el estado global de la planta (capacidad máxima del tanque = 6m)
            porcentaje_nivel = (altura_m / 6.0) * 100.0
            st.session_state['nivel_liquido'] = porcentaje_nivel
            st.metric("Nivel Enviado al SCADA:", f"{porcentaje_nivel:.1f} %")

    # =========================================================================
    # UNIDAD 3: FASES DE LA INDUSTRIA
    # =========================================================================
    elif unidad_sel == "3. Fases de la Industria":
        st.header("3️⃣ Unidad 3: Composición del Gas Natural")
        st.write("El gas natural es una mezcla. Mueva la composición para ver cómo impacta en el Peso Molecular Medio ($M_m$) y en la Gravedad Específica ($G_g$).")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🧪 Cromatografía del Gas")
            c1 = st.slider("Metano (C1) % mól:", 70.0, 95.0, 85.0)
            c2 = st.slider("Etano (C2) % mól:", 3.0, 15.0, 8.0)
            c3 = st.slider("Propano (C3) % mól:", 1.0, 8.0, 4.0)
            co2 = st.slider("Dióxido de Carbono (CO2) % mól:", 0.0, 5.0, 3.0)
            
            # Normalización rápida para la matemática
            suma = c1 + c2 + c3 + co2
            st.caption(f"Suma de componentes ingresados: {suma:.1f}%")
        
        with col2:
            st.subheader("📊 Propiedades de la Mezcla")
            # Pesos moleculares individuales
            mw_c1, mw_c2, mw_c3, mw_co2 = 16.04, 30.07, 44.1, 44.01
            # Cálculo de Peso Molecular Medio
            mw_mezcla = (c1*mw_c1 + c2*mw_c2 + c3*mw_c3 + co2*mw_co2) / suma
            # Gravedad específica (respecto al aire = 28.96 g/mol)
            sg_gas = mw_mezcla / 28.96
            
            st.metric("Peso Molecular Medio ($M_m$):", f"{mw_mezcla:.2f} g/mol")
            st.metric("Gravedad Específica del Gas (Aire=1):", f"{sg_gas:.3f}")
            
            if sg_gas > 0.65:
                st.warning("⚠️ **Gas Rico/Pesado:** Alto contenido de licuables. Requiere atención estricta en los separadores de entrada para evitar arrastres líquidos.")
            else:
                st.success("✅ **Gas Pobre/Liviano:** Mayormente metano. Comportamiento estable para transporte directo pre-endulzamiento.")

    # =========================================================================
    # UNIDAD 4: SEPARADORES
    # =========================================================================
    elif unidad_sel == "4. Separadores":
        st.header("4️⃣ Unidad 4: Operación de Separadores de Entrada (V-101)")
        st.write("Manipule las condiciones del separador para entender el fenómeno de arrastre de líquido (*Carry-over*).")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🎮 Controles de Proceso V-101")
            v_gas = st.slider("Caudal de Gas de Entrada (MMm³/día):", 1.0, 10.0, 5.0, step=0.5)
            apertura_lv = st.slider("Apertura Válvula de Control de Nivel (LV) %:", 0, 100, 45)
        
        with col2:
            st.subheader("🚨 Diagnóstico de Internos")
            # Simulación matemática del arrastre por velocidad crítica de Souders-Brown simplificada
            velocidad_gas = v_gas * 1.2
            nivel_actual = float(st.session_state['nivel_liquido'])
            
            # Lógica interactiva combinada
            if nivel_actual > 85.0 and velocidad_gas > 8.0:
                st.error("🚨 **CRÍTICO: CARRY-OVER INMINENTE.** El nivel del domo sobrepasó el extractor de niebla (*demister*). Hay arrastre masivo de hidrocarburo líquido hacia la planta criogénica.")
            elif nivel_actual > 70.0:
                st.warning("⚠️ **Alerta de Alto Nivel:** Espacio de separación de fases reducido. Reduzca el caudal de entrada o abra la válvula LV.")
            elif apertura_lv == 0 and velocidad_gas > 5.0:
                st.warning("⚠️ **Nivel acumulándose rápidamente:** Válvula de purga cerrada por completo.")
            else:
                st.success("✅ **Operación Nominal:** Velocidad de gas por debajo del límite crítico. Separación eficiente de fases.")
                
            st.progress(nivel_actual / 100.0)
            st.caption(f"Nivel actual medido en el domo: {nivel_actual:.1f} %")

    # =========================================================================
    # UNIDAD 5: EXTRACCIÓN DE LÍQUIDOS (DEW POINT)
    # =========================================================================
    elif unidad_sel == "5. Extracción de Líquidos":
        st.header("5️⃣ Unidad 5: Planta Criogénica y Control de Humedad")
        st.write("Regule el rendimiento del Chiller para cumplir con las especificaciones de entrega de gas seco a gasoducto.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("❄️ Control de Temperatura de Refrix")
            t_chiller = st.slider("Temperatura de Salida del Chiller (°C):", -40.0, 10.0, -15.0, step=1.0)
        
        with col2:
            st.subheader("📉 Calidad del Gas Resultante")
            # Relación física simulada: menor temperatura, menor humedad remanente en el gas
            humedad_calculada = max(2.0, 65.0 * np.exp(0.06 * t_chiller))
            st.session_state['humedad_salida'] = humedad_calculada
            
            st.metric("Contenido de Agua en Gas Residual:", f"{humedad_calculada:.1f} mg/m³")
            
            # Validación ENARGAS (Límite contractual típico argentino: 65 mg/m³)
            if humedad_calculada > 65.0:
                st.error("🚨 **FUERA DE NORMA (ENARGAS):** El gas supera los 65 mg/m³. Rechazo automático en cabecera de gasoducto.")
            elif humedad_calculada > 40.0:
                st.warning("⚠️ **Alerta operativa:** Margen de seguridad reducido. Baje la temperatura del Chiller inmediatamente.")
            else:
                st.success("✅ **Calidad Certificada:** Gas óptimo para transporte troncal sin riesgo de congelamiento.")

    # =========================================================================
    # UNIDAD 6: FRACCIONAMIENTO
    # =========================================================================
    elif unidad_sel == "6. Fraccionamiento":
        st.header("6️⃣ Unidad 6: Control de la Torre Deetanizadora")
        st.write("Interactúe con el perfil térmico de la torre de destilación para separar el Etano ($C_2$) del Gas Licuado del Petróleo (GLP).")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🔥 Balance Térmico")
            t_reboiler = st.slider("Temperatura del Reboiler (Fondo) °C:", 60.0, 110.0, 85.0, step=0.5)
            p_torre = st.number_input("Presión Operativa de la Torre (kPa):", value=2800.0)
        
        with col2:
            st.subheader("🗼 Pureza del Producto de Fondo")
            # Simulación de equilibrio líquido-vapor
            c2_en_fondo = max(0.1, 15.0 - (t_reboiler - 60.0) * 0.3)
            
            st.metric("Contenido de C2 (Etano) en el fondo:", f"{c2_en_fondo:.2f} % mol")
            
            if c2_en_fondo > 2.0:
                st.error("❌ **Producto Fuera de Especificación:** Demasiado etano retenido en el fondo. Aumente la energía térmica del reboiler para vaporizarlo.")
            else:
                st.success("✅ **Especificación Comercial Alcanzada:** Separación limpia. El producto de fondo cumple con la volatilidad requerida para la etapa de Depropanizadora.")

    # =========================================================================
    # UNIDAD 7: TURBOCOMPRESIÓN
    # =========================================================================
    elif unidad_sel == "7. Turbocompresión":
        st.header("7️⃣ Unidad 7: Compresión de Despacho y Curva de Surge")
        st.write("Evite el fenómeno destructivo del *Surge* (bombeo inverso) regulando el caudal y las RPM de la turbina.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("⚙️ Parámetros de Operación del Compresor")
            rpm = st.slider("Velocidad de la Turbina (RPM):", 5000, 11000, 8500, step=100)
            caudal_comp = st.slider("Caudal de paso por el compresor (m³/h):", 1000, 5000, 3200, step=100)
        
        with col2:
            st.subheader("🛡️ Sistema Anti-Surge")
            # Lógica de línea de surge simulada (el caudal mínimo requerido sube con las RPM)
            caudal_minimo_surge = (rpm * 0.4) - 500
            
            # Cálculo de la presión de descarga generada
            p_descarga = float(st.session_state['p_entrada']) + (rpm * 0.4)
            st.session_state['p_descarga_gasoducto'] = p_descarga
            st.metric("Presión de Despacho Calculada:", f"{p_descarga:.1f} kPa")
            
            if caudal_comp < caudal_minimo_surge:
                st.error(f"💥 **¡COMPRESOR EN SURGE!** El caudal actual ({caudal_comp} m³/h) es menor al límite crítico destructivo para {rpm} RPM ({caudal_minimo_surge:.0f} m³/h). Abra la válvula de recirculación (Anti-surge) YA.")
            elif caudal_comp < (caudal_minimo_surge + 400):
                st.warning("⚠️ **Proximidad de Línea de Control:** Active el lazo automático de reciclaje de gas.")
            else:
                st.success("✅ **Punto de Operación Seguro:** Flujo estable dentro de la envolvente del mapa del compresor.")

    # =========================================================================
    # UNIDAD 8: SEGURIDAD OPERACIONAL
    # =========================================================================
    elif unidad_sel == "8. Seguridad Operacional":
        st.header("8️⃣ Unidad 8: Matriz de Permisos y Parada de Emergencia (ESD)")
        st.write("Ponga a prueba su velocidad de reacción ante una contingencia mayor de planta.")
        
        st.subheader("🚨 Panel de Disparo de Seguridad (ESD - Emergency Shutdown)")
        st.markdown("""
        Frente a una rotura de cañería aguas abajo o fuego en el pool de bombas, el operador debe aislar la planta de manera inmediata para evitar fatalidades.
        """)
        
        # Botón crítico de intervención activa
        if st.button("🔥 DISPARAR PARADA DE EMERGENCIA GENERAL (ESD nivel 1)"):
            st.session_state['p_entrada'] = 0.0
            st.session_state['nivel_liquido'] = 0.0
            st.session_state['p_descarga_gasoducto'] = 0.0
            st.session_state['humedad_salida'] = 0.0
            
            st.error("🚨 **SISTEMA TOTALMENTE AISLADO:** Válvulas de bloqueo SDV de entrada y salida cerradas. Presión despresurizándose de forma segura hacia la antorcha (Flare). Planta segura.")
            st.balloons()
        else:
            st.info("ℹ️ **Simulación en Línea:** El sistema se encuentra operando bajo lazos cerrados distribuidos (DCS). Al presionar el botón superior se forzará la memoria estática a cero.")
