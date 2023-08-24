import os
import subprocess
import logging

from pandas import ExcelFile

from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.worksheet.worksheet import Worksheet

from datetime import datetime
from tqdm import tqdm
from typing import Tuple, List

from defs import *

class IPMIAutoCmdTest:
    def __init__(
        self, 
        excelFile: ExcelFile, 
        workBook: Workbook, 
        outputDir: str='./result/', 
        isOutOfBand: bool=False
    ) -> None:
        self.excelFile = excelFile
        self.workBook = workBook
        self.outputDir = os.path.abspath(outputDir)
        self.isOutOfBand = isOutOfBand

        self.time = datetime.now().strftime("%Y-%b-%d_%H-%M")
        self.logger = logging.getLogger(f'main.{self.__str__()}')

        projectInfoDf = self.excelFile.parse('Project Info')
        self.projectInfo = { key: value for key, value in zip(projectInfoDf["Variable"], projectInfoDf["Value"]) }

        if isOutOfBand:
            self.__commandTemplate = f"ipmitool -I lanplus -H {self.projectInfo['IP']} -U {self.projectInfo['Account_Name']} -P {self.projectInfo['Account_Password']} raw"
        else:
            self.__commandTemplate = "ipmitool raw"
    
    def __str__(self):
        return 'IPMIAutoCmdTest'

    def __checkConnection(self) -> bool:
        ping = subprocess.Popen(
            f"ping {self.projectInfo['IP']} {'-n' if os.name == 'nt' else '-c'} 4", 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True,
            shell=True
        )

        stdout, _ = ping.communicate()

        if "received, 100% packet loss" in stdout:
            self.logger.debug('PING LOSS 100%')
            return False

        return True

    def __rawCommand(
        self, 
        netfn: str, 
        cmd: str, 
        *args: List[str]
    ) -> Tuple[str, str]:
        shell = f"{self.__commandTemplate} {netfn} {cmd}"
        for arg in args:
            shell += f' {arg}'

        res = subprocess.Popen(
            shell,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True,
            shell=True
        )

        return res.communicate()

    def __writeCell(
        self, 
        workSheet: Worksheet,
        row: int, 
        col: int, 
        value: str, 
        fill: PatternFill=None
    ) -> None:
        cell = workSheet.cell(row=row, column=col)
        cell.value = value
        if bool(fill): 
            cell.fill = fill

    def saveOutput(self) -> None:
        outputPath = os.path.join(self.outputDir, self.time)
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)

        fileNameFormats = self.projectInfo["Output_File_Name"].split("+")
        fileName = 'OUTOFBAND' if self.isOutOfBand else 'INBAND'

        for format in fileNameFormats:
            format = format.strip()
            if (format[0] == '$'):
                fileName += '_' + str(self.projectInfo[format[1:]]).replace(' ', '-')
            else:
                fileName += '_' + format.strip('"').strip("'").strip().replace(' ', '-')

        self.workBook.save(os.path.join(outputPath, fileName + '.xlsx'))
        self.logger.info(f"Result generated at {os.path.join(outputPath, fileName + '.xlsx')}")
        logging.shutdown()
        os.rename(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logfile'),
            os.path.join(outputPath, 'logfile')
        )
        
    def testRawCmd(self) -> None:
        if self.isOutOfBand and not self.__checkConnection():
            raise Exception(f"Unable to ping {self.projectInfo['IP']}, make sure the connection is viable.")

        rawCmdDf = self.excelFile.parse('Raw CMD')
        rawCmdSheet = self.workBook['Raw CMD']
        for row in rawCmdSheet.iter_rows(max_row=1, values_only=True):
            supColNum = row.index('Availability (A: available/U: unavailable)') + 1
            resColNum = row.index('Response') + 1

        for netfn, cmd, isNan, rowNum in tqdm(
            zip(rawCmdDf['NetFn'], rawCmdDf['CMD'], rawCmdDf['NetFn'].isnull(), range(2, len(rawCmdDf['NetFn'])+2)),
            desc='Testing...',
            total=len(rawCmdDf['NetFn']),
            ncols=100,
            leave=True
        ):
            if isNan:
                continue

            stdout, stderr = self.__rawCommand(
                parseNetFn(netfn).value, 
                parseCmd(cmd),
            )
            self.logger.debug(stdout.rstrip("\n") if stdout else stderr.rstrip("\n"))

            if 'Invalid command' in stderr or 'Unknown' in stderr:
                self.__writeCell(rawCmdSheet, rowNum, supColNum, CommandStatus.UNAVAILABLE.value, RED_FILL)
                self.__writeCell(rawCmdSheet, rowNum, resColNum, stderr)
            else:
                self.__writeCell(rawCmdSheet, rowNum, supColNum, CommandStatus.AVAILABLE.value, GREEN_FILL)
                
