import subprocess
import pandas as pd
from datetime import datetime


class IPMICmdSupportVerification:
    def __init__(self, projectInfo, excelFile, workBook, isOutOfBand=True) -> None:
        self.projectInfo = projectInfo
        self.excelFile = excelFile
        self.workBook = workBook
        self.time = datetime.now().strftime("_%Y-%b-%d__%H_%M")

        if isOutOfBand:
            self.__command_template = f"ipmitool -I lanplus -H {projectInfo['IP']} -U {projectInfo['Account_name']} -P {projectInfo['Account_password']} raw"
        else:
            self.__command_template = f"ipmitool -I lanplus -U {projectInfo['Account_name']} -P {projectInfo['Account_password']} raw"

    def saveOutput(self):
        fileNameFormats = self.projectInfo["Output File Name"].split("+")
        fileName = ''

        for format in fileNameFormats:
            format = format.strip()
            if (format == '$Date'):
                fileName += self.time
            elif (format[0] == '$'):
                fileName += str(self.projectInfo[format[1:]])
            else:
                fileName += format.strip('"').strip("'")

        self.workBook.save(self.projectInfo["Output Path"].strip('"').strip("'").strip(" ") + fileName + '.xlsx')