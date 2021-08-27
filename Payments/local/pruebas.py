from app import session
from app import Pay
from validaciones import val_0_1, val_año, val_dia, val_mes
from fecha_lib import create_date


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
    
num_pagos_atrasados = session.query(Pay).filter(
            Pay.id_contrato == v_id_contrato
        ).filter(
            Pay.fecha > str_fecha
        ).count()




print("id_pago \t id_contrato \t id_cliente \t fecha \t \t \t monto")
for pay in payments:
    print(pay.id_pago,"\t\t",pay.id_contrato,"\t\t",pay.id_cliente,"\t\t", pay.fecha,"\t\t", pay.monto)

print("Cuenta: ")


"""add_new_user = Pay(id_contrato = v_id_contrato, id_cliente = v_id_cliente, fecha = v_fecha, monto = v_monto, activo = v_activo)
session.add(add_new_user)
session.commit()"""