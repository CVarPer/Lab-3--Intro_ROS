# Laboratorio 3 Introducción a ROS

<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/CVarPer/Lab-3--Intro_ROS">
    <img src="recursos/UNAL.png" alt="Logo" width="200">
  </a>

  <h3 align="center">Laboratorio 3: Introducción a ROS</h3>

  <p align="center">Robótica
    <br />
    <a href="https://github.com/Danmunozbe/Practica1/tree/Pain2"></a>
    <br />Daniel Muñoz · Christian Vargas
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Índice</summary>
  <ol>
    <li>
      <a href="#introducci%C3%B3n">Introducción</a>
    </li>
    <li>
      <a href="#Desarrollo">Desarrollo</a>
      <ul>
        <li><a href="#Metodología">Metodología</a></li>
        <li><a href="#Matlab">Matlab</a></li>
        <li><a href="#Python">Python</a></li>
      </ul>
    </li>
    <li><a href="#Conclusiones">Conclusiones</a></li>
  </ol>
</details>



<!-- Intro -->
## Introducción

Si bien el nombre sugiere lo contrario, ROS (Robot Operating System) es un conjunto de herramientas y bibliotecas de código abierto que ofrece un robusto ecosistema para desarrollar software orientado a robots. Para familiarizarse con él, fue necesario realizar la instalación de la distribución de Linux Ubuntu 20.04, y se trabajó fundamentalmente con Matlab, la Terminal del sistema operativo y el propio ROS.

En este documento se presentan los primeros pasos tomados para iniciarse en el entorno de trabajo de ROS, utilizando el programa introductorio ```turtlesim```, que ofrece una abstracción del movimiento y manejo de un robot, presentando una interfaz gráfica para facilidad en la comprensión del funcionamiento.

A continuación, se presenta el trabajo realizado en Matlab y Python a fin de alcanzar los objetivos de aprendizaje dispuestos en la guía de laboratorio.

<!-- GETTING STARTED -->
## Desarrollo


### Metodología

Una vez familiarizado con la inicialización del nodo principal mediante el comando ```roscore```, se ejecuta el nodo correspondiente a ```turtlesim```. Partiendo de este punto, como se observa en la figura a continuación, se procedió a trabajar en Matlab

![turtlesim](/recursos/setup.png)

### Matlab

Los códigos realizados en este apartado pueden ser encontrados en la sección: ```turtle_sim/scripts/Matlab```

0. Se incluye el script indicado en la guía.

1. En este caso, se solicitaba la suscripción al tópico de pose de la interfaz gráfica de la tortuga. 

  - Se utiliza ```rossubscriber``` para crear un suscriptor para el tópico de pose.
  - Se recibe el último mensaje de pose utilizando ```receive``` con la opción 1 para obtener solo el último mensaje.
  - Se muestra la información de la pose recibida.


2. Posteriormente se solicita enviar los valores asociados a la pose de la tortuga.

  - Se crea un publicador para el tópico de comandos de velocidad.
  - Se crea un mensaje de velocidad y se asignan valores de velocidad lineal y angular al mensaje.
  - Se envía el mensaje de velocidad al publicador.
  - Se hace una pausa de 1 segundo para permitir que la tortuga se mueva durante ese tiempo.
  - Se cierra la conexión con ROS al finalizar.

### Python

#### Definición de librerías
De forma preliminar, como es habitual, se incluyeron las librerías correspondientes para el funcionamiento del programa. En este caso, se tienen las siguientes:

```rospy```: Es la biblioteca principal de ROS para Python, que permite interactuar con el sistema ROS.
```sys, select, termios, tty```: Estas bibliotecas se utilizan para leer las teclas presionadas por el usuario.
```Twist```: Es el tipo de mensaje que se utiliza para enviar comandos de velocidad a la tortuga.
```TeleportAbsolute TeleportRelative```: Son los servicios que se utilizan para mover la tortuga a una posición absoluta o relativa.

#### Definición de funciones Propias
```getKey()```: Esta función se encarga de leer la tecla presionada por el usuario.
```movTortuga(key)```: Esta función determina qué acción tomar en función de la tecla presionada y publica el mensaje derotate velocidad correspondiente.
```Retorno()```: Esta función llama al servicio turtle1/teleport_absolute para resetear la posición de la tortuga al centro del área de trabajo.
```Giro180()```: Esta función llama al servicio turtle1/teleport_relative para rotar la tortuga 180 grados en su posición actual.
#### Definicion de funciones ROSPy
```rospy.wait_for_service(service,timeout=None)``` Función que bloquea el codigo hasta que el servicio (service) (En este caso  ```teleport_absolute``` y ```teleport_relative```) este habilitado.
```rospy.ServiceProxy('service_name', my_package.srv.Foo)```Llama el servicio "service_name", en este caso,  ```teleport_absolute``` y ```teleport_relative```) este habilitado.
```rospy.init_node('my_node_name')``` Crea un proceso Nodo "my_node_name".
```rospy.Publisher('topic_name', std_msgs.msg.String, queue_size=10)``` Clase que publica al topic, con un formato de mensaje y una cola para manejo asincrono (ignorable).


Ahora bien, en cuanto al funcionamiento general del código, primero se inicializa el nodo correspondiente al nombre del script, y se publica el tópico ```turtle1/cmd_vel``` para realizar la conexión con *turtlesim*. Por su parte, el objeto Twist almacena los valores de velocidad lineal y angular.

El código realizado puede ser consultado en la sección ```turtle_sim/scripts/myTeleopKey.py```. 

Se presenta también un video del programa en funcionamiento (hacer click en la imagen):

[![turtle](/recursos/turtle.png)](https://youtu.be/jihc9vAioDU) 


##  Conclusiones

1. Se demostró la capacidad de integrar ROS con MATLAB, lo que proporciona una amplia gama de herramientas de análisis y procesamiento de datos a los usuarios de ROS que están familiarizados con MATLAB.

2. Se utilizaron herramientas fundamentales de ROS, como los publicadores y suscriptores, para enviar y recibir mensajes entre los nodos, lo que permite la comunicación y el control de los diferentes componentes del sistema robótico.

3. Se demostró la capacidad de controlar la tortuga en turtlesim utilizando comandos de velocidad enviados a través de ROS. Esto es útil para comprender los principios básicos de control de robots y para realizar pruebas y experimentos en un entorno simulado.

4. Se utilizó la suscripción a tópicos para obtener información sobre la posición y orientación de la tortuga, así como el envío de comandos de velocidad a través de tópicos para controlar su movimiento. También se mencionó la posibilidad de utilizar servicios para modificar la pose de la tortuga.

5. Se mostró cómo establecer y cerrar la conexión con el nodo maestro de ROS, lo que es importante para garantizar una comunicación adecuada y evitar problemas de recursos.
