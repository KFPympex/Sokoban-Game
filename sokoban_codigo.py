#define el mapa
mapa = [3, 4, 4, 0, 4, 4, 3]
posicion_columna = 3

while True:
#imprime el mapa
    print(mapa)
#pide al usuario el movimiento
    movimiento = (input("Ingresa un movimiento entre a s d w: "))
#elementos
    if movimiento == "d":
        if mapa[posicion_columna] == 0 and mapa[posicion_columna + 1] == 4:
            mapa[posicion_columna] = 4  
            mapa[posicion_columna +1] = 0
            posicion_columna += 1

    if movimiento == "a":
        if mapa[posicion_columna] == 0 and mapa[posicion_columna - 1] == 4:
            mapa[posicion_columna] = 4
            mapa[posicion_columna -1] = 0
            posicion_columna -= 1
