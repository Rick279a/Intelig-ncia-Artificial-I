import random

jogar_novamente = True

def jogar ():
    opcoes = ["Pedra", "Papel", "Tesoura"]

    jogador = input("Escolha (Pedra, Papel ou Tesoura): ").strip().capitalize()
    while jogador not in opcoes:
        print("Opção inválida!")
        jogador = input("Escolha (Pedra, Papel ou Tesoura): ").strip().capitalize()

    computador = random.choice(opcoes)

    print(f"Você escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate !!")
    elif (jogador == "Pedra" and computador == "Tesoura") or \
            (jogador == "Papel" and computador == "Pedra") or \
            (jogador == "Tesoura" and computador == "Papel"):
        print("Voce ganhou !!")
    else:
        print("voce perdeu !!")

jogar()

jogar_novamente = True

while jogar_novamente:
    jogar()
    jogar_novamente = input("Deseja jogar novamente? (Sim/Não): ").lower().startswith("s")

if not jogar_novamente:
    print("Obrigado por jogar!")