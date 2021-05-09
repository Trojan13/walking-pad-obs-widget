try:
    from configparser import ConfigParser as _ConfigParser
except ImportError:  # Python 2
    from ConfigParser import ConfigParser as _ConfigParser


# Version of realpython-reader package
__version__ = "1.0.0"

# Read URL of feed from config file
_cfg = _ConfigParser()
with _resources.path("reader", "config.txt") as _path:
    _cfg.read(str(_path))
CONFIG_TOKEN = parser.get('walking-pad-twitch', 'token')
CONFIG_IP = parser.get('walking-pad-twitch', 'ip')
print("Config loaded...")
