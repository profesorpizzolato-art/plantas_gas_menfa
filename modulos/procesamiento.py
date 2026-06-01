# modulos/procesamiento.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render_procesamiento(p_entrada, t_entrada):
    st.header("❄️ Planta Criogénica por Turboexpander y Fraccionamiento de LGN")
    st.caption("Simulación de refrigeración extrema por caída de presión entálpica y separación por cortes de ebullición de LGN.")
    st.markdown("---")

    # --- PANEL DE VARIABLES OPERATIVAS (CONTROLES DEL ALUMNO) ---
    col_turbo, col_fracc = st.columns(2)
    
    with col_turbo:
        st.markdown("##### 🌀 Tren Criogénico (Turboexpander)")
        p_salida_tx = st.slider("Presión de Salida del Expander (kPa):", 1200.0, 3200.0, 1800.0, step=50.0,
                                help="A mayor caída de presión, mayor caída de temperatura por efecto isentrópico.")
        eficiencia_jt = st.checkbox("Bypass a Válvula Joule-Thomson (J-T)", value=False,
                                    help="Simula el paso de emergencia o mantenimiento por válvula de expansión simple (menos eficiente).")

    with col_fracc:
        st.markdown("##### 🗼 Columnas de Fraccionamiento")
        temp_reboiler_deeth = st.slider("Temperatura Reboiler Deetandizadora (°C):", 70.0, 110.0, 88.0, step=0.5,
                                        help="Controla el corte del Etano por el fondo de la torre.")
        reflejo_debut = st.slider("Relación de Reflujo Debutanizadora:", 1.0, 5.0, 2.2, step=0.1,
                                  help="Regula la pureza del Propano/Butano comercial (GLP).")

    st.markdown("---")

    # --- MOTOR MATEMÁTICO DE PROCESO (LGN / TECHINT) ---
    # Cálculo dinámico del efecto de enfriamiento por expansión
    if eficiencia_jt:
        # La expansión isoentálpica (J-T) enfría mucho menos que el Turboexpander
        drop_temp = (p_entrada - p_salida_tx) * 0.012
        rendimiento_liquidos = 40.0 # Caída abrupta de eficiencia
        tipo_exp = "Expansión Isoentálpica (J-T)"
    else:
        # Expansión Isentrópica por extractor de trabajo mecánico (Turboexpander)
        drop_temp = (p_entrada - p_salida_tx) * 0.035
        rendimiento_liquidos = float(np.clip(75.0 + (3200.0 - p_salida_tx) * 0.01, 50.0, 98.5))
        tipo_exp = "Expansión Isentrópica (Turboexpander)"

    t_criogenica = float(t_entrada - drop_temp)

    # Simulación del fraccionamiento de líquidos (Cortes comerciales)
    # Si el reboiler de la Deetandizadora está muy frío, el etano contamina los líquidos del fondo (fuera de especificación)
    off_spec_etano = temp_reboiler_deeth < 82.0 or temp_reboiler_deeth > 95.0
    # Si el reflujo es bajo, el GLP se contamina con pesados
    off_spec_glp = reflejo_debut < 1.8

    # --- CONSOLA DE MEDICIÓN EN TIEMPO REAL ---
    st.subheader(f"📊 Monitoreo del Proceso: {tipo_exp}")
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    
    col_m1.metric("Temperatura Criogénica", f"{t_criogenica:.1f} °C", 
                  delta="ZONA LÍQUIDA" if t_criogenica < -40 else "CALIENTE", 
                  delta_color="normal" if t_criogenica < -40 else "inverse")
    
    col_m2.metric("Recuperación de Etano/C3+", f"{rendimiento_liquidos:.1f} %",
                  help="Eficiencia de extracción de licuables del gas de entrada.")
    
    col_m3.metric("Especificación Líquidos (C2-)", "FUERA DE NORMA" if off_spec_etano else "OK",
                  delta="Reboiler Crítico" if off_spec_etano else "Estable",
                  delta_color="inverse" if off_spec_etano else "normal")
    
    col_m4.metric("Calidad GLP Despachado", "PENTANO ALTO" if off_spec_glp else "98.8% PURA",
                  delta="Bajo Reflujo" if off_spec_glp else "OK",
                  delta_color="inverse" if off_spec_glp else "normal")

    # --- ALERTAS OPERATIVAS ---
    if t_criogenica > -30.0:
        st.error("🚨 **ALERTA DE PROCESO:** La temperatura en el separador frío es demasiado alta ($> -30^\\circ\\text{C}$). Los componentes ricos (C2, C3 y C4) permanecen en fase gaseosa y se pierden por la línea de gas residual. *Acción:* Cierre el bypass J-T o aumente la caída de presión en el Expander.")
    if off_spec_etano:
        st.warning("⚠️ **DESVIACIÓN EN EN DEETANDIZADORA:** Temperatura fuera de rango óptimo ($82^\\circ\text{C} - 95^\\circ\text{C}$). Hay arrastre de metano por fondo o pérdida de etano por cabeza.")

    # --- GRÁFICO DE RENDIMIENTO DE FRACCIONAMIENTO ---
    st.markdown("### 📈 Perfil de Destilación de Líquidos (LGN)")
    cortes = ['Metano (C1)', 'Etano (C2)', 'Propano (C3)', 'Butano (C4)', 'Pentano+ (C5+)']
    
    # El perfil de composición varía dinámicamente según los controles del alumno
    if off_spec_etano:
        composicion = [12.0, 68.0, 15.0, 4.0, 1.0] # Contaminado con livianos
    elif off_spec_glp:
        composicion = [0.1, 5.0, 40.0, 35.0, 19.8] # Contaminado con pesados
    else:
        composicion = [0.0, 1.5, 52.0, 44.5, 2.0] # GLP Comercial Óptimo

    fig_fracc = go.Figure(data=[go.Pie(labels=cortes, values=composicion, hole=.4, marker_colors=['#ef553b','#636efa','#00cc96','#ab63fa','#ffa15a'])])
    fig_fracc.update_layout(template="plotly_dark", height=280, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_fracc, use_container_width=True)
