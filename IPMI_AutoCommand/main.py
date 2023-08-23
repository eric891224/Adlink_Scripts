import os
# import logging

from openpyxl import load_workbook

from defs import *
from testUnits import *
from parsers import IPMIAutoCommandParser


if __name__ == '__main__':
    parser = IPMIAutoCommandParser()
    args = parser.parse_args()

    excelFile = pd.ExcelFile(os.path.abspath(args.input_file_path))
    workBook = load_workbook(os.path.abspath(args.input_file_path))

    tester = IPMIAutoCmdTest(
        excelFile, 
        workBook, 
        output_dir=args.output_directory, 
        isOutOfBand=args.is_out_of_band
    )

    tester.testRawCmd()
    tester.saveOutput()