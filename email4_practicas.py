# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:58:26 2016

@author: dany
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

direccion_fuente = "xxxxxxxx"
direccion_destino = "xxxxxxxx"
password = "xxxxxxxx"
 
server = smtplib.SMTP('smtp.gmail.com', 587)
#server = smtplib.SMTP('smtp.live.com', 587) # para servidor hotmail
server.starttls()
server.login(direccion_fuente, password)

msg = MIMEMultipart()
msg['From'] = direccion_fuente
msg['To'] = direccion_destino
msg['Subject'] = "Mensaje de Prueba"

cuerpo_mensaje = "Me encanta Sevilla!!"
msg.attach(MIMEText(cuerpo_mensaje, 'plain'))

 
archivo = "Sevilla.jpg"
adjunto = open(archivo, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((adjunto).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % archivo)
msg.attach(part)

texto = msg.as_string()
print(texto)

try:
    print("Enviando email")
    print(server.sendmail(direccion_fuente, direccion_destino, texto))
except:
    print("Error al enviar el email")
    server.quit()
    
server.quit()
