# IPMI AutoTest
## Install Dependencies
```shell
$ pip install -r requirement.txt
```

## Project Config Flags
| Name | Flag | Description |
| --- | --- | --- |
| Project Name | `-p`, `--project-name` | Required: Project Name |
| Pass Level | `--pass-level` | `A: all match` `P: partial match` `I: ignored` Required: The threshold of passing level. Only the result pass level greater or equal than the pass level you set here will be considered a success and be marked green in the output file. |
| BMC IP Address | `-H`, `--ip` | Required: BMC IP Address |
| Cypher Suite | `-C`, `--cypher-suite` | Default=17: Cypher Suite Used By ipmitool |
| Username For BMC | `-U`, `--user-name` | Required: Username For BMC |
| Password For BMC | `-P`, `--password` | Required: Password For BMC |
| `*`Hardware Version | `--hardware-version` | Optional: HW Version |
| `*`Software Version | `--software-version` | Optional: SW Version |
| `*`Tester Name | `--tester` | Optional: Tester Name |
| Output Directory | `-o`, `--output-directory` | Default=`ipmi_autotest/result/`: Output Excel Path |

`*`: TBD

## Testing Options Flags
| Option | Flag | Description |
| --- | --- | --- |
| Toggle Out-of-band / In-band | `-I`, `--is-out-of-band` | Not set by default: Toggle Out-of-band / In-band |
| Toggle Raw Command Availability Test | `-A`, `--raw-availability-test` | Not set by default: Run IPMI Commands Availability Test |
| Toggle Raw Functional Test | `-F`, `--raw-functional-test` | Not set by default: Run IPMI Commands Functional Test |
| `*`Toggle Fru Test | `-f`, `--fru` | Not set by default: Run Fru Test |
| `*`Toggle Sensor Test | `-s`, `--sensor` | Not set by default: Run Sensor Test |

`*`: TBD

## Example Usage
```shell
$ python ipmi_autotest \
    -p example \
    --pass-level A \
    -H xxx.xxx.xxx.xxx \
    -U admin \
    -P admin \
    -IAF
```
this command should run the raw command's availability & functional test