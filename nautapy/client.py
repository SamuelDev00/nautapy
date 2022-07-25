import requests
import bs4
import os
import lxml.html
from bs4 import BeautifulSoup

class PortalClient(object):
    def __init__(self, user='', password=''):
        self.username = user
        self.password = password
        self.session = requests.Session()
        self.url = 'https://www.portal.nauta.cu/'
        self.captcha = ''
        self.csrf = ''
        self.cookies = ''
        self.headers = {'content-type': 'application/x-www-form-urlencoded', "User-agent":"Mozilla/5.0 (X11; Linux x86_64)"}
    
    #diccionario para obtener los datos de la cuenta
    datos = {"username": "usuario",
             "account_type": "tipo de cuenta",
             "service_type": "tipo de servicio",
             "credit": "saldo disponible",
             "time": "tiempo disponible de la cuenta",
             "mail_account": "cuenta de correo"}

    def get_csrf(self, url):
        resp = self.session.get(url, headers=self.headers)
        soup = BeautifulSoup(resp.text,'html.parser')
        csrf = soup.find('input',attrs={'name':'csrf'})['value']
        return csrf

    def get_captcha(self):
        url_captcha = self.url+'captcha/?'
        captcha = self.session.get(url_captcha, headers=self.headers).content
        return captcha
        
    def login(self, captcha):
        try: 
             login = self.url+'user/login/es-es'
             resp = self.session.get(login, headers=self.headers)
             user = self.username
             contra = self.password
             self.cookies = resp.cookies
             self.csrf = self.get_csrf(login)
             self.captcha = captcha
             payload = {'csrf': self.csrf,
                        'login_user': user,
                        'password_user': contra, 
                        'captcha': self.captcha,
                        'btn_submit': ''}
             resp2 = self.session.post(login, data=payload, headers=self.headers, cookies=self.cookies)
             if resp2.text.count('"msg_error">'):
                  mensaje_error = resp2.text.split('"msg_error">')[1].split("<")[0]
                  return print(f'No pude iniciar sesión: {mensaje_error}')
             else:
                  return print('\nHe iniciado sesión\n')
        except Exception as ex:
            print(ex)
    

    def get_info(self,attr):
        if attr == "blocking_date_home" or attr == "date_of_elimination_home":
            index = 1
        else:
            index = 0
        count = 0
        url = self.url+'useraaa/user_info'
        resp = self.session.get(url, headers=self.headers)
        soup = BeautifulSoup(resp.text,'html.parser')
        for div in soup.find_all("div", {"class": "col s12 m6"}):
            if div.find("h5").text.strip().lower() == PortalClient.datos[attr]:
                if index == 1 and count == 0:
                    count = 1
                    continue
                return div.find("p").text
    

    def recharge(self, code):
        url = self.url+'useraaa/recharge_account'
        self.csrf = self.get_csrf(url)
        payload = {'csrf': self.csrf,
                   'recharge_code': code,
                   'btn_submit': ''}
        resp = self.session.post(url, data=payload, headers=self.headers)
        error = resp.text
        if error.count("msg_error"):
            mensaje_error = error.split('"msg_error">')[1].split("<")[0]
            print(mensaje_error)
        elif error.count('"msg_message">'):
             mensaje_mensaje = error.split('"msg_message">')[1].split("<")[0]
             return print(mensaje_mensaje)
        else:
             return print('Error Desconocido')


    def transfer(self, monto, password, account_transfer):
        url = self.url+'useraaa/transfer_balance'
        self.csrf = self.get_csrf(url)
        payload = {'csrf': self.csrf,
                   'transfer': monto,
                   'password_user': password, 
                   'id_cuenta': account_transfer,
                   'action': 'checkdata'}
        resp = self.session.post(url, data=payload, headers=self.headers)
        error = resp.text
        root_element5 = lxml.html.fromstring(error)
        saldo = root_element5.xpath('//div[@class="card-panel"]/div/div/p')[0] 
        saldo_str = saldo.text_content()
        if error.count("msg_error"):
             mensaje_error = error.split('"msg_error">')[1].split("<")[0]
             print(f'{mensaje_error}: {saldo_str}')
        elif error.count('"msg_message">'):
             mensaje_error2 = error.split('"msg_message">')[1].split("<")[0]
             return print(f'{mensaje_error2}: {saldo_str}')
        else:
             return print("Error Desconocido")


    def change_password(self, old_password, new_password):
        url = self.url+'useraaa/change_password'
        self.csrf = self.get_csrf(url)
        payload = {'csrf': self.csrf,
                   'old_password': old_password,
                   'new_password': new_password, 
                   'repeat_new_password': new_password,
                   'btn_submit': ''}
        resp = self.session.post(url, data=payload, headers=self.headers)
        error = resp.text
        if error.count("msg_error"):
            mensaje_error = error.split('"msg_error">')[1].split("<")[0]
            print(mensaje_error)
        elif error.count('"msg_message">'):
             mensaje_error2 = error.split('"msg_message">')[1].split("<")[0]
             return print(mensaje_error2)
        else:
             return print('Error Desconocido')


    def change_mail_password(self, old_password, new_password):
        url = self.url+'email/change_password'
        self.csrf = self.get_csrf(url)
        payload = {'csrf': self.csrf,
                   'old_password': old_password,
                   'new_password': new_password, 
                   'repeat_new_password': new_password,
                   'btn_submit': ''}
        resp = self.session.post(url, data=payload, headers=self.headers)
        error = resp.text
        if error.count("msg_error"):
            mensaje_error = error.split('"msg_error">')[1].split("<")[0]
            print(mensaje_error)
        elif error.count('"msg_message">'):
             mensaje_error2 = error.split('"msg_message">')[1].split("<")[0]
             return print(mensaje_error2)
        else:
             return print('Error Desconocido')



