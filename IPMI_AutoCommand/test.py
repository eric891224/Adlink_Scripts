# from datetime import datetime
# import pandas as pd
# import subprocess
# from openpyxl import load_workbook

# workbook = load_workbook('../IPMI_BMC_test/IPMI_test_case_v03.xlsx')
# workbook.save('./test.xlsx')

# config = pd.read_json('../IPMI_BMC_test/config.json', typ='series')
# print(config['check_project']['raw'])

# ping = subprocess.Popen(
#     "ping 192.168.0.100 -c 4", 
#     stdout=subprocess.PIPE, 
#     stderr=subprocess.PIPE, 
#     universal_newlines=True,
#     shell=True
# )

# stdout, stderr = ping.communicate()

# print("STDOUT")
# print(stdout)
# print("STDERR")
# print(stderr)

# ping = subprocess.Popen(
#     "ipmitool -H 192.168.0.100 -U admin -P admin raw 0x06 0x22", 
#     stdout=subprocess.PIPE, 
#     stderr=subprocess.PIPE, 
#     universal_newlines=True,
#     shell=True
# )

# stdout, stderr = ping.communicate()

# # print(stdout.split(" "))
# print(bool(stdout))
# print(bool(stderr))

for i in range(1, 5):
    print(i)