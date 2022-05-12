def adiciona_em_ordem(paisx,distanciax,listapais):
    listapais = []
    for paisx in listapais:
        if paisx in listapais:
            listapais.append(paisx)
            listapais.append(distanciax)
        else:
            return 0
    return listapais
    
