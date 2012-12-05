#!/usr/bin/env python
# coding=UTF-8

import httplib2, urllib, json

"""
http://mymemory.translated.net/api/get?q=este%20es%20un%20gran%20dia%20para%20liberar%20software%20libre&langpair=es%7Cen
"""

# ejemplo de uso
# print translate( "es", "en", "hola amigos")

def translate(source, target, text):

  base_url = "http://mymemory.translated.net/api/get?"

  langs = "%s|%s" % (source, target)
  params = urllib.urlencode({'q': text, 'langpair': langs})
  url = base_url + params

  # url = "http://mymemory.translated.net/api/get?q=hola amigos del alma&langpair=es%7Cen"

  try:
    http = httplib2.Http()
    response, content = http.request(url)

    if response.status != 200:
      return "error accessing web service"

    json_data = json.loads(content)

    return str(json_data["responseData"]["translatedText"])

  except:
    return "error al traducir el texto"

