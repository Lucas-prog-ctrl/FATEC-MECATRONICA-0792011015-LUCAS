#Cria um log de temperatura
#Ler N temperaturas
temperaturas = []

#Quantas temperaturas o usuario quer informar
quantidade = int(input('Quantidade de temperaturas que deseja informar: '))

#Le os numeros para lista 
while len(temperaturas) < quantidade:
  temperatura = int(input('Valor:'))
  temperaturas.append(temperatura)

#Calcular a temperatura média
media = sum(temperaturas)/len(temperaturas)

#Encontrar todas as temperaturas acimda da média
temp_acima_da_media = []
for temperatura in temperaturas :
  if temperatura > media:
    temp_acima_da_media.append(temperaturas)

maior = max(temperaturas)
menor = min(temperaturas)

print("Temperaturas Informadas:")
print(temperaturas)
print('Temp. Media:', media)
print('Temp. acima da media:', temp_acima_da_media)
print('Maior temperatura:', maior)
print('Menor temperatura:', menor)
