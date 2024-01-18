from typing import Tuple, Dict
from .enums import NetFn, PassLevel, VerificationType

def parseNetFn(netfn: str) -> NetFn:
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

def parsePassLevel(passLevel: str) -> PassLevel:
    if passLevel == 'A': return PassLevel.ALL_MATCH
    elif passLevel == 'P': return PassLevel.PARTIAL_MATCH
    elif passLevel == 'I': return PassLevel.IGNORED
    else: raise Exception(f"PassLevel '{passLevel}' not defined.")

def parseVerificationType(verificationType: str) -> str:
    if verificationType == 'A': return VerificationType.ACCURACY
    elif verificationType == 'B': return VerificationType.BEHAVIOR
    else: raise Exception(f"Verification Type {verificationType} not defined")

def parseRawFunctionName(functionName: str) -> str:
    strings = functionName.replace('-', '_').split(' ')
    PascalCase = ""
    for string in strings:
        PascalCase += string.title()

    return PascalCase

# deprecated
# def parseLabelKey(key: str) -> Tuple[str]:
#     keys = key.lstrip('[').rstrip(']').replace(' ', "").split(',')
#     return tuple(keys)

# not used yet
def parseFruInfo(stdout: str) -> Dict[str, str]:
    stdout = stdout.split('\n')
    fruInfo = {}
    for line in stdout:
        if ':' in line:
            line = line.split(':')
            fruInfo[line[0].strip(" ")] = line[1].strip(' ') if len(line) <= 2 else ':'.join(line[1:]).strip(' ')

    return fruInfo

# not used yet
def parseSensorInfo(stdout: str) -> Dict[str, str]:
    stdout = stdout.split('\n')
    sensorInfo = {}
    for line in stdout:
        if ':' in line:
            line = line.split(':')
            sensorInfo[line[0].strip(' ')] = line[1].strip(' ') if len(line) <= 2 else ':'.join(line[1:]).strip(' ')

    return sensorInfo
