def uno():
    return 1
def dos():
    return 2
def tres():
    return 3
def cuatro():
    return 4
def otro():
    return "Opcion Invalida"

def switch(case):
    sw = {
        1: uno(),
        2: dos(),
        3: tres(),
        4: cuatro()
        }
    return sw.get(case, otro())


case = int(input("Seleccione una opcion: "))
print(switch(case))