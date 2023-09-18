"""
Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O programa deve solicitar
 a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do computador e determinar o vencedor.
"""
import random

jogadas = ['pedra', 'papel', 'tesoura']

index = random.randint(1,2)

opcao_usuario = int(input("Escolha uma opção: \n0 pedra\n1 papel\n2 tesoura"))

print(f'O usuário escolheu {jogadas[opcao_usuario]}')
print(f'O computador escolheu {jogadas[index]}')

if (jogadas[opcao_usuario] == 'pedra' and jogadas[index] == 'tesoura') or (jogadas[opcao_usuario] == 'tesoura' and jogadas[index] == 'papel') or (jogadas[opcao_usuario] == 'papel' and jogadas[index] == 'pedra'):
    print(f'Usuário venceu pois jogou {jogadas[opcao_usuario]}')

elif (jogadas[opcao_usuario] == 'tesoura' and jogadas[index] == 'pedra') or (jogadas[opcao_usuario] == 'papel' and jogadas[index] == 'tesoura') or (jogadas[opcao_usuario] == 'pedra' and jogadas[index] == 'papel'):
    print(f'Computador venceu pois jogou {jogadas[opcao_usuario]}')
else:
    print(f"Empate pois o computador colocou {jogadas[index]} e o usuário colocou {jogadas[opcao_usuario]}")
