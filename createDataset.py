import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parámetros
num_dias = 30
fecha_inicio = datetime(2025, 5, 1)

fechas = [fecha_inicio + timedelta(days=i) for i in range(num_dias)]
temperaturas = []
humedades = []

# Generamos datos controlados
for i in range(num_dias):
    # Primeros días normales
    if i < 10:
        temp = np.random.normal(28, 1.5)  # temperatura moderada
        hum = np.random.normal(60, 5)
    # 3 días de aumento consecutivo de temperatura (alerta sobrecalentamiento)
    elif 10 <= i <= 12:
        temp = 31 + (i - 10)  # 31, 32, 33
        hum = 50
    # Días con temperatura alta y humedad baja (alerta sequía)
    elif 20 <= i <= 22:
        temp = np.random.uniform(34, 36)  # alta
        hum = np.random.uniform(18, 25)  # baja
    else:
        temp = np.random.normal(29, 1)
        hum = np.random.normal(55, 6)

    temperaturas.append(round(temp, 1))
    humedades.append(round(hum, 1))

# Crear DataFrame
df = pd.DataFrame({
    'fecha': [f.strftime('%Y-%m-%d') for f in fechas],
    'temperatura': temperaturas,
    'humedad': humedades
})

# Guardar como CSV
df.to_csv('datos_clima.csv', index=False)
print("✅ Dataset generado con escenarios forzados: datos_clima.csv")




