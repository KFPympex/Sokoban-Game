class Soko:

    mapa = [] # mapa del juego
    personaje_columna = 0
    personaje_fila = 0

    def __init__(self):
        # Define el mapa de juego
        self.mapa =[
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,0,4,4,4,4,1,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,1,4,4,4,4,4,2,2,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,2,2,4,4,3],
            [3,4,4,4,1,4,4,1,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        ]

        # Definimos la posicion inicial del personaje
        self.personaje_columna = 3
        self.personaje_fila = 2

    def imprimirMapa(self):
        for filas in self.mapa:
            print(filas)

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



    def derecha(self):
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






    def izquierda(self):
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
      




    def arriba(self):
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






    def abajo(self):
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
            


