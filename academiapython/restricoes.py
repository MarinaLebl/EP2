import random 
def sorteia_letra(palavra, restrita):
    palavra=palavra.lower()
    especiais=['.', ',', '-', ';', ' ']
    for item in restrita:
        especiais.append(item)
    for m in palavra:
        if m in especiais:
            palavra=palavra.replace(m, "")
    if palavra=="":
        return("")
    letra=random.choice(palavra)
    while letra in especiais:
        letra=random.choice(palavra)
    return letra

print(sorteia_letra("Andorra a-Velha", ['a', 'r']))