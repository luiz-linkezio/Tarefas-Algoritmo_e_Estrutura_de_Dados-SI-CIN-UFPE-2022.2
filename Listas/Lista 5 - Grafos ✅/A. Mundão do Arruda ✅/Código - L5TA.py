#Classe de vértice de um grafo
class Vertice:
  #Iniciando o valor, a coordenada e a lista de arestas do vértice
  def __init__(self, valor, coordenada):
    self.valor = valor #valor armazenado
    self.coordenada = coordenada
    self.saidas = list() #Arestas de saída
  
  #Adicionando arestas do vértice  
  def adicionar_saidas(self, saidas):  
    for saida in saidas:
      self.saidas.append(saida)

#Classe de um grafo    
class Grafo:
  def __init__(self):
    self.grafo = dict()
    self.menor_caminho = float('inf')
    self.caminhos = 0
  
  #Método para adicionar um vértice no grafo
  def adicionar_vertice(self, valor, coordenada, saidas):
    vertice = Vertice(valor, coordenada)
    self.grafo[coordenada] = vertice

    vertice.adicionar_saidas(saidas)

  #Método para procurar o caminho mais curto entre dois vértices
  def procurar_caminho_curto(self, origem, fim, contador=0, visitados=None):
    #Cria uma lista para monitorar os locais visitados para que eles não se repitam
    if visitados is None:
      visitados = list()

    #Cada caminho que conseguir chegar no fim, tentará armazenar seu valor, porém apenas o menor caminho irá ser armazenado no final de tudo
    if origem == fim:
      if contador < self.menor_caminho:
        self.menor_caminho = contador
        self.caminhos = visitados.copy()  
      return

    visitados.append(origem)

    #Recursão para ir para o vértice seguinte
    for saida in self.grafo[origem].saidas:
      if saida not in visitados:
        self.procurar_caminho_curto(saida, fim, contador + 1, visitados)

    visitados.remove(origem)

  #Printa o caminho mais curto no formato que a tarefa pede
  def printar(self, caminhos):
    if self.menor_caminho == float('inf'):
      print("Infelizmente Grafite não pode chegar no Arruda.")
    else:
      caminhos_string = list()
      for caminho in caminhos:
        caminhos_string.append(self.grafo[caminho].valor)
      caminhos_string.append("Arruda")  
      caminhos_string = " -> ".join(caminhos_string)

      print(f"Grafite precisou passar por {self.menor_caminho+1} pontos através do caminho {caminhos_string}.")

#Inicializa a classe Grafo
grafo = Grafo()

#Locais que serão analisados
locais = input().split()

#Adição dos locais como vértices no grafo
contador = 0
for local in locais:
    saidas = input().split()
    saidas = [int(saida) for saida in saidas]
    grafo.adicionar_vertice(local, contador, saidas)
    contador += 1

#Procurando o caminho mais curto e printando em seguida
grafo.procurar_caminho_curto(0, len(locais) - 1)
grafo.printar(grafo.caminhos)