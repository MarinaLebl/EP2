def esta_na_lista(pais,lista):
    res=0
    for item in lista:
        if pais==item:
            res==1
        if res==1:
            return True
        else:
            return False