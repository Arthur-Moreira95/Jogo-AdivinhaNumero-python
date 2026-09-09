# Adivinha o número entre 1 e 20, e o sistema vai falar se você chutou um numero maior ou menor:  
import random

numero_secreto = random.randint(1,20)

numero_resposta = int(input("Digite seu chute: "))

while numero_secreto != numero_resposta:
    if abs(numero_resposta - numero_secreto) == 1:
        print(f"O seu chute de {numero_resposta} está pertíssimo!")
    elif numero_resposta < numero_secreto:
        print(f'Seu chute de {numero_resposta} é maior que o número secreto')
    elif numero_resposta > numero_secreto:
        print(f'Seu chute de {numero_resposta} é menor que o número secreto')
    numero_resposta = int(input("Digite seu chute: " ))


if numero_secreto == numero_resposta:
    print(f'Parabéns! Seu chute de {numero_resposta} foi certo! O número secreto era {numero_secreto}')