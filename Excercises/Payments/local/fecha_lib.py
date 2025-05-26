
def create_date(dia, mes, año):
    if len(str(dia)) == 1:
        if len(str(mes)) == 1:
            date_str = str(str(año) + "-" + "0" + str(mes) + "-" + "0" + str(dia))

        if len(str(mes)) == 2:
            date_str = str(str(año) + "-" + str(mes) + "-" + "0" + str(dia))

    if len(str(dia)) == 2:
        if len(str(mes)) == 1:
            date_str = str(str(año) + "-" + "0" + str(mes) + "-" + str(dia))

        if len(str(mes)) == 2:
            date_str = str(str(año) + "-" + str(mes) + "-" + str(dia))

    return date_str
