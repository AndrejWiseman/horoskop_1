from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
import time

# url = 'https://www.olx.ba/pretraga?trazilica=nikon%20objektiv'
url_d = 'http://www.horoskopius.com/dnevni-horoskop/ovan/'
url_n = 'http://www.horoskopius.com/nedeljni-horoskop/ovan/'

req_d = Request(url_d, headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
})
html_text = urlopen(req_d).read()

req_n = Request(url_n, headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
})
html_text_n = urlopen(req_n).read()

soup = BeautifulSoup(html_text, 'lxml')
soup_n = BeautifulSoup(html_text_n, 'lxml')


dnevni = soup.find('div', class_='horoscope-txt').text
nedeljni = soup_n.find('div', class_='horoscope-txt').text



# for index, artikl in enumerate(artikli):
#         # da se preskoci ako je NoneType
#   try:
#     naslov = artikl.find('p', class_='na').text
#     cena = artikl.find('div', class_='datum').span.text
#             # vreme = artikl.find('div', class_='kada').text
#   except Exception as e:
#     naslov = None
#     cena = None


        # with open(f'oglasi/{index}.txt', 'w') as f:
        #
        #     f.write(f'Artikl: {naslov}')
        #     f.write(f'Cena: {cena}')
  # print(f'{naslov}, {cena}')
print(nedeljni)



# Aktiviranje programa u odredjeni trenutak
# if __name__ == '__main__':
#     while True:
#
#         time_wait = 1 #jedan minut
#         print(f'Cekanje {time_wait} minuta...')
#         time.sleep(time_wait * 5)
