# MQTT Client Runner

Este projeto implementa um cliente MQTT configurável para publicar dados simulados de sensores usando o protocolo MQTT. Ele utiliza a biblioteca `paho-mqtt` para comunicação.

## Instalação

1. Certifique-se de que o Python 3 está instalado no sistema.
2. Instale as dependências necessárias:
   ```bash
   pip install paho-mqtt
   ```
3. Clone este repositório e certifique-se de que o arquivo MQTT_Client está no mesmo diretório do script principal.
Uso
Execute o script mqtt_client_runner.py passando os argumentos necessários para configurar o cliente MQTT. Cada comando opcional chama uma função correspondente no programa.

## Comandos disponíveis
Comando	Argumentos	Descrição	Função chamada
```bash
options:
  -h, --help            show this help message and exit
  -b BROKER, --broker BROKER
                        Set the broker URL (setup_broker)
  -m INIT_ID END_ID, --machines INIT_ID END_ID
                        Set the range of machine IDs (setup_machines)
  -s INIT_ID COUNT, --sensors INIT_ID COUNT
                        Set the initial sensor ID and count per machine (setup_sensors)
  -u USER PASSWORD, --user USER PASSWORD
                        Set the MQTT user and password (setup_mqtt_user)
  -t TOPICS, --topics TOPICS
                        Set the topic signature (setup_topics_signature)
  -v INIT_VALUE END_VALUE, --values INIT_VALUE END_VALUE
                        Set the range of values for sensors (setup_value_ranges)
```

## Exemplos de uso
- Configurar o broker:
```bash
python Mqtt_client_runner.py -b "mqtt.example.com"
```
- Configurar IDs de máquinas:
```bash
python Mqtt_client_runner.py -m 1 10
```
- Configurar sensores:
```bash
python Mqtt_client_runner.py -s 100 4
```
- Configurar usuário e senha MQTT:
```bash
python Mqtt_client_runner.py -u "username" "password"
```
- Configurar assinatura de tópicos:
```bash
python Mqtt_client_runner.py -t "IoT/Devices/"
```
- Configurar intervalo de valores dos sensores:
```bash
python Mqtt_client_runner.py -v 50.0 60.0
```
### Comportamento padrão
Se nenhum comando for especificado, o cliente usará as configurações padrão definidas na classe MQTT_Client.

## Licença
Este projeto é licenciado sob a MIT License.