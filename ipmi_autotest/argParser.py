import argparse
import os

from defs.enums import PassLevel

def IPMIAutoTestParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-p', '--project-name',
        type=str,
        required=True,
        help='Project Name',
    )
    parser.add_argument(
        '--pass-level',
        type=str,
        choices=[PassLevel.ALL_MATCH.value, PassLevel.PARTIAL_MATCH.value, PassLevel.IGNORED.value],
        required=True,
        help=
            '''
                The threshold of passing level.
                Only the result pass level greater or equal than the pass level you set here will be considered a success and be marked green in the output file.
                A: all match
                P: partial match
                I: ignored
            '''
    )
    parser.add_argument(
        '-H', '--ip',
        type=str,
        required=True,
        help='BMC IP Address'
    )
    parser.add_argument(
        '-C', '--cypher_suite',
        type=int,
        default=17,
        help='Cypher Suite Used By ipmitool'
    )
    parser.add_argument(
        '-U', '--user-name',
        type=str,
        required=True,
        help='Username For BMC'
    )
    parser.add_argument(
        '-P', '--password',
        type=str,
        required=True,
        help='Password For BMC'
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
        '-A', '--raw-availability-test',
        action='store_true',
        help='Run IPMI Commands Availability Test'
    )
    parser.add_argument(
        '-F', '--raw-functional-test',
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

    parser.add_argument(
        '--hardware-version',
        type=str,
        default=None,
        help='(Optional) HW Version'
    )
    parser.add_argument(
        '--software-version',
        type=str,
        default=None,
        help='(Optional) SW Version'
    )
    parser.add_argument(
        '--tester',
        type=str,
        default=None,
        help='(Optional) Tester Name'
    )

    return parser