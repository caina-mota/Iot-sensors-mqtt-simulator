import paho.mqtt.client as mqtt
from random import uniform
from time import sleep
from Pack_unpack import generate_binary_packet


class MQTT_Client():
    machine_ids = []
    sensors = {}
    client_id = 1
    broker_url = "localhost"
    topics_signature = "IoTSensors/Machines/"
    conversion_value = 4096

    def __init__(self):
        self.setup_default_machines()
        self.setup_value_ranges(50, 60)
        self.client = mqtt.Client(client_id=f"Client {self.client_id}", protocol=mqtt.MQTTv31)
        

    def setup_default_machines(self):
        # setup das máquinas e sensores
        self.machine_ids = [1, 2, 3, 4, 5, 6, 7, 8]
        self.sensors = {1: [1, 2, 3, 4],
                        2: [5, 6, 7, 8],
                        3: [9, 10, 11],
                        4: [12, 13, 14],
                        5: [15, 16],
                        6: [17, 18, 18, 20],
                        7: [21, 22, 23],
                        8: [24, 25, 26, 27]}

    def setup_conversion_value(self, conversion_value: int):
        self.conversion_value = conversion_value

    def setup_mqtt_client(self):
        # cria um identificador baseado no id da maquina
        self.client = mqtt.Client(client_id="Client %d" % (self.client_id),
                                  protocol=mqtt.MQTTv31)

        # conecta no broker
        self.client.connect(self.broker_url, 1883)

    def setup_mqtt_user(self, username: str, password: str):
        if self.client is None:
            print("mqtt client ainda não foi configurado")
            return -1

        # seta senha e usuario
        self.client.username_pw_set(username=username, password=password)

        # conecta no broker
        self.client.connect(self.broker_url, 1883)
        return 1

    def setup_broker(self, url: str):
        self.broker_url = url
        # conecta no broker
        self.client.connect(self.broker_url, 1883)

    def setup_topics_signature(self, topics_signature: str):
        self.topics_signature = topics_signature

    def setup_machines(self, init_id: int, end_id: int):
        self.machine_ids = list(range(init_id, end_id, 1))
        self.setup_sensors(1, 2)

    def setup_sensors(self, init_id: int, count_per_machine: int):
        end_id = init_id + count_per_machine
        for machine_id in self.machine_ids:
            self.sensors[machine_id] = (list(range(init_id, end_id, 1)))
            init_id = end_id
            end_id = init_id + count_per_machine

    def setup_value_ranges(self, init_value: float, end_value: float):
        self.initial_value = init_value
        self.end_value = end_value

    def initialize_client(self):
        if (len(self.machine_ids) < 1):
            self.setup_default_machines()

        while True:
            for machine_id in self.machine_ids:
                for sensor_id in self.sensors[machine_id]:
                    sensor_value = round(uniform(self.initial_value,
                                                 self.end_value), 3)
                    # monta o pacote a ser enviados
                    packet, _ = generate_binary_packet(machine_id=machine_id,
                                                       sensor_id=sensor_id,
                                                       float_value=sensor_value,
                                                       conversion_value=self.conversion_value)

                    # envia a publicação
                    self.client.publish(topic=self.topics_signature +
                                        str(machine_id),
                                        payload=packet,
                                        qos=0)
                    print('Data sent to: ' +
                          f'\"{self.topics_signature + str(machine_id)}\" Topic' +
                          f'\tSensor value: {sensor_value}'
                          f'\tData: {packet}')

            # timer para a próxima interação
            sleep(1)


if __name__ == "__main__":
    mqtt_client = MQTT_Client()
    mqtt_client.initialize_client()
