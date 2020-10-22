personagens = {"dps": [], "healer": [], "support": [], "tank": []}

quantidade_de_personagens = int(input("Quantidade de personagens:"))

contador = 0
while contador < quantidade_de_personagens:
  nome = input("Qual o nome de personagens:")
  classe = input("Qual a classe do personagem:").lower()
  #Verifica se a classe informada é valida
  if classe in personagens.keys():
    personagens[classe].append(nome)
    #Avança para o proximo registro
    contador += 1
  else:
    print("Classe de personagem invalida!")
  print(personagens)
