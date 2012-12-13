# coding=UTF-8

from info_lib import log_activacion

CODIGO_ACTIVACION = 'imwatchingU'

def verificar_activacion():

  if not esta_activado():

    import getpass

    codigo_activacion = getpass.getpass("Ingrese su código de activación: ")

    if not codigo_activacion == CODIGO_ACTIVACION:
      print "Código de activación inválido"
      log_activacion(codigo_activacion, 'Código de activación inválido')
      return False
    else:
      activar_copia()
      log_activacion(codigo_activacion, 'Activación exitosa')
      return True

  return True

def activar_copia():
  import os, datetime

  if not esta_activado():
    f = open('.activacion', 'w')
    f.write('activado el %s' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    f.close()

def esta_activado():
  import os

  try:
    f = open('.activacion', 'r')
    content = f.read()
    f.close()
    return content.startswith('activado el')

  except:
    return False