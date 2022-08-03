# -*- coding: utf-8 -*-

import smtplib
import email.message
import os
import platform
import json
import pathlib

# Captura o diretorio atual
cwd = pathlib.Path(__file__).parent.absolute()

# Importação de arquivo de configuração
with open(f"{cwd}/config.json") as f:
    data_dict = json.load(f)

# Limpa o shell de qualquer SO
def cleaner():
    if platform.system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
cleaner()

# Destinatário e conteudo do email
email_destination = input('Para quem o email será enviado: ')
email_body = input('Conteúdo do email: ')


def send_email():
    msg = email.message.Message()
    msg['Subject'] = "." # Assunto do email
    msg['From'] = data_dict['yourGmail'] # Quem está enviando
    msg['To'] = email_destination # Para quem está enviando
    password = data_dict['googlePassword']# Senha de aplicativo dispnibilizada pela Google
    msg.add_header('Content-Type', 'text/html') # Tipo de conteudo da mensagem (Também pode ser definido como MKDW)
    msg.set_payload(email_body) # Setagem de mensagem que será enviada

    # Configuração padrão para conexão e codificação da mensagem
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    print('\nEmail enviado!')
send_email()