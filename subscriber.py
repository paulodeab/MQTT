import paho.mqtt.client as mqtt

# Callback chamada quando a conexão com o broker é estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker com código de resultado: " + str(rc))
    # Subscreve ao tópico
    client.subscribe("photon/breaker")

# Callback chamada quando uma mensagem é recebida em um tópico inscrito
def on_message(client, userdata, msg):
    print("Mensagem recebida no tópico " + msg.topic + ": " + str(msg.payload))

# Configuração do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conecta ao broker MQTT público (test.mosquitto.org)
client.connect("broker.hivemq.com", 1883, 8000)

# Inicia o loop de comunicação
client.loop_forever()
