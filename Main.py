from Menu import Menu
from Listas import Lista
from Pilas import Pila
from Colas import Cola
import os

class Main(Menu):
    
    def __init__(self):
        pass
    
    def menu_main(self):
        opcion = self.menu(["1) Lista", "2) Pilas", "3) Colas", "4) Salir"],"*"*18+" MENU PRINCIPAL "+"*"*18)
        os.system("cls")
        
        if opcion == '1':
            try:
                pregunta = input("La Longitud de su Lista es de 4 elementos\n¿Desea cambiar la longitud? ").lower()

                if pregunta == "si":
                    size = int(input("Ingrese la Longitud de la lista: "))
                    print("Su lista tendra la longitud de {} elementos".format(size))
                    input("\nPresione una tecla para continuar..."), os.system("cls")
                    
                    lista = Lista(size)
                    if lista.menu_lista() != '7':
                        os.system("cls"), self.menu_main()
                
                elif pregunta == "no":
                    print("Su lista tendra un maximo de 4 elementos") 
                    input("\nPresione una tecla para continuar..."), os.system("cls")
                    lista = Lista()
                    if lista.menu_lista() != '7':
                        os.system("cls"), self.menu_main()
                    
                else:
                    input("\nDebes ingresar solo valores numericos!"), os.system('cls'), self.menu_main()
            except ValueError:
                input("\nDebes ingresar solo valores numericos!"), os.system('cls'), self.menu_main()
                
        elif opcion == '2':
            try:
                pregunta = input("La Longitud de su Pila(lista) es de 4 elementos\n¿Desea cambiar la longitud? ").lower()

                if pregunta == "si":
                    size = int(input("Ingrese la Longitud de la Pila(lista): "))
                    print("Su lista tendra la longitud de {} elementos".format(size))
                    input("\nPresione una tecla para continuar..."), os.system("cls")
                    
                    pila = Pila(size)
                    if pila.menu_pila() != '6':
                        os.system("cls"), self.menu_main()
                
                elif pregunta == "no":
                    print("Su lista tendra un maximo de 4 elementos") 
                    input("\nPresione una tecla para continuar..."), os.system("cls")
                    pila = Pila()
                    if pila.menu_pila() != '6':
                        os.system("cls"), self.menu_main()
                    
                else:
                    input("\nDebes ingresar solo valores numericos!"), os.system('cls'), self.menu_main()
            except ValueError:
                input("\nDebes ingresar solo valores numericos!"), os.system('cls'), self.menu_main()
                
        elif opcion == '3':
            try:
                pregunta = input("La Longitud de su Cola(lista) es de 4 elementos\n¿Desea cambiar la longitud? ").lower()

                if pregunta == "si":
                    size = int(input("Ingrese la Longitud de la Cola(lista): "))
                    print("Su lista tendra la longitud de {} elementos".format(size))
                    input("\nPresione una tecla para continuar..."), os.system("cls")
                    
                    cola = Cola(size)
                    if cola.menu_cola() != '6':
                        os.system("cls"), self.menu_main()
                
                elif pregunta == "no":
                    print("Su lista tendra un maximo de 4 elementos") 
                    input("\nPresione una tecla para continuar..."), os.system("cls")
                    cola = Cola()
                    if cola.menu_cola() != '6':
                        os.system("cls"), self.menu_main()
                    
                else:
                    input("\nDebes ingresar solo valores numericos!"), os.system('cls'), self.menu_main()
            except ValueError:
                input("\nDebes ingresar solo valores numericos!"), os.system('cls'), self.menu_main()
        
        elif opcion == '4':
            print("*"*15+" FINALIZANDO PROGRAMA "+"*"*15)
            
                
opc = Main()
opc.menu_main()
