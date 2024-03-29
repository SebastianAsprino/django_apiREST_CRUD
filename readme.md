Para iniciar nuestro proyecto de Django se requieren los siguientes comandos, el proyecto se realizó ejecutando los comandos en **Creación de proyecto**, sin embargo es pertinente explicarlos.

## Creación de proyecto
Instalar el framework Django
```
pip install django
```
Para crear el proyecto se ha usado el siguiente comando
```
django-admin startproject pokemon_api
```

## Requerimientos
Luego de clonar el repositorio es necesario instalar los requerimientos para que no haya ningún error relacionado a las dependencias usadas.
Ubicarse en la carpeta DJANGO_APIREST_CRUD y ejecutar el siguiente comando:
```
pip install -r requirements.txt
```
Si se instala otra dependencia esta debe ser incluida en el archivo `requirements.txt`.
Ubicarse en la carpeta DJANGO_APIREST_CRUD y ejecutar el siguiente comando:
```
pip freeze > requirements.txt
```

## Estructura del proyecto
Se han creado dos carpetas con el nombre `pokemon_api`, sin embargo la que contendrá el proyecto se le ha cambiado el nombre a `src` y la que unirá cada app creada está dentro de `src` llamada `pokemon_api`

Siempre que se requiera realizar o ejecutar algo en el proyecto, se debe acceder a la carpeta `src`
```
cd src
```

Desde ahora todo cambio o acción a realizar en el proyecto debe hacerse con cualquiera de los dos siguientes comandos.
```
./manage.py
or
py manage.py 
```

Para ejecutar el proyecto
```
py manage.py runserver
```

Luego se debe buscar una línea similar a la siguiente

```
Starting development server at http://127.0.0.1:8000/
```
Se debe dar ctrl + clic en `http://127.0.0.1:8000/`

Habiendo abierto una página en el navegador, al url se le debe añadir admin/ para entrar en un login
```
Username:user1
Password:123!
```

Introducido el superuser, se mostrará el panel de administración de Django.
