import random
from dificuldade import escolher_dificuldade  # Importando a função do módulo

def jogar(limite_tentativas, limite_numero):
    """Função principal do jogo, que executa as tentativas."""
    numero_secreto = random.randint(1, limite_numero)
    tentativas = 0
    acertou = False

    print(f"\nEu escolhi um número entre 1 e {limite_numero}. Você tem {limite_tentativas} tentativas. Boa sorte!")

    while tentativas < limite_tentativas:
        try:
            palpite = int(input("\nDigite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
                acertou = True
                break
        except ValueError:
            print("Por favor, digite um número válido.")

    if not acertou:
        print(f"\nVocê perdeu! O número secreto era {numero_secreto}. Tente novamente!")

def jogo_adivinhe():
    """Função que organiza o fluxo do jogo."""
    print("Bem-vindo ao jogo de adivinhar o número!")
    limite_tentativas, limite_numero = escolher_dificuldade()  # Chamada para a função importada
    jogar(limite_tentativas, limite_numero)

# Executa o jogo
if __name__ == "__main__":
    jogo_adivinhe()
