import os
import time


file = open('bulk-report.txt', 'w')

with open('ip-source.txt') as file2:
    dump = file2.read()
    dump = dump.splitlines()


for ip in dump:
    file.write(f'Pinging {ip}\n')
    response = os.popen(f'ping -n 2 {ip}')

    for y in response.readlines():
        file.write(y)

    file.write('-'*60 + '\n'*3)
    time.sleep(5)

file.close()
