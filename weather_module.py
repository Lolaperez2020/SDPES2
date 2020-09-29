from pyowm import OWM
import datetime

owm = OWM('b0ccb7c328aa0cb542693180a026acd9')
mgr = owm.weather_manager()


def get_geo():    # пока костыль
    return 'Naberezhnye chelny, RU'


def get_weather_stat():
    observation = mgr.weather_at_place(get_geo())
    w = observation.weather
    state = [round(w.temperature('celsius')['temp']), w.status, w.wind()['speed'], w.humidity,
             str(datetime.datetime.today()).split(' ')[1].split(':')[0]]
    return state


if __name__ == '__main__':
    print(get_weather_stat())
    # print(str(datetime.datetime.today()).split(' ')[1].split(':')[0])
