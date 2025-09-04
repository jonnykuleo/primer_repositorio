#agenda
contacto = []

def agregar_contacto(nombre,telefono):
    contacto.append({"nombre": nombre, "telefono":telefono})

def lista_contactos():
    print("\nlista de contactos: ")
    for c in contactos:
        print(f"{c["nombre"]} - {c["telefono"]}")


nombre = input("ingresael nombre :")
telefono = input("ingrese el telefono: ")
agregar_contacto(nombre,telefono)
print("Contacto agregado")

lista_contactos()