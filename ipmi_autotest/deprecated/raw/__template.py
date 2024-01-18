from typing import List, Dict, Tuple

from .base import TestCase
from defs import Result

class TestCaseTemplate(TestCase):
    '''
        For following conditions, one must implement the getDataN() and behavioralVerification() methods:
        1. Request Length = N (N > 0):          Must implement getData1(), getData2(), ..., getDataN()
        2. Verification Type = B (Behavior):    Must implement behavioralVerification()
    '''
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
            this function should return a list of all possible data for this data field.
        '''
        ### TODO
        ### Example: Get Sensor Reading 

        # data1 = []
        #
        # # call sdr elist and obtain all sensor numbers
        # stdout, stderr = self.generalCommand("sdr", "elist")
        # sensors = stdout.split('\n')
        # for sensor in sensors:
        #     if '|' in sensor:
        #         sensorNumber = sensor.split('|')[1].strip(' ').rstrip('h').lower()
        #         data1.append(f'0x{sensorNumber}')
        
        # return data1

        pass

    def behavioralVerification() -> Tuple[Result, str]:
        '''
            this function only needs to be implemented when verificationType == BEHAVIOR
            this function verifies the behavior of the raw command

            return: (result, info)
                result: whether the behavior is correct or not (Result.PASS or Result.FAIL)
                info: comments about the behavior, set to None if not needed
        '''
        ### TODO
        ### Example:

        # [do something to check if the command is correct...]
        # result = Result.PASS
        # info = None
        #
        # return result, info

        pass