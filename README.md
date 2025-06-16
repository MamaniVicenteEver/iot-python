# Proyecto IoT: Generación y Publicación de Alertas Ambientales

Este proyecto simula datos de temperatura y humedad, detecta eventos críticos como sobrecalentamiento y sequía, y publica alertas mediante MQTT hacia un suscriptor ESP32 virtual (Wokwi).

---

## Introducción

Esta práctica consistió en desarrollar un sistema IoT funcional mediante el uso de Python, MQTT y un microcontrolador ESP32 simulado. El sistema simula condiciones ambientales, detecta eventos críticos y comunica dichas alertas a través de un broker MQTT hacia un suscriptor que reacciona visualmente.

---

## Objetivos

- Crear un entorno virtual para desarrollo con Python.
- Generar y analizar datos de temperatura y humedad.
- Detectar eventos anómalos y exportarlos a un archivo JSON.
- Publicar alertas mediante MQTT con seguridad TLS.
- Simular un suscriptor en Wokwi (ESP32 + LCD + LEDs).
- Implementar autenticación en la comunicación MQTT.

---

## Configuración del entorno

### 1. Crear y activar entorno virtual

```bash
python -m venv venv
# Activar en Windows
venv\Scripts\activate
# Activar en Linux/macOS
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si no tienes un `requirements.txt`, puedes instalar manualmente:
```bash
pip install pandas numpy matplotlib paho-mqtt
```

---

## Ejecución del proyecto

### 1. Generar dataset y JSON de alertas

```bash
python generar_csv.py
python procesar_datos.py
```

### 2. Publicar alertas vía MQTT

```bash
python publisher.py
```

---

## Simulación Wokwi (ESP32)

El código cargado en Wokwi permite:
- Conectarse al broker MQTT.
- Mostrar las alertas en un LCD I2C.
- Encender LEDs: rojo para sobrecalentamiento, azul para sequía.

**Conexiones en ESP32 (Wokwi):**

| Componente      | ESP32 Pin      |
|-----------------|----------------|
| LCD I2C (VCC)    | 3.3V           |
| LCD I2C (GND)    | GND            |
| LCD I2C (SDA)    | GPIO21         |
| LCD I2C (SCL)    | GPIO22         |
| LED rojo (anodo) | GPIO18         |
| LED azul (anodo) | GPIO19         |
| Ambos cátodos    | GND            |


---

## Archivos importantes

- `generar_csv.py`: genera datos simulados
- `procesar_datos.py`: analiza datos y exporta alertas
- `publisher.py`: publica alertas por MQTT
- `datos_clima.csv`: datos generados
- `eventos_alerta.json`: alertas detectadas
- `grafico_temperatura_alertas.png`: gráfico de análisis

---

## Seguridad MQTT

El sistema fue adaptado para usar HiveMQ Cloud, implementando:
- Autenticación por usuario/contraseña
- Conexión segura con TLS (puerto 8883)

---

## Conclusiones

- Se logró simular condiciones ambientales y detectar eventos críticos usando Python.
- El uso de MQTT permitió una comunicación efectiva y en tiempo real.
- La implementación de TLS y autenticación refuerza buenas prácticas en IoT.
- Wokwi permitió validar el comportamiento visual del sistema sin hardware físico.
- Se integraron sensores simulados, procesamiento, envío seguro y visualización.

---