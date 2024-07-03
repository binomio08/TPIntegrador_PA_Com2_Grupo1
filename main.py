from models.datos_covid import DatosCovid
from models.visualizador import Visualizador

# Cargar datos
datos = DatosCovid('data/Covid19Casos.csv')
df = datos.obtener_datos()

# Crear visualizaciones
visualizador = Visualizador(df)
visualizador.graficar_casos_por_fecha()
visualizador.graficar_casos_por_genero()
visualizador.graficar_casos_por_edad()
visualizador.graficar_tasa_mortalidad_por_provincia()
