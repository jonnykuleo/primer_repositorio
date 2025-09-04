import agenda
from agenda import agregar_contacto, listar_contactos, buscar_contacto, contactos[]

while True:
    print("Menu:")
    print("1. agregar contactos ")
    print("2. listar contactos")
    print("3. buscar contactos")
    print("4. salir")
    c = input("seleciona una opcion: ")
    
    if c == '1':
        print("agregar contacto")
        nombre = input("ingresa el nombre :")
        telefono = input("ingrese  el telefono: ")
        agregar_contacto(nombre,telefono)
        print("Contacto agregado")
    if c == '2':
        listar_contactos()
    if c == '3':
        nombre = input("ingresa el nombre a buscar: ")
        buscar_contacto(nombre)
    if c == '4':
        print("saliendo...")
        
    

        




