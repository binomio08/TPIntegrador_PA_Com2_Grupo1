import pandas as pd

class DatosCovid:
    def __init__(self, ruta_archivo):
        # Cargar datos desde un archivo CSV
        self.datos = pd.read_csv(ruta_archivo, parse_dates=[
            'fecha_inicio_sintomas', 'fecha_apertura', 'fecha_internacion', 
            'fecha_cui_intensivo', 'fecha_fallecimiento', 'fecha_diagnostico', 
            'ultima_actualizacion'])
        self._convertir_fechas()

    def _convertir_fechas(self):
        # Convertir columnas de fecha a formato datetime
        columnas_fecha = ['fecha_inicio_sintomas', 'fecha_apertura', 'fecha_internacion', 
                          'fecha_cui_intensivo', 'fecha_fallecimiento', 'fecha_diagnostico', 
                          'ultima_actualizacion']
        for columna in columnas_fecha:
            self.datos[columna] = pd.to_datetime(self.datos[columna], errors='coerce')

    def obtener_datos(self):
        # Devolver el DataFrame cargado y procesado
        return self.datos

