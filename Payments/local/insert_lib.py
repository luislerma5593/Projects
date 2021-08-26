from app import session
from app import Pay
from validaciones import val_0_1

def insert():  
    v_id_contrato = int(input("Introduce el número de contrato: "))
    v_id_cliente = int(input("Introudce el número de cliente: "))
    v_fecha = str(input("Introduce la fecha (aaaa-mm-dd): "))
    v_monto = float(input("Introduce el monto: "))
    
    act = val_0_1("1 Activo - 0 No activo: ")
        
    #act = int(input("1 - True / 0 - False"))

    if act == 0:
        v_activo = False
    
    if act == 1:
        v_activo = True
    

    add_new_user = Pay(id_contrato = v_id_contrato, id_cliente = v_id_cliente, fecha = v_fecha, monto = v_monto, activo = v_activo)
    session.add(add_new_user)
    session.commit()

