def adiciona_em_ordem(paisx,distanciax,listapais):
    listapais = []
    for paisx in listapais:
        if paisx in listapais:
            return 0
        else:
            listapais.append(paisx)
            listapais.append(distanciax)
    return listapais
