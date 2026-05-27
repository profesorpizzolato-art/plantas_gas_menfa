# modulos/manual_digital.py
import streamlit as st

def render_manual():
    st.header("📚 Manual Digital de Operaciones y Procesos")
    st.caption("Material de referencia técnica extraído de los procedimientos de Planta y Transporte.")
    
    capitulo = st.selectbox("Seleccione el Capítulo del Manual:", [
        "Capítulo 1: Separación de Entrada y Slug Catchers",
        "Capítulo 2: Tratamiento de Gas (Deshidratación por TEG)",
        "Capítulo 3: Sistema de Transporte y Gasoductos"
    ])
    
    if "Capítulo 1" in capitulo:
        st.subheader("Separación Líquido-Gas")
        st.markdown("""
        * **Función:** Amortiguar las llegadas bruscas de líquido (*baches o slugs*) provenientes del gasoducto de alimentación y separar la fase gaseosa de la líquida.
        * **Sistemas de Seguridad:** Cuenta con dos interruptores de nivel. El **segundo interruptor (Nivel Alto-Alto)** actúa directamente sobre la matriz de interlocks, ejecutando el **Cierre de Emergencia (CDE)** de la planta.
        """)
    elif "Capítulo 2" in capitulo:
        st.subheader("Deshidratación por Glicol (TEG)")
        st.markdown("""
        * **Mecanismo:** Absorción en contracorriente. El gas húmedo asciende por los platos o empaque de la torre contactora mientras el glicol pobre desciende absorbiendo el agua.
        * **Especificación de Red:** El gas de salida no debe superar los **64 mg/m³** de contenido de agua para evitar la formación de hidratos en el gasoducto de transporte.
        """)
