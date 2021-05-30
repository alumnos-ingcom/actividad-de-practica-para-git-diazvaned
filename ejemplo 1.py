def nombre_identificador(arg1, arg2):
    return arg1 + arg2

def prueba():
    otravar = "Hola mundo"
    unavar = nombre_identificador(10,20)
    otravar = input("carga un valor")
    try:
        print (int(otravar))
    except ValueError:
        print ("Eso no era un numero")
    
    
if __name__ == "__main__":
    prueba()