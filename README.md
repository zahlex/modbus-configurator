# modbus-configurator

## Principle

This program sets modbus registers of a device according to a CSV file

## Installation

Latest Python3 needs to be present on the system, then run:
```
git clone https://github.com/zahlex/modbus-configurator
cd modbus-configurator
pip install -r requirements.txt
```

## CSV Format:

```
Type, Address, Value
```
```
HOLDING, 120, 123
COIL, 210, 1
```

## Usage:

```
python3 write_config.py <csv_file> <host> [<port>] [<unit>]
```

## License

All resources of this project are licensed under the BSD 3-Clause License