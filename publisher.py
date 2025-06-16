import json
import time
import ssl
import paho.mqtt.client as mqtt

# --------------------------------------
# 1. Configuración del broker HiveMQ Cloud (MODIFICAR)
# --------------------------------------
BROKER = "broker.hivemq.com"  # URL de HiveMQ Cloud
PORT = 8883  # Cambiar a Puerto TLS
TOPIC = "/iot/alertas"

# --------------------------------------
# 2. Cargar el archivo JSON con las alertas 
# --------------------------------------
with open("eventos_alerta.json", "r") as archivo:
    alertas = json.load(archivo)

# --------------------------------------
# 3. Definir funciones de conexión 
# --------------------------------------
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado al broker MQTT con TLS")
    else:
        print(f"❌ Fallo de conexión, código {rc}")

# --------------------------------------
# 4. Crear cliente MQTT con TLS y autenticación (MODIFICAR)
# --------------------------------------
client = mqtt.Client()
client.on_connect = on_connect

# 🔐 AUTENTICACIÓN: usuario y contraseña del publicador (NUEVO)
client.username_pw_set("USUARIO", "CONTRASEÑA")  # INCLUYA LAS CREDENCIALES USERNAME Y PASS: autenticación HiveMQ

# TLS (acepta conexión sin verificar CA, útil para pruebas en local) (MODIFICADO)
client.tls_set(cert_reqs=ssl.CERT_NONE)
client.tls_insecure_set(True)

# --------------------------------------
# 5. Conectar al broker HiveMQ Cloud (SIN CAMBIOS)
# --------------------------------------
client.connect(BROKER, PORT)
client.loop_start()

# --------------------------------------
# 6. Publicar cada alerta con intervalo (SIN CAMBIOS)
# --------------------------------------
for alerta in alertas:
    payload = json.dumps(alerta)
    client.publish(TOPIC, payload)
    print(f"📤 Publicada alerta en {TOPIC}: {payload}")
    time.sleep(1.5)

client.loop_stop()
client.disconnect()
print("🔌 Conexión cerrada")