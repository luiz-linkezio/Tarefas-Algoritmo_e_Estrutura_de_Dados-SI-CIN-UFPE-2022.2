class Node:
  def __init__(self, cpf, nome):
    self.valor = cpf
    self.nome = nome
    
    self.filhoD = None
    self.filhoE = None
    self.pai = None

class Arvore_bi:
  
  def __init__(self):
    self.raiz = None
  
  def criarArvore(self, lista_cpf, lista_nomes):
    
    contador = 0
    for cpf in lista_cpf:
      node = Node(cpf, lista_nomes[contador])
      contador += 1
      
      if self.raiz == None:
        self.raiz = node
  
      else:
        entrou = False
        item_atual = self.raiz
        while not entrou:
          
          if item_atual.valor < node.valor:
            if item_atual.filhoD == None:
              item_atual.filhoD = node
              item_atual.filhoD.pai = item_atual
              
              entrou = True 
              
            else:
              item_atual = item_atual.filhoD
              
          elif item_atual.valor > node.valor:
            if item_atual.filhoE == None:
              item_atual.filhoE = node
              item_atual.filhoE.pai = item_atual
              
              entrou = True
              
            else:
              item_atual = item_atual.filhoE
  
  def remocao(self, nome):
    nome_index = lista_suspeitos_nomes.index(nome)
    cpf = lista_suspeitos_cpfs[nome_index]
    
    no_atual = (self.busca(cpf))[0]
    
    
    #nó removido tem 2 filhos
    if no_atual.filhoD and no_atual.filhoE:
      #nó à direita do nó removido tem um filho à esquerda
      if no_atual.filhoD.filhoE:
        #jogando o filho pro outro lado
        no_atual_2 = no_atual.filhoE
        while no_atual_2.filhoD:
          no_atual_2 = no_atual_2.filhoD
          
        no_atual_2.filhoD = no_atual.filhoD.filhoE
        no_atual.filhoD.filhoE.pai = no_atual_2
        
        #assumindo a posição do nó q foi removido
        no_atual.filhoE.pai = no_atual.filhoD
        no_atual.filhoD.filhoE = no_atual.filhoE
        
        no_atual.filhoD.pai = no_atual.pai
        if no_atual.pai.filhoD and no_atual.pai.filhoD.valor == no_atual.valor:
          no_atual.pai.filhoD = no_atual.filhoD
        if no_atual.pai.filhoE and no_atual.pai.filhoE.valor == no_atual.valor:
          no_atual.pai.filhoE = no_atual.filhoD
       
      #nó à direita do nó removido não tem um filho à esquerda 
      else:
        #assumindo a posição do nó q foi removido
        no_atual.filhoE.pai = no_atual.filhoD
        no_atual.filhoD.filhoE = no_atual.filhoE
        
        no_atual.filhoD.pai = no_atual.pai
        if no_atual.pai.filhoD and no_atual.pai.filhoD.valor == no_atual.valor:
          no_atual.pai.filhoD = no_atual.filhoD
        if no_atual.pai.filhoE and no_atual.pai.filhoE.valor == no_atual.valor:
          no_atual.pai.filhoE = no_atual.filhoD
  
    #nó removido só tem filho à direita
    elif no_atual.filhoD:  
      
      no_atual.filhoD.pai = no_atual.pai
      if no_atual.pai.filhoD and no_atual.pai.filhoD.valor == no_atual.valor:
        no_atual.pai.filhoD = no_atual.filhoD
      if no_atual.pai.filhoE and no_atual.pai.filhoE.valor == no_atual.valor:
        no_atual.pai.filhoE = no_atual.filhoD
    
    #nó removido só tem filho à esquerda    
    elif no_atual.filhoE:
      
      no_atual.filhoE.pai = no_atual.pai
      if no_atual.pai.filhoD and no_atual.pai.filhoD.valor == no_atual.valor:
        no_atual.pai.filhoD = no_atual.filhoE
      if no_atual.pai.filhoE and no_atual.pai.filhoE.valor == no_atual.valor:
        no_atual.pai.filhoE = no_atual.filhoE
        
    #nó removido não tem filho    
    else:
      
      if no_atual.pai.filhoD and no_atual.pai.filhoD.valor == no_atual.valor:
        no_atual.pai.filhoD = None
      if no_atual.pai.filhoE and no_atual.pai.filhoE.valor == no_atual.valor:
        no_atual.pai.filhoE = None
      
      no_atual.pai = None  
        
  
  def transformar_no_em_raiz(self, nome):
    nome_index = lista_suspeitos_nomes.index(nome)
    cpf = lista_suspeitos_cpfs[nome_index]
    
    no_atual = (self.busca(cpf))[0]
    
    #enquanto ainda não chegou na raiz...
    while no_atual.pai and (self.busca(cpf))[1] != 0:
      
      #giro pra direita, vai subir pra direita
      if no_atual.pai.filhoE and no_atual.valor == no_atual.pai.filhoE.valor:
        
        #nó que for subir tem filho á direita
        if no_atual.filhoD:
          
          #o nó pai pega o filho À direita do nó atual
          no_atual.filhoD.pai = no_atual.pai
          no_atual.pai.filhoE = no_atual.filhoD
          
          #nó subindo
          no_atual.filhoD = no_atual.pai
          
          #tem algo acima do pai
          if no_atual.pai.pai:
          
            if no_atual.pai.pai.filhoD and no_atual.pai.pai.filhoD.valor == no_atual.pai.valor: 
              no_atual.pai.pai.filhoD = no_atual
            elif no_atual.pai.pai.filhoE and no_atual.pai.pai.filhoE.valor == no_atual.pai.valor:  
              no_atual.pai.pai.filhoE = no_atual          
            
            no_atual.pai = no_atual.pai.pai
            
          else:
            no_atual.pai = None  
          
          no_atual.filhoD.pai = no_atual
          
        #nó que for subir não tem filho à direita  
        else:
          
          #nó subindo
          no_atual.filhoD = no_atual.pai
          
          #tem algo em cima do pai
          if no_atual.pai.pai:
          
            if no_atual.pai.pai.filhoD and no_atual.pai.pai.filhoD.valor == no_atual.pai.valor: 
              no_atual.pai.pai.filhoD = no_atual
            elif no_atual.pai.pai.filhoE and no_atual.pai.pai.filhoE.valor == no_atual.pai.valor:  
              no_atual.pai.pai.filhoE = no_atual          
            
            no_atual.pai = no_atual.pai.pai
            
          else:
            no_atual.pai = None
          
          
          no_atual.filhoD.pai = no_atual
          no_atual.filhoD.filhoE = None
        
      #giro pra esquerda, vai subir pra esquerda
      elif no_atual.pai.filhoD.valor and no_atual.valor == no_atual.pai.filhoD.valor:
        
        #nó que for subir tem filho á esquerda
        if no_atual.filhoE:
          
          #o nó pai pega o filho À esquerda do nó atual
          no_atual.filhoE.pai = no_atual.pai
          no_atual.pai.filhoD = no_atual.filhoE
          
          #nó subindo
          no_atual.filhoE = no_atual.pai
          
          
          #tem algo em cima do pai
          if no_atual.pai.pai:
          
            if no_atual.pai.pai.filhoD and no_atual.pai.pai.filhoD.valor == no_atual.pai.valor: 
              no_atual.pai.pai.filhoD = no_atual
            elif no_atual.pai.pai.filhoE and no_atual.pai.pai.filhoE.valor == no_atual.pai.valor:  
              no_atual.pai.pai.filhoE = no_atual          
          
            no_atual.pai = no_atual.pai.pai
          
          else:
            no_atual.pai = None
          
          no_atual.filhoE.pai = no_atual
            
          
        #nó que for subir não tem filho à esquerda 
        else:
          
          #nó subindo
          no_atual.filhoE = no_atual.pai
          
          
          #tem algo em cima do pai
          if no_atual.pai.pai:
          
            if no_atual.pai.pai.filhoD and no_atual.pai.pai.filhoD.valor == no_atual.pai.valor: 
              no_atual.pai.pai.filhoD = no_atual
            elif no_atual.pai.pai.filhoE and no_atual.pai.pai.filhoE.valor == no_atual.pai.valor:  
              no_atual.pai.pai.filhoE = no_atual          
            
            no_atual.pai = no_atual.pai.pai
            
          else:
            no_atual.pai = None  
          
          no_atual.filhoE.pai = no_atual
          no_atual.filhoE.filhoD = None
    
    self.raiz = no_atual    
      
  def busca(self, cpf, altura=0, no_atual=None):
    
    if altura == 0:
      no_atual = self.raiz
    
    if no_atual and cpf == no_atual.valor:
      return no_atual, altura
    
    elif no_atual and no_atual.filhoE and cpf < no_atual.valor:
      altura += 1
      return self.busca(cpf, altura, no_atual.filhoE)
      
    elif no_atual and no_atual.filhoD and cpf > no_atual.valor:
      altura += 1
      return self.busca(cpf, altura, no_atual.filhoD)  




entrada = input()
lista_suspeitos_cpfs = list()
lista_suspeitos_nomes = list()

while entrada != "--- REAÇÕES ---":
  entrada = input()
  
  if entrada != "--- REAÇÕES ---":
    entrada_splitada = entrada.split()
    
    lista_suspeitos_cpfs.append(int(entrada_splitada[1]))
    lista_suspeitos_nomes.append(entrada_splitada[2])
    
arvore = Arvore_bi()
arvore.criarArvore(lista_suspeitos_cpfs, lista_suspeitos_nomes)    

reacao_raiz = "disse que achou a coca saborosa."
reacao_raiz = reacao_raiz.split()

reacao_remocao = "doou uma coca café para a Taylor!"
reacao_remocao = reacao_remocao.split()

while entrada != "FIM":
  entrada = input()
  if entrada != "FIM":
    entrada_splitada = entrada.split()
    nome = entrada_splitada[0]
    entrada_splitada.remove(nome)
    
    nome_index = lista_suspeitos_nomes.index(nome)
    cpf = lista_suspeitos_cpfs[nome_index]
    
    
    if entrada_splitada == reacao_raiz:
      print(f"{nome} virou o principal suspeito e estava no nível {(arvore.busca(cpf))[1]}.")
      arvore.transformar_no_em_raiz(nome)
      
    elif entrada_splitada == reacao_remocao:
      print(f"{nome} deixou de ser o principal suspeito e estava no nível {(arvore.busca(cpf))[1]}.")
      arvore.remocao(nome)
      
      
print(f"{arvore.raiz.nome} foi declarado o ladrão da coca!")