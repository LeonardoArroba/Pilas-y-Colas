from Menu import Menu
import os

class Lista(Menu):
    def __init__(self,tamanio=4):
       self.lista = []
       self.tope = 0
       self.size = tamanio
       
    
    def menu_lista(self):
        opcion = self.menu(["1) Push", "2) Pop", "3) Show", "4) Eliminar", "5) Insertar", "6) Buscar", "7) Salir"],"*"*20+" MENU LISTA "+"*"*20) 
        os.system("cls")
        if opcion == '1':
            print("*"*15+" INGRESO DE DATOS "+"*"*15)
            dato = input("Escribe una dato para agregarlo a tu lista: ")
            print("*"*48)
            if dato != "[ ]":
                self.push(dato)
                input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_lista()
                
        elif opcion == '2':
            print("*"*15+" EXTRACCIÓN DE DATO "+"*"*15)
            print(self.pop())
            print("*"*51)
            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_lista()
                
        elif opcion == '3':
            print("*"*15+" DATOS DE LA LISTA "+"*"*15)
            self.mostrar()
            print("*"*49)
            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_lista()
        
        elif opcion == '4':
            print("*"*15+" ELIMINAR UN DATO "+"*"*15)
            self.mostrar()
            try:
                pos = int(input("Ingrese la posición del dato a eliminar: "))
                print(self.eleminarElemento(pos)) 
                print("*"*48)
                input("\nPresione una tecla para continuar..."),os.system("cls"), self.menu_lista()
                
            except ValueError:
                print("*"*48)
                input("\nDebes ingresar un dato!"), os.system("cls"), self.menu_lista()
        
        elif opcion == '5':
            print("*"*15+" INSERTAR UN DATO "+"*"*15)
            self.mostrar()
            try:
                print(self.insertarElemento())
                print("*"*48)
                input("\nPresione una tecla para continuar..."),os.system("cls"), self.menu_lista()
                
            except ValueError:
                print("*"*48)
                input("\nDebes ingresar un dato!"), os.system("cls"), self.menu_lista()
        
        elif opcion == '6':
            print("*"*15+" BUSCADOR DE DATO "+"*"*15)
            print(self.buscar())
            print("*"*46)
            input("\nPresione una tecla para continuar..."), os.system("cls"), self.menu_lista()      
                
        elif opcion == '7': 
            pass
         
    def push(self,dato):
        if self.tope < self.size:
            self.lista = self.lista + [dato]
            self.tope += 1 
        else:
            print("La Lista esta llena")
        
    def pop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return "El dato se a eliminado correctamente: {}".format(top)
    
    def eleminarElemento(self,pos):
        if pos < 0 or pos >= self.tope:
            return "El rango esta fuera del alcance!"
        else:
            self.tope -= 1
            self.lista = self.lista[:pos] + self.lista[pos + 1:]
            return f"Se actualizo la lista {self.lista}"
            
    def insertarElemento(self):
        if len(self.lista) == self.size or self.tope > self.size:
            return "Lista llena, elimine un dato"
            
        else:
            pos = int(input("Ingresa la posición: "))
            dato = input("Ingrese un valora: ")
            self.lista.insert(pos, dato)
            self.tope += 1
            return "Valor agregado exitosamente"
    
    def buscar(self):
        if self.tope == 0:
            return "La Lista esta vacia"
        else:
            self.mostrar()
            try:
                
                buscado = input("Ingrese el dato de la posicion a buscar: ")
                enc = False
                for pos, elemento in enumerate(self.lista):
                    if elemento == buscado:
                        enc = True
                        break
                if enc == True:  
                    return "La posición es: {}".format(pos)
                else:
                    return "-1"
            except ValueError:
                return "Debes intruducir un dato"      
    
    def mostrar(self):
        if self.lista != 0:
            print("Posicion"," "*4, "Valor")
            for pos,ele in enumerate(self.lista):
                print("   {}          [{}]".format(pos,ele))
        else:
            print("La lista esta vacia!")

    def empty(self):
        if self.tope == 0:
            return True
        else:
            return False

