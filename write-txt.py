import configparser
import time

parser = configparser.ConfigParser()
parser.read_file(open(r'config.txt'))
CONFIG_TOKEN = parser.get('walking-pad-twitch', 'token')
CONFIG_IP = parser.get('walking-pad-twitch', 'ip')
print(CONFIG_TOKEN)
print(CONFIG_IP)

i = 0
while True:
    i += 1
    time.sleep(1)
    with open('walkingdata.txt', 'w') as f:
        f.write(str(i))
