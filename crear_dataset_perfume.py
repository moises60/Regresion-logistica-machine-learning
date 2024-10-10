# crear_dataset_perfume.py

"""
Creado el 6 de octubre de 2024

Este script genera un dataset simulado sobre si un conjunto de mujeres compran un perfume o no,
basado en su edad y poder económico. El dataset se guarda como 'datos_perfume.csv'.
"""

import numpy as np
import pandas as pd

# semillaa
np.random.seed(42)

# Número de muestras
n_samples = 400

# Generar edades entre 18 y 65 años
edad = np.random.randint(18, 66, n_samples)

# Generar poder económico (0: Bajo, 1: Medio, 2: Alto)
poder_economico = np.random.choice([0, 1, 2], size=n_samples, p=[0.4, 0.4, 0.2])

# Crear un DataFrame
datos = pd.DataFrame({
    'Edad': edad,
    'Poder_Economico': poder_economico
})

# Función para determinar si compró perfume (1) o no (0)
def comprar_perfume(row):
    probabilidad = 0.0
    # Ajustar probabilidad según el poder económico
    if row['Poder_Economico'] == 2:
        probabilidad += 0.6
    elif row['Poder_Economico'] == 1:
        probabilidad += 0.3
    else:
        probabilidad += 0.1

    # Ajustar probabilidad según la edad
    if 41 <= row['Edad'] <= 55:
        probabilidad += 0.5
    elif 25 <= row['Edad'] <= 40:
        probabilidad += 0.2
    else:
        probabilidad += 0.1

    # Limitar la probabilidad máxima a 0.99
    probabilidad = min(probabilidad, 0.99)

    # Determinar si compra o no
    return 1 if np.random.rand() < probabilidad else 0

# Aplicar la función al DataFrame
datos['Compra'] = datos.apply(comprar_perfume, axis=1)

# Mapear valores para mejor legibilidad
datos['Poder_Economico'] = datos['Poder_Economico'].map({0: 'Bajo', 1: 'Medio', 2: 'Alto'})

# Guardar el dataset a un archivo CSV
datos.to_csv('datos_perfume.csv', index=False)

print("Dataset 'datos_perfume.csv' creado exitosamente.")
