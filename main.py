# EDGAR GARCIA ALVAREZ
# EJERCIO 1 GITHUB

from clases import Plataforma

def borrar():
    nombre = input("Introduce la plataforma a eliminar: ")

    if not nombre in dicc:
        print("Error! No existe")
    else:
        dicc.pop(nombre)

def anadir():    
    nombre = input("Introduce la plataforma a agregar: ")
    precio = float(input("Introduce el precio: "))

    if nombre in dicc:
        print("Error! Ya existe")
    else:
        dicc[nombre] = Plataforma(nombre, precio) #asignamos a la clave correspondiente, el valor Plataforma(nombre, precio)
    

def mostrar():
    nombre = input("Introduce la plataforma: ")
    
    if not nombre in dicc:
        print("Error! No existe")
    else:
        print(f"La plataforma {nombre} cuesta {dicc[nombre].precio} €")

def mostrar_todo():
    mostrar = ""

    for nombre in dicc:
        mostrar += f"{nombre} - {dicc[nombre].precio} €\n"

    print(mostrar)

def leer_positivo():

    num = int(input("Introduce número de meses: "))

    while num < 0:
        print ("Error, el número ha de ser positivo")
        num = int(input("Introduce número de meses: "))
    
    return num

def suscribir():
    nombre = input("Introduce la plataforma: ")
    meses = leer_positivo()
    
    if not nombre in dicc:
        print("Error! No existe")
    else:
        plat = dicc[nombre]
        print(f"El precio de suscripción de {nombre} elegida es de {plat.calcular_subscripcion(meses)} €") #usamos el método calcular_subscripción para obtener el precio de la misma
    
def main():

    continuar = True

    while continuar:
        
        print("---------")
        print("Opciones:")
        print("---------")
        print("1. Eliminar plataforma")
        print("2. Agregar plataforma")
        print("3. Mostrar precio de plataforma")
        print("4. Listar plataformas")
        print("5. Suscribirse a plataforma")
        print("6. Salir")
        print("---------------------------")
        opcion = int(input("Ingrese una opcion: "))
        
        if not 1 <= opcion <= 6:
            print("Error! Opcion no valida")

        elif opcion == 1:
            borrar()
        
        elif opcion == 2:
            anadir()
        
        elif opcion == 3:
            mostrar()

        elif opcion == 4:
            mostrar_todo()
        
        elif opcion == 5:
            suscribir()

        elif opcion == 6:
            continuar = False


dicc = {}
main()