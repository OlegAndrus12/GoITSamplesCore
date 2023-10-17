# https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
import pytz
from datetime import datetime


poland = pytz.timezone("Poland")

print(datetime.now().astimezone(poland))


