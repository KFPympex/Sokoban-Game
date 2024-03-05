class Soko:

    mapa = [] # mapa del juego
    personaje_columna = 0
    personaje_fila = 0

    def __init__(self):
        # Define el mapa de juego
        self.mapa =[
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,0,1,4,4,4,2,4,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        ]

        # Definimos la posicion inicial del personaje
        self.personaje_columna = 6
        self.personaje_fila = 3

    def imprimirMapa(self):
        for filas in self.mapa:
            print(filas)

## Mover derecha
            
    # Movimiento 5: [0,4] -> [4,0]
    def movimiento5(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.personaje_columna+=1

    # Movimiento 6: [0,2] -> [4,6]
    def movimiento6(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
        self.personaje_columna+=1
    
    # Movimiento 7: [0,1,4] -> [4,0,1]
    def movimiento7(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.personaje_columna+=1





    def derecha(self):
        # Movimiento 5: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.movimiento5()

        # Movimiento 6: [0,2] -> [4,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            self.movimiento6()

        # Movimiento 7: [0,1,4] -> [4,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4: 
             self.movimiento7()
                







## Mover izquerda
             
    def movimiento17(self):
        self.mapa[self.personaje_fila][self.personaje_columna -1 ] = 0
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.personaje_columna-=1
    
    def izquierda(self):
        # Movimiento 17: [4,0] -> [0,4]
        if self.mapa[self.personaje_fila][self.personaje_columna -1] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
           self.movimiento17()    

        # Movimiento 19: [4,2,0] -> [2,0,4]
                


## Moverse arriba
           
    def movimiento29(self):
        self.mapa[self.personaje_fila -1][self.personaje_columna ] = 0
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.personaje_fila-=1    

    def arriba(self):
        # Movimiento 29: [4,0] -> [0,4]
        if self.mapa[self.personaje_fila -1][self.personaje_columna ] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
           self.movimiento29()        

## Moverse abajo
    
    def movimiento41(self):
        self.mapa[self.personaje_fila +1][self.personaje_columna ] = 0
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.personaje_fila+=1  

    def abajo(self):
        # Movimiento 2: [4,0] -> [0,4]
        if self.mapa[self.personaje_fila +1][self.personaje_columna ] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
           self.movimiento41()         


    def jugar(self):
        while True:
            # Imprime el mapa
            self.imprimirMapa()
            # Pide al usuario el movimiento
            movimiento = input("Selecciona el movimiento: ")
            # Moverse a la derecha
            if movimiento == 'd':
                self.derecha()
            if movimiento == 'a':
                self.izquierda()
            if movimiento == 'w':
                self.arriba()
            if movimiento == 's':
                self.abajo()
            

soko = Soko()
soko.jugar()

