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
        '-F', '--functional-test',
        action='store_true',
        help='Run Functional Test For IPMI Commands. When Not Set, Only Check Commands Support'
    )

    return parser