"""
Uso de librería de fecha y tiempo
Conversión del tiempo

"""
from datetime import datetime

"""Uso del método: timestamp"""
time_now = datetime.strptime("2026/10/06 20:30:00", "%Y/%m/%d %H:%M:%S").timestamp()

"""
timestamp: 1970-01-01 (Epoch)
"""

print(time_now)