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

| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | Por hacer | - | | - |
| 1. | Repetir el juego hasta terminar el nivel. | Por hacer | - | | - |
| 2. | Imprimir mapa.| Por hacer | - |
| 3. | Leer el movimiento. | Por hacer | - |
| 4. | Evaluar el movimiento del usuario. | Por hacer | - |

## Derecha

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, pasillo  | Echo | [0,4] | [4,0] | 5/3/24 |
| 6. | Personaje, meta  | Por hacer | [0,2] | [4,6] | - |
| 7. | Personaje, caja, pasillo | Echo | [0,1,4] | [4,0,1] | 5/3/24 |
| 8. | Personaje, caja,  meta | Por hacer | [0,1,2] | [4,0,6] | - |
| 9. | Personaje, caja_meta, pasillo | Por hacer | [0,6,4] | [4,5,1] | - |
| 10. |Personaje, caja_meta, meta | Por hacer | [0,6,2] | [4,5,6] | - |
| 11. | Personaje_meta, pasillo | Por hacer | [5,4] | [2,0] | - |
| 12. | Personaje_meta, meta | Por hacer | [5,2] | [2,5] | - |
| 13. | Personaje_meta, caja, pasillo | Por hacer | [5,1,4] | [2,0,1] | - |
| 14. | Personaje_meta, caja, meta | Por hacer | [5,1,2] | [2,0,6] | - | 
| 15. | Personaje_meta, caja_meta, pasillo | Por hacer | [5,6,4] | [2,5,1] | - |
| 16. | Personaje_meta, caja_meta, meta | Por hacer | [5,6,2] | [2,5,6] | - |

## Izquierda

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 17. | Personaje y espacio | Echo | [4,0] | [0,4] | 5/3/24 |
| 18. | Personaje y meta | Por hacer | [2,0] | [6,4] | - |
| 19. | Personaje, caja y espacio | Por hacer | [4,1,0] | [1,0,4] | - |
| 20. | Personaje, caja y meta | Por hacer | [2,1,0] | [6,0,4] | - |
| 21. | Personaje, caja_meta y espacio | Por hacer | [4,6,0] | [1,5,4] | - |
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
| 30. | Personaje y meta | Por hacer | [] | [] | - | 
| 31. | Personaje, caja y espacio | Por hacer | [] | [] | - |
| 32. | Personaje, caja y meta | Por hacer | [] | [] | - |
| 33. | Personaje, caja_meta y espacio | Por hacer | [] | [] | - |
| 34. | Personaje, caja_meta y meta | Por hacer | [] | [] | - |
| 35. | Personaje_meta y espacio | Por hacer | [] | [] | - |
| 36. | Personaje_meta y meta | Por hacer | [] | [] | - |
| 37. | Personaje_meta, caja y espacio | Por hacer | [] | [] | - |
| 38. | Personaje_meta, caja y meta | Por hacer | [] | [] | - |
| 39. | Personaje_meta, caja_meta y espacio | Por hacer | [] | [] | - |
| 40. | Personaje_meta, caja_meta y meta | Por hacer | [] | [] | - |

## Abajo

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 41. | Personaje y espacio | Echo | [0,4] | [4,0] | 5/3/24 |
| 42. | Personaje y meta | Por hacer | [0,2] | [4,6] | - |
| 43. | Personaje, caja y espacio | Por hacer | [0,1,4] | [4,0,1] | - |
| 44. | Personaje, caja y meta | Por hacer | [0,1,2] | [4,0,6] | - |
| 45. | Personaje, caja_meta y espacio | Por hacer | [0,6,4] | [4,5,1] | - |
| 46. | Personaje, caja_meta y meta | Por hacer | [0,6,2] | [4,5,6] | - |
| 47. | Personaje_meta y espacio | Por hacer | [5,4] | [2,0] | - |
| 48. | Personaje_meta y meta | Por hacer | [5,2] | [2,5] | - |
| 49. | Personaje_meta, caja y espacio | Por hacer | [5,1,4] | [2,0,1] | - |
| 50. | Personaje_meta, caja y meta | Por hacer | [5,1,2] | [2,0,6] | - |
| 51. | Personaje_meta, caja_meta y espacio | Por hacer | [5,6,4] | [2,5,1] | - |
| 52. | Personaje_meta, caja_meta y meta | Por hacer | [] | [] | - |

## Determina si se completo el nivel o no

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 53. | Evaluar si el nivel esta terminado.  | Por hacer | - |
| 54. | Si el nivel esta terminado cargar el siguiente nivel.  | Por hacer | - |

## Función extra

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 55. | Función adicional o powerup (descripción). | Por hacer | - |






