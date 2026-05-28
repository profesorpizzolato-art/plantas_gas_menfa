# modulos/evaluacion.py
import streamlit as st
# Importamos de forma directa las 40 preguntas sanitizadas
from modulos.banco_preguntas import BANCO_40_PREGUNTAS

def render_evaluacion():
    st.header("📝 Pilar 2: Sistema de Evaluación de Competencia")
    st.caption("Cuestionario formal obligatorio de operaciones de planta y control de procesos (40 Preguntas - Mínimo aprobación: 70%).")
    st.markdown("---")
    
    # Estructura para almacenar las opciones elegidas por el operario
    respuestas_usuario = {}
    
    # Desplegar los reactivos organizados en acordeones por Módulo Técnico para una lectura cómoda
    modulos_disponibles = ["Módulo I", "Módulo II", "Módulo III", "Módulo IV", "Módulo V", "Módulo VI"]
    titulos_modulos = {
        "Módulo I": "🌋 Módulo I: Termodinámica e Hidratos de Gas",
        "Módulo II": "💧 Módulo II: Hidráulica de Separación de Entrada y Slugs",
        "Módulo III": "🗼 Módulo III: Deshidratación por Glicol (TEG)",
        "Módulo IV": "❄️ Módulo IV: Plantas Criogénicas y Turboexpansión",
        "Módulo V": "🌀 Módulo V: Dinámica de la Compresión Centrífuga",
        "Módulo VI": "🛡️ Módulo VI: Filosofía de Protecciones SIS y Norma NAG-125"
    }
    
    st.info("💡 **Indicación para el Alumno:** Expanda cada bloque técnico y complete las opciones. Al finalizar todos los módulos, presione el botón inferior para procesar su calificación.")
    
    # Ciclo inteligente para renderizar las preguntas ordenadas por su pilar de ingeniería
    for m in modulos_disponibles:
        with st.expander(titulos_modulos[m], expanded=False):
            preguntas_del_modulo = [p for p in BANCO_40_PREGUNTAS if p["modulo"] == m]
            
            for item in preguntas_del_modulo:
                respuestas_usuario[item["id"]] = st.radio(
                    item["pregunta"],
                    options=item["opciones"],
                    index=None,
                    key=f"q_40_{item['id']}"
                )
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True) # Separador visual fino
                
    st.markdown("---")
    
    # Procesamiento matemático de las respuestas
    if st.button("📊 Enviar y Calificar Evaluación General", use_container_width=True):
        # Validar si falta responder alguna de las 40 preguntas
        if None in respuestas_usuario.values():
            preguntas_sin_responder = [str(k) for k, v in respuestas_usuario.items() if v is None]
            st.warning(f"⚠️ Evaluación incompleta. Por favor responda todas las consignas antes de enviar. Preguntas pendientes: {', '.join(preguntas_sin_responder)}")
        else:
            correctas = 0
            total_preguntas = len(BANCO_40_PREGUNTAS)
            
            # Validación uno a uno contra el vector de respuestas correctas
            for item in BANCO_40_PREGUNTAS:
                if respuestas_usuario[item["id"]] == item["correcta"]:
                    correctas += 1
            
            # Cálculo porcentual exacto
            nota_final = int((correctas / total_preguntas) * 100)
            
            st.markdown("---")
            st.subheader(f"📊 Resultados de la Evaluación Técnica")
            
            # Indicadores de rendimiento del alumno
            col_res1, col_res2 = st.columns(2)
            col_res1.metric("Puntaje Obtenido", f"{nota_final} %", delta="APROBADO" if nota_final >= 70 else "RECHAZO", delta_color="normal" if nota_final >= 70 else "inverse")
            col_res2.metric("Respuestas Correctas", f"{correctas} / {total_preguntas}")
            
            if nota_final >= 70:
                st.success(f"🎉 **COMPETENCIA VALIDADA.** El operario ha demostrado los conocimientos de ingeniería exigidos para el manejo seguro de los activos de la suite MENFA.")
            else:
                st.error("❌ **PROGRAMA DE REPASO REQUERIDO.** El puntaje no alcanza el estándar mínimo del 70%. Se solicita al alumno revisar los capítulos de detalle en el Manual Digital e intentarlo nuevamente.")
                
            # Panel pedagógico de retroalimentación en tiempo real
            with st.expander("🔍 Auditoría Técnica: Revisar Justificación por Pregunta"):
                for item in BANCO_40_PREGUNTAS:
                    usr_ans = respuestas_usuario[item["id"]]
                    es_correcta = usr_ans == item["correcta"]
                    
                    st.markdown(f"**Consigna {item['id']}** ({item['modulo']})")
                    if es_correcta:
                        st.markdown(f"↳ 🟢 *Respuesta del alumno:* {usr_ans} (Correcto)")
                    else:
                        st.markdown(f"↳ 🔴 *Respuesta del alumno:* {usr_ans}")
                        st.markdown(f"↳ 🟢 *Línea correcta de proceso:* {item['correcta']}")
                    st.caption(f"💡 *Sustento de Ingeniería:* {item['feedback']}")
                    st.markdown("---")
