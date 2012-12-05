#!/usr/bin/env python
# coding=UTF-8

# floss-demo
# ==========
# 
# Script de ejemplo para explicar los principios del software librerías
# 
# Librería para utilizar el servicio web de http://mymemory.translated.net
# para traducir frases de un idioma al otro
# 
# Actualmente el uso gratuito de esta herramienta se 
# encuentra limitada a 2.000 traducciones por día
# 
# Más información acerca del servicio web en:
# http://mymemory.translated.net/doc/spec.php
# 
# Ejemplo de uso:
# 
# http://mymemory.translated.net/api/get?q=Hola amigos&langpair=es|en
# 

# declaramos librerías a utilizar
import httplib2, urllib, json

# función traducir: Traduce el texto ingresado de un idioma a otro
# 
# Parámetros:
#   idioma_fuente:  idioma del texto a traducir. Ej: es
#   idioma_destino: idioma al cual se quiere traducir el texto. Ej: en
#   texto:          texto a traducir
# 
# Retorna:
#   el texto traducido, o un mensaje de error si no pudo utilizar el servicio web

def traducir(idioma_fuente, idioma_destino, texto):

  url_base = "http://mymemory.translated.net/api/get?"

  # formateamos los idiomas de entrada y salida para agregar al url
  idiomas = "%s|%s" % (idioma_fuente, idioma_destino)
  parametros = urllib.urlencode({'q': texto, 'langpair': idiomas})

  # armamos el url completo
  url = url_base + parametros

  try:

    # intentamos acceder al servicio web de traducción
    respuesta, contenido = httplib2.Http().request(url)

    # verificamos si hubo un error
    if respuesta.status != 200:
      return "error accessing web service"

    # decodificamos la información devuelta en formato json
    json_data = json.loads(contenido)

    # extraemos el texto traducido y lo retornamos
    return str(json_data["responseData"]["translatedText"])

  except:
    return "error al traducir el texto"

