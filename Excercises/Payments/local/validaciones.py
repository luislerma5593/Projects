#Validar 1 o 2

def val_0_1(texto):
    while True:
        try:
            val = int(input(texto))
        except ValueError:
            print("ValueError")
            continue

        if val != 0 and val != 1:
            print("Ingresa 0 o 1")
            continue
        else:
            return val
            break

def val_1_2_3(texto):
    while True:
        try:
            val = int(input(texto))
        except ValueError:
            print("ValueError")
            continue

        if val != 1 and val != 2 and val != 3 and val != 4:
            print("Ingresa una opción valida")
            continue
        else:
            return val
            break

def val_dia(texto):
    while True:
        try:
            val = int(input(texto))
        except ValueError:
            print("ValueError")
            continue

        if val < 1 or val > 31:
            print("Ingresa una opción valida")
            continue
        else:
            return val
            break

def val_mes(texto):
    while True:
        try:
            val = int(input(texto))
        except ValueError:
            print("ValueError")
            continue

        if val < 1 or val > 12:
            print("Ingresa una opción valida")
            continue
        else:
            return val
            break

def val_año(texto):
    while True:
        try:
            val = int(input(texto))
        except ValueError:
            print("ValueError")
            continue

        if val < 2000 or val > 2021:
            print("Ingresa una opción valida")
            continue
        else:
            return val
            break