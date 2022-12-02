from flask import Flask, render_template, request, url_for

from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from datetime import time, date
import time
from vreme import prognoza


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')



def horoskopScrap():
    # Ovan
    @app.route('/ovan')
    def ovan():
        url = 'http://www.horoskopius.com/dnevni-horoskop/ovan/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/ovan/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/ovan/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/ovan/'

        req = Request(url, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('ovan.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


    # Bik
    @app.route('/bik')
    def bik():
        url = 'http://www.horoskopius.com/dnevni-horoskop/bik/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/bik/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/bik/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/bik/'

        req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('bik.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


    # Blizanci
    @app.route('/blizanci')
    def blizanci():
        url = 'http://www.horoskopius.com/dnevni-horoskop/blizanci/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/blizanci/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/blizanci/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/blizanci/'

        req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('blizanci.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


    # Rak
    @app.route('/rak')
    def rak():
        url = 'http://www.horoskopius.com/dnevni-horoskop/rak/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/rak/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/rak/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/rak/'

        req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('rak.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


    # Lav
    @app.route('/lav')
    def lav():
        url = 'http://www.horoskopius.com/dnevni-horoskop/lav/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/lav/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/lav/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/lav/'

        req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('lav.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


    # Devica
    @app.route('/devica')
    def devica():
        url = 'http://www.horoskopius.com/dnevni-horoskop/devica/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/devica/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/devica/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/devica/'

        req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('devica.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


    # Vaga
    @app.route('/vaga')
    def vaga():
        url = 'http://www.horoskopius.com/dnevni-horoskop/vaga/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/vaga/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/vaga/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/vaga/'

        req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('vaga.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


    # Skorpion
    @app.route('/skorpion')
    def skorpion():
        url = 'http://www.horoskopius.com/dnevni-horoskop/skorpija/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/skorpija/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/skorpija/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/skorpija/'

        req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('skorpion.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


    # Strelac
    @app.route('/strelac')
    def strelac():
        url = 'http://www.horoskopius.com/dnevni-horoskop/strelac/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/strelac/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/strelac/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/strelac/'

        req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('strelac.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


    # Jarac
    @app.route('/jarac')
    def jarac():
        url = 'http://www.horoskopius.com/dnevni-horoskop/jarac/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/jarac/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/jarac/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/jarac/'

        req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('jarac.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


    # Vodolija
    @app.route('/vodolija')
    def vodolija():
        url = 'http://www.horoskopius.com/dnevni-horoskop/vodolija/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/vodolija/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/vodolija/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/vodolija/'

        req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        datum = soup.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('vodolija.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


    # Ribe
    @app.route('/ribe')
    def ribe():
        url = 'http://www.horoskopius.com/dnevni-horoskop/ribe/'
        url_n = 'http://www.horoskopius.com/nedeljni-horoskop/ribe/'
        url_m = 'http://www.horoskopius.com/mesecni-horoskop/ribe/'
        url_g = 'http://www.horoskopius.com/godisnji-horoskop/ribe/'

        req = Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_n = Request(url_n, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_m = Request(url_m, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })
        req_g = Request(url_g, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        })

        html_text = urlopen(req).read()
        html_text_n = urlopen(req_n).read()
        html_text_m = urlopen(req_m).read()
        html_text_g = urlopen(req_g).read()

        soup = BeautifulSoup(html_text, 'lxml')
        soup_n = BeautifulSoup(html_text_n, 'lxml')
        soup_m = BeautifulSoup(html_text_m, 'lxml')
        soup_g = BeautifulSoup(html_text_g, 'lxml')

        datum = soup.find('span', class_='date').text
        datum_n = soup_n.find('span', class_='date').text
        datum_m = soup_m.find('span', class_='date').text
        datum_g = soup_g.find('span', class_='date').text

        dnevni = soup.find('div', class_='horoscope-txt').text
        nedeljni = soup_n.find('div', class_='horoscope-txt').text
        mesecni = soup_m.find('div', class_='horoscope-txt').text
        godisnji = soup_g.find('div', class_='horoscope-txt').text

        return render_template('ribe.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji, datum=datum, datum_n=datum_n, datum_m=datum_m, datum_g=datum_g)


# Vise o znaku
@app.route('/vise-o-layout')
def vise():

    return render_template('vise-o-layout.html')



#Podznak
@app.route('/podznak')
def podznak():
    return render_template('podznak.html')


@app.route('/vreme')
def vreme():
    return prognoza()



#### Podznak-rezultat ####
# @app.route('/podznak_rezultat', methods=['POST'])
# def podznak_rezultat():
#     datum = request.form['datum']
#     mesec = request.form['mesec']
#     sat = request.form['sat']
#     minut = request.form['minut']
#
#     # time = sat, minut
#     # input 15:25
#
#     # h, m = map(int, time)
#     vreme = str(time(hour=int(sat), minute=(int(minut))))


    # day = int(datum)
    # month = int(mesec)

    # dtF = date(day=day, month=month, year=1990)
    # dt1 = date(day=21, month=3, year=1990)
    # dt2 = date(day=31, month=3, year=1990)
    # dt3 = date(day=1, month=4, year=1990)
    # dt4 = date(day=10, month=4, year=1990)


    # dt = str(date(date=int(datum)))

    # znak = vreme, datum, mesec

    # znak = ''


    #podz Ovan
    # if datum >= '21' and datum <= '31' and mesec == '3':
    #     if vreme >= '00:00' and vreme < '02:00':
    #         znak = 'Strelac'
    #     elif vreme >= '02:00' and vreme <= '03:30':
    #         znak = 'Jarac'
    #     elif vreme >= '04:00' and vreme <= '04:30':
    #         znak = 'Vodolija'
    #     elif vreme >= '05:00' and vreme <= '05:30':
    #         znak = 'Ribe'
    #     elif vreme >= '06:00' and vreme <= '06:30':
    #         znak = 'Ovan'
    #     elif vreme >= '07:00' and vreme <= '07:30':
    #         znak = 'Bik'
    #     elif vreme >= '08:00' and vreme <= '09:30':
    #         znak = 'Blizanci'
    #     elif vreme >= '10:00' and vreme <= '12:00':
    #         znak = 'Rak'
    #     elif vreme >= '12:01' and vreme <= '14:30':
    #         znak = 'Lav'
    #     elif vreme >= '14:31' and vreme <= '17:29':
    #         znak = 'Devica'
    #     elif vreme >= '17:30' and vreme <= '19:59':
    #         znak = 'Vaga'
    #     elif vreme >= '20:00' and vreme <= '23:00':
    #         znak = 'Skorpion'
    #     elif vreme >= '23:01' and vreme <= '23:59':
    #         znak = 'Strelac'
    #
    # elif datum >= '1' and datum <= '10' and mesec == '4':
    #     if vreme >= '00:00' and vreme <= '00:44':
    #         znak = 'Strelac'
    #     elif vreme >= '00:45' and vreme <= '02:44':
    #         znak = 'Jarac'
    #     elif vreme >= '02:45' and vreme <= '03:44':
    #         znak = 'Vodolija'
    #     elif vreme >= '03:45' and vreme <= '04:44':
    #         znak = 'Ribe'
    #     elif vreme >= '04:45' and vreme <= '05:44':
    #         znak = 'Ovan'
    #     elif vreme >= '05:45' and vreme <= '07:14':
    #         znak = 'Bik'
    #     elif vreme >= '07:15' and vreme <= '08:44':
    #         znak = 'Blizanci'
    #     elif vreme >= '08:45' and vreme <= '11:14':
    #         znak = 'Rak'
    #     elif vreme >= '11:15' and vreme <= '14:14':
    #         znak = 'Lav'
    #     elif vreme >= '14:15' and vreme <= '16:44':
    #         znak = 'Devica'
    #     elif vreme >= '16:45' and vreme <= '19:14':
    #         znak = 'Vaga'
    #     elif vreme >= '19:15' and vreme <= '22:14':
    #         znak = 'Skorpion'
    #     elif vreme >= '22:15' and vreme <= '23:59':
    #         znak = 'Strelac'
    #
    # elif datum >= '11' and datum <= '20' and mesec == '4':
    #     if vreme >= '00:00' and vreme <= '00:44':
    #         znak = 'Strelac'
    #     elif vreme >= '00:45' and vreme <= '02:44':
    #         znak = 'Jarac'
    #     elif vreme >= '02:45' and vreme <= '03:44':
    #         znak = 'Vodolija'
    #     elif vreme >= '03:45' and vreme <= '04:44':
    #         znak = 'Ribe'
    #     elif vreme >= '04:45' and vreme <= '05:44':
    #         znak = 'Ovan'
    #     elif vreme >= '05:45' and vreme <= '07:14':
    #         znak = 'Bik'
    #     elif vreme >= '07:15' and vreme <= '08:44':
    #         znak = 'Blizanci'
    #     elif vreme >= '08:45' and vreme <= '11:14':
    #         znak = 'Rak'
    #     elif vreme >= '11:15' and vreme <= '14:14':
    #         znak = 'Lav'
    #     elif vreme >= '14:15' and vreme <= '16:44':
    #         znak = 'Devica'
    #     elif vreme >= '16:45' and vreme <= '19:14':
    #         znak = 'Vaga'
    #     elif vreme >= '19:15' and vreme <= '22:14':
    #         znak = 'Skorpion'
    #     elif vreme >= '22:15' and vreme <= '23:59':
    #         znak = 'Strelac'
    #
    #
    # # Podz Bik
    # elif datum >= '21' and datum <= '30' and mesec == '4':
    #     if vreme >= '00:00' and vreme <= '01:14':
    #         znak = 'Jarac'
    #     elif vreme >= '01:15' and vreme <= '02:44':
    #         znak = 'Vodolija'
    #     elif vreme >= '02:45' and vreme <= '03:44':
    #         znak = 'Ribe'
    #     elif vreme >= '03:45' and vreme <= '04:44':
    #         znak = 'Ovan'
    #     elif vreme >= '04:44' and vreme <= '05:44':
    #         znak = 'Bik'
    #     elif vreme >= '05:45' and vreme <= '07:14':
    #         znak = 'Blizanci'
    #     elif vreme >= '07:15' and vreme <= '09:44':
    #         znak = 'Rak'
    #     elif vreme >= '09:45' and vreme <= '12:44':
    #         znak = 'Lav'
    #     elif vreme >= '12:44' and vreme <= '15:44':
    #         znak = 'Devica'
    #     elif vreme >= '15:45' and vreme <= '18:14':
    #         znak = 'Vaga'
    #     elif vreme >= '18:15' and vreme <= '21:14':
    #         znak = 'Skorpion'
    #     elif vreme >= '21:15' and vreme <= '23:59':
    #         znak = 'Strelac'
    #
    # elif datum >= '1' and datum <= '10' and mesec == '5':
    #     if vreme >= '00:00' and vreme <= '00:44':
    #         znak = 'Jarac'
    #     elif vreme >= '00:45' and vreme <= '02:14':
    #         znak = 'Vodolija'
    #     elif vreme >= '02:15' and vreme <= '02:59':
    #         znak = 'Ribe'
    #     elif vreme >= '03:00' and vreme <= '03:44':
    #         znak = 'Ovan'
    #     elif vreme >= '03:45' and vreme <= '05:14':
    #         znak = 'Bik'
    #     elif vreme >= '05:15' and vreme <= '06:44':
    #         znak = 'Blizanci'
    #     elif vreme >= '06:45' and vreme <= '09:14':
    #         znak = 'Rak'
    #     elif vreme >= '09:15' and vreme <= '12:14':
    #         znak = 'Lav'
    #     elif vreme >= '12:15' and vreme <= '14:44':
    #         znak = 'Devica'
    #     elif vreme >= '14:45' and vreme <= '17:44':
    #         znak = 'Vaga'
    #     elif vreme >= '17:45' and vreme <= '20:44':
    #         znak = 'Skorpion'
    #     elif vreme >= '20:45' and vreme <= '23:44':
    #         znak = 'Strelac'
    #     elif vreme >= '23:45' and vreme <= '23:59':
    #         znak = 'Jarac'
    #
    # elif datum >= '11' and datum <= '20' and mesec == '5':
    #     if vreme >= '00:00' and vreme <= '00:14':
    #         znak = 'Jarac'
    #     elif vreme >= '00:15' and vreme <= '01:14':
    #         znak = 'Vodolija'
    #     elif vreme >= '01:15' and vreme <= '02:14':
    #         znak = 'Ribe'
    #     elif vreme >= '02:14' and vreme <= '03:14':
    #         znak = 'Ovan'
    #     elif vreme >= '03:15' and vreme <= '04:14':
    #         znak = 'Bik'
    #     elif vreme >= '04:15' and vreme <= '06:14':
    #         znak = 'Blizanci'
    #     elif vreme >= '06:15' and vreme <= '08:44':
    #         znak = 'Rak'
    #     elif vreme >= '08:45' and vreme <= '11:14':
    #         znak = 'Lav'
    #     elif vreme >= '11:15' and vreme <= '14:14':
    #         znak = 'Devica'
    #     elif vreme >= '14:15' and vreme <= '17:14':
    #         znak = 'Vaga'
    #     elif vreme >= '17:15' and vreme <= '19:44':
    #         znak = 'Skorpion'
    #     elif vreme >= '19:45' and vreme <= '22:14':
    #         znak = 'Strelac'
    #     elif vreme >= '22:15' and vreme <= '23:59':
    #         znak = 'Jarac'
    #
    # # Podz Blizanci
    # elif datum >= '21' and datum <= '31' and mesec == '5':
    #     if vreme >= '01:15' and vreme <= '00:44':
    #         znak = 'Vodolija'
    #     elif vreme >= '00:45' and vreme <= '01:44':
    #         znak = 'Ribe'
    #     elif vreme >= '01:45' and vreme <= '02:44':
    #         znak = 'Ovan'
    #     elif vreme >= '02:45' and vreme <= '03:44':
    #         znak = 'Bik'
    #     elif vreme >= '03:45' and vreme <= '05:14':
    #         znak = 'Blizanci'
    #     elif vreme >= '05:15' and vreme <= '07:44':
    #         znak = 'Rak'
    #     elif vreme >= '07:45' and vreme <= '11:44':
    #         znak = 'Lav'
    #     elif vreme >= '11:44' and vreme <= '14:14':
    #         znak = 'Devica'
    #     elif vreme >= '14:15' and vreme <= '16:44':
    #         znak = 'Vaga'
    #     elif vreme >= '16:45' and vreme <= '19:44':
    #         znak = 'Skorpion'
    #     elif vreme >= '19:45' and vreme <= '21:44':
    #         znak = 'Strelac'
    #     elif vreme >= '21:45' and vreme <= '23:14':
    #         znak = 'Jarac'
    #     elif vreme >= '23:15' and vreme <= '23:59':
    #         znak = 'Vodolija'
    #
    # elif datum >= '1' and datum <= '11' and mesec == '6':
    #     if vreme >= '00:00' and vreme <= '00:44':
    #         znak = 'Ribe'
    #     elif vreme >= '00:45' and vreme <= '01:44':
    #         znak = 'Ovan'
    #     elif vreme >= '01:45' and vreme <= '02:45':
    #         znak = 'Bik'
    #     elif vreme >= '02:46' and vreme <= '04:44':
    #         znak = 'Blizanci'
    #     elif vreme >= '04:45' and vreme <= '07:14':
    #         znak = 'Rak'
    #     elif vreme >= '07:15' and vreme <= '10:14':
    #         znak = 'Lav'
    #     elif vreme >= '10:15' and vreme <= '12:44':
    #         znak = 'Devica'
    #     elif vreme >= '12:45' and vreme <= '15:44':
    #         znak = 'Vaga'
    #     elif vreme >= '15:45' and vreme <= '18:14':
    #         znak = 'Škorpion'
    #     elif vreme >= '18:15' and vreme <= '20:44':
    #         znak = 'Strelac'
    #     elif vreme >= '20:45' and vreme <= '22:44':
    #         znak = 'Jarac'
    #     elif vreme >= '22:45' and vreme <= '23:59':
    #         znak = 'Vodolija'
    #
    # elif datum >= '12' and datum <= '21' and mesec == '6':
    #     if vreme >= '00:00' and vreme <= '00:30':
    #         znak = 'Ribe'
    #     elif vreme >= '00:31' and vreme <= '01:14':
    #         znak = 'Ovan'
    #     elif vreme >= '01:15' and vreme <= '02:14':
    #         znak = 'Bik'
    #     elif vreme >= '02:15' and vreme <= '04:14':
    #         znak = 'Blizanci'
    #     elif vreme >= '04:15' and vreme <= '06:44':
    #         znak = 'Rak'
    #     elif vreme >= '06:45' and vreme <= '09:14':
    #         znak = 'Lav'
    #     elif vreme >= '09:15' and vreme <= '12:14':
    #         znak = 'Devica'
    #     elif vreme >= '12:15' and vreme <= '14:44':
    #         znak = 'Vaga'
    #     elif vreme >= '14:45' and vreme <= '17:44':
    #         znak = 'Škorpion'
    #     elif vreme >= '17:45' and vreme <= '20:14':
    #         znak = 'Strelac'
    #     elif vreme >= '20:15' and vreme <= '21:44':
    #         znak = 'Jarac'
    #     elif vreme >= '21:45' and vreme <= '23:14':
    #         znak = 'Vodolija'
    #     elif vreme >= '23:15' and vreme <= '23:59':
    #         znak = 'Ribe'
    #
    # # Podz Rak
    # elif datum >= '22' and datum <= '30' and mesec == '6' or datum == '1' and mesec == '7':
    #     if vreme >= '00:00' and vreme <= '00:14':
    #         znak = 'Ovan'
    #     elif vreme >= '00:15' and vreme <= '01:44':
    #         znak = 'Bik'
    #     elif vreme >= '01:45' and vreme <= '03:14':
    #         znak = 'Blizanci'
    #     elif vreme >= '03:15' and vreme <= '05:44':
    #         znak = 'Rak'
    #     elif vreme >= '05:45' and vreme <= '08:44':
    #         znak = 'Lav'
    #     elif vreme >= '08:45' and vreme <= '11:14':
    #         znak = 'Devica'
    #     elif vreme >= '11:15' and vreme <= '14:14':
    #         znak = 'Vaga'
    #     elif vreme >= '14:15' and vreme <= '17:14':
    #         znak = 'Škorpion'
    #     elif vreme >= '17:15' and vreme <= '19:44':
    #         znak = 'Strelac'
    #     elif vreme >= '19:45' and vreme <= '21:14':
    #         znak = 'Jarac'
    #     elif vreme >= '21:15' and vreme <= '22:14':
    #         znak = 'Vodolija'
    #     elif vreme >= '22:15' and vreme <= '23:14':
    #         znak = 'Ribe'
    #     elif vreme >= '23:15' and vreme <= '23:59':
    #         znak = 'Ovan'
    #
    # elif datum >= '2' and datum <= '12' and mesec == '7':
    #     if vreme >= '00:00' and vreme <= '00:44':
    #         znak = 'Bik'
    #     elif vreme >= '00:45' and vreme <= '02:44':
    #         znak = 'Blizanci'
    #     elif vreme >= '02:45' and vreme <= '05:14':
    #         znak = 'Rak'
    #     elif vreme >= '05:15' and vreme <= '07:44':
    #         znak = 'Lav'
    #     elif vreme >= '07:45' and vreme <= '10:44':
    #         znak = 'Devica'
    #     elif vreme >= '10:45' and vreme <= '13:44':
    #         znak = 'Vaga'
    #     elif vreme >= '13:45' and vreme <= '16:14':
    #         znak = 'Škorpion'
    #     elif vreme >= '16:15' and vreme <= '18:44':
    #         znak = 'Strelac'
    #     elif vreme >= '18:45' and vreme <= '20:44':
    #         znak = 'Jarac'
    #     elif vreme >= '20:45' and vreme <= '21:14':
    #         znak = 'Vodolija'
    #     elif vreme >= '21:15' and vreme <= '22:14':
    #         znak = 'Ribe'
    #     elif vreme >= '22:15' and vreme <= '23:59':
    #         znak = 'Ovan'
    #
    # elif datum >= '13' and datum <= '22' and mesec == '7':
    #     if vreme >= '00:00' and vreme <= '00:14':
    #         znak = 'Bik'
    #     elif vreme >= '00:15' and vreme <= '02:14':
    #         znak = 'Blizanci'
    #     elif vreme >= '02:15' and vreme <= '04:44':
    #         znak = 'Rak'
    #     elif vreme >= '04:45' and vreme <= '07:14':
    #         znak = 'Lav'
    #     elif vreme >= '07:15' and vreme <= '10:14':
    #         znak = 'Devica'
    #     elif vreme >= '10:15' and vreme <= '12:44':
    #         znak = 'Vaga'
    #     elif vreme >= '12:45' and vreme <= '16:44':
    #         znak = 'Škorpion'
    #     elif vreme >= '16:45' and vreme <= '18:14':
    #         znak = 'Strelac'
    #     elif vreme >= '18:15' and vreme <= '19:44':
    #         znak = 'Jarac'
    #     elif vreme >= '19:45' and vreme <= '21:14':
    #         znak = 'Vodolija'
    #     elif vreme >= '21:15' and vreme <= '22:14':
    #         znak = 'Ribe'
    #     elif vreme >= '22:15' and vreme <= '23:14':
    #         znak = 'Ovan'
    #     elif vreme >= '23:15' and vreme <= '23:59':
    #         znak = 'Bik'
    #
    # # Podz Lav
    # elif datum >= '23' and datum <= '31' and mesec == '7' or datum >= '1' and datum <= '2' and mesec == '8':
    #     if vreme >= '00:00' and vreme <= '01:14':
    #         znak = 'Blizanci'
    #     elif vreme >= '01:15' and vreme <= '03:44':
    #         znak = 'Rak'
    #     elif vreme >= '03:45' and vreme <= '07:44':
    #         znak = 'Lav'
    #     elif vreme >= '07:45' and vreme <= '09:14':
    #         znak = 'Devica'
    #     elif vreme >= '09:15' and vreme <= '12:14':
    #         znak = 'Vaga'
    #     elif vreme >= '12:15' and vreme <= '14:44':
    #         znak = 'Škorpion'
    #     elif vreme >= '12:45' and vreme <= '17:14':
    #         znak = 'Strelac'
    #     elif vreme >= '17:15' and vreme <= '19:14':
    #         znak = 'Jarac'
    #     elif vreme >= '19:15' and vreme <= '20:14':
    #         znak = 'Vodolija'
    #     elif vreme >= '20:15' and vreme <= '21:14':
    #         znak = 'Ribe'
    #     elif vreme >= '21:15' and vreme <= '22:14':
    #         znak = 'Ovan'
    #     elif vreme >= '22:15' and vreme <= '23:59':
    #         znak = 'Bik'
    #
    # elif  datum >= '3' and datum <= '12' and mesec == '8':
    #     if vreme >= '00:00' and vreme <= '00:44':
    #         znak = 'Blizanci'
    #     elif vreme >= '00:45' and vreme <= '03:14':
    #         znak = 'Rak'
    #     elif vreme >= '03:15' and vreme <= '05:44':
    #         znak = 'Lav'
    #     elif vreme >= '05:45' and vreme <= '08:44':
    #         znak = 'Devica'
    #     elif vreme >= '08:45' and vreme <= '11:44':
    #         znak = 'Vaga'
    #     elif vreme >= '12:45' and vreme <= '14:14':
    #         znak = 'Škorpion'
    #     elif vreme >= '14:15' and vreme <= '16:44':
    #         znak = 'Strelac'
    #     elif vreme >= '16:45' and vreme <= '18:44':
    #         znak = 'Jarac'
    #     elif vreme >= '18:45' and vreme <= '19:44':
    #         znak = 'Vodolija'
    #     elif vreme >= '19:45' and vreme <= '20:44':
    #         znak = 'Ribe'
    #     elif vreme >= '20:45' and vreme <= '21:44':
    #         znak = 'Ovan'
    #     elif vreme >= '21:45' and vreme <= '22:44':
    #         znak = 'Bik'
    #     elif vreme >= '22:45' and vreme <= '23:59':
    #         znak = 'Blizanci'
    #
    # elif datum >= '13' and datum <= '23' and mesec == '8':
    #     if vreme >= '00:00' and vreme <= '02:14':
    #         znak = 'Rak'
    #     elif vreme >= '02:15' and vreme <= '05:14':
    #         znak = 'Lav'
    #     elif vreme >= '05:15' and vreme <= '08:14':
    #         znak = 'Devica'
    #     elif vreme >= '08:15' and vreme <= '10:44':
    #         znak = 'Vaga'
    #     elif vreme >= '10:45' and vreme <= '13:44':
    #         znak = 'Škorpija'
    #     elif vreme >= '13:45' and vreme <= '16:14':
    #         znak = 'Strelac'
    #     elif vreme >= '16:15' and vreme <= '17:44':
    #         znak = 'Jarac'
    #     elif vreme >= '17:45' and vreme <= '19:14':
    #         znak = 'Vodolija'
    #     elif vreme >= '19:15' and vreme <= '19:44':
    #         znak = 'Ribe'
    #     elif vreme >= '19:45' and vreme <= '20:44':
    #         znak = 'Ovan'
    #     elif vreme >= '20:45' and vreme <= '22:14':
    #         znak = 'Bik'
    #     elif vreme >= '22:15' and vreme <= '23:59':
    #         znak = 'Blizanci'
    #
    #
    # # Podz Devica
    # elif datum >= '24' and datum <= '31' and mesec == '8' or datum >= '1' and datum <= '2' and mesec == '9':
    #     if vreme >= '00:00' and vreme <= '01:44':
    #         znak = 'Rak'
    #     elif vreme >= '01:45' and vreme <= '04:44':
    #         znak = 'Lav'
    #     elif vreme >= '04:45' and vreme <= '07:14':
    #         znak = 'Devica'
    #     elif vreme >= '07:15' and vreme <= '10:14':
    #         znak = 'Vaga'
    #     elif vreme >= '10:15' and vreme <= '12:44':
    #         znak = 'Škorpion'
    #     elif vreme >= '12:45' and vreme <= '15:14':
    #         znak = 'Strelac'
    #     elif vreme >= '15:15' and vreme <= '17:14':
    #         znak = 'Jarac'
    #     elif vreme >= '17:15' and vreme <= '18:14':
    #         znak = 'Vodolija'
    #     elif vreme >= '18:15' and vreme <= '19:14':
    #         znak = 'Ribe'
    #     elif vreme >= '19:15' and vreme <= '20:14':
    #         znak = 'Ovan'
    #     elif vreme >= '20:15' and vreme <= '23:14':
    #         znak = 'Bik'
    #     elif vreme >= '23:15' and vreme <= '23:59':
    #         znak = 'Blizanci'
    #     else:
    #         znak = 'Ne znam!'
    #
    #
    # elif datum >= '3' and datum <= '12' and mesec == '9':
    #     if vreme >= '00:00' and vreme <= '01:14':
    #         znak = 'Rak'
    #     elif vreme >= '01:15' and vreme <= '03:44':
    #         znak = 'Lav'
    #     elif vreme >= '03:45' and vreme <= '06:44':
    #         znak = 'Devica'
    #     elif vreme >= '06:45' and vreme <= '09:14':
    #         znak = 'Vaga'
    #     elif vreme >= '09:15' and vreme <= '12:14':
    #         znak = 'Škorpion'
    #     elif vreme >= '12:15' and vreme <= '14:44':
    #         znak = 'Strelac'
    #     elif vreme >= '14:45' and vreme <= '16:44':
    #         znak = 'Jarac'
    #     elif vreme >= '16:45' and vreme <= '17:44':
    #         znak = 'Vodolija'
    #     elif vreme >= '17:45' and vreme <= '18:44':
    #         znak = 'Ribe'
    #     elif vreme >= '18:45' and vreme <= '19:44':
    #         znak = 'Ovan'
    #     elif vreme >= '19:45' and vreme <= '20:44':
    #         znak = 'Bik'
    #     elif vreme >= '20:45' and vreme <= '22:44':
    #         znak = 'Blizanci'
    #     elif vreme >= '22:45' and vreme <= '23:59':
    #         znak = 'Rak'
    #     else:
    #         znak = 'Ne znam!'
    #
    # elif datum >= '13' and datum <= '23' and mesec == '9':
    #     if vreme >= '00:00' and vreme <= '00:14':
    #         znak = 'Rak'
    #     elif vreme >= '00:15' and vreme <= '03:14':
    #         znak = 'Lav'
    #     elif vreme >= '03:15' and vreme <= '05:44':
    #         znak = 'Devica'
    #     elif vreme >= '05:45' and vreme <= '08:44':
    #         znak = 'Vaga'
    #     elif vreme >= '08:45' and vreme <= '11:44':
    #         znak = 'Škorpion'
    #     elif vreme >= '11:45' and vreme <= '14:14':
    #         znak = 'Strelac'
    #     elif vreme >= '14:15' and vreme <= '15:44':
    #         znak = 'Jarac'
    #     elif vreme >= '15:45' and vreme <= '17:14':
    #         znak = 'Vodolija'
    #     elif vreme >= '17:15' and vreme <= '11:44':
    #         znak = 'Ribe'
    #     elif vreme >= '17:45' and vreme <= '18:44':
    #         znak = 'Ovan'
    #     elif vreme >= '18:45' and vreme <= '20:14':
    #         znak = 'Bik'
    #     elif vreme >= '20:15' and vreme <= '21:44':
    #         znak = 'Blizanci'
    #     elif vreme >= '21:45' and vreme <= '23:59':
    #         znak = 'Rak'
    #     else:
    #         znak = 'Ne znam!'
    #
    # # Vaga
    # elif datum >= '24' and datum <= '30' and mesec == '9' or datum >= '1' and datum <= '3' and mesec == '10':
    #     if vreme >= '00:00' and vreme <= '00:14':
    #         znak = 'Lav'
    #     elif vreme >= '00:15' and vreme <= '03:14':
    #         znak = 'Devica'
    #     elif vreme >= '03:15' and vreme <= '05:44':
    #         znak = 'Vaga'
    #     elif vreme >= '05:45' and vreme <= '08:44':
    #         znak = 'Škorpion'
    #     elif vreme >= '08:45' and vreme <= '11:44':
    #         znak = 'Strelac'
    #     elif vreme >= '11:45' and vreme <= '14:14':
    #         znak = 'Jarac'
    #     elif vreme >= '14:15' and vreme <= '15:44':
    #         znak = 'Vodolija'
    #     elif vreme >= '15:45' and vreme <= '17:14':
    #         znak = 'Ribe'
    #     elif vreme >= '17:15' and vreme <= '11:44':
    #         znak = 'Ovan'
    #     elif vreme >= '17:45' and vreme <= '18:44':
    #         znak = 'Bik'
    #     elif vreme >= '18:45' and vreme <= '20:14':
    #         znak = 'Blizanci'
    #     elif vreme >= '20:15' and vreme <= '21:44':
    #         znak = 'Rak'
    #     elif vreme >= '21:45' and vreme <= '23:59':
    #         znak = 'Lav'
    #     else:
    #         znak = 'Ne znam!'
    #
    # else:
    #     znak = 'Ne mogu naci!'


    # br1 = int(datum) * 4
    # br2 = (int(sat) + int(1)) * 60
    # br3 = int(minut)
    # br4 = int(mesec)
    #
    # sabrano = br1 + br2 + br3 + br4
    #
    # if sabrano > 1440:
    #     znak = sabrano - 1440
    # else:
    #     znak = sabrano

    # if znak >= 77 and znak <= 181:
    #     znak = 'Ovan'
    # elif znak >= 182 and znak <= 302:
    #     znak = 'Bik'
    # elif znak >= 303 and znak <= 436:
    #     znak = 'Blizanci'
    # elif znak >= 437 and znak <= 566:
    #     znak = 'Rak'
    # elif znak >= 567 and znak <= 691:
    #     znak = 'Lav'
    # elif znak >= 692 and znak <= 818:
    #     znak = 'Devica'
    # elif znak >= 819 and znak <= 949:
    #     znak = 'Vaga'
    # elif znak >= 950 and znak <= 1083:
    #     znak = 'Skorpija'
    # elif znak >= 1084 and znak <= 1208:
    #     znak = 'Strelac'
    # elif znak >= 1209 and znak <= 1319:
    #     znak = 'Jarac'
    # elif znak >= 1320 and znak <= 1419:
    #     znak = 'Vodolija'
    # elif znak >= 1420 and znak <= 1419 or znak >= 1 and znak <= 76:
    #     znak = 'Ribe'



    # return render_template('podznak_ovan.html',  znak=znak)
























# if __name__ == '__main__':
#     horoskopScrap()
#     app.run(debug=True)


# # Aktiviranje programa u odredjeni trenutak
if __name__ == '__main__':
    while True:
        horoskopScrap()
        app.run(debug=True)

        time_wait = 60 #jedan minut
        print(f'Cekanje {time_wait} minuta...')
        time.sleep(time_wait * 60)
