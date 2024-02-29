# Sokoban-Game
Mi juego de Sokoban (Implementación de Sokoban Retro en Python)

"""
Markdown
1.Objetivo: acomodar cajas en un punto de terminante
2.Elementos del juego: 0.-Personaje
                       1.-Cajas
                       2.-Metas
                       3.-Paredes
                       4.-Espacios/Pisos

*Niveles de juego 1 a N

3.-Reglas a mecanica del juego:

Empujar 1 caja 

1.-Moverse hacia arriba sobre piso #MOVERSE CON ESPACIO#
2.-Moverse hacia abajo sobre piso #MOVERSE CON ESPACIO#
3.-Moverse hacia derecha sobre piso #MOVERSE CON ESPACIO#
4.-Moverse hacia izquierda sobre piso
5.-Reiniciar nivel
6.-Empujar 1 caja hacia arriba y que adelante este 1 piso #MOVERSE CON CAJA Y ESPACIO#
7.-Empujar 1 caja hacia abajo y que adelante este 1 piso #MOVERSE CON CAJA Y ESPACIO#
"""


# Sokoban

## 0. Objetivos

Programar eljuego de Sokoban en una version retro para consola.

## 1. Reglas del juego

El juego Sokoban consiste en acomodar cajas en puntos determinados por las metas.

1. El personaje se puede mover hcaia arriba, abajo, derecha y izquierda.
2. El personaje solo puede empujar una caja a la vez
3. El personaje se movera sobre un mapa definido.
4. Para terminar el nivel todad las cojas deberan de estar sobre las metas.

## 2. Elementos del juego

Cada elemento  del juego sera colocado dentro de un array bidimensional, colocando numeros para representar los elementos del juego. A continuacion se muestra un ejemplo del mapa  (array bidimensional).

[3, 4, 4, 0, 1, 4, 4, 3]

- 0 - Personaje
- 1 - Cajas
- 2 - Metas
- 3 - Paredes
- 4 - Piso
- 5 - Personaje_meta
- 6 - Caja_meta

## 3. Controles

Para moverse en el juego el usuario utilizara elguna de las siguientes letras para indicar hacia donde se quiere mover.

- a -> Izquierda
- b -> Derecha
- w -> Arriba
- s -> Abajo

## 4. Lista de movimientos

| No. | Sentido   | Movimiento      | Inicio | Fin   | Estado |
|-----|-----------|-----------------|--------|-------|--------|
|  1  | Izquierda | personaje, piso | [0,4]  | [4,0] | Done   |
|  2  | Derecha   | piso, personaje | [4,0]  | [0,4] | Done   |
