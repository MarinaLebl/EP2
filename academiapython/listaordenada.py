def adiciona_em_ordem(paisx,distanciax,listapais):
    total=0
    paisx_distanciax=[paisx, distanciax]
    for x in listapais:
        if distanciax>x[1]:
            total+=1
    listapais.insert(total, paisx_distanciax)
    return listapais
