#agenda
contacto = []

def agregar_contacto(nombre,telefono):
    contacto.append({"nombre": nombre, "telefono":telefono})

def buscar_contacto(nombre:)
    for c in contactos:
    if c['nombre'].lower() == nombre.lower():
        print(f"caontactos encontrado: {c["nombre"]} - {c["telefono"]}")
        return
    print('contacto no encontrado')
    

def lista_contactos():
    print("\nlista de contactos: ")
    for c in contactos:
        print(f"{c["nombre"]} - {c["telefono"]}")

lista_contactos()


nombre = input("ingresael nombre :")
telefono = input("ingrese el telefono: ")
agregar_contacto(nombre,telefono)
print("Contacto agregado")

