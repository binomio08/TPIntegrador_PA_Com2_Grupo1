import pandas as pd

def cargar_datos(url_onedrive):
    """
    Carga datos desde un archivo CSV en OneDrive y los devuelve como un DataFrame.
    """
    try:
        df = pd.read_csv(url_onedrive, parse_dates=['fecha_inicio_sintomas', 'fecha_apertura', 'fecha_internacion', 'fecha_cui_intensivo', 'fecha_fallecimiento', 'fecha_diagnostico', 'ultima_actualizacion'])
        
        # Convertir las columnas de fecha a datetime
        date_columns = ['fecha_inicio_sintomas', 'fecha_apertura', 'fecha_internacion', 'fecha_cui_intensivo', 'fecha_fallecimiento', 'fecha_diagnostico', 'ultima_actualizacion']
        for column in date_columns:
            df[column] = pd.to_datetime(df[column], errors='coerce')
        
        return df
    except Exception as e:
        print(f"No se pudo cargar el archivo desde OneDrive: {e}")
        return None

# URL de ejemplo en OneDrive (reemplaza con tu URL real)
url_onedrive = "https://1drv.ms/u/s!AnsuwNmVA67Aio1o2txeDEYquGX8fg?e=YUkHmx"

# Cargar datos desde OneDrive
datos = cargar_datos(url_onedrive)

# Verificar si los datos se cargaron correctamente
if datos is not None:
    print("Datos cargados correctamente desde OneDrive.")
    # Aquí puedes seguir trabajando con tus datos...
else:
    print("No se pudieron cargar los datos desde OneDrive.")
