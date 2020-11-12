# SistemaIntercambio
En éste proyecto, se busca imitar una red de sistemas de intercambios culturales, de viajes por profesión o por simple gusto. Se desarrolla en el framework de Django junto con HTML, CSS y Javascript para la construcción de la página. 
Para poder ejectutar el proyecto se debe instalar propiamente DJango, dentro de un entorno virtual, de ésta manera:
	1. instalamos virtualenv :
	 $ sudo pip install virtualenv
     
	2. Creamos el entorno virtual:
	  $ virtualenv mi_entorno
      
    3. activamos el entorno virtual al ingresar éste comando:
      $ workon mi_entorno
      
    4. Desactivamos el entorno virtual con el siguiente comando:
      $ deactivate
      
 Dentro de nuestro entorno, ahora lo que queremos hacer es instalar el propio Django junto con una adaptación visual para nuestro admin del proyecto llamado "suit".
 Dentro de nuestro entorno virtual, ingresamos los siguientes comandos:
    1.  (mi_entorno)$ pip install Django==2.2
    2.  (mi_entorno)$ pip install django-suit
 Una vez instalado todo, se ingresa un último comando dentro del entorno virtual para poder correr el proyecto sin nungún problema : **(mi_entorno)$ python manage.py runserver**
 Con eso podemos concluir con la instalación y ejecución del proyecto. Muchas gracias por descargarlo!!
