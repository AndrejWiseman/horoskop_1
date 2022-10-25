# from flask import Flask, render_template, request, url_for
# from datetime import time, date
# import time
#
#
#
# app = Flask(__name__)
#
#
#
# #Podznak
# # @app.route('/podznak')
# # def podznak():
# #     return render_template('podznak.html')
#
# #### Podznak-rezultat ####
# def racunanjeP():
#     @app.route('/podznak_rezultat', methods=['POST'])
#     def podznak_rezultat():
#         datum = request.form['datum']
#         mesec = request.form['mesec']
#         sat = request.form['sat']
#         minut = request.form['minut']
#
#         # time = sat, minut
#         # input 15:25
#
#         # h, m = map(int, time)
#         vreme = str(time(hour=int(sat), minute=(int(minut))))
#
#
#         # day = int(datum)
#         # month = int(mesec)
#
#         # dtF = date(day=day, month=month, year=1990)
#         # dt1 = date(day=21, month=3, year=1990)
#         # dt2 = date(day=31, month=3, year=1990)
#         # dt3 = date(day=1, month=4, year=1990)
#         # dt4 = date(day=10, month=4, year=1990)
#
#
#         # dt = str(date(date=int(datum)))
#
#         # znak = vreme, datum, mesec
#
#         znak = ''
#
#
#         #podz Ovan
#         if datum >= '21' and datum <= '31' and mesec == '3':
#             if vreme >= '00:00' and vreme < '02:00':
#                 znak = 'Strelac'
#             elif vreme >= '02:00' and vreme <= '03:30':
#                 znak = 'Jarac'
#             elif vreme >= '04:00' and vreme <= '04:30':
#                 znak = 'Vodolija'
#             elif vreme >= '05:00' and vreme <= '05:30':
#                 znak = 'Ribe'
#             elif vreme >= '06:00' and vreme <= '06:30':
#                 znak = 'Ovan'
#             elif vreme >= '07:00' and vreme <= '07:30':
#                 znak = 'Bik'
#             elif vreme >= '08:00' and vreme <= '09:30':
#                 znak = 'Blizanci'
#             elif vreme >= '10:00' and vreme <= '12:00':
#                 znak = 'Rak'
#             elif vreme >= '12:01' and vreme <= '14:30':
#                 znak = 'Lav'
#             elif vreme >= '14:31' and vreme <= '17:29':
#                 znak = 'Devica'
#             elif vreme >= '17:30' and vreme <= '19:59':
#                 znak = 'Vaga'
#             elif vreme >= '20:00' and vreme <= '23:00':
#                 znak = 'Skorpion'
#             elif vreme >= '23:01' and vreme <= '23:59':
#                 znak = 'Strelac'
#
#         return render_template('podznak_ovan.html',  znak=znak)
#
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
