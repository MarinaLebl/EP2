def normaliza(dic):
    d={} 
    for cont in dic:
        for pais in dic[cont]:
            pais2= dic[cont][pais]
            pais2["continente"]=cont
            d[pais]= pais2
    return d
