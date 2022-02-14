from Listas import Lista
import os

class Cola(Lista):
    def __init__(self, tamanio=4):
        super().__init__(tamanio)
        
    def menu_cola(self):
        opcion = self.menu(["1) Push", "2) Pop", "3) Show", "4) Buscar", "5) Longitud", "6) Salir"],"*"*20+" MENU COLA "+"*"*21)
        os.system("cls") 
        if opcion == '1':
            try:
                print("*"*15+" INGRESO DE DATOS "+"*"*15)
                dato = int(input("Escribe una dato para agregarlo a tu lista: "))
                print("*"*48)
                self.push(dato)
                input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_cola()

            except ValueError:
                print("*"*48), input("\nDebes ingresar solo valores numericos!"), os.system("cls"), self.menu_cola()
        
        elif opcion == '2':
            print("*"*15+" EXTRACCIÓN DE DATO "+"*"*15)
            print("El dato se a eliminado correctamente:",self.pop())
            print("*"*50)
            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_cola()
        
        elif opcion == '3':
            print("*"*15+" DATOS DE LA COLA "+"*"*15)
            self.show_cola()
            print("*"*48)
            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_cola()
        
        elif opcion == '4':
            print("*"*15+" BUSCADOR DE DATO "+"*"*15)
            print(self.buscar())
            print("*"*48)
            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_cola()
            
        elif opcion == '5':
            print("*"*12+" LONGITUD DE LOS DATOS "+"*"*13)
            print("La longitud de la Lista es:",self.longitud())
            print("*"*48)
            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_cola()
        
        elif opcion == '6':
            pass
            
    def pop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            top = self.lista[0]
            self.tope -= 1
            self.lista = self.lista[1:]
            return top
    
    def show_cola(self):
        if self.empty():
            print("Lista vacia")
        else: 
            print(" Valor")                 
            for tope in range(self.tope):
                    print(" [{}]".format(self.lista[tope])) 
                
    def longitud(self):
        return self.tope
    
    def empty(self):
        return self.tope == 0
