#from new_u import new_user
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
        return "\nINSERT Done"

    def UPDATE():
        update()
        return "\nUPDATE Done"

    def SELECT():
        select_f()
        return "\nSELECT Done"
    
    def default():
        return "Invalid Option"

    def menu():
        print("----------- Choose an option -----------")
        print("1. INSERT")
        print("2. UPDATE")
        print("3. SELECT")
        print("-----------------------------------")

    def function(case):
        switcher = {
                1: INSERT,
                2: UPDATE,
                3: SELECT
                }

        return switcher.get(case, default())()

    os.system('CLS')
    menu()
    case = int(input("Choose an option: "))
    os.system('CLS')
    print(function(case))

    enter = str(input("\nContinue?\n\nYES: Press 1\nNO:  Press anything else\n"))


os.system('CLS')
print("\nGracias!")

