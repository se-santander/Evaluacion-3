import os
def cls():
    os.system("cls")

menu = """---- BIENVENIDO A AUTOMOTRIZ ----
1. Resgitrar Vehiculo
2. Listar todos los vehiculos
3. Imprimir Orden de Reparacion
4. Salir del programa
\nIngrese opcion: """

titulo = f"""{"                                         LISTADO DE VEHICULOS"}
{'-' * 130}
{"MARCA":<13}{"AÑO DE FABR.":<15}{"KILOMETRAJE":>15}{"COSTO DE REP. EST.":>25}{"IMPUESTO DE SERVICIO":>25}{"COSTO TOTAL A PAGAR":>30}
{'-' * 130}
"""
datos_vehiculos = []
marcas_vehiculos = ["TOYOTA","FORD","CHEVROLET","BMW","FERRARI","MAGDA",]

def registrar_vehiculo():
    try:
        cls()
        print("---- REGISTRAR VEHICULO ----")
        marca = input("Ingrese marca del vehiculo: ").strip().upper()
        año_fab = int(input("Año de fabrica: "))
        klm = int(input("Ingrese kilometraje del vehiculo: "))
        costo_re_est = int(input("Ingrese costo de reparacion estimado: "))
        if len(marca) < 1 or año_fab <= 0 or klm < 0 or costo_re_est <= 0:
            input("Error al ingresar datos\n\nReingrese")
        else:
            impuesto_serv = round(costo_re_est * 0.08)
            costo_total = round(costo_re_est + impuesto_serv)
            datos_vehiculos.append([marca,año_fab,klm,costo_re_est,impuesto_serv,costo_total])
            cls()
            input("VEHICULO REGISTRADO EXITOSAMENTE!\n\nEnter para continuar")
    except Exception as e:
        input(f"Excepcion en {str(e)}, Reingrese")

def lista_marca(marca):
    salida = titulo
    for t in datos_vehiculos:
        if marca == t[0]:
            salida += f"{t[0]:<13}"
            salida += f"{t[1]:<25}"
            salida += f"{t[2]:<14}"
            salida += f"{t[3]:<25}"
            salida += f"{t[4]:<30}"
            salida += f"{t[5]:<30}"
            salida += "\n"
    return salida

def listar_vehiculos():
    cls()
    salida = titulo
    for t in datos_vehiculos:
        salida += f"{t[0]:<13}"
        salida += f"{t[1]:<25}"
        salida += f"{t[2]:<14}"
        salida += f"{t[3]:<25}"
        salida += f"{t[4]:<30}"
        salida += f"{t[5]:<30}"
        salida += "\n"
    return salida

def Imprimir_orden_reparacion():
    cls()
    x = input(f"Marca a imprimir [todas/{marcas_vehiculos}]\n\nIngrese opcion: ").strip().upper()
    if x == "TODAS":
        with open("Listado todas las marcas.txt","w") as archivo:
            archivo.write(listar_vehiculos())
    elif x in marcas_vehiculos:
        with open(f"Lista Marca {x}.txt", "w") as archivo:
            archivo.write(lista_marca(x))
    else:
        input("Error de ingreso\n\nReingrese")

while True:
    try:
        cls()
        opc = int(input(menu))
        if opc == 4:
            break
        elif opc == 1:
            registrar_vehiculo()
        elif opc == 2:
            input(listar_vehiculos())
        elif opc == 3:
            Imprimir_orden_reparacion()
        else:
            input("OPCION INVALIDA, REINTENTE")
    except Exception as e:
        input(f"Excepcion en {str(e)}, Reingrese")