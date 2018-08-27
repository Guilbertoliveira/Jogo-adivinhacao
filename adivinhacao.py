import random # modulo que necessita ser adicionado pelo random



print("***********************")
print("Bem vindo no jogo de advinhação")
print("*****************************")


# numero_secreto = round(random.random()* 100) #pegando um numero aleatorio e arredondando ele para um int.
numero_secreto = random.randrange(0,51) # com esse conseguimos limitar de 0 a 50 o numero secreto


total_tentativas = 3

# print(numero_secreto) testando resultado

for rodada in range(1, total_tentativas+1):

    print("tentativa {} de {}".format(rodada, total_tentativas))
    chute = input("digite o seu numero entre 1 e 50")
    chuteconvertido = int(chute)
 
    if (chuteconvertido < 1 or chuteconvertido > 50):
        print("digite numero entre 1 e 50")
        continue

    print("voce digitou", chute)

    acertou =   chuteconvertido == numero_secreto
    maior=   chuteconvertido > numero_secreto
    menor=  chuteconvertido < numero_secreto

    if(acertou):
        print("voce acertou")
        break

    else:
        if(maior):
            print("voce errou! o seu numero foi maior que o numero secreto")
        elif(menor):
            print("voce errou! o seu numero foi menor que o numero secreto")



print("Fim")
