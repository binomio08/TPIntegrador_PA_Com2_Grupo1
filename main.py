from models.datos_covid import DatosCovid
from models.visualizador import Visualizador

if __name__ == "__main__":
    
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
