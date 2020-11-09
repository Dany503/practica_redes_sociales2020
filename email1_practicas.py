# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:35:57 2016

@author: dany
"""

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

direccion_fuente = "xxxxxxx@gmail.com"
direccion_destino = "xxxxxx@gmail.com"
password = "xxxxxxx"

server.login(direccion_fuente, password)
 
msg = "Hola mundo!"
server.sendmail(direccion_fuente, direccion_destino, msg)

server.quit()

