import adivinhacao
import Forca


print("*****************************")
print("Bem vindo Aos Jogos !!")
print("*****************************")
print("Qual jogo voce deseja: 1 Jogo da Adivinhacão ou 2 Jogo da Forca \n")
opcao = int(input("digite o valor"))

if (opcao==1):
    print("jogando jogo da Advinhacão \n")
    adivinhacao.jogar() #chamando do arquivo adivinhacao a função jogar

else:
    print("jogando jogo da forca \n")
    Forca.jogar() #chamando do arquivo forca a função jogar

