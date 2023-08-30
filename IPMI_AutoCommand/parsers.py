import argparse
import os

def IPMIAutoCommandParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i', '--input-file-path',
        default='./IPMI_Commands.xlsx',
        type=os.path.abspath,
        help='IPMI Commands Checklist Excel Path'
    )
    parser.add_argument(
        '-o', '--output-directory',
        default='./result/',
        type=os.path.abspath,
        help='Ouput Excel Path'
    )
    parser.add_argument(
        '-I', '--is-out-of-band',
        action='store_true',
        help='Toggle Out-of-band / In-band'
    )
    parser.add_argument(
        '-S', '--raw-support-test',
        action='store_true',
        help='Run IPMI Commands Support Verification'
    )
    parser.add_argument(
        '-F', '--functional-test',
        action='store_true',
        help='Run IPMI Commands Functional Test'
    )
    parser.add_argument(
        '-f', '--fru',
        action='store_true',
        help='Run Fru Test'
    )
    parser.add_argument(
        '-s', '--sensor',
        action='store_true',
        help='Run Sensor Test'
    )

    return parser