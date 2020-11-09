# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:58:26 2016

@author: dany
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


direccion_fuente = "xxxxxx@gmail.com"
direccion_destino = "xxxxxx@gmail.com"
password = "xxxxxxxxx"
 
server = smtplib.SMTP('smtp.gmail.com', 587)
#server = smtplib.SMTP('smtp.live.com', 587) # para servidor hotmail
server.starttls()
server.login(direccion_fuente, password)

msg = MIMEMultipart()
msg['From'] = direccion_fuente
msg['To'] = direccion_destino
msg['Subject'] = "Mensaje de Prueba"
 
cuerpo_mensaje = "Hola mundo!!"
msg.attach(MIMEText(cuerpo_mensaje, 'plain'))

texto = msg.as_string()
print(texto)

try:
    print("Enviando email")
    print(server.sendmail(direccion_fuente, direccion_destino, texto))
except:
    print("Error al enviar el email")
    server.quit()
    
server.quit()
