# cultura_app/app/analisis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

class AnalisisParticipantes:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.df = None

    def cargar_datos(self):
        if os.path.exists(self.ruta_archivo):
            self.df = pd.read_csv(self.ruta_archivo)
            print("Datos cargados correctamente.")
        else:
            print("Archivo no encontrado.")

    def total_participantes(self):
        if self.df is not None:
            total = len(self.df)
            print("Total de participantes:", total)
            return total
        return 0

    def datos_incompletos(self):
        if self.df is not None:
            incompletos = self.df[self.df.isnull().any(axis=1)]
            print("Participantes con datos incompletos:")
            print(incompletos)
            return incompletos
        return pd.DataFrame()

    def promedio_pagos_por_taller(self):
        if self.df is not None:
            self.df["valor_total"] = self.df["taller"].map({
                "Pintura": 6000,
                "Teatro": 8000,
                "Música": 10000,
                "Danza": 7000
            }) * self.df["clases_asistidas"]
            promedio = self.df.groupby("taller")["valor_total"].mean()
            print("Promedio de pagos por taller:")
            print(promedio)
            return promedio
        return pd.Series()

    def taller_mas_participantes(self):
        if self.df is not None:
            conteo = self.df["taller"].value_counts()
            taller = conteo.idxmax()
            print("Taller con más participantes:", taller)
            return taller
        return None

    def mayor_valor_pagado(self):
        if self.df is not None:
            self.df["valor_total"] = self.df["taller"].map({
                "Pintura": 6000,
                "Teatro": 8000,
                "Música": 10000,
                "Danza": 7000
            }) * self.df["clases_asistidas"]
            participante = self.df.loc[self.df["valor_total"].idxmax()]
            print("Participante con mayor valor pagado:")
            print(participante)
            return participante
        return None

    def graficos(self):
        if self.df is not None:
            plt.figure(figsize=(8,5))
            sns.countplot(data=self.df, x='taller', palette='pastel')
            plt.title('Número de participantes por taller')
            plt.tight_layout()
            plt.show()

            plt.figure(figsize=(8,5))
            sns.histplot(data=self.df, x='edad', bins=10, kde=True, color='skyblue')
            plt.title('Histograma de edades')
            plt.tight_layout()
            plt.show()

            plt.figure(figsize=(6,6))
            self.df['taller'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'))
            plt.title('Distribución de participantes por taller')
            plt.tight_layout()
            plt.show()



