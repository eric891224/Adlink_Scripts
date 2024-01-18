from typing import Dict, Tuple

from base import TestCase
from defs.enums import Result

class TestCaseTemplate(TestCase):
    '''
        For following conditions, one must prepare label pairs or implement behavioralVerification() method:
        1. Verification Type = A (Accuracy):    Must prepare labels/xxxLabels.json, in which the size of req == Request Length
        2. Verification Type = B (Behavior):    Must implement behavioralVerification()
    '''
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

    def behavioralVerification(self) -> Tuple[Result, str]:
        '''
            This function only needs to be implemented when verificationType == BEHAVIOR.
            This function verifies the behavior of the raw command.

            return: (Result, Info)
                Result (Result.PASS | Result.FAIL): whether the behavior is correct or not (Result.PASS or Result.FAIL)
                Info (str): comments about the behavior, set to None if not needed 
        '''
        ### TODO
        ### Example:

        # [do something to check if the command is correct...]
        # result = Result.PASS
        # info = None
        #
        # return result, info

        pass