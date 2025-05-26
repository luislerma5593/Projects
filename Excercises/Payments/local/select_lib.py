from app import session
from app import Pay
import os

def select_f():

    print("----------- Choose an option -----------")
    print("1. Id contrato")
    print("2. Id cliente")
    print("----------------------------------------\n")

    opc = str(input("Ingresa una opción: "))
    os.system('CLS')

    if opc == "1":
        id = int(input("Ingresa el número de contrato: "))
        payments = session.query(Pay).filter(
            Pay.id_contrato == id
        )

    elif opc == "2":
        id = int(input("Ingresa el número de cliente: "))
        payments = session.query(Pay).filter(
            Pay.id_cliente == id
        )

    else: 
        print("Opción inválida")

    if (opc == "1") or (opc == "2"):
        print("id_operacion \t id_contrato \t id_cliente \t fecha \t \t \t monto \t\t\t activo")
        for pay in payments:
            print(pay.id_operacion,"\t\t",pay.id_contrato,"\t\t",pay.id_cliente,"\t\t", pay.fecha,"\t\t", pay.monto,"\t\t", pay.activo)
    