<!-- # Proyecto integrantes:
# - Lucas Montoby
# - Julian Rodriguez -->
<!-- #Para crear un proyecto usamos el comando:
django-admin startproject "nombre del proyecto"

Para interactuar con el proyecto debemos acceder a él con el comando cd "nombre del proyecto".

Para crear una "app" o "modulo" aplicamos el comando:
python manage.py startapp "nombre de la app o modulo"

Para crear un modelo dentro de la app que creamos:
#Recordemos que el modelo es el encargado de comunicarse con la base de datos.

1) Ingresamos al archivo models.py

2) Declaramos una clase que heredará de Django models.Model quedando:
	class nombreclase(modles.Model)

3) Aquí ya seremos libres de ingresar todos los parametros que tendrá nuestra base de datos. 
La base de datos como la estructura de celdas de un excel, por lo que al crear una variable estaríamos
creando una columna:
	nombre = models.CharField(max_length=40)
		 #llamamos a la clase models que heredamos en primera instancia.
		 #y usamos el metodo CharField() que le indicará que la variable.
		 #tendrá alojada dentro de ella un string, acompañamos a esto.
		 #con un max_length para indicar el límite máximo de caracteres que tendrá.

Una vez creados todos los modelos que usaremos, nos dirigimos a los ajustes del proyecto y en la seccion de
INSTALLED_APPS agregamos la aplicación o modulo que acabamos de crear.

Tras agregar la aplicacion procedemos a migrar nuestros modelos a la base de datos, en este caso lo haremos con sqlite.
Lo hacemos con los comandos:

python manage.py makemigrations
# Al finalizar esta migración en la terminal se nos indicará dónde quedó alojado el archivo
#que contiene la estructura para crear la base de datos, el nombre de este archivo será muy importante para espeficifarlo 
#en el comando que veremos más adelante, mucho ojo que el archivo quedará con un _initial_ esa parte del nombre no la necesitamos.

python manage.py sqlmigrate nombre_app nombreclave_migracion
# Este comando recibe dos parametros, el primero es el nombre de la app que estamos creando
#y el segundo es el identificador clave de la migración que hicimos con el comando anterior

python manage.py migrate
#Por ultimo este comando es el que se encargará de migrar completamente todo lo que hicimos anteriormente a la base de datos del proyecto. -->

# Entrega1-LucasMontoby-JulianRodriguez


