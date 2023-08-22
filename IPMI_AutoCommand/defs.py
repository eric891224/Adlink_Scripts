from enum import Enum

class CommandStatus(Enum):
    AVAILABLE = 'A'
    UNAVAILABLE = 'U'
    # LIMITAION = 'L'
    # INCOMPLETE = 'I'

class NetFn(Enum):
    CHASSIS = '0x00'
    BRIDGE = '0x02'
    SENSOR_EVENT = '0x04'
    APPLICATION = '0x06'
    FIRMWARE = '0x08'
    STORAGE = '0x0a'
    TRANSPORT = '0x0c'
