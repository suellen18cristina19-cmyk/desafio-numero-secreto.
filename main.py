
numero_secreto = 7

print("Bem-vindo ao jogo de adivinhação!")
print("Você tem 5 tentativas!")

for tentativa in range(5):
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite > numero_secreto:
        print("O número secreto é menor!")
    else:
        print("O número secreto é maior!")

else:
    print("Você perdeu! O número correto era", numero_secreto)
