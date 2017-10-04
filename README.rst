Esta aplicación se trata de un demo para implementar django.contrib.gis.

A continuación se presenta los pasos para instalar la aplicación en modo desarrollo

1-) Instalar el controlador de versiones git:
    
    $ su
    # aptitude install git

2-) Descargar el codigo fuente de geodjango-demo:

    Para descargar el código fuente del proyecto contenido en su repositorio GIT realice un clon del proyecto geodjango-demo:

    Si da problemas con el certificado digital entonces debemos saltar su chequeo con el siguiente comando
    
    $ export GIT_SSL_NO_VERIFY=True

    Realizar clone

    $ git clone https://github.com/leonelphm/geodjango-demo.git

3-) Crear un Ambiente Virtual:

    El proyecto está desarrollado con el lenguaje de programación Python, se debe instalar Python v3.4.2. Con los siguientes comandos puede instalar Python y PIP.

    Entrar como root para la instalacion 

    # aptitude install python3.4 python3-pip python3.4-dev python3-setuptools

    # aptitude install python3-virtualenv virtualenvwrapper

    Salir del modo root y crear el ambiente:

    $ mkvirtualenv --python=/usr/bin/python3 geodjango


4-) Instalar los requerimientos del proyecto 

    Para activar el ambiente virtual geodjango ejecute el siguiente comando:

    $ workon geodjango
    (geodjango)$

    Entrar en la carpeta raiz del proyecto:

    (geodjango)$ cd sapic
    (geodjango)geodjango-demo$ 

    Desde ahi se deben instalar los requirimientos del proyecto con el siguiente comando:

    (geodjango)$ pip install -r requerimientos.txt


5-) Crear base de datos y Migrar los modelos:

    El manejador de base de datos que usa el proyecto es postgres, es necesario, tener instalado postgres y crear la base de datos desde postgres de la siguiente manera si se usa la consola de postgres, ademas se debe instalar postgis para el uso de una base de datos georeferenciada:

    como super usuario instalar postgis
    # aptitude install postgis
    # aptitude install postgresql-x.x-postgis-x.x


    postgres=# CREATE DATABASE geodjango OWNER=postgres ENCODING='UTF−8';
    postgres=# \q
    $ psql geodjango
    sapic=# CREATE EXTENSION postgis;

    Para migrar los modelos del proyecto se debe usar el siguiente comando:

    (geodjango)$ python manage.py makemigrations
    (geodjango)$ python manage.py migrate


7-) Ejecutar la aplicacion geodjango-demo

    Para ejecutar la apliacion se debe  ejecutar el siguiente comando:

    (geodjango)$ python manage.py runserver

    Ingresar a la ruta para registrar un zipcode en geodjango-demo.

    http://localhost:8000/geolocation/register-poly/


Contacto:
leonelphm@gmail.com
lhernandez@cenditel.go.ve