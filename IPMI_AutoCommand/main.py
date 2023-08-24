import os
import logging

from pandas import ExcelFile
from openpyxl import load_workbook

from defs import *
from testUnits import *
from parsers import IPMIAutoCommandParser


if __name__ == '__main__':
    parser = IPMIAutoCommandParser()
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG, 
        format="[%(asctime)s][%(name)-5s][%(levelname)-5s] %(message)s (%(filename)s:%(lineno)d)",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=getLoggingFileHandler(os.path.dirname(os.path.realpath(__file__))),
    )

    excelFile = ExcelFile(os.path.abspath(args.input_file_path))
    workBook = load_workbook(os.path.abspath(args.input_file_path))

    tester = IPMIAutoCmdTest(
        excelFile, 
        workBook, 
        outputDir=args.output_directory, 
        isOutOfBand=args.is_out_of_band
    )

    tester.testRawCmd()
    tester.saveOutput()