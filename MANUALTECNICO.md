# **Manual técnico del Sistema de Calificación de Tesis**
## Dirigido a desarrolladores 
###### Nota: El sistema está basado en el modelo MVC(Modelo-Vista-Controlador) y utiliza pruebas unitarias y excepciones como buena práctica de la ingeniería de software.
### El sistema planteado consiste en un sistema de información que facilita la calificación de los trabajos de grado de maestría cuando los estudiantes realizan su sustentación pública.
### A continuación, se explican cada uno de los parámetros para implementar el modelo MVC en el sistema de información:
## Modelo
#### Se definieron las clases que permitieron "modelar" a lo usuarios que tienen acceso al sistema y a las interacciones entre ellos. Así, se definieron las clases Acta, Asistente, Criterio, DetalleCriterio, Director, Jurado y Usuario. 
#### A continuación, se mencionan algunos criterios de diseño que se tomaron en cuenta:
<ol>
<li>Se cuenta con una clase Usuario que funciona como clase padre para las clases Jurado, Director y Asistente. Esto, con el fin de implementar atributos protegidos que hereden las clases hijas.</li>
<li>Se implementa una clase Detalle criterio con el ánimo de que en ella se guarden los datos correspondientes a las calificaciones de cada criterio. Como dicha información es dinámica, se opta por separar las interacciones estáticas de los criterios de las dinámicas; es decir, separar la definición del criterio(ponderación, descripción e indentificador) de la información correspondiente a las calificaciones. </li>
<li>Cada instancia de clase la clase Acta tiene un diccionario llamado "detalles_criterios"  el  cual contiene distintas intancias de tipo Detalle Criterio y es aquí donde se guardan las calificaciones n°1 y n°2 para cada uno de los criterios.</li>
</ol>

## Controlador
#### El controlador interactúa con el modelo y la vista y cuenta con diversos métodos que permiten realizar esto. A continuación, se presentan descripciones de algunos de dichos métodos:
<ol>
<li>Se cuenta con el método agregar_detalles_criterios que permite asociar criterios particulares a diferentes instancias Detalle criterio; luego, dicho diccionario entra como parámetro al momento de agregar un acta nueva.</li>
<li>El método inicializar_criterios permite definir unos criterios predeterminados cada vez que inicia el sistema.</li>
<li>El método validar_criterios tiene como función revisar si, al sumar los valores de todas las ponderaciones de los criterios, se obtiene como resultado 1 (equivalente a 100%). </li>
<li>El método cambiar_estado_acta busca verificar en qué momento se encuentra la evaluación de un acta. Además, la idea prinicipal es lograr cambiar de estado dependiendo de la situación. Por ejemplo, si solamente uno de los dos jurados ha realizado la evaluación de la tesis, el estado del acta cambia a "En proceso". Por otro lado, si ya ambos jurados han realizado sus respectivas evaluaciones, el estado del acta pasa a ser "Terminado"</li>
<li>El método encontrar_nota_parcial_jurado permite encontrar la nota parcial que colocó un jurado a la evaluación de la tesis. Es decir, obtiene la nota correspondiente a la evaluación final que realizó uno de los jurados; esto se consigue al sumar las notas obtenidas en cada unos de los criterios considerando las ponderaciones respectivas. </li>
</ol>

## Vista
#### Para la vista se utiliza el framework "Streamlit", el cual permite crear un Front-End con menos nivel de complejidad para el programador.
###### Nota: si desea conocer más de streamlit, visite el siguiente link: https://streamlit.io/ 
#### Para el sistema de la vista se trabajó con una clase MainView principal la cual permite crear la interfaz completa del sistema mediante streamlit. Además, se utilizaron otros 3 archivos que permiten complementar esta interfaz:
<ol>
<li>ViewJurado</li>
<li>ViewAsistente</li>
<li>ViewDirector</li>
</ol>

##### Importante: Streamlit trabaja por sesiones, por lo que es importante almacenar en variables de instancia(atributos) los valores que se obtienen. 

## Otros temas de interés:
### Excepciones y pruebas unitarias
#### El sistema implementa excepciones y pruebas unitarias para mejorar la interacción con el usuario. Las pruebas unitarias implementadas pueden verse en la carpeta **test**. 
###### Nota: es importante mencionar que no se implementaron pruebas unitarias para todos los métodos debido a que se requería un conocimiento más profundo del Framework.
### Modelación del sistema 
#### A continuación puede encontrar el link que permite observar el diagrama UML planteado para modelar el sistema: https://drive.google.com/file/d/1S_JvWkAoW4_CJKJq_c5AR-a1QxN4L4f1/view?usp=sharing 

