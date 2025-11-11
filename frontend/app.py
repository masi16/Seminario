import streamlit as st
import pandas as pd
import sys
import os

try:
    ruta_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(ruta_proyecto)
    from backend.motor_recomendacion import obtener_recomendaciones, obtener_lista_materias
    BACKEND_CONECTADO = True
except (ImportError, ModuleNotFoundError) as e:
    st.error(f"Error al conectar con el backend: {e}")
    BACKEND_CONECTADO = False

st.set_page_config(page_title="Recomendador Inteligente de Cursos", page_icon="🎓", layout="wide")

if 'historial' not in st.session_state:
    st.session_state.historial = []

st.title('🎓 Tu Tutor Personal con IA')

if not BACKEND_CONECTADO:
    st.error("Error Critico: No se pudo conectar con el motor de recomendacion (backend).")
    st.stop()

lista_materias_disponibles = obtener_lista_materias()

col_izq, col_der = st.columns(2)

with col_izq:
    st.header("1. ¿Qué materia quieres reforzar o avanzar?")
    st.info("Selecciona una materia, ingresa tu ultima calificacion y la IA te dara una recomendacion personalizada.")

    with st.form("formulario_notas", clear_on_submit=True):
        if lista_materias_disponibles:
            materia_nombre = st.selectbox("Selecciona la Materia", options=lista_materias_disponibles)
        else:
            st.warning("No se pudieron cargar las materias desde el backend.")
            materia_nombre = None
        
        curso_nota = st.number_input("Tu ultima calificacion en esta materia (de 1 a 10)", min_value=1.0, max_value=10.0, step=0.1, value=7.0)
        submitted = st.form_submit_button("Anadir y Evaluar")

        if submitted and materia_nombre:
            st.session_state.historial.append({"Materia": materia_nombre, "Calificacion": curso_nota})

    if st.session_state.historial:
        st.write("Tu historial de consulta:")
        st.dataframe(pd.DataFrame(st.session_state.historial), use_container_width=True)
        if st.button("Limpiar Historial"):
            st.session_state.historial = []
            st.rerun()

    st.divider()
    st.header("2. ¿Cual es tu motivacion ahora?")
    motivacion = st.radio("Nivel de motivacion:", ('Tengo muchas ganas', 'Estoy algo motivado', 'Tengo pocas ganas'), key='motivacion')
    
    obtener_recs_button = st.button('Obtener Mi Recomendacion', type="primary", use_container_width=True)

with col_der:
    st.header("3. Tu Recomendacion Personalizada")
    if obtener_recs_button:
        if not st.session_state.historial:
            st.warning("Por favor, anade al menos una materia a tu historial.")
        else:
            historial_df = pd.DataFrame(st.session_state.historial)
            mapa_motivacion = {'Tengo muchas ganas': 'Muy motivado', 'Estoy algo motivado': 'Algo motivado', 'Tengo pocas ganas': 'Poco motivado'}
            respuestas_usuario = {'motivacion': mapa_motivacion[motivacion]}
            
            with st.spinner("Tu tutor de IA esta preparando tu proxima leccion..."):
                recomendaciones, mensaje = obtener_recomendaciones(respuestas_usuario, historial_df)
            
            st.success(mensaje)
            st.divider()
            
            if not recomendaciones.empty:
                for index, row in recomendaciones.iterrows():
                    st.subheader(f"[{row['Titulo']}]({row['URL']})")
                    st.video(row['URL'])
                    st.markdown(f"**Area:** {row['Area']} | **Nivel:** {row['Nivel']}")
                    st.markdown("---")
            else:
                st.warning("No se encontraron videos para los filtros seleccionados (area de interes + nivel de motivacion). Intenta con otra motivacion o anade mas materias.")
    else:
        st.info("Completa los pasos 1 y 2, y luego haz clic en el boton.")