from app import session
from app import Pay

def update():

    v_id_operacion = int(input("Inserta el id de operacion que deseas modificar: "))  
    #v_id_contrato = int(input("Introduce el nuevo número de contrato: "))
    #v_id_cliente = int(input("Introudce el nuevo número de cliente: "))
    #v_fecha = str(input("Introduce la nueva fecha (aaaa-mm-dd): "))
    v_monto = float(input("Introduce el nuevo monto: "))
    #v_activo = True

    session.query(Pay).filter(
        Pay.id_operacion == v_id_operacion
    ).update(
        {
            #Pay.id_contrato : v_id_contrato,
            #Pay.id_cliente : v_id_cliente,
            #Pay.fecha : v_fecha,
            Pay.monto :  v_monto,
            #Pay.activo : v_activo
        }
    )

    session.commit()



def update_to_false(v_id_operacion):
    
    v_activo = False
    session.query(Pay).filter(
        Pay.id_operacion == v_id_operacion
    ).update(
        {
            Pay.activo : v_activo
        }
    )
    session.commit()