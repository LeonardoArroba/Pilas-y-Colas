import re
from Listas import Lista
import os

class Pila(Lista):                
    def __init__(self,tamanio=4):
        super().__init__(tamanio)
    
    def menu_pila(self):
        opcion = self.menu(["1) Push", "2) Pop", "3) Show", "4) Buscar" , "5) Longitud", "6) Salir"],"*"*20+" MENU PILA "+"*"*21)
        os.system("cls") 
        if opcion == '1':
            try:
                print("*"*15+" INGRESO DE DATOS "+"*"*15)
                dato = int(input("Escribe una dato para agregarlo a tu lista: "))
                print("*"*48)
                self.push(dato)
                input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_pila()

            except ValueError:
                print("*"*48), input("\nDebes ingresar solo valores numericos!"), os.system("cls"), self.menu_pila()
        
        elif opcion == '2':
            print("*"*15+" EXTRACIÓN DE DATOS "+"*"*15)
            print("El dato se a eliminado correctamente:",self.pop())
            print("*"*48)
            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_pila()
        
        elif opcion == '3':
            print("*"*15+" DATOS DE LA PILA "+"*"*15)
            self.show()
            print("*"*48)
            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_pila()
        
        elif opcion == '4':
            print("*"*15+" BUSCADOR DE DATO "+"*"*15)
            print(self.buscar())
            print("*"*48)
            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_pila()
            
        elif opcion == '5':
            print("*"*15+" LONGITUD DE LA PILA "+"*"*15)
            print("La longitud de la Lista es:",self.longitud())
            print("*"*48)
            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_pila()
            
            
        elif opcion == '6':
            pass
        
    def empty(self):
        return self.tope == 0
           
    def longitud(self):
            return self.tope
        
    def show(self):
        if self.empty():
            print("Lista vacia")
        else:  
            print(" Valor")                  
            for tope in range(self.tope-1,-1,-1):
                print(" [{}]".format(self.lista[tope]))    

