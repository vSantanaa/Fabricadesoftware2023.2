#obtendo número escolhido pelo usuário
número = input("digite um número:")

#variáveis criadas para antecessor e sucessor do número escolhido
antecessor = 0
sucessor = 0

# número em inteiro, caso o usuário digite outro, aparecerá a mensagem de digitar apenas números
try:
    sucessor = int(número) + 1
    antecessor = int(número) - 1
except ValueError:
    raise ValueError("digite um número válido")
    print("Digite um número válido")

#resultado
print(f"o número digitado foi {número}, seu sucessor é {sucessor} e seu antecessor é {antecessor}.")