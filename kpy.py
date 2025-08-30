#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
CONSTANTE_BONUS = 1000

nome = input("Digite seu nome: ")
salario = float(input ("Informe o seu salario: "))
bonus = float(input ("Informe a Porcentagem do Bonus: "))

total_bonus = CONSTANTE_BONUS + (salario * bonus)

print(f"Olá {nome}, seu bônus foi de {total_bonus})
