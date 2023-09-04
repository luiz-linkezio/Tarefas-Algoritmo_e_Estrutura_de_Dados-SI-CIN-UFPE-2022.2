def mapear_rotas(planetas, indices, rota=None, rotas=None):
    #Transformando None em listas vazias, esta estratégia foi usada, pois o uso de apenas listas vazias estava causando problemas
    if rota is None:
        rota = []
    if rotas is None:
        rotas = []

    for indice in indices: #Para cada indice na lista de indices...
        nova_rota = rota + [planetas[indice]]  #Aumenta a rota, adicionando o novo planeta
        novos_indices = [i for i in indices if i > indice]  #Remove o índice atual da lista e os antecessores dele também

        
        rotas.append(nova_rota)#Adiciona a rota à lista de rotas

        mapear_rotas(planetas, novos_indices, nova_rota, rotas) #Recursão com a LISTA DE INDICES MODIFICADA, quando recursar, terá menos planetas disponíveis para adicionar à rota

    return rotas

#Tratamento de input, transformando os planetas em uma lista e ordenando esta lista
planetas = list()
entrada = input()
entrada = entrada.split(", ")
for planeta in entrada:
  planetas.append(planeta)
planetas.sort()

#Verificando se a entrada é vazia
vazio = False
for elemento in planetas:
  if elemento.isspace():
    vazio = True

if vazio == False: #Se a entrada não for vazia...
  rotas = mapear_rotas(planetas, list(range(len(planetas)))) #Chama a função responsável por criar as rotas, enviando como parâmetro: a lista de planetas e uma lista numerando os índices dos planetas
  rotas.append([]) #Adicionando a lista vazia às rotas (SEMPRE ESTÁ PRESENTE)
  rotas.sort() #Ordenando, para o output sair como no enunciado, em ordem alfabética
else: #Se a entrada for vazia...
  rotas = [[]] #Apenas a lista vazia estará presente na lista de rotas

print(f"O número de subsets de visitação é {len(rotas)}\nSão eles: {rotas}") #Print que o enunciado pede
