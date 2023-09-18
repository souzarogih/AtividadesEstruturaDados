"""
Faça um programa que determine se um número é primo ou não.
"""

num = int(input("Digite um valor para verificar se é número primo: "))

if num > 1:

    for i in range(2, num):

        if (num % i) == 0:
            print(num, "Não é um número primo.")
            break
    else:
        print(num, "É um número primo.")

else:
    print(num, "Não é um número primo.")