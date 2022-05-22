# Segundo Proyecto Programación Orientada a Objetos, Primer Semestre 2022
## Integrantes:

> Juan Francesco García Vargas y Juan Jose Toro Restrepo

## Descripción General:
El objetivo del proyecto busca la solución al problema de la calificación 
de los trabajos de grado para los estudiantes de posgrado de la 
Pontificia Universidad Javeriana. 
El desarrollo consiste en una pagina web la cual cuenta con una interfaz
grafica realizada en el framework de python (**version 3.10.4**), **streamlit**. 
Las funcionalidades de la pagina web parten del tipo de usuario(Tres tipos
de Usuario, Directore, Jurado, Asistente). 
En terminos generales el software permite a partir de unas actas de calificación
calificar los trabajos de los estudiantes, también estan los procesos de cración
de acta, modificación de los criterior de evaluación del acta y exportación a PDF
de un acta cuando esta se encuentre totalmente calificada.

## Especificaciones:

- Creación de actas y almacenamiento de estas en un diccionario(entendiendo el estado
del acta como el proceso de calificación que esta se encuentra, "Vacio","En proceso" y/o 
"Terminado").
- Funcionalidad que permite modificar los criterios de evaluación verificando que la suma de 
estos sea no mayor ni menor al 1.0 o 100%.
- Organización de las actas y los Usuarios a partir de una identificación númerica unica, con 
el fin de realizar un programa que cuente con una estructura de datos con una complejidad 
computacional no mayor al **O(n)**.
- Proceso de evaluación en tiempo real, calificación de actas, cambio de su estado, reconocimiento(
trabajo aprobado o rechazado) y calculo de nota final.
- Exportación a formato PDF información del acta requerida por el cliente. Proceso que solo se ejecutará
cuando un acta posea nota final y reconocimiento.
- Sección de la interfaz grafica que permite ver para cada Usuario su respectivos argumentos. Por ejemplo,
Para el director ver las actas calificadas y que posean a su nombre y/o identificación como director 
en el acta o codirector.
