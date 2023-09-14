import paho.mqtt.client as mqtt
import time
import random
import datetime
import json



def json_serial(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError("Type not serializable")


def message():
    dados = {
        'date_measure': datetime.datetime.now(),
        'consume_breaker': random.uniform(0.1, 2.0),
        'demand_breaker': random.uniform(1.0, 10.0),
        'phase_one_power_factor': random.uniform(0.85, 1.15),
        'phase_two_power_factor': random.uniform(0.85, 1.15),
        'phase_three_power_factor': random.uniform(0.85, 1.15),
        'phase_one_voltage': random.uniform(0.1, 2.0),
        'phase_two_voltage': random.uniform(0.1, 2.0),
        'phase_three_voltage': random.uniform(0.1, 2.0),
        'temperature_measurement': random.uniform(25.5, 70.5),
        'gateway_number': 150,
        'breaker_idbreaker': 9
    }

    return dados

broker="127.0.0.1"
port=1883


def on_publish(client, userdata, result):
    print("Mensagem publicada com sucesso!")


while(True):
    try:
        client1 = mqtt.Client('photon')
        client1.on_publish = on_publish
        client1.connect(broker, port)
        ret = client1.publish('photon', json.dumps(message(), default= json_serial))
        time.sleep(60)
    except:
        pass
    







