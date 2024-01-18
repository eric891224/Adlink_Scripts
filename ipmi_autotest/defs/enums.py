from enum import Enum
from functools import total_ordering

class AutoTestType(Enum):
    AVAILABILITY = 'A'
    FUNCTIONAL = 'F'

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

class VerificationType(Enum):
    ACCURACY = 'accuracy'
    BEHAVIOR = 'behavior'

class Result(Enum):
    PASS = 'P'
    FAIL = 'F'

@total_ordering
class PassLevel(Enum):
    ALL_MATCH = 'A'
    PARTIAL_MATCH = 'P'
    IGNORED = 'I'
    # strict: A > P > I

    def __eq__(self, other):
        if not isinstance(other, PassLevel):
            raise TypeError(f"Cannot compare PassLevel with {other}, type of which is {type(other)}")

        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, PassLevel):
            raise TypeError(f"Cannot compare PassLevel with {other}, type of which is {type(other)}")
        
        cmpTable = {
            PassLevel.ALL_MATCH.value: 3,
            PassLevel.PARTIAL_MATCH.value: 2,
            PassLevel.IGNORED.value: 1
        }

        return cmpTable[self.value] < cmpTable[other.value]