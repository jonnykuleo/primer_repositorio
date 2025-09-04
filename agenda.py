#agenda
contacto = []

def agregar_contacto(nombre,telefono):
    contacto.append({"nombre": nombre, "telefono":telefono})

nombre = input("ingresael nombre :")
telefono = input("ingrese el telefono: ")
agregar_contacto(nombre,telefono)
print("Contacto agregado")