#!/usr/bin/env python3

"""
This program sets modbus registers of a device according to a CSV file

Usage:
python3 write_config.py <csv_file> <host> [<port>] [<unit>]
"""

import csv
import sys
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

def main():
    """Entrypoint if script is run standalone"""

    if len(sys.argv) < 3:
        print("Please refer to the usage instructions")
        sys.exit(1)

    path = sys.argv[1]
    host = sys.argv[2]

    try:
        port = sys.argv[3]
    except IndexError:
        port = 502

    try:
        unit = sys.argv[4]
    except IndexError:
        unit = 0xFF

    config_parser(host, port, unit, path)


def config_parser(host, port, unit, path):
    """Parses the CSV file and writes line by line to the modbus device"""
    try:
        connection = ModbusClient(host, port)
        with open(path, "r", encoding="utf-8") as handle:
            reader = csv.reader(handle)
            for row in reader:
                value_writer(connection, unit, row)
        connection.close()
    except KeyboardInterrupt:
        connection.close()
        sys.exit(0)


def value_writer(connection, unit, row):
    """Writes the value to the provided modbus device connection"""
    reg_type = row[0]
    register = row[1]
    value = row[2]

    print(f"Type: {reg_type}, Address: {register}, Value: {value} ... ", end="")

    if reg_type == "HOLDING":
        result = connection.write_register(int(register), int(value), unit=unit)
    if reg_type == "COIL":
        result = connection.write_coil(int(register), int(value), unit=unit)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
