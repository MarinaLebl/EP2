def esta_na_lista(pais, lista):
    esta = 0
    for i in lista:
        if pais == i[0]:
            esta = 1
    if esta == 1:
        return True
    else:
        return False
