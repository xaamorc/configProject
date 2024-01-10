from resources.config import ConfigSettings
from resources.config import StartSettings

config = ConfigSettings()
print(config.NAME)
print(config.MODEL)
print(config.BRAND)

start = StartSettings()
print(start.START)
print(start.STOP)
print(start.PAUSE)