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

# 2.0 Mapa de juego

Cada elemento  del juego sera colocado dentro de un array bidimensional, colocando numeros para representar los elementos del juego. A continuacion se muestra un ejemplo del mapa  (array bidimensional).

[3, 4, 4, 0, 1, 4, 4, 3]

## Lista de elementos

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

