import random 

def sorteia_letra(palavra, lista):
    palavra=palavra.lower()
    especiais= ['.', ',', '-', ';', ' ']
    for item in lista:
        especiais.append(item)
    for m in palavra:
        if m in especiais:
            palavra=palavra.replace(m, "")
    if palavra=="":
        return""
    letra=random.choice(palavra)
    while letra in especiais:
        letra=random.choice(palavra)
    return letra