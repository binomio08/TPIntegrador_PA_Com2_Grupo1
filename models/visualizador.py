import seaborn as sns
import matplotlib.pyplot as plt

class Visualizador:
    def __init__(self, datos):
        # Guardar el DataFrame para su uso en métodos de visualización
        self.datos = datos

    def graficar_casos_por_fecha(self):
        # Crear visualización de casos diarios y muertes por fecha de inicio de síntomas
        datos_agrupados = self.datos.groupby('fecha_inicio_sintomas').size().reset_index(name='casos')
        datos_muertes = self.datos[self.datos['fallecido'] == 'SI'].groupby('fecha_inicio_sintomas').size().reset_index(name='muertes')

        plt.figure(figsize=(14, 7))
        sns.lineplot(data=datos_agrupados, x='fecha_inicio_sintomas', y='casos', label='Casos Diarios')
        sns.lineplot(data=datos_muertes, x='fecha_inicio_sintomas', y='muertes', label='Muertes Diarias', color='red')
        plt.title('Evolución Diaria de Casos y Muertes por COVID-19')
        plt.xlabel('Fecha de Inicio de Síntomas')
        plt.ylabel('Número de Casos/Muertes')
        plt.legend()
        plt.show()

    def graficar_casos_por_genero(self):
        # Crear visualización de casos por género
        datos_genero = self.datos.groupby('sexo').size().reset_index(name='casos')

        plt.figure(figsize=(10, 6))
        sns.barplot(data=datos_genero, x='sexo', y='casos')
        plt.title('Número de Casos por Género')
        plt.xlabel('Género')
        plt.ylabel('Número de Casos')
        plt.show()

    def graficar_casos_por_edad(self):
        # Limitar la edad entre 0 y 99
        datos_filtrados = self.datos[(self.datos['edad'] >= 0) & (self.datos['edad'] <= 99)]
        
        # Crear visualización de casos por edad
        plt.figure(figsize=(14, 7))
        sns.histplot(datos_filtrados['edad'], bins=30, kde=True)
        plt.title('Distribución de Casos por Edad (0-99)')
        plt.xlabel('Edad')
        plt.ylabel('Número de Casos')
        plt.show()

    def graficar_tasa_mortalidad_por_provincia(self):
        # Crear visualización de la tasa de mortalidad por provincia
        datos_provincias = self.datos.groupby('residencia_provincia_nombre').agg({
            'fallecido': lambda x: (x == 'SI').sum(), 
            'id_evento_caso': 'size'
        }).reset_index()
        datos_provincias['tasa_mortalidad'] = datos_provincias['fallecido'] / datos_provincias['id_evento_caso'] * 100

        plt.figure(figsize=(14, 7))
        sns.barplot(data=datos_provincias, x='tasa_mortalidad', y='residencia_provincia_nombre', orient='h')
        plt.title('Tasa de Mortalidad por Provincia')
        plt.xlabel('Tasa de Mortalidad (%)')
        plt.ylabel('Provincia')
        plt.show()
