import pandas as pd
import os

try:
    ruta_backend = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(ruta_backend, 'materias_disponibles.csv')
    cursos_disponibles_df = pd.read_csv(ruta_csv)
except FileNotFoundError:
    print("Error: No se encontro el archivo 'materias_disponibles.csv'.")
    cursos_disponibles_df = pd.DataFrame()

def obtener_lista_materias():
    if not cursos_disponibles_df.empty:
        return sorted(cursos_disponibles_df['Area'].unique().tolist())
    return []

def obtener_recomendaciones(respuestas_encuesta, historial_df):
    motivacion = respuestas_encuesta.get('motivacion')
    
    ultima_materia_ingresada = historial_df.iloc[-1]
    materia = ultima_materia_ingresada['Materia']
    calificacion = ultima_materia_ingresada['Calificacion']
    
    videos_relevantes = cursos_disponibles_df[cursos_disponibles_df['Area'] == materia]
    
    # 1. LOGICA DE REFUERZO (Nota baja)
    if calificacion < 6.0:
        mensaje = f"Vimos que tuviste dificultades en {materia}. ¡No te preocupes! La clave es reforzar las bases. Aqui tienes algunos videos fundamentales para empezar:"
        recomendaciones_df = videos_relevantes[videos_relevantes['Nivel'] == 'Basico'].head(3)
        
    # 2. ¡NUEVA LOGICA DE SOLIDIFICACION MEJORADA! (Nota media)
    elif calificacion < 8.0:
        mensaje_base = f"Una nota aceptable en {materia}. Dependiendo de tu motivacion, te sugerimos: "
        if motivacion == 'Poco motivado':
            mensaje = mensaje_base + "un repaso de los fundamentos para ganar confianza."
            recomendaciones_df = videos_relevantes[videos_relevantes['Nivel'] == 'Basico'].head(3)
        elif motivacion == 'Algo motivado':
            mensaje = mensaje_base + "practicar con estos temas de nivel intermedio."
            recomendaciones_df = videos_relevantes[videos_relevantes['Nivel'] == 'Intermedio'].head(3)
        else: # 'Muy motivado'
            mensaje = mensaje_base + "¡ir por un desafio! Aqui tienes contenido avanzado."
            recomendaciones_df = videos_relevantes[videos_relevantes['Nivel'] == 'Avanzado'].head(3)
        
    # 3. LOGICA DE PROGRESION (Nota alta)
    else:
        if motivacion == 'Poco motivado':
            mensaje = f"¡Excelente trabajo en {materia}! Para tu proximo paso, aqui tienes algunos temas de nivel basico para explorar sin presion:"
            recomendaciones_df = videos_relevantes[videos_relevantes['Nivel'] == 'Basico'].head(3)
        elif motivacion == 'Algo motivado':
            mensaje = f"¡Muy bien en {materia}! Estas listo para el siguiente nivel. Aqui tienes algunos videos de nivel intermedio:"
            recomendaciones_df = videos_relevantes[videos_relevantes['Nivel'] == 'Intermedio'].head(3)
        else: # 'Muy motivado'
            mensaje = f"¡Dominas {materia}! La IA ha encontrado los desafios mas avanzados para que sigas creciendo:"
            recomendaciones_df = videos_relevantes[videos_relevantes['Nivel'] == 'Avanzado'].head(3)
            
    return recomendaciones_df, mensaje