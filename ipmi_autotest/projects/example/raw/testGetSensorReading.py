from typing import Dict, Tuple

from base import TestCase

class TestGetSensorReading(TestCase):
    def __init__(
            self, 
            testRoutine: 'IPMIAutoTest',
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

    '''
        Since [Get Sensor Reading] requires only accuracy verification, one doesn't need to implement behavioralVerification().
        Instead, one needs to prepare labels/getSensorReadingLabels.json for computing accuracy.
        
        Leaving this place as blank is fine.
    '''