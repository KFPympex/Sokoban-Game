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
| 2. | Imprimir mapa.| Hecho | - | - | 29/2/24 |
| 3. | Leer el movimiento. | Por hacer | - | - | - |
| 4. | Evaluar el movimiento del usuario. | Por hacer | - | - | - |

## Derecha

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, espacio  | Hecho | [0,4] | [4,0] | 5/3/24 |
| 6. | Personaje, meta  | Hecho | [0,2] | [4,5] | 6/3/24 |
| 7. | Personaje, caja, espacio | Hecho | [0,1,4] | [4,0,1] | 7/3/24 |
| 8. | Personaje, caja,  meta | Hecho | [0,1,2] | [4,0,6] | 7/3/24 |
| 9. | Personaje, caja_meta, espacio | Hecho | [0,6,4] | [4,5,1] | 7/3/24 |
| 10. |Personaje, caja_meta, meta | Hecho | [0,6,2] | [4,5,6] | 7/3/24 |
| 11. | Personaje_meta, espacio | Hecho | [5,4] | [2,0] | 7/3/24 |
| 12. | Personaje_meta, meta | Hecho | [5,2] | [2,5] | 7/3/24 |
| 13. | Personaje_meta, caja, espacio | Hecho | [5,1,4] | [2,0,1] | 7/3/24 |
| 14. | Personaje_meta, caja, meta | Hecho | [5,1,2] | [2,0,6] | 6/3/24 | 
| 15. | Personaje_meta, caja_meta, espacio | Hecho | [5,6,4] | [2,5,1] | 7/3/24 |
| 16. | Personaje_meta, caja_meta, meta | Hecho | [5,6,2] | [2,5,6] | 7/3/24 |

## Izquierda

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 17. | Personaje y espacio | Hecho | [4,0] | [0,4] | 5/3/24 |
| 18. | Personaje y meta | Hecho | [2,0] | [5,4] | 6/3/24 |
| 19. | Personaje, caja y espacio | Hecho | [4,1,0] | [1,0,4] | 7/3/24 |
| 20. | Personaje, caja y meta | Hecho | [2,1,0] | [6,0,4] | 7/3/24 |
| 21. | Personaje, caja_meta y espacio | Hecho | [4,6,0] | [1,5,4] | 7/3/24 |
| 22. | Personaje, caja_meta y meta | Hecho | [2,6,0] | [6,5,4] | 7/3/24 |
| 23. | Personaje_meta y espacio | Hecho | [4,5] | [0,2] | 7/3/24 |
| 24. | Personaje_meta y meta | Hecho | [2,5] | [5,2] | 7/3/24 |
| 25. | Personaje_meta, caja y espacio | Hecho | [4,1,5] | [1,0,2] | 7/3/24 |
| 26. | Personaje_meta, caja y meta | Hecho | [2,1,5] | [6,0,2] | 7/3/24 |
| 27. | Personaje_meta, caja_meta y espacio | Hecho | [4,6,5] | [1,5,2] | 7/3/24 |
| 28. | Personaje_meta, caja_meta y meta | Hecho | [2,6,5] | [6,5,2] | 7/3/24 |

## Arriba

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 29. | Personaje y espacio | Hecho | [4,0] | [0,4] | 5/3/24 |
| 30. | Personaje y meta | Hecho | [2,0] | [5,4] | 6/3/24 | 
| 31. | Personaje, caja y espacio | Hecho | [4,1,0] | [1,0,4] | 7/3/24 |
| 32. | Personaje, caja y meta | Hecho | [2,1,0] | [6,0,4] | 7/3/24 |
| 33. | Personaje, caja_meta y espacio | Hecho | [4,6,0] | [1,5,4] | 7/3/24 |
| 34. | Personaje, caja_meta y meta | Hecho | [2,6,0] | [6,5,4] | 7/3/24 |
| 35. | Personaje_meta y espacio | Hecho | [4,5] | [0,2] | 7/3/24 |
| 36. | Personaje_meta y meta | Hecho | [2,5] | [5,2] | 7/3/24 |
| 37. | Personaje_meta, caja y espacio | Hecho | [4,1,5] | [1,0,2] | 7/3/24 |
| 38. | Personaje_meta, caja y meta | Hecho | [2,1,5] | [6,0,2] | 7/3/24 |
| 39. | Personaje_meta, caja_meta y espacio | Hecho | [4,6,5] | [1,5,2] | 7/3/24 |
| 40. | Personaje_meta, caja_meta y meta | Hecho | [2,6,5] | [6,5,2] | 7/3/24 |

## Abajo

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 41. | Personaje y espacio | Hecho | [0,4] | [4,0] | 5/3/24 |
| 42. | Personaje y meta | Hecho | [0,2] | [4,5] | 6/3/24 |
| 43. | Personaje, caja y espacio | Hecho | [0,1,4] | [4,0,1] | 7/3/24 |
| 44. | Personaje, caja y meta | Hecho | [0,1,2] | [4,0,6] | 7/3/24 |
| 45. | Personaje, caja_meta y espacio | Hecho | [0,6,4] | [4,5,1] | 7/3/24 |
| 46. | Personaje, caja_meta y meta | Hecho | [0,6,2] | [4,5,6] | 7/3/24 |
| 47. | Personaje_meta y espacio | Hecho | [5,4] | [2,0] | 7/3/24 |
| 48. | Personaje_meta y meta | Hecho | [5,2] | [2,5] | 7/3/24 |
| 49. | Personaje_meta, caja y espacio | Hecho | [5,1,4] | [2,0,1] | 7/3/24 |
| 50. | Personaje_meta, caja y meta | Hecho | [5,1,2] | [2,0,6] | 7/3/24 |
| 51. | Personaje_meta, caja_meta y espacio | Hecho | [5,6,4] | [2,5,1] | 7/3/24 |
| 52. | Personaje_meta, caja_meta y meta | Hecho | [5,6,2] | [2,5,6] | 7/3/24 |

## Determina si se completo el nivel o no

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 53. | Evaluar si el nivel esta terminado.  | Por hacer | - | - | - |
| 54. | Si el nivel esta terminado cargar el siguiente nivel.  | Por hacer | - | - | - |




## Función extra

| No. | Función | Kanban |  Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 55-106. | Función adicional o powerup (El personaje puede empujar 2 cajas). | Por hacer | - | - | - |

## Funcion extra derecha

| No. | Función | Kanban |  Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 55. | Personaje, caja, caja y espacio | Hecho | [0,1,1,4] | [4,0,1,1] | 20/3/24 |
| 56. | Personaje, caja, caja_meta y espacio | Hecho | [0,1,6,4] | [4,0,6,1] | 20/3/24 |
| 57. | Personaje, caja, caja y meta | Hecho | [0,1,1,2] | [4,0,1,6] | 20/3/24 |
| 58. | Personaje, caja_meta, caja y meta | Hecho | [0,6,1,2] | [4,5,1,6] | 20/3/24 |
| 59. | Personaje, caja, caja_meta y meta | Hecho | [0,1,6,2] | [4,0,6,6] | 20/3/24 |
| 60. | Personaje, caja_meta, caja_meta y espacio | Hecho | [0,6,6,4] | [4,5,6,1] | 20/3/24 |
| 61. | Personaje_meta, caja_meta, caja y espacio | Hecho | [5,6,1,4] | [2,5,1,1] | 20/3/24 |
| 62. | Personaje_meta, caja, caja y espacio | Hecho | [5,1,1,4] | [2,0,1,1] | 20/3/24 |
| 63. | Personaje_meta, caja, caja_meta y espacio | Hecho | [5,1,6,4] | [2,0,6,1] | 20/3/24 |
| 64. | Personaje, caja_meta, caja y espacio | Hecho | [0,6,1,4] | [4,5,1,1] | 20/3/24 |
| 65. | Personaje, caja_meta, caja_meta y meta | Hecho | [0,6,6,2] | [4,5,6,6] | 20/3/24 |
| 66. | Personaje_meta, caja_meta, caja_meta y espacio | Hecho | [5,6,6,4] | [2,5,6,1] | 20/3/24 |
| 67. | Personaje_meta, caja_meta, caja, espacio | Hecho | [5,6,1,4] | [2,5,1,1] | 20/3/24 |

## Funcion extra izquierda

| No. | Función | Kanban |  Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 68. | Personaje, caja, caja y espacio | Hecho | [4,1,1,0] | [1,1,0,4] | 20/3/24 |
| 69. | Personaje, caja, caja_meta y espacio | Hecho | [4,6,1,0] | [1,6,0,4] | 20/3/24 |
| 70. | Personaje, caja, caja y meta | Hecho | [2,1,1,0] | [6,1,0,4] | 20/3/24 |
| 71. | Personaje, caja_meta, caja y meta | Hecho | [2,1,6,0] | [6,1,5,4] | 20/3/24 |
| 72. | Personaje, caja, caja_meta y meta | Hecho | [2,6,1,0] | [6,6,0,4] | 20/3/24 |
| 73. | Personaje, caja_meta, caja_meta y espacio | Hecho | [4,6,6,0] | [1,6,5,4] | 20/3/24 |
| 74. | Personaje_meta, caja_meta, caja y espacio | Hecho | [4,1,6,5] | [1,1,5,2] | 20/3/24 |
| 75. | Personaje_meta, caja, caja y espacio | Hecho | [4,1,1,5] | [1,1,0,2] | 20/3/24 |
| 76. | Personaje_meta, caja, caja_meta y espacio | Hecho | [4,6,1,5] | [1,6,0,2] | 20/3/24 |
| 77. | Personaje, caja_meta, caja y espacio | Hecho | [4,1,6,0] | [1,1,5,4] | 20/3/24 |
| 78. | Personaje, caja_meta, caja_meta y meta | Hecho | [2,6,6,0] | [6,6,5,4] | 20/3/24 |
| 79. | Personaje_meta, caja_meta, caja_meta y espacio | Hecho | [4,6,6,5] | [1,6,5,2] | 20/3/24 |
| 80. | Personaje_meta, caja_meta, caja, espacio | Hecho | [4,1,6,5] | [1,1,5,2] | 20/3/24 |

## Funcion extra arriba

| No. | Función | Kanban |  Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 81. | Personaje, caja, caja y espacio | Hecho | [4,1,1,0] | [1,1,0,4] | - |
| 82. | Personaje, caja, caja_meta y espacio | Hecho | [4,6,1,0] | [1,6,0,4] | - |
| 83. | Personaje, caja, caja y meta | Hecho | [2,1,1,0] | [6,1,0,4] | - |
| 84. | Personaje, caja_meta, caja y meta | Hecho | [2,1,6,0] | [6,1,5,4] | - |
| 85. | Personaje, caja, caja_meta y meta | Hecho | [2,6,1,0] | [6,6,0,4] | - |
| 86. | Personaje, caja_meta, caja_meta y espacio | Hecho | [4,6,6,0] | [1,6,5,4] | - |
| 87. | Personaje_meta, caja_meta, caja y espacio | Hecho | [4,1,6,5] | [1,1,5,2] | - |
| 88. | Personaje_meta, caja, caja y espacio | Hecho | [4,1,1,5] | [1,1,0,2] | - |
| 89. | Personaje_meta, caja, caja_meta y espacio | Hecho | [4,6,1,5] | [1,6,0,2] | - |
| 90. | Personaje, caja_meta, caja y espacio | Hecho | [4,1,6,0] | [1,1,5,4] | - |
| 91. | Personaje, caja_meta, caja_meta y meta | Hecho | [2,6,6,0] | [6,6,5,4] | - |
| 92. | Personaje_meta, caja_meta, caja_meta y espacio | Hecho | [4,6,6,5] | [1,6,5,2] | - |
| 93. | Personaje_meta, caja_meta, caja, espacio | Hecho | [4,1,6,5] | [1,1,5,2] | - |

## Funcion extra abajo

| No. | Función | Kanban |  Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 94. | Personaje, caja, caja y espacio | Hecho | [0,1,1,4] | [4,0,1,1] | - |
| 95. | Personaje, caja, caja_meta y espacio | Hecho | [0,1,6,4] | [4,0,6,1] | - |
| 96. | Personaje, caja, caja y meta | Hecho | [0,1,1,2] | [4,0,1,6] | - |
| 97. | Personaje, caja_meta, caja y meta | Hecho | [0,6,1,2] | [4,5,1,6] | - |
| 98. | Personaje, caja, caja_meta y meta | Hecho | [0,1,6,2] | [4,0,6,6] | - |
| 99. | Personaje, caja_meta, caja_meta y espacio | Hecho | [0,6,6,4] | [4,5,6,1] | - |
| 100. | Personaje_meta, caja_meta, caja y espacio | Hecho | [5,6,1,4] | [2,5,1,1] | - |
| 101. | Personaje_meta, caja, caja y espacio | Hecho | [5,1,1,4] | [2,0,1,1] | - |
| 102. | Personaje_meta, caja, caja_meta y espacio | Hecho | [5,1,6,4] | [2,0,6,1] | - |
| 103. | Personaje, caja_meta, caja y espacio | Hecho | [0,6,1,4] | [4,5,1,1] | - |
| 104. | Personaje, caja_meta, caja_meta y meta | Hecho | [0,6,6,2] | [4,5,6,6] | - |
| 105. | Personaje_meta, caja_meta, caja_meta y espacio | Hecho | [5,6,6,4] | [2,5,6,1] | - |
| 106. | Personaje_meta, caja_meta, caja, espacio | Hecho | [5,6,1,4] | [2,5,1,1] | - |







