import pandas as pd
import matplotlib.pyplot as plt

class Analisis:
def __init__(self, archivo):
self.df = pd.read_csv(archivo)

def total_participantes(self):
return len(self.df)

def datos_incompletos(self):
return self.df[self.df.isnull().any(axis=1)]

def promedio_pagos_por_taller(self):
return self.df.groupby("Taller")["Valor Pagado"].mean()

def taller_mas_participantes(self):
return self.df["Taller"].value_counts().idxmax()

def participante_mayor_pago(self):
max_valor = self.df["Valor Pagado"].max()
return self.df[self.df["Valor Pagado"] == max_valor]

def graficos(self):
# Gráfico de barras
self.df["Taller"].value_counts().plot(kind="bar", title="Participantes por Taller")
plt.xlabel("Taller")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()

# Histograma de edades
self.df["Edad"].plot(kind="hist", bins=10, title="Distribución de Edades")
plt.xlabel("Edad")
plt.tight_layout()
plt.show()

# Gráfico circular
self.df["Taller"].value_counts().plot(kind="pie", autopct='%1.1f%%', title="Distribución por Taller")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Ejemplo de uso
if __name__ == "__main__":
analisis = Analisis("app/datos/participantes.csv")

print("Total participantes:", analisis.total_participantes())
print("Participantes con datos incompletos:\n", analisis.datos_incompletos())
print("Promedio de pagos por taller:\n", analisis.promedio_pagos_por_taller())
print("Taller con más participantes:", analisis.taller_mas_participantes())
print("Participante con mayor pago:\n", analisis.participante_mayor_pago())

analisis.graficos()
