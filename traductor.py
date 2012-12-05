#!/usr/bin/env python
# coding=UTF-8

# declaramos librerías que vamos a utilizar
from translate import translate
from argparse import ArgumentParser

# funciones varias
# 

# lee los parámetros de la línea de comandos
def leer_parametros():
  parser = ArgumentParser(description='Permite traducir una frase del castellano al inglés.')
  parser.add_argument('frase', metavar='frase', help='frase a traducir')
  args = parser.parse_args()
  return args.frase


# programa principal
# 

# leemos la frase que el usuario ingresó desde la línea de comandos
frase = leer_parametros()

# traducimos la frase
frase_traducida = translate("es", "en", frase)

# imprimimos la frase traducida
print frase_traducida
