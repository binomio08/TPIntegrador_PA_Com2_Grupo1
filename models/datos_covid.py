from models.visualizador import Visualizador
import pandas as pd

class DatosCovid:
    def __init__(self, url_onedrive):
        # Guardar la URL de OneDrive
        self.url_onedrive = url_onedrive

    def obtener_datos(self):
        """
        Cargar datos desde OneDrive y devolver un DataFrame.
        """
        try:
            df = pd.read_csv(self.url_onedrive, parse_dates=['fecha_inicio_sintomas', 'fecha_apertura', 'fecha_internacion', 'fecha_cui_intensivo', 'fecha_fallecimiento', 'fecha_diagnostico', 'ultima_actualizacion'])
            
            # Convertir las columnas de fecha a datetime
            date_columns = ['fecha_inicio_sintomas', 'fecha_apertura', 'fecha_internacion', 'fecha_cui_intensivo', 'fecha_fallecimiento', 'fecha_diagnostico', 'ultima_actualizacion']
            for column in date_columns:
                df[column] = pd.to_datetime(df[column], errors='coerce')
            
            return df
        except Exception as e:
            print(f"No se pudo cargar el archivo desde OneDrive: {e}")
            return None

# Ejemplo de uso
if __name__ == "__main__":
    # URL de ejemplo en OneDrive (reemplaza con tu URL real)
    url_onedrive = "https://1drv.ms/u/s!AnsuwNmVA67Aio1o2txeDEYquGX8fg?e=YUkHmx"

    # Crear instancia de DatosCovid con la URL de OneDrive
    datos_covid = DatosCovid(url_onedrive)
    
    # Obtener datos desde OneDrive
    df = datos_covid.obtener_datos()

    if df is not None:
        # Crear visualizador con los datos cargados
        visualizador = Visualizador(df)
        
        # Crear las visualizaciones
        visualizador.graficar_casos_por_fecha()
        visualizador.graficar_casos_por_genero()
        visualizador.graficar_casos_por_edad()
        visualizador.graficar_tasa_mortalidad_por_provincia()
    else:
        print("No se pudieron cargar los datos desde OneDrive.")
