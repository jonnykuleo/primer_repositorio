#agenda
contactos = []

def agregar_contacto(nombre,telefono):
    contactos.append({"nombre": nombre, "telefono":telefono})

def listar_contactos():
    print("\nlista de contactos: ")
    for c in contactos:
        print(f"{c["nombre"]} - {c["telefono"]}")

def buscar_contacto(nombre):
    for c in contactos:
        if c['nombre'].lower() == nombre.lower():
            print(f"contacto encontrado: {c["nombre"]} - {c["telefono"]}")
            return
        print('contacto no encontrado')
    
listar_contactos()


nombre = input("ingresael nombre :")
telefono = input("ingrese el telefono: ")
agregar_contacto(nombre,telefono)
print("Contacto agregado")

