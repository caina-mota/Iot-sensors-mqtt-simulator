import argparse
from Mqtt_client import MQTT_Client


def main():
    # Instancia o cliente MQTT
    mqtt_client = MQTT_Client()

    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description="Configure and initialize the MQTT Client")
    
    # Argumentos opcionais para configurar o cliente
    parser.add_argument("-b", "--broker", type=str, help="Set the broker URL (setup_broker)")
    parser.add_argument("-m", "--machines", nargs=2, type=int, metavar=("INIT_ID", "END_ID"),
                        help="Set the range of machine IDs (setup_machines)")
    parser.add_argument("-s", "--sensors", nargs=2, type=int, metavar=("INIT_ID", "COUNT"),
                        help="Set the initial sensor ID and count per machine (setup_sensors)")
    parser.add_argument("-u", "--user", nargs=2, type=str, metavar=("USER", "PASSWORD"),
                        help="Set the MQTT user and password (setup_mqtt_user)")
    parser.add_argument("-t", "--topics", type=str, help="Set the topic signature (setup_topics_signature)")
    parser.add_argument("-v", "--values", nargs=2, type=float, metavar=("INIT_VALUE", "END_VALUE"),
                        help="Set the range of values for sensors (setup_value_ranges)")
    parser.add_argument("-c", "--conversion_value", type=int, help="Set the conversion value (setup_conversion_value)")

    # Analisa os argumentos fornecidos
    args = parser.parse_args()

    # Executa as funções correspondentes com base nos argumentos fornecidos
    if args.broker:
        mqtt_client.setup_broker(args.broker)
    
    if args.machines:
        init_id, end_id = args.machines
        mqtt_client.setup_machines(init_id, end_id)
    
    if args.sensors:
        init_id, count = args.sensors
        mqtt_client.setup_sensors(init_id, count)
    
    if args.user:
        user, password = args.user
        mqtt_client.setup_mqtt_user(user, password)
    
    if args.topics:
        mqtt_client.setup_topics_signature(args.topics)
    
    if args.values:
        init_value, end_value = args.values
        mqtt_client.setup_value_ranges(init_value, end_value)

    if args.conversion_value:
        conversion_value = args.conversion_value
        mqtt_client.setup_conversion_value(conversion_value)
    
    # Inicializa o cliente MQTT
    mqtt_client.initialize_client()


if __name__ == "__main__":
    main()