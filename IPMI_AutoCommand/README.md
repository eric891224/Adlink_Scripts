# IPMI Auto Command
## Install Dependencies
```shell
$ pip install -r requirement.txt
```

## Verify IPMI Command Support
### In-Band
```shell
$ python main.py
```

### Out-of-Band
```shell
$ python main.py -I
```

### Optional Flags
| name | flag | description |
| - | - | - |
| input excel path | -i, --input-file-path | default=./IPMI_Commands.xlsx |
| output directory | -o, --output-dir | default=./result/ |
| toggle out-of-band / in-band | -I, --is-out-of-band |  |