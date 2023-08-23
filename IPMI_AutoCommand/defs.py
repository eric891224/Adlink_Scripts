from enum import Enum
from openpyxl.styles import PatternFill

class CommandStatus(Enum):
    AVAILABLE = 'A'
    UNAVAILABLE = 'U'

class NetFn(Enum):
    CHASSIS = '0x00'
    BRIDGE = '0x02'
    SENSOR_EVENT = '0x04'
    APPLICATION = '0x06'
    FIRMWARE = '0x08'
    STORAGE = '0x0a'
    TRANSPORT = '0x0c'
    PICMG = '0x2c'

GREEN_FILL = PatternFill(start_color='00ff00', fill_type='solid')
RED_FILL = PatternFill(start_color='ff0000', fill_type='solid')

def parseNetFn(netfn: str) -> None:
    if netfn == 'Chassis': return NetFn.CHASSIS
    elif netfn == 'Bridge': return NetFn.BRIDGE
    elif netfn == 'S/E': return NetFn.SENSOR_EVENT
    elif netfn == 'App': return NetFn.APPLICATION
    elif netfn == 'Firmware': return NetFn.FIRMWARE
    elif netfn == 'Storage': return NetFn.STORAGE
    elif netfn == 'Transport': return NetFn.TRANSPORT
    elif netfn == 'PICMG': return NetFn.PICMG
    else: raise Exception(f"Netfn '{netfn}' not found.")

def parseCmd(cmd: str) -> str:
    return f'0x{cmd.rstrip("h")}'