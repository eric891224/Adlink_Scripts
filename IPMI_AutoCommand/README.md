# IPMI Auto Command
## Install Dependencies
```shell
$ pip install -r requirement.txt
```

## Flags
| name | flag | description |
| - | - | - |
| input excel path | `-i`, `--input-file-path` | default=`./IPMI_Commands.xlsx` |
| output directory | `-o`, `--output-dir` | default=`./result/` |
| toggle out-of-band / in-band | `-I`, `--is-out-of-band` | not set by default |
| toggle raw command support test | `-S`, `--raw-support-test` | not set by default |
| toggle raw functional test | `-F`, `--functional-test` | not set by default |
| toggle fru test | `-f`, `--fru` | not set by default |
| toggle sensor test | `-s`, `--sensor` | not set by default |

## Verify IPMI Command Support
### In-Band
```shell
$ python main.py -S
```

### Out-of-Band
```shell
$ python main.py -IS
```