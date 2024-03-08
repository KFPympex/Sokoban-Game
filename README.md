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

## 4. Funcion a implementar

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | Por hacer | - | - | - | 
| 1. | Repetir el juego hasta terminar el nivel. | Por hacer | - | -  | - |
| 2. | Imprimir mapa.| Por hacer | - | - | - |
| 3. | Leer el movimiento. | Por hacer | - | - | - |
| 4. | Evaluar el movimiento del usuario. | Por hacer | - | - | - |

## Derecha

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, espacio  | Echo | [0,4] | [4,0] | 5/3/24 |
| 6. | Personaje, meta  | Echo | [0,2] | [4,5] | 6/3/24 |
| 7. | Personaje, caja, espacio | Por hacer | [0,1,4] | [4,0,1] | 7/3/24 |
| 8. | Personaje, caja,  meta | Por hacer | [0,1,2] | [4,0,6] | 7/3/24 |
| 9. | Personaje, caja_meta, espacio | Por hacer | [0,6,4] | [4,5,1] | 7/3/24 |
| 10. |Personaje, caja_meta, meta | Por hacer | [0,6,2] | [4,5,6] | - |
| 11. | Personaje_meta, espacio | Por hacer | [5,4] | [2,0] | - |
| 12. | Personaje_meta, meta | Por hacer | [5,2] | [2,5] | - |
| 13. | Personaje_meta, caja, espacio | Por hacer | [5,1,4] | [2,0,1] | - |
| 14. | Personaje_meta, caja, meta | Por hacer | [5,1,2] | [2,0,6] | 6/3/24 | 
| 15. | Personaje_meta, caja_meta, espacio | Por hacer | [5,6,4] | [2,5,1] | - |
| 16. | Personaje_meta, caja_meta, meta | Por hacer | [5,6,2] | [2,5,6] | - |

## Izquierda

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 17. | Personaje y espacio | Echo | [4,0] | [0,4] | 5/3/24 |
| 18. | Personaje y meta | Por hacer | [2,0] | [5,4] | 6/3/24 |
| 19. | Personaje, caja y espacio | Por hacer | [4,1,0] | [1,0,4] | 7/3/24 |
| 20. | Personaje, caja y meta | Por hacer | [2,1,0] | [6,0,4] | 7/3/24 |
| 21. | Personaje, caja_meta y espacio | Por hacer | [4,6,0] | [1,5,4] | 7/3/24 |
| 22. | Personaje, caja_meta y meta | Por hacer | [2,6,0] | [6,5,4] | - |
| 23. | Personaje_meta y espacio | Por hacer | [4,5] | [0,2] |- |
| 24. | Personaje_meta y meta | Por hacer | [2,5] | [5,2] | - |
| 25. | Personaje_meta, caja y espacio | Por hacer | [4,1,5] | [1,0,2] |- |
| 26. | Personaje_meta, caja y meta | Por hacer | [2,1,5] | [6,0,2] |- |
| 27. | Personaje_meta, caja_meta y espacio | Por hacer | [4,6,5] | [1,5,2] | - |
| 28. | Personaje_meta, caja_meta y meta | Por hacer | [2,6,5] | [6,5,2] |- |

## Arriba

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 29. | Personaje y espacio | Echo | [4,0] | [0,4] | 5/3/24 |
| 30. | Personaje y meta | Por hacer | [2,0] | [5,4] | 6/3/24 | 
| 31. | Personaje, caja y espacio | Por hacer | [4,1,0] | [1,0,4] | 7/3/24 |
| 32. | Personaje, caja y meta | Por hacer | [2,1,0] | [6,0,4] | 7/3/24 |
| 33. | Personaje, caja_meta y espacio | Por hacer | [4,6,0] | [1,5,4] | 7/3/24 |
| 34. | Personaje, caja_meta y meta | Por hacer | [2,6,0] | [6,5,4] | - |
| 35. | Personaje_meta y espacio | Por hacer | [4,5] | [0,2] | - |
| 36. | Personaje_meta y meta | Por hacer | [2,5] | [5,2] | - |
| 37. | Personaje_meta, caja y espacio | Por hacer | [4,1,5] | [1,0,2] | - |
| 38. | Personaje_meta, caja y meta | Por hacer | [2,1,5] | [6,0,2] | - |
| 39. | Personaje_meta, caja_meta y espacio | Por hacer | [4,6,5] | [1,5,2] | - |
| 40. | Personaje_meta, caja_meta y meta | Por hacer | [2,6,5] | [6,5,2] | - |

## Abajo

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 41. | Personaje y espacio | Echo | [0,4] | [4,0] | 5/3/24 |
| 42. | Personaje y meta | Por hacer | [0,2] | [4,5] | 6/3/24 |
| 43. | Personaje, caja y espacio | Por hacer | [0,1,4] | [4,0,1] | 7/3/24 |
| 44. | Personaje, caja y meta | Por hacer | [0,1,2] | [4,0,6] | 7/3/24 |
| 45. | Personaje, caja_meta y espacio | Por hacer | [0,6,4] | [4,5,1] | 7/3/24 |
| 46. | Personaje, caja_meta y meta | Por hacer | [0,6,2] | [4,5,6] | # Sokoban

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

## 4. Funcion a implementar

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | Por hacer | - | - | - | 
| 1. | Repetir el juego hasta terminar el nivel. | Por hacer | - | -  | - |
| 2. | Imprimir mapa.| Por hacer | - | - | - |
| 3. | Leer el movimiento. | Por hacer | - | - | - |
| 4. | Evaluar el movimiento del usuario. | Por hacer | - | - | - |

## Derecha

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, espacio  | Echo | [0,4] | [4,0] | 5/3/24 |
| 6. | Personaje, meta  | Echo | [0,2] | [4,5] | 6/3/24 |
| 7. | Personaje, caja, espacio | Por hacer | [0,1,4] | [4,0,1] | 7/3/24 |
| 8. | Personaje, caja,  meta | Por hacer | [0,1,2] | [4,0,6] | 7/3/24 |
| 9. | Personaje, caja_meta, espacio | Por hacer | [0,6,4] | [4,5,1] | 7/3/24 |
| 10. |Personaje, caja_meta, meta | Por hacer | [0,6,2] | [4,5,6] | 7/3/24 |
| 11. | Personaje_meta, espacio | Por hacer | [5,4] | [2,0] | 7/3/24 |
| 12. | Personaje_meta, meta | Por hacer | [5,2] | [2,5] | 7/3/24 |
| 13. | Personaje_meta, caja, espacio | Por hacer | [5,1,4] | [2,0,1] | 7/3/24 |
| 14. | Personaje_meta, caja, meta | Por hacer | [5,1,2] | [2,0,6] | 6/3/24 | 
| 15. | Personaje_meta, caja_meta, espacio | Por hacer | [5,6,4] | [2,5,1] | 7/3/24 |
| 16. | Personaje_meta, caja_meta, meta | Por hacer | [5,6,2] | [2,5,6] | 7/3/24 |

## Izquierda

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 17. | Personaje y espacio | Echo | [4,0] | [0,4] | 5/3/24 |
| 18. | Personaje y meta | Por hacer | [2,0] | [5,4] | 6/3/24 |
| 19. | Personaje, caja y espacio | Por hacer | [4,1,0] | [1,0,4] | 7/3/24 |
| 20. | Personaje, caja y meta | Por hacer | [2,1,0] | [6,0,4] | 7/3/24 |
| 21. | Personaje, caja_meta y espacio | Por hacer | [4,6,0] | [1,5,4] | 7/3/24 |
| 22. | Personaje, caja_meta y meta | Por hacer | [2,6,0] | [6,5,4] | 7/3/24 |
| 23. | Personaje_meta y espacio | Por hacer | [4,5] | [0,2] | 7/3/24 |
| 24. | Personaje_meta y meta | Por hacer | [2,5] | [5,2] | 7/3/24 |
| 25. | Personaje_meta, caja y espacio | Por hacer | [4,1,5] | [1,0,2] | 7/3/24 |
| 26. | Personaje_meta, caja y meta | Por hacer | [2,1,5] | [6,0,2] | 7/3/24 |
| 27. | Personaje_meta, caja_meta y espacio | Por hacer | [4,6,5] | [1,5,2] | 7/3/24 |
| 28. | Personaje_meta, caja_meta y meta | Por hacer | [2,6,5] | [6,5,2] | 7/3/24 |

## Arriba

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 29. | Personaje y espacio | Echo | [4,0] | [0,4] | 5/3/24 |
| 30. | Personaje y meta | Por hacer | [2,0] | [5,4] | 6/3/24 | 
| 31. | Personaje, caja y espacio | Por hacer | [4,1,0] | [1,0,4] | 7/3/24 |
| 32. | Personaje, caja y meta | Por hacer | [2,1,0] | [6,0,4] | 7/3/24 |
| 33. | Personaje, caja_meta y espacio | Por hacer | [4,6,0] | [1,5,4] | 7/3/24 |
| 34. | Personaje, caja_meta y meta | Por hacer | [2,6,0] | [6,5,4] | 7/3/24 |
| 35. | Personaje_meta y espacio | Por hacer | [4,5] | [0,2] | 7/3/24 |
| 36. | Personaje_meta y meta | Por hacer | [2,5] | [5,2] | 7/3/24 |
| 37. | Personaje_meta, caja y espacio | Por hacer | [4,1,5] | [1,0,2] | 7/3/24 |
| 38. | Personaje_meta, caja y meta | Por hacer | [2,1,5] | [6,0,2] | 7/3/24 |
| 39. | Personaje_meta, caja_meta y espacio | Por hacer | [4,6,5] | [1,5,2] | 7/3/24 |
| 40. | Personaje_meta, caja_meta y meta | Por hacer | [2,6,5] | [6,5,2] | 7/3/24 |

## Abajo

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 41. | Personaje y espacio | Echo | [0,4] | [4,0] | 5/3/24 |
| 42. | Personaje y meta | Por hacer | [0,2] | [4,5] | 6/3/24 |
| 43. | Personaje, caja y espacio | Por hacer | [0,1,4] | [4,0,1] | 7/3/24 |
| 44. | Personaje, caja y meta | Por hacer | [0,1,2] | [4,0,6] | 7/3/24 |
| 45. | Personaje, caja_meta y espacio | Por hacer | [0,6,4] | [4,5,1] | 7/3/24 |
| 46. | Personaje, caja_meta y meta | Por hacer | [0,6,2] | [4,5,6] | 7/3/24 |
| 47. | Personaje_meta y espacio | Por hacer | [5,4] | [2,0] | 7/3/24 |
| 48. | Personaje_meta y meta | Por hacer | [5,2] | [2,5] | 7/3/24 |
| 49. | Personaje_meta, caja y espacio | Por hacer | [5,1,4] | [2,0,1] | 7/3/24 |
| 50. | Personaje_meta, caja y meta | Por hacer | [5,1,2] | [2,0,6] | 7/3/24 |
| 51. | Personaje_meta, caja_meta y espacio | Por hacer | [5,6,4] | [2,5,1] | 7/3/24 |
| 52. | Personaje_meta, caja_meta y meta | Por hacer | [5,6,2] | [2,5,6] | 7/3/24 |

## Determina si se completo el nivel o no

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 53. | Evaluar si el nivel esta terminado.  | Por hacer | - | - | - |
| 54. | Si el nivel esta terminado cargar el siguiente nivel.  | Por hacer | - | - | - |

## Función extra

| No. | Función | Kanban |  Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 55. | Función adicional o powerup (descripción). | Por hacer | - | - | - |






