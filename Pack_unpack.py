import struct
from datetime import datetime


def generate_binary_packet(machine_id, sensor_id, float_value,
                           conversion_value=4096):
    # Garantir que os valores estejam no intervalo especificado para cada campo
    machine_id = machine_id & 0xFFFF               # 16 bits max 4095
    sensor_id = sensor_id & 0xFFFF                 # 16 bits
    int_value = int(float_value * conversion_value) & 0xFFFF   # 16 bits max signed int 32767
    conversion_value = conversion_value & 0xFFFF   # 16 bits, UInt padrão como 4096

    # Timestamp
    timestamp = datetime.now()
    day = timestamp.day & 0xFF          # 8 bits
    month = timestamp.month & 0xFF      # 8 bits
    year = timestamp.year & 0xFFFF      # 16 bits
    hour = timestamp.hour & 0xFF        # 8 bits
    minute = timestamp.minute & 0xFF    # 8 bits
    second = timestamp.second & 0xFF    # 8 bits

    # Formato da estrutura binária
    # 'B' = 8 bits (unsigned char), 'H' = 16 bits (unsigned short)
    packet_format = ">HHHHBBHBBB"
    packet = struct.pack(packet_format, machine_id, sensor_id, int_value,
                         conversion_value, day, month, year, hour, minute,
                         second)

    # Retorna o pacote e o representa como hexadecimal para facilitar a leitura
    return packet, packet.hex()


def unpack_binary_packet(packet):
    # Formato para descompactar
    packet_format = ">HHHHBBHBBB"

    # Descompacta os dados com struct.unpack
    unpacked_data = struct.unpack(packet_format, packet)

    # Atribui os valores aos campos individuais
    machine_id = unpacked_data[0]
    sensor_id = unpacked_data[1]
    int_value = unpacked_data[2]
    conversion_value = unpacked_data[3]

    day = unpacked_data[4]
    month = unpacked_data[5]
    year = unpacked_data[6]
    hour = unpacked_data[7]
    minute = unpacked_data[8]
    second = unpacked_data[9]

    timestamp = datetime(year, month, day, hour, minute, second)

    return {
        "machine_id": machine_id,
        "sensor_id": sensor_id,
        "int_value": int_value,
        "conversion_value": conversion_value,
        "float_value": float(int_value / conversion_value),
        "timestamp": timestamp
    }


if __name__ == "__main__":
    # Exemplo de uso
    machine_id = 1
    sensor_id = 5
    int_value = 1500

    packet, hex_representation = generate_binary_packet(machine_id, sensor_id,
                                                        int_value)
    print("Pacote Binário:", packet)
    print("Hexadecimal:", hex_representation)

    unpacked_data = unpack_binary_packet(packet)

    print("Dados Descompactados:", unpacked_data)
