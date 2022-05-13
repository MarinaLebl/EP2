def adiciona_em_ordem(paisx,distanciax,listapais):
    nomes = []
    for elemen in listapais:
        nome = elemen[0]
        nomes.append(nome)
    if paisx in nomes:
        return listapais
    for elemen in listapais:
        distancia = elemen[1]
        nomes.append(distancia)
    if distanciax in distancia:
        return listapais
