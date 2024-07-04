import pandas as pd

def cargar_datos(ruta_archivo):
    """
    Carga datos desde un archivo CSV y los devuelve como un DataFrame.
    """
    datos = pd.read_csv(ruta_archivo, parse_dates=['fecha_inicio_sintomas', 'fecha_apertura', 'fecha_internacion', 'fecha_cui_intensivo', 'fecha_fallecimiento', 'fecha_diagnostico', 'ultima_actualizacion'])
    
    # Convertir las columnas de fecha a datetime
    columnas_fecha = ['fecha_inicio_sintomas', 'fecha_apertura', 'fecha_internacion', 'fecha_cui_intensivo', 'fecha_fallecimiento', 'fecha_diagnostico', 'ultima_actualizacion']
    for columna in columnas_fecha:
        datos[columna] = pd.to_datetime(datos[columna], errors='coerce')
    
    return datos
