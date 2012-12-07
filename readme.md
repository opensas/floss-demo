floss-demo
==========

El presente proyecto forma parte del "Taller práctico de Software Libre", que tiene por objeto difundir entre personas sin conocimientos técnicos en informática, las ventajas del uso de software libre o floss (free-libre open source software).

Para ello hemos creado un requerimiento ficticio: un aplicativo de línea de comandos que permita traducir una frase del idioma castellano al idioma inglés.

Dicho requerimiento será llevado a cabo con una empresa que desarrollará una solución privativa (disponible en [privativo](https://github.com/opensas/floss-demo/tree/master/privativo)) y otra empresa que llevará adelante el mismo requerimiento desarrollando una solución libre (disponible en [libre](https://github.com/opensas/floss-demo/tree/master/libre)).

Entregables
===========

En el caso de la versión privativa, los entregables se encuentran en [privativo/dist](https://github.com/opensas/floss-demo/tree/master/privativo/dist), y consisten en:

- priv-translate

Se trata de un único archivo ejecutable, fruto de compilar y empaquetar todas las dependencias necesarias utilizando pytinstaller-2.0

- licencia.pdf

Se trata de una _licencia de uso de usuario final_ ficticia, creada a partir de la licencia de uso de Windows XP edición en español, que acompañamos en [licencia/Windows XP SP2_Professional_Spanish.pdf](https://github.com/opensas/floss-demo/blob/master/privativo/licencia/Windows%20XP%20SP2_Professional_Spanish.pdf)

En el caso de la versión libre, los entregables se encuentran en [libre](https://github.com/opensas/floss-demo/tree/master/privativo/dist), y consisten en:

- traductor

Archivo bash para facilitar el acceso al script de python

- traductor.py

Archivo fuente de python que implementa la interfaz vía línea de comando para utilizar la funcionalidad provista por la librería traductor_lib.py

- traductor_lib.py

Librería de terceros creada a los efectos de esta demostración, publicada bajo una licencia libre (GPLv3).

- gpl.txt y gpl_es.txt

Texto oficial de la licencia GPLv3 en inglés junto con una traducción al castellano.