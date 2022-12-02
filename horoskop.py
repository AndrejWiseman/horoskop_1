from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from flask import Flask, render_template, request, url_for


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


# # Bik
# @app.route('/bik')
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
