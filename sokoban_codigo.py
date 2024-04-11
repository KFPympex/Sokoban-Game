import copy
class Soko:

    def __init__(self, nivel=0):
        
        self.movimientos = 0

        self.niveles = [
            [  # Nivel 0
                [4,4,4,4,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4],
                [4,4,4,4,3,4,4,4,3,4,4,4,4,4,4,4,4,4,4],
                [4,4,4,4,3,1,4,4,3,4,4,4,4,4,4,4,4,4,4],
                [4,4,3,3,3,4,4,1,3,3,4,4,4,4,4,4,4,4,4],
                [4,4,3,4,4,1,4,1,4,3,4,4,4,4,4,4,4,4,4],
                [3,3,3,4,3,4,3,3,4,3,4,4,4,3,3,3,3,3,3],
                [3,4,4,4,3,4,3,3,4,3,3,3,3,3,4,4,2,2,3],
                [3,4,1,4,4,1,4,4,4,4,4,4,4,4,4,4,2,2,3],
                [3,3,3,3,3,4,3,3,3,4,3,0,3,3,4,4,2,2,3],
                [4,4,4,4,3,4,4,4,4,4,3,3,3,3,3,3,3,3,3],
                [4,4,4,4,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4]

            ],
            [  # Nivel 1
                [3,3,3,3,3,3,3],
                [3,4,1,4,2,2,3],
                [3,4,1,4,3,2,3],
                [3,4,3,4,1,4,3],
                [3,0,4,4,4,4,3],
                [3,3,3,3,3,3,3]
            ],
            [  # Nivel 2
                [3,3,3,3,3,3,3,3,3],
                [3,4,4,4,3,4,4,4,3],
                [3,4,1,0,4,1,2,4,3],
                [3,4,4,3,2,3,4,4,3],
                [3,3,3,4,1,4,4,4,3],
                [3,4,2,4,4,4,3,3,3],
                [3,4,4,4,3,4,4,4,3],
                [3,3,3,3,3,3,3,3,3]
            
            ],
            [  # Nivel 3
                [3,3,3,3,3,3,3,3,3,3,3,3,3],
                [3,4,4,4,4,4,4,4,4,4,4,4,3],
                [3,4,4,4,4,4,4,4,4,1,4,4,3],
                [3,4,4,4,4,4,4,4,4,4,4,4,3],
                [3,4,4,4,1,4,4,4,2,2,4,4,3],
                [3,4,4,1,4,4,4,4,2,2,4,4,3],
                [3,4,0,4,4,1,4,4,4,4,4,4,3],
                [3,4,4,4,4,4,4,4,4,4,4,4,3],
                [3,3,3,3,3,3,3,3,3,3,3,3,3]
            ],
            [  # Nivel 4
                [3,3,3,3,3,3,3,3,3,3,3],
                [3,4,4,4,4,0,4,4,4,4,3],
                [3,4,1,4,3,3,3,4,1,4,3],
                [3,4,4,4,3,2,3,4,4,4,3],
                [3,3,4,4,4,2,4,4,4,3,3],
                [3,4,4,4,4,2,3,4,4,4,3],
                [3,4,1,4,3,3,3,4,4,4,3],
                [3,4,4,4,4,4,4,4,4,4,3],
                [3,3,3,3,3,3,3,3,3,3,3]
            ],
            [  # Nivel 5
                [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
                [3,4,4,4,4,3,4,4,4,4,4,4,4,4,3],
                [3,4,1,3,4,3,0,3,4,3,1,4,3,4,3],
                [3,4,4,3,4,4,4,4,4,3,4,4,3,4,3],
                [3,3,4,3,3,3,2,3,3,3,4,3,3,4,3],
                [3,4,4,4,4,4,2,4,4,4,4,4,4,4,3],
                [3,4,1,3,4,4,2,3,4,3,4,4,3,4,3],
                [3,4,4,4,4,4,4,4,4,4,4,4,4,4,3],
                [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
            ]

        ]
        self.cargar_nivel(nivel)
    
    

    def cargar_nivel(self, nivel):
        self.mapa = copy.deepcopy(self.niveles[nivel])  # Usa deepcopy para crear una copia del nivel
        self.nivel_actual = nivel
        # Inicializar los contadores para cajas y metas
        conteo_cajas = 0
        conteo_metas = 0
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[fila])):
                if self.mapa[fila][columna] == 0:
                    self.personaje_fila = fila
                    self.personaje_columna = columna
                elif self.mapa[fila][columna] == 1:
                    conteo_cajas += 1
                elif self.mapa[fila][columna] == 2:
                    conteo_metas += 1
    # Verificar si el número de cajas es igual al número de metas
        if conteo_cajas != conteo_metas:
        # Lanzar una excepción si no coinciden
            raise ValueError(f"Error en el nivel {nivel}: número de cajas ({conteo_cajas}) y metas ({conteo_metas}) no coincide.")

    def nivel_completado(self):
        for fila in self.mapa:
            if 1 in fila:  # Si hay alguna caja que no esté en una meta
                return False
        return True

    def imprimirMapa(self):

        print(f"Movimientos: {self.movimientos}")

        representacion = {
        0: "🧍",  # Personaje
        1: "📦",  # Caja
        2: "🏁",  # Meta
        3: "🧱",  # Pared
        4: "  ",  # Espacio en blanco
        5: "🕺",  # Personaje en la meta 
        6: "🎁",  # Caja en la meta 
    }
        for fila in self.mapa:
            for celda in fila:
                print(representacion.get(celda, " "), end=" ")
            print()
    

    def mover(self, df, dc):
        # Mover el personaje. 
        nueva_fila = self.personaje_fila + df
        nueva_columna = self.personaje_columna + dc
        if self.mapa[nueva_fila][nueva_columna] in [4, 2]:  # Mover a piso o meta
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  # Dejar el piso donde estaba el personaje
            self.personaje_fila = nueva_fila
            self.personaje_columna = nueva_columna
            self.mapa[nueva_fila][nueva_columna] = 0  # Colocar al personaje en la nueva posición


    
## Mover derecha
            
    # Movimiento 5: [0,4] -> [4,0]
    def movimiento5(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.personaje_columna+=1

    # Movimiento 6: [0,2] -> [4,5]
    def movimiento6(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.personaje_columna+=1
    
    # Movimiento 7: [0,1,4] -> [4,0,1]
    def movimiento7(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.personaje_columna+=1

    # Movimiento 8: [0,1,2] -> [4,0,6]
    def movimiento8(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.personaje_columna+=1    

    # Movimiento 9: [0,6,4] -> [4,5,1]
    def movimiento9(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.personaje_columna+=1
        
    # Movimiento 10: [0,6,2] -> [4,5,6]
    def movimiento10(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.personaje_columna+=1    

    # Movimiento 11: [5,4] -> [2,0]
    def movimiento11(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.personaje_columna+=1

    # Movimiento 12: [5,2] -> [2,5]
    def movimiento12(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.personaje_columna+=1
        
    # Movimiento 13: [5,1,4] -> [2,0,1]
    def movimiento13(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.personaje_columna+=1
        
    # Movimiento 14: [5,1,2] -> [2,0,6]
    def movimiento14(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.personaje_columna+=1
        
    # Movimiento 15: [5,6,4] -> [2,5,1]
    def movimiento15(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.personaje_columna+=1
        
    # Movimiento 16: [5,6,2] -> [2,5,6]
    def movimiento16(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.personaje_columna+=1

    
    
    ################ MOVIMIENTOS EXTRA DERECHA

    # movimiento extra derecha 55: [0,1,1,4] -> [4,0,1,1]
    def movimiento55(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 1
        self.personaje_columna+=1   

    # movimiento extra derecha 56 [0,1,6,4] -> [4,0,6,1]
    def movimiento56(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 1
        self.personaje_columna+=1    

    # movimiento extra derecha 57 [0,1,1,2] -> [4,0,1,6]
    def movimiento57(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 6
        self.personaje_columna+=1      
        
    # movimiento extra derecha 58 [0,6,1,2] -> [4,5,1,6]
    def movimiento58(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 6
        self.personaje_columna+=1    
    
    # movimiento extra derecha 59 [0,1,6,2] -> [4,0,6,6]
    def movimiento59(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 6
        self.personaje_columna+=1

    # movimiento extra derecha 60 [0,6,6,4] -> [4,5,6,1]
    def movimiento60(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 1
        self.personaje_columna+=1
    
    # movimiento extra derecha 61 [5,6,1,4] -> [2,5,1,1]
    def movimiento61(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 1
        self.personaje_columna+=1   

    # movimiento extra derecha 62 [5,1,1,4] -> [2,0,1,1]
    def movimiento62(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 1
        self.personaje_columna+=1
    
    # movimiento extra derecha 63 [5,1,6,4] -> [2,0,6,1]
    def movimiento63(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 1
        self.personaje_columna+=1

    # movimiento extra derecha 64 [0,6,1,4] -> [4,5,1,1]   
    def movimiento64(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 1
        self.personaje_columna+=1
    
    # movimiento extra derecha 65 [0,6,6,2] -> [4,5,6,6]
    def movimiento65(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 6
        self.personaje_columna+=1
    
    # movimiento extra derecha 66 [5,6,6,4] -> [2,5,6,1]
    def movimiento66(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 1
        self.personaje_columna+=1

    # movimiento extra derecha 67 [5,6,1,4] -> [2,5,1,1]
    def movimiento67(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna + 3] = 1
        self.personaje_columna+=1


    
    def derecha(self):

        self.movimientos += 1  # Incrementa el contador aquí

        nueva_fila = self.personaje_fila
        nueva_columna = self.personaje_columna + 1  # Mover a la derecha incrementa la columna
        print(f"Moviendo a: [{nueva_fila}, {nueva_columna}]")

        # Movimiento 5: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.movimiento5()

        # Movimiento 6: [0,2] -> [4,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            self.movimiento6()

        # Movimiento 7: [0,1,4] -> [4,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4: 
             self.movimiento7()
                
        # Movimiento 8: [0,1,2] -> [4,0,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2: 
             self.movimiento8()

        # Movimiento 9: [0,6,4] -> [4,5,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4: 
             self.movimiento9()
        
        # Movimiento 10: [0,6,2] -> [4,5,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2: 
             self.movimiento10()
        
        # Movimiento 11: [5,4] -> [2,0]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.movimiento11()     
        
        # Movimiento 12: [5,2] -> [2,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            self.movimiento12()
        
        # Movimiento 13: [5,1,4] -> [2,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4: 
             self.movimiento13()    
        
        # Movimiento 14: [5,1,2] -> [2,0,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2: 
             self.movimiento14()
        
        # Movimiento 15: [5,6,4] -> [2,5,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4: 
             self.movimiento15()
        
        # Movimiento 16: [5,6,2] -> [2,5,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2: 
             self.movimiento16()
        

        ################ MOVIMIENTOS EXTRA DERECHA
  
        # movimiento extra derecha 55: [0,1,1,4] -> [4,0,1,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 4:
             self.movimiento55()
             
        # movimiento extra 56 derecha [0,1,6,4] -> [4,0,6,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 4:
             self.movimiento56()

        # movimiento extra 57 derecha [0,1,1,2] -> [4,0,1,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 2:
             self.movimiento57()
    
        # movimiento extra 58 derecha [0,6,1,2] -> [4,5,1,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 2:
             self.movimiento58()

        # movimiento extra 59 derecha [0,1,6,2] -> [4,0,6,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 2:
             self.movimiento59()    
             
        # movimiento extra 60 derecha [0,6,6,4] -> [4,5,6,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 4:
             self.movimiento60()
        
        # movimiento extra 61 derecha [5,6,1,4] -> [2,5,1,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 4:
             self.movimiento61()

        # movimiento extra derecha 62 [5,1,1,4] -> [2,0,1,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 4:
             self.movimiento62()

        # movimiento extra derecha 63 [5,1,6,4] -> [2,0,6,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 4:
             self.movimiento63()
    
        # movimiento extra derecha 64 [0,6,1,4] -> [4,5,1,1]   
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 4:
             self.movimiento64()
            
        # movimiento extra derecha 65 [0,6,6,2] -> [4,5,6,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 2:
             self.movimiento65()

        # movimiento extra derecha 66 [5,6,6,4] -> [2,5,6,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 4:
             self.movimiento66()

        # movimiento extra derecha 67 [5,6,1,4] -> [2,5,1,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 4:
             self.movimiento67()



###########################################################################################################################


## Mover izquerda
             
    # Movimiento 17: [4,0] -> [0,4]         
    def movimiento17(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.personaje_columna-=1
    
    # Movimiento 18: [2,0] -> [5,4]
    def movimiento18(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.personaje_columna-=1

    # Movimiento 19: [4,1,0] ->	[1,0,4]
    def movimiento19(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.personaje_columna-=1    

    # Movimiento 20: [2,1,0] ->	[6,0,4]
    def movimiento20(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.personaje_columna-=1     

    # Movimiento 21: [4,6,0] ->	[1,5,4]
    def movimiento21(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.personaje_columna-=1    

    # Movimiento 22: [2,6,0] ->	[6,5,4]	
    def movimiento22(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.personaje_columna-=1     

    # Movimiento 23: [4,5] -> [0,2]
    def movimiento23(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.personaje_columna-=1    

    # Movimiento 24: [2,5] -> [5,2]
    def movimiento24(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.personaje_columna-=1    

    # Movimiento 25: [4,1,5] ->	[1,0,2]	
    def movimiento25(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.personaje_columna-=1    

    # Movimiento 26: [2,1,5] ->	[6,0,2]	
    def movimiento26(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.personaje_columna-=1
            
    # Movimiento 27: [4,6,5] ->	[1,5,2]	
    def movimiento27(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.personaje_columna-=1    

    # Movimiento 28: [2,6,5] ->	[6,5,2]
    def movimiento28(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.personaje_columna-=1

    ########################## MOVIMIENTO EXTRA IZQUIERDA
    
    # Movimiento extra izquierda 68: [4,1,1,0] -> [1,1,0,4]
    def movimiento68(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 1
        self.personaje_columna-=1
    
    # Movimiento extra izquierda 69: [4,6,1,0] -> [1,6,0,4]
    def movimiento69(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 1
        self.personaje_columna-=1
        
    # Movimiento extra izquierda 70: [2,1,1,0] -> [6,1,0,4]
    def movimiento70(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 6
        self.personaje_columna-=1
        
    # Movimiento extra izquierda 71: [2,1,6,0] -> [6,1,5,4]
    def movimiento71(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 6
        self.personaje_columna-=1
        
    # Movimiento extra izquierda 72: [2,6,1,0] -> [6,6,0,4]
    def movimiento72(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 6
        self.personaje_columna-=1
    
        
    # Movimiento extra izquierda 73: [4,6,6,0] -> [1,6,5,4]
    def movimiento73(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 1
        self.personaje_columna-=1
        
    # Movimiento extra izquierda 74: [4,1,6,5] -> [1,1,5,2]
    def movimiento74(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 1
        self.personaje_columna-=1
        
    # Movimiento extra izquierda 75: [4,1,1,5] -> [1,1,0,2]
    def movimiento75(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 1
        self.personaje_columna-=1
    
    # Movimiento extra izquierda 76: [4,6,1,5] -> [1,6,0,2]
    def movimiento76(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 1
        self.personaje_columna-=1
    
    # Movimiento extra izquierda 77: [4,1,6,0] -> [1,1,5,4]
    def movimiento77(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 1
        self.personaje_columna-=1
        
    # Movimiento extra izquierda 78: [2,6,6,0] -> [6,6,5,4]
    def movimiento78(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 6
        self.personaje_columna-=1
    
    # Movimiento extra izquierda 79: [4,6,6,5] -> [1,6,5,2]
    def movimiento79(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 1
        self.personaje_columna-=1
    
    # Movimiento extra izquierda 80: [4,1,6,5] -> [1,1,5,2]
    def movimiento80(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.mapa[self.personaje_fila][self.personaje_columna - 3] = 1
        self.personaje_columna-=1


    

    def izquierda(self):

        self.movimientos += 1  # Incrementa el contador aquí

        nueva_fila = self.personaje_fila
        nueva_columna = self.personaje_columna - 1  # Mover a la izquierda disminuye la columna
        print(f"Moviendo a: [{nueva_fila}, {nueva_columna}]")

        # Movimiento 17: [4,0] -> [0,4]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
            self.movimiento17() 

        # Movimiento 18: [2,0]	[5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
            self.movimiento18()

        # Movimiento 19: [4,1,0] ->	[1,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4: 
             self.movimiento19()

        # Movimiento 20: [2,1,0] ->	[6,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2: 
             self.movimiento20()

        # Movimiento 21: [4,6,0] ->	[1,5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4: 
             self.movimiento21()

        # Movimiento 22: [2,6,0] ->	[6,5,4]	
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2: 
             self.movimiento22()

        # Movimiento 23: [4,5] -> [0,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
            self.movimiento23() 

        # Movimiento 24: [2,5] -> [5,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
            self.movimiento24()

        # Movimiento 25: [4,1,5] ->	[1,0,2]	
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4: 
             self.movimiento25()

        # Movimiento 26: [2,1,5] ->	[6,0,2]	
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2: 
             self.movimiento26()

        # Movimiento 27: [4,6,5] ->	[1,5,2]	
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4: 
             self.movimiento27()

        # Movimiento 28: [2,6,5] ->	[6,5,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2: 
             self.movimiento28()  


        ########################## MOVIMIENTO EXTRA IZQUIERDA
    
        # Movimiento extra izquierda 68: [4,1,1,0] -> [1,1,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 4:
             self.movimiento68()

        # Movimiento extra izquierda 69: [4,6,1,0] -> [1,6,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 4:
             self.movimiento69()

        # Movimiento extra izquierda 70: [2,1,1,0] -> [6,1,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 2:
             self.movimiento70()

        # Movimiento extra izquierda 71: [2,1,6,0] -> [6,1,5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 2:
             self.movimiento71()

        # Movimiento extra izquierda 72: [2,6,1,0] -> [6,6,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 2:
             self.movimiento72()

        # Movimiento extra izquierda 73: [4,6,6,0] -> [1,6,5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 4:
             self.movimiento73()

        # Movimiento extra izquierda 74: [4,1,6,5] -> [1,1,5,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 4:
             self.movimiento74()

        # Movimiento extra izquierda 75: [4,1,1,5] -> [1,1,0,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 4:
             self.movimiento75()

        # Movimiento extra izquierda 76: [4,6,1,5] -> [1,6,0,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 4:
             self.movimiento76()

        # Movimiento extra izquierda 77: [4,1,6,0] -> [1,1,5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 4:
             self.movimiento77()

        # Movimiento extra izquierda 78: [2,6,6,0] -> [6,6,5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 2:
             self.movimiento78()

        # Movimiento extra izquierda 79: [4,6,6,5] -> [1,6,5,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 4:
             self.movimiento79()

        # Movimiento extra izquierda 80: [4,1,6,5] -> [1,1,5,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 3] == 4:
             self.movimiento80()
 





###########################################################################################################################


## Moverse arriba
            
    # Movimiento 29: [4,0] -> [0,4]     
    def movimiento29(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.personaje_fila-=1  

    # Movimiento 30: [2,0] ->[5,4]
    def movimiento30(self):
        self.mapa[self.personaje_fila][self.personaje_columna ] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.personaje_fila-=1     
        
    # Movimiento 31: [4,1,0] ->	[1,0,4]
    def movimiento31(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.personaje_fila-=1    
        
    # Movimiento 32: [2,1,0] ->	[6,0,4]
    def movimiento32(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.personaje_fila-=1    
        
    # Movimiento 33: [4,6,0] ->	[1,5,4]
    def movimiento33(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.personaje_fila-=1    
        
    # Movimiento 34: [2,6,0] ->	[6,5,4]
    def movimiento34(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.personaje_fila-=1     
        
    # Movimiento 35: [4,5] -> [0,2]
    def movimiento35(self):
        self.mapa[self.personaje_fila][self.personaje_columna ] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.personaje_fila-=1     
        
    # Movimiento 36: [2,5] -> [5,2]
    def movimiento36(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.personaje_fila-=1      
        
    # Movimiento 37: [4,1,5] ->	[1,0,2]	
    def movimiento37(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.personaje_fila-=1    
        
    # Movimiento 38: [2,1,5] ->	[6,0,2]	
    def movimiento38(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.personaje_fila-=1    
        
    # Movimiento 39: [4,6,5] ->	[1,5,2]	
    def movimiento39(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.personaje_fila-=1     
        
    # Movimiento 40: [2,6,5] ->	[6,5,2]	
    def movimiento40(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.personaje_fila-=1


########################## MOVIMIENTO EXTRA ARRIBA
        
    # Movimiento extra arriba 81: [4,1,1,0] -> [1,1,0,4]
    def movimiento81(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 1
        self.personaje_fila-=1  

    # Movimiento extra arriba 82: [4,6,1,0] -> [1,6,0,4]
    def movimiento82(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 1
        self.personaje_fila-=1    

    # Movimiento extra arriba 83: [2,1,1,0] -> [6,1,0,4]
    def movimiento83(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 6
        self.personaje_fila-=1    

    # Movimiento extra arriba 84: [2,1,6,0] -> [6,1,5,4]
    def movimiento84(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 6
        self.personaje_fila-=1    

    # Movimiento extra arriba 85: [2,6,1,0] -> [6,6,0,4]
    def movimiento85(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 6
        self.personaje_fila-=1    

    # Movimiento extra arriba 86: [4,6,6,0] -> [1,6,5,4]
    def movimiento86(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 1
        self.personaje_fila-=1    

    # Movimiento extra arriba 87: [4,1,6,5] -> [1,1,5,2]
    def movimiento87(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 1
        self.personaje_fila-=1    

    # Movimiento extra arriba 88: [4,1,1,5] -> [1,1,0,2]
    def movimiento88(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 1
        self.personaje_fila-=1    

    # Movimiento extra arriba 89: [4,6,1,5] -> [1,6,0,2]
    def movimiento89(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 1
        self.personaje_fila-=1    
    
    # Movimiento extra arriba 90: [4,1,6,0] -> [1,1,5,4]
    def movimiento90(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 1
        self.personaje_fila-=1    

    # Movimiento extra arriba 91: [2,6,6,0] -> [6,6,5,4]
    def movimiento91(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 6
        self.personaje_fila-=1    

    # Movimiento extra arriba 92: [4,6,6,5] -> [1,6,5,2]
    def movimiento92(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 1
        self.personaje_fila-=1    

    # Movimiento extra arriba 93: [4,1,6,5] -> [1,1,5,2]
    def movimiento93(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila - 3][self.personaje_columna] = 1
        self.personaje_fila-=1




    def arriba(self):

        self.movimientos += 1  # Incrementa el contador aquí

        nueva_fila = self.personaje_fila - 1  # Mover hacia arriba disminuye la fila
        nueva_columna = self.personaje_columna
        print(f"Moviendo a: [{nueva_fila}, {nueva_columna}]")

        # Movimiento 29: [4,0] -> [0,4]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.movimiento29()        

        # Movimiento 30: [2,0] ->[5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
            self.movimiento30()   
        
        # Movimiento 31: [4,1,0] ->	[1,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4: 
             self.movimiento31()   
        
        # Movimiento 32: [2,1,0] ->	[6,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2: 
             self.movimiento32()   
        
        # Movimiento 33: [4,6,0] ->	[1,5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4: 
             self.movimiento33()   
        
        # Movimiento 34: [2,6,0] ->	[6,5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2: 
             self.movimiento34()   
        
        # Movimiento 35: [4,5] -> [0,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.movimiento35() 
  

        # Movimiento 36: [2,5] -> [5,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
            self.movimiento36()   
        
        # Movimiento 37: [4,1,5] ->	[1,0,2]	
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4: 
             self.movimiento37()   
        
        # Movimiento 38: [2,1,5] ->	[6,0,2]	
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2: 
             self.movimiento38()   
        
        # Movimiento 39: [4,6,5] ->	[1,5,2]	
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4: 
             self.movimiento39()   
        
        # Movimiento 40: [2,6,5] ->	[6,5,2]	
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2: 
             self.movimiento40()     



########################## MOVIMIENTO EXTRA ARRIBA
        
        # Movimiento extra arriba 81: [4,1,1,0] -> [1,1,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 4:
             self.movimiento81()


        # Movimiento extra arriba 82: [4,6,1,0] -> [1,6,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 4:
             self.movimiento82()

        # Movimiento extra arriba 83: [2,1,1,0] -> [6,1,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 2:
             self.movimiento83()

        # Movimiento extra arriba 84: [2,1,6,0] -> [6,1,5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 2:
             self.movimiento84()

        # Movimiento extra arriba 85: [2,6,1,0] -> [6,6,0,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 2:
             self.movimiento85()

        # Movimiento extra arriba 86: [4,6,6,0] -> [1,6,5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 4:
             self.movimiento86()

        # Movimiento extra arriba 87: [4,1,6,5] -> [1,1,5,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 4:
             self.movimiento87()

        # Movimiento extra arriba 88: [4,1,1,5] -> [1,1,0,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 4:
             self.movimiento88()

        # Movimiento extra arriba 89: [4,6,1,5] -> [1,6,0,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 4:
             self.movimiento89()
    
        # Movimiento extra arriba 90: [4,1,6,0] -> [1,1,5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 4:
             self.movimiento90()

        # Movimiento extra arriba 91: [2,6,6,0] -> [6,6,5,4]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 2:
             self.movimiento91()

        # Movimiento extra arriba 92: [4,6,6,5] -> [1,6,5,2]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 4:
             self.movimiento92()

        # Movimiento extra arriba 93: [4,1,6,5] -> [1,1,5,2]   
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 3][self.personaje_columna] == 4:
             self.movimiento93()

    


###########################################################################################################################


## Moverse abajo
    
    # Movimiento 41: [0,4] -> [4,0]
    def movimiento41(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.personaje_fila+=1  

    # Movimiento 42: [0,2] -> [4,5]
    def movimiento42(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.personaje_fila+=1         
    
    # Movimiento 43: [0,1,4] ->	[4,0,1]
    def movimiento43(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.personaje_fila+=1
    

    # Movimiento 44: [0,1,2] ->	[4,0,6]
    def movimiento44(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.personaje_fila+=1    
 
    # Movimiento 45: [0,6,4] ->	[4,5,1]	
    def movimiento45(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.personaje_fila+=1    

    # Movimiento 46: [0,6,2] ->	[4,5,6]
    def movimiento46(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.personaje_fila+=1     

    # Movimiento 47: [5,4] -> [2,0]
    def movimiento47(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.personaje_fila+=1 

    # Movimiento 48: [5,2] -> [2,5]
    def movimiento48(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.personaje_fila+=1    

    # Movimiento 49: [5,1,4] ->	[2,0,1]	
    def movimiento49(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.personaje_fila+=1    

    # Movimiento 50: [5,1,2] ->	[2,0,6]	
    def movimiento50(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.personaje_fila+=1     

    # Movimiento 51: [5,6,4] ->	[2,5,1]
    def movimiento51(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.personaje_fila+=1    

    # Movimiento 52: [5,6,2] ->	[2,5,6]
    def movimiento52(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.personaje_fila+=1

################ MOVIMIENTOS EXTRA ABAJO

    # Movimiento extra abajo 94: [0,1,1,4] -> [4,0,1,1]  
    def movimiento94(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 1
        self.personaje_fila+=1    

    # Movimiento extra abajo 95: [0,1,6,4] -> [4,0,6,1]
    def movimiento95(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 1
        self.personaje_fila+=1    

    # Movimiento extra abajo 96: [0,1,1,2] -> [4,0,1,6]
    def movimiento96(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 6
        self.personaje_fila+=1    

    # Movimiento extra abajo 97: [0,6,1,2] -> [4,5,1,6]
    def movimiento97(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 6
        self.personaje_fila+=1    
    
    # Movimiento extra abajo 98: [0,1,6,2] -> [4,0,6,6]
    def movimiento98(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 6
        self.personaje_fila+=1    

    # Movimiento extra abajo 99: [0,6,6,4] -> [4,5,6,1]
    def movimiento99(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 1
        self.personaje_fila+=1    

    # Movimiento extra abajo 100: [5,6,1,4] -> [2,5,1,1]
    def movimiento100(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 1
        self.personaje_fila+=1    

    # Movimiento extra abajo 101: [5,1,1,4] -> [2,0,1,1]
    def movimiento101(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 1
        self.personaje_fila+=1    

    # Movimiento extra abajo 102: [5,1,6,4] -> [2,0,6,1]
    def movimiento102(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 1
        self.personaje_fila+=1    

    # Movimiento extra abajo 103: [0,6,1,4] -> [4,5,1,1]
    def movimiento103(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 1
        self.personaje_fila+=1    

    # Movimiento extra abajo 104: [0,6,6,2] -> [4,5,6,6]
    def movimiento104(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 6
        self.personaje_fila+=1    
    
    # Movimiento extra abajo 105: [5,6,6,4] -> [2,5,6,1]
    def movimiento105(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 1
        self.personaje_fila+=1    

    # Movimiento extra abajo 106: [5,6,1,4] -> [2,5,1,1]
    def movimiento106(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.mapa[self.personaje_fila + 3][self.personaje_columna] = 1
        self.personaje_fila+=1





    def abajo(self):

        self.movimientos += 1  # Incrementa el contador aquí

        nueva_fila = self.personaje_fila + 1  # Mover hacia abajo aumenta la fila
        nueva_columna = self.personaje_columna
        print(f"Moviendo a: [{nueva_fila}, {nueva_columna}]")

        # Movimiento 41: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.movimiento41()         

        # Movimiento 42: [0,2] -> [4,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
            self.movimiento42()

        # Movimiento 43: [0,1,4] ->	[4,0,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4: 
             self.movimiento43()
                

        # Movimiento 44: [0,1,2] ->	[4,0,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2: 
             self.movimiento44()
 
        # Movimiento 45: [0,6,4] ->	[4,5,1]	
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4: 
             self.movimiento45()

        # Movimiento 46: [0,6,2] ->	[4,5,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2: 
             self.movimiento46()

        # Movimiento 47: [5,4] -> [2,0]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.movimiento47() 

        # Movimiento 48: [5,2] -> [2,5]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
            self.movimiento48()

        # Movimiento 49: [5,1,4] ->	[2,0,1]	
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4: 
             self.movimiento49() 

        # Movimiento 50: [5,1,2] ->	[2,0,6]	
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2: 
             self.movimiento50() 

        # Movimiento 51: [5,6,4] ->	[2,5,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4: 
             self.movimiento51()

        # Movimiento 52: [5,6,2] ->	[2,5,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2: 
             self.movimiento52()


################ MOVIMIENTOS EXTRA ABAJO

        # Movimiento extra abajo 94: [0,1,1,4] -> [4,0,1,1]  
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 4:
             self.movimiento94()

        # Movimiento extra abajo 95: [0,1,6,4] -> [4,0,6,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 4:
             self.movimiento95()

        # Movimiento extra abajo 96: [0,1,1,2] -> [4,0,1,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 2:
             self.movimiento96()

        # Movimiento extra abajo 97: [0,6,1,2] -> [4,5,1,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 2:
             self.movimiento97()
    
        # Movimiento extra abajo 98: [0,1,6,2] -> [4,0,6,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 2:
             self.movimiento98()

        # Movimiento extra abajo 99: [0,6,6,4] -> [4,5,6,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 4:
             self.movimiento99()

        # Movimiento extra abajo 100: [5,6,1,4] -> [2,5,1,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 4:
             self.movimiento100()

        # Movimiento extra abajo 101: [5,1,1,4] -> [2,0,1,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 4:
             self.movimiento101()

        # Movimiento extra abajo 102: [5,1,6,4] -> [2,0,6,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 4:
             self.movimiento102()

        # Movimiento extra abajo 103: [0,6,1,4] -> [4,5,1,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 4:
             self.movimiento103()

        # Movimiento extra abajo 104: [0,6,6,2] -> [4,5,6,6]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 2:
             self.movimiento104()
    
        # Movimiento extra abajo 105: [5,6,6,4] -> [2,5,6,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 4:
             self.movimiento105()

        # Movimiento extra abajo 106: [5,6,1,4] -> [2,5,1,1]
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 3][self.personaje_columna] == 4:
             self.movimiento106()



    def jugar(self):
        continuar_jugando = True
        while continuar_jugando:
            self.cargar_nivel(self.nivel_actual)  
            while True:
                self.imprimirMapa()
                movimiento = input("Selecciona el movimiento (w/a/s/d), 'r' para reiniciar: ")
                if movimiento == 'd':
                    self.derecha()
                elif movimiento == 'a':
                    self.izquierda()
                elif movimiento == 'w':
                    self.arriba()
                elif movimiento == 's':
                    self.abajo()
                elif movimiento == 'r':  # reiniciar el nivel actual
                    print("Reiniciando nivel...")
                    self.cargar_nivel(self.nivel_actual)
                    continue

                if self.nivel_completado():
                    print("¡Nivel completado!")
                    break  # Salir del bucle interno para preguntar al jugador qué hacer a continuación

            # Preguntar al jugador qué hacer después de completar un nivel o decidir salir del bucle de movimiento
            eleccion = input("Presiona 'n' para el siguiente nivel, 'r' para repetir, cualquier otra tecla para salir: ")
            if eleccion == 'n' and self.nivel_actual + 1 < len(self.niveles):
                self.nivel_actual += 1  # Preparar para cargar el siguiente nivel
            elif eleccion != 'r':  # Si no se elige repetir, salir del juego
                print("Juego terminado.")
                continuar_jugando = False
                    
            

soko = Soko()
soko.jugar()
