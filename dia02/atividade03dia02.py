# verificação de idade do usuário 
idade = (input("digite sua idade:"))

# idade em inteiro, caso o usuário digite outro, aparecerá a mensagem de digitar apenas números
try:
    idade_int = int(idade)
except ValueError:
    raise ValueError("digite apenas números")

#condicional para verificar se o usuário tem idade para obter a CNH
if    idade_int >= 18:
    print("Você pode obter sua carteira de motorista (CNH)")
else:
    print("Você não tem a idade miníma para obter sua carteira de habilitação (CNH)")    

