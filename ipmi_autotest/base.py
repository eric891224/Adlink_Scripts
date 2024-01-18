from abc import ABC, ABCMeta, abstractmethod
from typing import List, Dict, Tuple, Union

from defs.enums import VerificationType, Result

class TestCaseMeta(ABCMeta):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

        # deprecated

        # Check for the existence of getData methods based on numData
        # if 'numData' in attrs:
        #     for i in range(1, attrs['numData'] + 1):
        #         method_name = f'getData{i}'
        #         if method_name not in attrs:
        #             raise NotImplementedError(f"Class {name} is missing the method {method_name}, please implement the method before testing.")


class TestCase(ABC, metaclass=TestCaseMeta):
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
        self.testRoutine = testRoutine
        self.netfn = netfn
        self.cmd = cmd
        self.numData = numData
        self.needVerify = needVerify

        self.generalCommand = testRoutine._IPMIAutoTest__generalCommand
        self.rawCommand = testRoutine._IPMIAutoTest__rawCommand

        if needVerify:
            self.response = dict()
            self.labels = labels
            self.verificationType = verificationType

    def getData(self) -> List[List[str]]:
        '''
            this function returns all possible data fields from json file
        '''
        data = []

        if self.verificationType == VerificationType.ACCURACY:
            for i, label in enumerate(self.labels, start=1):
                if (len(label) != self.numData):
                    self.testRoutine.logger.warn(f"\tReq length mismatched in {i}th req. Number of data should be {self.numData} but received {len(label.req)} from JSON")
                data.append(label.req)

        return data
    
    def test(self) -> Tuple[Union[int, Result], str]:
        self.testRoutine.logger.debug(f"NetFn: {self.netfn}, CMD: {self.cmd}")
        if self.verificationType == VerificationType.ACCURACY:
            for args in self.getData():
                stdout, stderr = self.rawCommand(self.netfn, self.cmd, *args)
                stdout = stdout.strip('\n').strip(' ')
                if self.needVerify:
                    self.response[tuple(args)] = stdout if not stderr else stderr
                else:
                    self.testRoutine.logger.debug(f"\tReq: {args}\tRes: {stdout if not stderr else stderr}")

        if self.needVerify:
            result, info = self.verify(self.verificationType)
        else:
            result = Result.PASS
            info = None

        return result, info

    def verify(self, verificationType: str=None) -> Tuple[Union[int, Result], str]:
        '''
            verificationType:
                1. ACCURACY: verify raw command response acc
                2. BEHAVIOR: verify raw command behavior
        '''
        result = info = None
        
        if verificationType == VerificationType.ACCURACY:
            total = len(self.labels)
            correct = 0

            # for input in self.labels.keys():
            #     if self.response.get(input) == None:    # error: test case not exist
            #         self.testRoutine.logger.debug(f"\tERROR: Req: {input} untested, please make sure getData() includes this test case")
            #         continue

            #     if self.response[input] != self.labels[input]:  # error: mismatch
            #         self.testRoutine.logger.debug(f"\tERROR: Req: {input}\tRes: {self.response[input]} mismatch with expected Res {self.labels[input]}")
            #         continue
            #     else:   # pass
            #         self.testRoutine.logger.debug(f"\tPASS: Req: {input}\tRes: {self.response[input]}")
            #         correct += 1

            for label in self.labels:
                key = tuple(label.req)
                if self.response.get(key) == None:     # error: test case not exist
                    self.testRoutine.logger.debug(f"\tERROR: Req: {key} untested, please make sure getData() includes this test case")
                    continue
                    
                if self.response[key] != self.labels[key]:      # error: mismatch
                    self.testRoutine.logger.debug(f"\tERROR: Req: {key}\tRes: {self.response[key]} mismatch with expected Res {self.labels[key]}")
                    continue
                else:   # pass
                    self.testRoutine.logger.debug(f"\tPASS: Req: {key}\tRes: {self.response[key]}")
                    correct += 1

            result = int(correct / total * 100) if total != 0 else 100
            info = "check log file for incorrect test case results" if result < 100 else None

        elif verificationType == VerificationType.BEHAVIOR:
            result, info = self.behavioralVerification()

        return result, info
    
    def behavioralVerification(self) -> Tuple[Result, str]:
        raise NotImplementedError("Must implement method behavioralVerification() when needVerify is set to True.")