# modulos/evaluacion.py
import streamlit as st

def render_evaluacion():
    st.header("📝 Sistema Integrado de Evaluación Técnica Operativa")
    st.caption("Consola automatizada para auditar las maniobras del operador y validar competencias regulatorias.")
    st.markdown("---")

    # --- DATOS DEL POSTULANTE / ALUMNO ---
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        nombre_alumno = st.text_input("Nombre y Apellido del Operador:", placeholder="Ej: Juan Pérez")
    with col_d2:
        dni_alumno = st.text_input("DNI / Registro Legajo Técnico:", placeholder="Ej: 38444555")

    if not nombre_alumno or not dni_alumno:
        st.info("💡 **Acceso Protegido:** Ingrese su Nombre y DNI para procesar la auditoría de la planta en tiempo real.")
        return

    st.markdown("---")
    st.subheader(f"🔍 Auditoría en Vivo - Planta Operada por: {nombre_alumno}")

    # --- AUDITORÍA DE CRITERIOS DE INGENIERÍA EN SEGUNDO PLANO ---
    puntos = 100
    errores = []

    # 1. Validación Separador de Entrada (El Pozo Ilustrado / Instrumentation)
    nivel_sep = st.session_state.get('nivel_liquido', 45.0)
    if nivel_sep > 80.0:
        puntos -= 30
        errores.append("❌ Permitió la inundación del Separador de Entrada V-101 (>80%). Causó Carry-over de crudo.")
    elif nivel_sep < 15.0:
        puntos -= 15
        errores.append("❌ Nivel críticamente bajo en el Separador de Entrada (<15%). Riesgo de arrastre de gas (Gas Blowby).")

    # 2. Validación de Deshidratación TEG (Dialnet)
    humedad = st.session_state.get('humedad_salida', 24.5)
    if humedad > 64.0:
        puntos -= 30
        errores.append("❌ Gas de salida fuera de especificación comercial (>64 mg/m³). Incumplimiento de Contrato de Despacho.")

    # 3. Validación de Compresión (Plantas Compresoras)
    # Reificamos si la planta sufrió un trip por vibración axial (Surge)
    p_descarga = st.session_state.get('p_descarga_gasoducto', 6100.0)
    p_entrada = st.session_state.get('p_entrada', 3500.0)
    if p_descarga == p_entrada and p_entrada > 1000.0:
        puntos -= 25
        errores.append("❌ Provocó el TRIP por enclavamiento del Turbocompresor debido a vibración axial extrema (Fenómeno de Surge).")

    # --- MOSTRAR RESULTADO DE LA EVALUACIÓN ---
    col_res1, col_res2 = st.columns([1, 2])
    
    with col_res1:
        st.markdown("##### Nota Obtenida:")
        if puntos >= 70:
            st.success(f"### 🎉 {puntos} / 100")
            st.balloons()
        else:
            st.error(f"### 📉 {puntos} / 100")
            
    with col_res2:
        st.markdown("##### Dictamen Operativo:")
        if puntos == 100:
            st.markdown("🟢 **OPERADOR APTO - EXCELENCIA:** El sistema no detectó desvíos en ningún lazo de control. Operación Fail-Safe ideal.")
        elif puntos >= 70:
            st.markdown("🟡 **OPERADOR APTO CON OBSERVACIONES:** Mantiene la planta en línea, pero operó cerca de los límites críticos de alarma.")
        else:
            st.markdown("🔴 **OPERADOR NO APTO:** Se detectaron maniobras que comprometieron la integridad física de los equipos o la calidad del gas.")

    # Listar fallas pedagógicas cometidas
    if errores:
        st.markdown("---")
        st.markdown("##### ⚠️ Desvíos Técnicos Detectados por el Sistema:")
        for err in errores:
            st.write(err)
            
    st.markdown("---")
    st.caption("Nota: Esta evaluación se actualiza dinámicamente. El alumno puede volver a los módulos, corregir la apertura de las válvulas o las marchas de los equipos, y su nota se recalculará automáticamente en vivo.")
