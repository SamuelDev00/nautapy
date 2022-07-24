nautapy
===========
## Librería creada en Python para acceder al Portal Nauta

nautapy fue creada con el objetivo de ofrecer un api que interactúe con el Portal Nauta de ETECSA,
para facilitar el desarrollo de aplicaciones Python que faciliten la gestión de los servicios
ofrecidos por [Portal de Usuario](https://www.portal.nauta.cu/).

## Accediendo al Portal Nauta
```python
from PortalClient import PortalClient  # se importa el cliente para el Portal Nauta

client = PortalClient('usuario@nauta.com.cu','Contraseña')         # se instancia el cliente

with open("captcha.png", 'wb') as img:
    img.write(client.get_captcha())  # guarda la imagen captcha

client.login(input("Captcha: "))  # inicia sesión en el portal

print(client.get_info('credit'))       # imprime en pantalla el saldo de la cuenta logeada

```
## Funciones y propiedades de PortalClient
### Funciones
* init_session: Crea la session donde se guardan las cookies y datos
* login: Loguea al usuario en el portal y carga la información de la cuenta
* recharge: Recarga la cuenta logueada
* transfer: Transfiere saldo a otra cuenta nauta
* change_password: Cambia la contraseña de la cuenta logueada
* change_email_password: Cambia la contraseña de la cuenta de correo asociada a la cuenta logueada
* get_lasts: Devuelve las últimas `large` `action` realizadas, donde `large` es la cantidad Ej: 5 y `action` las operaciones realizadas Ej: "connections" (las `action` disponibles son: "connections", "recharges" y "transfers")
* get_connections: Devuelve las conexiones realizadas en el mes especificado incluyendo el año (`año-mes`: 2022-03)
* get_recharges: Devuelve las recargas realizadas en el mes especificado incluyendo el año (`año-mes`: 2022-03)
* get_transfers: Devuelve las transferencias realizadas en el mes especificado incluyendo el año (`año-mes`: 2022-03)
### Propiedades
* captcha_as_bytes: Imagen captcha en bytes
* block_date: Fecha de bloqueo
* delete_date: Fecha de eliminación
* account_type: Tipo de cuenta
* service_type: Tipo de servicio
* credit: Saldo
* time: Tiempo disponible
* mail_account: Cuenta de correo asociada

Todas las contribuciones son bienvenidas al proyecto :)

Si te gusta el proyecto dale una estrella para que otros lo encuentren más facilmente.

## Módulos
```text
requests~=2.27.1
beautifulsoup4~=4.10.0
```
