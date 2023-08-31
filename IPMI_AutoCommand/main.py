import os
import logging
import sys
import signal

from functools import partial
from pandas import ExcelFile
from openpyxl import load_workbook

from defs import *
from testUnits import IPMIAutoCommandTest
from parsers import IPMIAutoCommandParser

def exit_gracefully(logger: logging.Logger, sig: int, frame) -> None:
    logger.info('Program terminated')
    logging.shutdown()
    os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), LOGFILE_NAME))
    sys.exit(0)

if __name__ == '__main__':
    parser = IPMIAutoCommandParser()
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG, 
        format="[%(asctime)s][%(name)-5s][%(levelname)-5s] %(message)s (%(filename)s:%(lineno)d)",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=getLoggingFileHandler(os.path.dirname(os.path.realpath(__file__))),
    )

    signal.signal(signal.SIGINT, partial(exit_gracefully, logging.getLogger('main')))

    excelFile = ExcelFile(os.path.abspath(args.input_file_path))
    workBook = load_workbook(os.path.abspath(args.input_file_path))

    tester = IPMIAutoCommandTest(
        excelFile, 
        workBook, 
        outputDir=args.output_directory, 
        isOutOfBand=args.is_out_of_band,
        doRawSupportTest=args.raw_support_test,
        doFunctionalTest=args.functional_test,
        doFruTest=args.fru,
        doSensorTest=args.sensor
    )

    tester.runTest()