#!/usr/bin/env python
# coding=UTF-8

# floss-demo
# ==========
# 
# Script de ejemplo para explicar los principios del software librerías
# 
# Utilidad de línea de comandos para traducir 
# una frase del castellano al idioma inglés
# 
# versión 1.0
# 

# declaramos librerías a utilizar
from activation_lib   import verificar_activacion
from traductor_lib    import traducir
from info_lib         import log_traduccion

from sys import exit

# funciones varias
# 

# leemos los parámetros de la línea de comandos
def leer_parametros():
  from argparse import ArgumentParser
  parser = ArgumentParser(description='Permite traducir una frase del castellano al inglés.')
  parser.add_argument('frase', metavar='frase', help='frase a traducir (entre comillas)')
  args = parser.parse_args()
  return args.frase

# programa principal
# 

#verificamos que el programa haya sido activado
#

if not verificar_activacion():
  print "Copia de programa no autorizada."
  exit()

# leemos la frase que el usuario ingresó desde la línea de comandos
frase = leer_parametros()

# traducimos la frase
frase_traducida = traducir("es", "en", frase)

# imprimimos la frase traducida
print frase_traducida

log_traduccion("es", "en", frase, frase_traducida)
