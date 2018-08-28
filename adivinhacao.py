import random # modulo que necessita ser adicionado pelo random



print("***********************")
print("Bem vindo no jogo de advinhação")
print("*****************************")


# numero_secreto = round(random.random()* 100) #pegando um numero aleatorio e arredondando ele para um int.
numero_secreto = random.randrange(0,51) # com esse conseguimos limitar de 0 a 50 o numero secreto


total_tentativas = 0
pontos = 1000

print("qual numero de dificuldade deseja ?")
print("Facil : 1, Medio  : 2, Dificil: 3 ")

nivel = int(input("defina o nivel \n")) # pegando dados e passando para variavel nivel, porem antes convertendo para int

if (nivel==1):
    total_tentativas = 15
elif (nivel==2):
    total_tentativas = 10
else:
    total_tentativas = 5

# print(numero_secreto) testando resultado

for rodada in range(1, total_tentativas+1):

    print("tentativa {} de {}".format(rodada, total_tentativas))

    chute = input("digite o seu numero entre 1 e 50 \n")
    chuteconvertido = int(chute)
 
    if (chuteconvertido < 1 or chuteconvertido > 50):
        print("digite numeros entre 1 e 50 ! \n")
        continue #continue passa uma vez do laço porem continua nele, diferente do break que sai do laço.
    print("voce digitou \t", chute)

    acertou =   chuteconvertido == numero_secreto
    maior=   chuteconvertido > numero_secreto
    menor=  chuteconvertido < numero_secreto

    if(acertou):
        print("voce acertou e fez {} pontos".format(pontos) )
        break

    else:
        if(maior):
            print("voce errou! o seu numero foi maior que o numero secreto \n")
        elif(menor):
            print("voce errou! o seu numero foi menor que o numero secreto \n")

            pontos_perdidos = abs(numero_secreto - chuteconvertido) # numero aleatorio - valordigitadopelousuario com o abs o valor se torna absoluro (sempre positivo)
            pontos = pontos - pontos_perdidos



print("Fim")
