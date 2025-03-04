# Proyecto-PC
En este repositorio podrás encontrar un código que te permitirá jugar el tradicional juego de mesa de parqués junto con otras 3 personas, puedes ampliar la información sobre cómo hacerlo en el archivo README

Cómo jugar Parqués (Basado en el código) Objetivo del Juego El objetivo principal en Parqués es ser el primer jugador en mover todas tus cuatro fichas desde la cárcel, alrededor del tablero, y llevarlas a la zona de llegada de tu color ("llegadas").

Componentes del Juego (Representados en el Código) Tablero: El tablero está representado implícitamente a través de las posiciones numéricas. Las posiciones van de 0 a 67 alrededor del tablero principal. Las zonas de llegada de cada jugador son posiciones separadas (68-75 para Rojo, 76-83 para Azul, etc.).

Fichas: Cada jugador tiene 4 fichas. Inicialmente, todas las fichas están en la "cárcel".

Dados: Se utilizan dos dados de seis caras.

Preparación del Juego Ejecutar el Código: Ejecuta el script de Python.

Seleccionar el Modo de Juego: El juego te preguntará si quieres jugar en modo "Real" o "Desarrollador".

Modo Real: Los dados se lanzan aleatoriamente.

Modo Desarrollador: Tú introduces los valores de los dados manualmente (útil para probar el juego).

El juego comienza automáticamente.

Desarrollo del Juego Turnos: Los jugadores se turnan para jugar en el orden: Rojo, Azul, Verde, Amarillo.

Lanzar los Dados: Al principio de tu turno, el juego "lanza" los dados (aleatoriamente en modo real, manualmente en modo desarrollador). Se mostrarán los valores de los dados.

Sacar Fichas de la Cárcel:

Para sacar una ficha de la cárcel, necesitas sacar un 5 en al menos uno de los dados, o que la suma de ambos dados sea 5.

Si sacas un 5, el juego te preguntará si quieres sacar una ficha. Si lo haces, una de tus fichas se moverá de la cárcel a tu casilla de salida (5 para Rojo, 22 para Azul, etc.).

Sólo puede haber un máximo de 2 fichas en la casilla de salida, si ya hay 2, no puedes sacar una ficha hasta que una de las que están allí se mueva.

Si sacas una ficha de la cárcel, no tienes derecho a utilizar los valores de los dados para mover otras fichas a menos que hayas sacado pares (dobles).

Mover Fichas:

Si ya tienes fichas en el tablero, puedes usar los valores de los dados para moverlas.

El juego calculará y mostrará los movimientos posibles. Por ejemplo, si sacas un 2 y un 3, puedes mover una ficha 2 casillas y otra 3 casillas, o mover una ficha 5 casillas (2+3).

El juego te pedirá que elijas qué ficha quieres mover y cuántas casillas quieres moverla.

Casillas Seguras: Las casillas seguras (marcadas en el código como self.seguros) son casillas donde tus fichas no pueden ser capturadas por otros jugadores.

Capturar Fichas ("Comer"):

Si mueves una de tus fichas a una casilla ocupada por una ficha de otro jugador, y esa casilla no es una casilla segura, "comes" la ficha del otro jugador. La ficha capturada regresa a la cárcel.

Bloqueos:

Si dos fichas del mismo jugador terminan en la misma casilla, se crea un "bloqueo".

Ningún jugador (incluido tú) puede mover una ficha a través de un bloqueo.

Llegada:

Para llevar una ficha a la zona de llegada de tu color, debes moverla exactamente al número correcto de casillas. Por ejemplo, si estás cerca de tu zona de llegada, es posible que necesites sacar un número específico en los dados para entrar.

Pares (Dobles):

Si sacas pares (los dos dados muestran el mismo número), tienes derecho a otro turno.

Si sacas tres pares consecutivos, la última ficha que moviste regresa a la cárcel.

Cómo Usar el Código Requisitos: Asegúrate de tener Python 3 instalado en tu sistema.

Guardar el Código: Guarda el código como un archivo .py (por ejemplo, parques.py).

Ejecutar el Código: Abre una terminal o línea de comandos, navega hasta el directorio donde guardaste el archivo y ejecuta el código con el comando python parques.py.

Interactuar con el Juego: Sigue las instrucciones que aparecen en la pantalla. El juego te pedirá que ingreses valores para los dados (en modo desarrollador) y que elijas qué fichas mover y cómo.

