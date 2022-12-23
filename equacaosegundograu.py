#Exercício 2. Escreva um programa que pede ao usuário os valores dos coeficientes de uma equação de segundo grau e a resolve. O programa deverá levar e conta todos os casos possíveis e imprimir as raízes da equação (ou uma mensagem, caso o discriminante seja negativo).

#Importação do math
import math

#Equação do 2° grau
print("Fórmula das equações do 2° grau: ax² + bx + c = 0")

a = int(input("\n\nInforme um valor para o coeficiente a: "))
if a == 0:
	print("Se a = 0, essa equação não poderá ser resolvida.")
else:
    b = int(input("Informe um valor para o coeficiente b: "))
    c = int(input("Informe um valor para o coeficiente c: "))
    
    #Texto informativo sobre como obter as raízes:

    print("\n\nPara se obter as raízes de uma equação do 2° grau, utiliza-se a fórmula de Bháskara.")

    #Definição das raízes:

    d = (b**2 - (4 * a * c))
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    
    #Condições para que a equação tenha raízes:

    if d < 0:
        print("\n\nA equação não possui raízes reais.")
    elif d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        print(f"\n\nA equação possui apenas uma raíz, que é: {round(x, 3)}.")
    elif d > 0:
        print(f"\n\nAs raízes da equação são {x1} e {x2}.")