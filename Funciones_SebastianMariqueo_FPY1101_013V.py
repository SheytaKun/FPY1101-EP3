Libros = []
Datos = ["titulo","autor","año de publicacion","sku","usuario"]

def registra_libros():
    try:
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        año_publicacion = int(input("Ingrese el año de publicacion del libro: "))
        sku = input("Ingrese el SKU del libro: ")
    except ValueError:
        print("El año de publicacion deben ser numeros.")
        return
    if titulo == "" or autor == "" or año_publicacion == "" or sku == "" <=0:
        print("Debe ingresar todos los datos correspondiente")
    
    libro = {
        'Titulo': titulo,
        'Autor': autor,
        'Año de publicacion': año_publicacion,
        'sku': sku,
    }
    Libros.append(libro)
    print("Libro ingresado con exito.")

def prestar_libro():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    sku = input("Ingrese el SKU del libro: ")
    if nombre_usuario == "" or sku == "" <=0:
        print("Debe ingresar todos los datos para hacer la reservacion.")
        return
    libro = {
        'Nombre de usuario': nombre_usuario,
        'sku': sku,
    }
    Libros.append(libro)
    print("Disfrute su libro.")

def listar_libros():
    print("Titulo:\t Autor:\t año de publicacion:\t sku: ")
    for libro in Libros:
        print(f"{libro['Titulo']}\t {libro['Autor']}\t {libro['Año de publicacion']}\t\t\t {libro['sku']}")

def imprimir_reporte_prestamo(libros):
    sku = input("Presione ENTER para poder generar un reporte de los libros prestados: ")
    print("Generando planilla....")
    with open("Planilla_reporte.txt","w") as archivo:
        for libro in libros:
            if sku == "" or libro ['sku'] == sku:
                archivo.write (f"Usuario: {libro['usuario']}\t Titulo: {libro['titulo']}\t Fecha del prestamo: {libro['fecha del prestamo.']}")
    print("Plantilla generada con exito.")

def menu():
    while True:
        try:
            print("--------MENU-------- \n1.-Registrar libro.\n2.-Prestar libro.\n3.-Listar todos los libros.\n4.-Imprimir reporte de prestamos.\n5.-Salir del programa.")
            opcion = int(input("Escoja una opcion: "))
            if opcion==1:
                registra_libros()
            elif opcion==2:
                prestar_libro()
            elif opcion==3:
                listar_libros()
            elif opcion==4:
                imprimir_reporte_prestamo(Libros)
            elif opcion==5:
                print("Programa finalizado....\nDesarrollado por Sebastian Mariqueo\nRut: 20.670.472-1")
                break
            else:
                print("Opcion no valida.")
        except ValueError:
            print("Solo se deben ingresar numeros para elegir sus opciones.")
    menu()
