import seaborn as sns
import matplotlib.pyplot as plt

class Visualizador:
    def __init__(self, df):
        self.df = df
    
    def graficar_casos_por_fecha(self):
        """
        Crea una visualización de casos diarios y muertes por fecha de inicio de síntomas.
        """
        df_grouped = self.df.groupby('fecha_inicio_sintomas').size().reset_index(name='cases')
        df_deaths = self.df[self.df['fallecido'] == 'SI'].groupby('fecha_inicio_sintomas').size().reset_index(name='deaths')

        plt.figure(figsize=(14, 7))
        sns.lineplot(data=df_grouped, x='fecha_inicio_sintomas', y='cases', label='Casos Diarios')
        sns.lineplot(data=df_deaths, x='fecha_inicio_sintomas', y='deaths', label='Muertes Diarias', color='red')
        plt.title('Evolución Diaria de Casos y Muertes por COVID-19')
        plt.xlabel('Fecha de Inicio de Síntomas')
        plt.ylabel('Número de Casos/Muertes')
        plt.legend()
        plt.show()

    def graficar_casos_por_genero(self):
        """
        Crea una visualización de casos por género.
        """
        df_gender = self.df.groupby('sexo').size().reset_index(name='cases')

        plt.figure(figsize=(10, 6))
        sns.barplot(data=df_gender, x='sexo', y='cases')
        plt.title('Número de Casos por Género')
        plt.xlabel('Género')
        plt.ylabel('Número de Casos')
        plt.show()

    def graficar_casos_por_edad(self, edad_min=0, edad_max=99):
        """
        Crea una visualización de casos por grupo etario, limitando la distribución por edad.
        """
        plt.figure(figsize=(14, 7))
        sns.histplot(self.df[(self.df['edad'] >= edad_min) & (self.df['edad'] <= edad_max)]['edad'], bins=30, kde=True)
        plt.title('Distribución de Casos por Edad')
        plt.xlabel('Edad')
        plt.ylabel('Número de Casos')
        plt.show()

    def graficar_tasa_mortalidad_por_provincia(self):
        """
        Crea una visualización de la tasa de mortalidad por provincia.
        """
        df_provinces = self.df.groupby('residencia_provincia_nombre').agg({'fallecido': lambda x: (x == 'SI').sum(), 'id_evento_caso': 'size'}).reset_index()
        df_provinces['death_rate'] = df_provinces['fallecido'] / df_provinces['id_evento_caso'] * 100

        plt.figure(figsize=(14, 7))
        sns.barplot(data=df_provinces, x='death_rate', y='residencia_provincia_nombre', orient='h')
        plt.title('Tasa de Mortalidad por Provincia')
        plt.xlabel('Tasa de Mortalidad (%)')
        plt.ylabel('Provincia')
        plt.show()
