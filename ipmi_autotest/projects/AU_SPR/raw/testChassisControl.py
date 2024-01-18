from typing import Dict, Tuple

from base import TestCase
from defs.enums import Result

class TestChassisControl(TestCase):
    '''
        Chassis Control 
            0x00 0x02 D[0]

        D[0]:
            0x00: power off
            0x01: power on
            0x02: power cycle
            0x03: power reset

            0x04, 0x05: not tested in this project

        refer to ipmi spec section "Chassis Control Command" for further information
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
        import time

        result = Result.PASS
        info = ""

        # test power on
        self.testRoutine.logger.debug(f"\tTEST: power on")
        self.rawCommand(self.netfn, self.cmd, '0x01')
        time.sleep(10)
        stdout, stderr = self.generalCommand('power', 'status')
        stdout = stdout.strip('\n').strip(' ').split(' ')[-1]
        stderr = stderr.strip('\n').strip(' ')
        if stdout != 'on':
            info += f"FAILED: Req: '0x01' should be power on\n"
            self.testRoutine.logger.debug(f"\tFAILED: Req: '0x01' should be power on")
            result = Result.FAIL

        # test power off
        self.testRoutine.logger.debug(f"\tTEST: power off")
        self.rawCommand(self.netfn, self.cmd, '0x00')
        time.sleep(10)
        stdout, stderr = self.generalCommand('power', 'status')
        stdout = stdout.strip('\n').strip(' ').split(' ')[-1]
        stderr = stderr.strip('\n').strip(' ')
        if stdout != 'off':
            info += f"FAILED: Req: '0x00' should be power off"
            self.testRoutine.logger.debug(f"\tFAILED: Req: '0x00' should be power off")
            result = Result.FAIL

        # TODO: test power cycle
        # self.rawCommand(self.netfn, self.cmd, '0x02')

        # TODO: test power reset
        # self.testRoutine.logger.debug(f"\tTEST: power reset")
        # self.rawCommand(self.netfn, self.cmd, '0x03')
        # time.sleep(10)
        # stdout, stderr = self.generalCommand('power', 'status')
        # stdout = stdout.strip('\n').strip(' ').split(' ')[-1]
        # stderr = stderr.strip('\n').strip(' ')
        # if stdout != 'off':
        #     info += f"FAILED: Req: '0x03' should be power reset"
        #     self.testRoutine.logger.debug(f"\tFAILED: Req: '0x03' should be power reset")
        #     result = Result.FAIL

        return result, info