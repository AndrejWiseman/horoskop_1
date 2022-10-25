# from bs4 import BeautifulSoup as soup
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
import time
import csv

### Prvi tutorijal sa mojim sajtom ####
# with open('templates/supa.html', 'r') as html_file:
#     content = html_file.read()
#
#     soup = BeautifulSoup(content, 'lxml')
#
#     course_cards = soup.find_all('div', class_='card-body')
#     for course in course_cards:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1]
#
#         print(f'{course_name} costs  {course_price}')


### Tutorijal sa pravim web sajtom #####
# html_text =  requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=nikon+d7500&_sacat=0&LH_TitleDesc=0&_odkw=nikon&_osacat=0').text
#
# soup = BeautifulSoup(html_text, 'lxml')
# job = soup.find('li', class_="s-item s-item__pl-on-bottom s-item--watch-at-corner")
#
# naslov_oglasa = job.find('div', class_="s-item__title").text
#
# print(naslov_oglasa)




### ako ima 403 forbiden greska ##
# url = 'https://www.olx.ba/pretraga?trazilica=nikon%20objektiv'
#
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# get webpage
# webpage = urlopen(req).read()
#
# page_soup = soup(webpage, 'html.parser')
#
# artikl = page_soup.find('div', class_='listitem artikal obicniArtikal  imaHover-disabled g')
#
# naslov = page_soup.find('p', class_='na').text
# cena = page_soup.find('div', class_='datum').span.text
#
#
# print(page_soup)


# nova proba kombinacija
def oglasi():
    url = 'https://www.olx.ba/pretraga?trazilica=nikon%20objektiv'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    html_text = urlopen(req).read()
    soup = BeautifulSoup(html_text, 'lxml')

    artikli = soup.find_all('div', class_='listitem')



    for index, artikl in enumerate(artikli):
        # da se preskoci ako je NoneType
        try:
            naslov = artikl.find('p', class_='na').text
            cena = artikl.find('div', class_='datum').span.text
            # vreme = artikl.find('div', class_='kada').text
        except Exception as e:
            naslov = None
            cena = None


        # with open(f'oglasi/{index}.txt', 'w') as f:
        #
        #     f.write(f'Artikl: {naslov}')
        #     f.write(f'Cena: {cena}')
        print(f'{naslov}, {cena}')



# Aktiviranje programa u odredjeni trenutak
if __name__ == '__main__':
    while True:
        oglasi()
        time_wait = 1 #jedan minut
        print(f'Cekanje {time_wait} minuta...')
        time.sleep(time_wait * 5)
















