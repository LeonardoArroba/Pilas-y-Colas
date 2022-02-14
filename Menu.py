class Menu:
    
    def __init__(self):
        pass
    
    def menu(self,opciones,titulo):
        print(titulo)
        for opcion in opciones:
            print(opcion)
        print("*"*52)
        opc = input("\nElija Opcion[1...{}]: ".format(len(opciones)))
        return opc
    

        
        