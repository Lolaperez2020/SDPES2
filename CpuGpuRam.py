from pyowm import OWM
import sys
import psutil
import time


def cpu_test():
    val = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    mem_total = mem.total / (2 ** 30)
    mem_used = mem.used / (2 ** 30)
    # print(mem.used / (2 ** 30), mem.total / (2 ** 30))
    return val, mem_used, mem_total


def weather_test():
    owm = OWM('b0ccb7c328aa0cb542693180a026acd9')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Naberezhnye chelny, RU')
    w = observation.weather
    print(w.status)
    print(w.wind())                # {'speed': 4.6, 'deg': 330}
    print(w.humidity)           # 87
    print(w.temperature('celsius'))
    # {'temp': 18.0, 'temp_max': 18.0, 'temp_min': 18.0, 'feels_like': 15.05, 'temp_kf': None}


if __name__ == '__main__':
    while True:
        print(cpu_test())
