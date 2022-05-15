print('Bem-vindo ao Insper Países')

a = input('Pressione qualquer tecla para iniciar: ')
b = input('Menu: Pressione ''1'' para jogar ou pressione ''2'' para sair ')


if b == '2':
    print('até a próxima')
if b != '1' and b !='2':
    print('comando inválido')

def instrucoes(instrucao):
    print('Comandos:')
    print('dica -  entra no mercado de dicas')
    print('desisto -  desiste da rodadaa')
    print('inventario -  exibe sua posição')
    return instrucao

def jogo(jogadas):
    jogadas.instrucoes()
    while jogadas.tentativas > 0:
