nautapy
===========
## Librería creada en Python para acceder al Portal Nauta

nautapy fue creada con el objetivo de ofrecer un api que interactúe con el Portal Nauta de ETECSA,
para facilitar el desarrollo de aplicaciones Python que faciliten la gestión de los servicios
ofrecidos por [Portal de Usuario](https://www.portal.nauta.cu/).

## Accediendo al Portal Nauta
```python
from nautapy.client import PortalClient  # se importa el cliente para el Portal Nauta

client = PortalClient('usuario@nauta.com.cu','Contraseña')         # se instancia el cliente

with open("captcha.png", 'wb') as img:
    img.write(client.get_captcha())  # guarda la imagen captcha

client.login(input("Captcha: "))  # inicia sesión en el portal

print(client.get_info('credit'))       # imprime en pantalla el saldo de la cuenta logueada

```
## Funciones y datos de PortalClient
### Funciones
* login: Loguea al usuario en el portal.
* recharge: Recarga la cuenta logueada.
* transfer: Transfiere saldo a otra cuenta nauta.
* change_password: Cambia la contraseña de la cuenta logueada.
* change_mail_password: Cambia la contraseña de la cuenta de correo asociada a la cuenta logueada.
### Datos
* username: Usuario de la cuenta.
* account_type: Tipo de cuenta.
* service_type: Tipo de servicio.
* credit: Saldo.
* time: Tiempo disponible.
* mail_account: Cuenta de correo asociada.

Todas las contribuciones son bienvenidas al proyecto :)

## Módulos
```text
beautifulsoup4==4.10.0
requests==2.27.1
lxml==4.7.1
```
