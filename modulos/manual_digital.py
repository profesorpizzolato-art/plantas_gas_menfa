# modulos/manual_digital.py
import streamlit as st

def render_manual():
    st.header("📚 Pilar 1: Manual Técnico Digital de Operaciones")
    capitulo = st.selectbox("Seleccione el módulo de estudio:", [
        "Módulo A: Separación Primaria y Slug Catchers",
        "Módulo B: Deshidratación por Glicol (TEG)"
    ])
    st.markdown("---")
    if "Módulo A" in capitulo:
        st.subheader("Sistemas de Separación de Entrada")
        st.write("Los slug catchers amortiguan las llegadas bruscas de líquido de los gasoductos de alimentación, permitiendo separar la fase gaseosa de los condensados por decantación gravitacional.")
    else:
        st.subheader("Torres Contactoras de Glicol")
        st.write("La absorción del vapor de agua se realiza en contracorriente. El gas húmedo asciende por los platos de la torre contactora interactuando con el glicol pobre que desciende absorbiendo el agua.")
