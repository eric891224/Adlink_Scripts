from typing import List, Dict, Tuple

from .base import TestCase

class TestGetSensorReading(TestCase):
    def __init__(
            self, 
            testRoutine: 'IPMIAutoCommandTest',
            netfn: str,
            cmd: str,
            numData: int, 
            needVerify: bool=False,
            labels: Dict[Tuple[str], str]=None,
            verificationType: str=None
    ) -> None:
        super().__init__(
            testRoutine, 
            netfn, 
            cmd, 
            numData, 
            needVerify=needVerify, 
            labels=labels, 
            verificationType=verificationType
        )

    def getData1(self) -> List[str]:
        '''
            this function should obtain all possible data for this data field.
        '''
        data1 = []
        
        # call sdr elist and obtain all sensor numbers
        stdout, stderr = self.generalCommand("sdr", "elist")
        sensors = stdout.split('\n')
        for sensor in sensors:
            if '|' in sensor:
                sensorNumber = sensor.split('|')[1].strip(' ').rstrip('h').lower()
                data1.append(f'0x{sensorNumber}')
        
        return data1