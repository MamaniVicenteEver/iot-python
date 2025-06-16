# Importar librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

# --------------------------------------
# 1. Cargar el CSV con datos simulados
# --------------------------------------
df = pd.read_csv('datos_clima.csv')  # Leer el archivo generado previamente

# Convertir la columna 'fecha' al tipo datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# Ordenar por fecha (por si acaso) y usarla como índice
df = df.sort_values('fecha')
df.set_index('fecha', inplace=True)

# --------------------------------------
# 2. Calcular promedios móviles de 3 días
# --------------------------------------
df['temp_mov_avg'] = df['temperatura'].rolling(window=3).mean()  # Temperatura
df['hum_mov_avg'] = df['humedad'].rolling(window=3).mean()       # Humedad

# --------------------------------------
# 3. Aplicar reglas de inferencia simuladas
# --------------------------------------

# 3.1 Alerta de sobrecalentamiento:
# Si la temperatura aumenta 3 días consecutivos → alerta
df['alerta_sobrecalentamiento'] = df['temperatura'].diff().gt(0).rolling(window=3).sum() == 3

# 3.2 Posible sequía:
# Si temperatura > 30°C y humedad < 30%
df['posible_sequia'] = (df['temperatura'] > 30) & (df['humedad'] < 30)

# --------------------------------------
# 4. Exportar eventos detectados como JSON
# --------------------------------------
eventos = []

for fecha, fila in df.iterrows():
    if fila['alerta_sobrecalentamiento'] or fila['posible_sequia']:
        eventos.append({
            'fecha': fecha.strftime('%Y-%m-%d'),
            'temperatura': fila['temperatura'],
            'humedad': fila['humedad'],
            'alerta': 'sobrecalentamiento' if fila['alerta_sobrecalentamiento'] else 'posible sequia'
        })

# Guardar la lista de eventos como archivo JSON
with open('eventos_alerta.json', 'w') as archivo:
    json.dump(eventos, archivo, indent=4)

print(f"✅ {len(eventos)} eventos exportados a 'eventos_alerta.json'")

# --------------------------------------
# 5. Visualización con Matplotlib
# --------------------------------------

# Crear gráfico de temperatura con promedio móvil y puntos de alerta
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['temperatura'], label='Temperatura')
plt.plot(df.index, df['temp_mov_avg'], label='Promedio Móvil (3 días)', linestyle='--')

# Marcar los puntos donde hay alerta de sobrecalentamiento
plt.scatter(df[df['alerta_sobrecalentamiento']].index,
            df[df['alerta_sobrecalentamiento']]['temperatura'],
            color='red', label='Alerta: sobrecalentamiento', zorder=5)

# Marcar los puntos donde hay posible sequía
plt.scatter(df[df['posible_sequia']].index,
            df[df['posible_sequia']]['temperatura'],
            color='blue', label='Alerta: posible sequía', zorder=5)

plt.title('Tendencia de Temperatura y Alertas')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('grafico_temperatura_alertas.png')
# plt.show()
