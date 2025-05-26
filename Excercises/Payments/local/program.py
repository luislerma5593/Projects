#from new_u import new_user
from validaciones import val_0_1, val_1_2_3
from insert_lib import insert
from update_lib import update
from select_lib import select_f
from app import session
from app import Pay
import os

enter = "1"

while enter == "1":

    def INSERT():
        insert()
        return ""

    def UPDATE():
        update()
        return "\nUPDATE Done"

    def SELECT():
        select_f()
        return "\nSELECT Done"
    
    def EXIT():
        os.system('CLS')
        return ""

    def menu():
        print("--------------- Opciones ---------------")
        print("1. INSERT")
        print("2. UPDATE")
        print("3. SELECT")
        print("4. Exit")
        print("-----------------------------------")

    def function(case):
        switcher = {
                1: INSERT,
                2: UPDATE,
                3: SELECT,
                4: EXIT
                }

        return switcher.get(case)()

    os.system('CLS')
    menu()
  
    case = val_1_2_3("Selecciona una opción: ")
    os.system('CLS')
    print(function(case))

    enter = str(val_0_1("Continuar?\n\nSI: 1\nNO: 0\n"))


os.system('CLS')
print("Gracias!")

