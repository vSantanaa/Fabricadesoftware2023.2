# recebendo a velocidade do veículo
velocidade = input("qual era a velocidade do veículo?")

#velocidade em inteiro, caso o usuário digite outro, aparecerá a mensagem de digitar apenas números
try: 
    velocidade_int = int(velocidade)
except ValueError:
    raise ValueError("digite apenas números")

#condicionais para verificar se o usuário estava acima, no limite, ou dentro do limite permitido da via
if velocidade_int > 80:
    print(f"Você excedeu a velocidade permitida da via, estava a {velocidade_int}.")
    print(f"Multa de: R${(velocidade_int - 80)*7}")

elif velocidade_int == 80:
    print("Você estava na velocidade limite da via")
    
else:
    print("Você estava dentro da velocidade permitida da via.")  


