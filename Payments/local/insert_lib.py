from app import session
from app import Pay
from validaciones import val_0_1, val_año, val_dia, val_mes
from fecha_lib import create_date
from update_lib import update_to_false
import os

def insert():  

    #v_id_pago = int(input("Introduce el número de pago: "))
    v_id_contrato = int(input("Introduce el número de contrato: "))
    v_id_cliente = int(input("Introudce el número de cliente: "))
    dia = val_dia("Ingresa el día: ")
    mes = val_mes("Ingresa el mes: ")
    año = val_año("Ingresa el año: ")

    str_fecha = create_date(dia, mes, año)

    v_fecha = str_fecha
    v_monto = float(input("Introduce el monto: "))
    v_activo = True

    payments = session.query(Pay).filter(
            Pay.id_contrato == v_id_contrato
        ).filter(
            Pay.fecha > str_fecha
        )

    num_pagos_posteriores = payments.count()

    add_new_user = Pay(id_contrato = v_id_contrato, id_cliente = v_id_cliente, fecha = v_fecha, monto = v_monto, activo = v_activo)
    session.add(add_new_user)
    session.commit()

    if num_pagos_posteriores == 0:

        print("\nRealizado")

    else:
        os.system('CLS')
        id_primer_pago_posterior = payments[0].id_pago
        id_ultimo_pago_posterior = payments[-1].id_pago
        print("Hay",num_pagos_posteriores,"pagos posteriores a la fecha:",str_fecha)
        print("Se modificaran los siguientes ID de pago")
        print("\nid_pago \t id_contrato \t id_cliente \t fecha \t \t  monto")
        for pay in payments:
            print(pay.id_pago,"\t\t",pay.id_contrato,"\t\t",pay.id_cliente,"\t\t", pay.fecha,"\t", pay.monto)

        i = 0

        for id_pago in range(id_primer_pago_posterior,id_ultimo_pago_posterior+1):
            
            if payments[i].activo == 1 and payments[i].id_contrato == v_id_contrato and payments[i].id_cliente == v_id_cliente:
                add_missing_user = Pay(id_contrato = payments[i].id_contrato, id_cliente = payments[i].id_cliente, fecha = payments[i].fecha, monto = payments[i].monto, activo = True)
                session.add(add_missing_user)
                session.commit()
            
            i+=1

            update_to_false(id_pago)
            
        

