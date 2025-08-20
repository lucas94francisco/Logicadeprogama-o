import random
nome_do_jogador=input("digite seu nome")


numero_aleatorio = random.randint(1,100)
palpite_jogador = int(input('digite um inteiro de 1 a 100 '))
numero_tentativas = 1

while numero_aleatorio != palpite_jogador:
    numero_tentativas += 1 # numero_tentativas = numero_tentativas + 1

    if palpite_jogador > numero_aleatorio:
        print('muito alto')
    else:
        print('muito baixo')

    palpite_jogador = int(input('digite um inteiro de 1 a 100 '))
 
print(f"acertou em {numero_tentativas} tentativas")
print(nome_do_jogador, "certou em",numero_tentativas,"tntativas")


