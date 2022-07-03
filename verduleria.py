usuarios = [
    {
        "nombre": "Juan",
        "password": "1234",
    },
    {
        "nombre": "Pedro",
        "password": "5678",
    },
]

productos = [
    {
        "nombre": "Tomate",
        "precio": "1.5",
        "cantidad": 20,
    },
    {
        "nombre": "Banana",
        "precio": "3.5",
        "cantidad": 20,
    },
    {
        "nombre": "Manzana",
        "precio": "2.5",
        "cantidad": 50,
    }
]

carrito = [
    {
        "nombre": "Tomate",
        "precio": "1.5",
        "cantidad": 2,
    },
]

def login():
    usuario_input = input("Ingrese un nombre de usuario: ")
    password_input = input("Ingrese una password: ")

    for usuario in usuarios:
        if usuario["nombre"] == usuario_input and usuario["password"] == password_input:
            print("-----------------")
            print("Bienvenido " + usuario["nombre"])
            return True
    print("-----------------")
    print("Usuario o password incorrectos")
    return False

def menu():
    print("1. Ver productos")
    print("2. Seleccionar productos")
    print("3. Comprar productos")
    print("4. Ver carrito")
    print("5. Salir")
    print("-----------------")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        ver_productos()
    if opcion == "2":
        seleccionar_productos()
    elif opcion == "3":
        comprar_productos()
    elif opcion == "4":
        ver_carrito()
    elif opcion == "5":
        print("Hasta luego")
        return
    else:
        print("Opcion incorrecta")
        menu()

def ver_productos():
    print("-----------------")
    for idx, producto in enumerate(productos):
        print(str(idx) + ". " + producto["nombre"] + " - " + producto["precio"] + " - " + str(producto["cantidad"]))
    print("-----------------")
    menu()
    
def ver_carrito():
    print("-----------------")
    print("Carrito:")
    for producto in carrito:
        print(producto["nombre"] + " - " + str(producto["cantidad"]))
    print("-----------------")
    menu()

def validar_cantidad(numero_producto, cantidad):
    if (int(cantidad) > int(productos[numero_producto]["cantidad"])):
        print("No hay suficientes productos")
        menu()
    else:
        agregar_al_carrito(numero_producto, cantidad)

def agregar_al_carrito(numero_producto, cantidad):
    carrito.append({
        "nombre": productos[numero_producto]["nombre"],
        "precio": productos[numero_producto]["precio"],
        "cantidad": cantidad,
    })
    menu()

def seleccionar_productos():
    numero_producto = input("Ingrese una numero de producto: ")
    cantidad = input("Ingrese cantidad: ")
    validar_cantidad(int(numero_producto), int(cantidad))

def comprar_productos():
    print("-----------------")
    print("Carrito:")
    cantidad_total = 0
    precio_total = 0
    for producto in carrito:
        print(producto["nombre"] + " - " + str(producto["cantidad"]) + " - Precio unitario: " + str(producto["precio"]) + " - Total por producto: " + str(float(producto["precio"]) * producto["cantidad"]))
        cantidad_total = cantidad_total + int(producto["cantidad"])
        precio_total = precio_total + (int(producto["cantidad"]) * float(producto["precio"]))
    
    if cantidad_total >= 10:
        print("Obtiene un descuento del 15%")
    elif cantidad_total >= 5:
        print("Obtiene un descuento del 10%")
    else:
        print("No obtiene descuento") 
    print("-----------------")
    print("Usted pagó " + str(precio_total))
    print("Gracias por su compra")
    print("-----------------")


def init():
    if login():
        menu()
    else:
        print("No se pudo logear")
        print("-----------------")
        init()

init()