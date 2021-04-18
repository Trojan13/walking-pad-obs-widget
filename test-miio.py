from miio import Walkingpad, DeviceException
import configparser
parser = configparser.ConfigParser()
parser.read_file(open(r'config.txt'))
CONFIG_TOKEN = parser.get('walking-pad-twitch', 'token')
CONFIG_IP = parser.get('walking-pad-twitch', 'ip')
try:
    walkingpad = Walkingpad(CONFIG_IP, CONFIG_TOKEN)
except DeviceException:
    raise PlatformNotReady
