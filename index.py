from flask import Flask, render_template

# from bs4 import BeautifulSoup
# import requests
# from urllib.request import Request, urlopen
# from datetime import time, date
# import time
from vreme import prognoza

from horoskop import ovan
from horoskop import bik
from horoskop import blizanci
from horoskop import rak
from horoskop import lav
from horoskop import devica
from horoskop import vaga
from horoskop import skorpion
from horoskop import strelac
from horoskop import jarac
from horoskop import vodolija
from horoskop import ribe

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


# Webscrap horoskopskih znakova
@app.route('/ovan')
def horo():
    return ovan()


@app.route('/bik')
def horb():
    return bik()


@app.route('/blizanci')
def horbl():
    return blizanci()


@app.route('/rak')
def horr():
    return rak()


@app.route('/lav')
def horl():
    return lav()


@app.route('/devica')
def hord():
    return devica()


@app.route('/vaga')
def horv():
    return vaga()


@app.route('/skorpija')
def hors():
    return skorpion()


@app.route('/strelac')
def horst():
    return strelac()


@app.route('/jarac')
def horj():
    return jarac()


@app.route('/vodolija')
def horv():
    return vodolija()


@app.route('/ribe')
def horri():
    return ribe()


# Vise o znaku
@app.route('/vise-o-layout')
def vise():
    return render_template('vise-o-layout.html')


# Podznak
@app.route('/podznak')
def podznak():
    return render_template('podznak.html')


# Vreme
@app.route('/vreme')
def vreme():
    return prognoza()








if __name__ == '__main__':
    # ovan()
    app.run(debug=True)

# # Aktiviranje programa u odredjeni trenutak
# if __name__ == '__main__':
#     while True:
#         ovan()
#         app.run(debug=True)
#
#         time_wait = 60 #jedan minut
#         print(f'Cekanje {time_wait} minuta...')
#         time.sleep(time_wait * 60)
