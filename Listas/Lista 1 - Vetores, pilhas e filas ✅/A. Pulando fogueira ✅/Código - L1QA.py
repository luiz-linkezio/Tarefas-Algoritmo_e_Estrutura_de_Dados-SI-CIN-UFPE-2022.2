class Pessoa():
  
  def __init__(self, n, nome, pulos):
    
    self.n = n
    self.nome = nome
    self.pulos = pulos
    
  def pular(self):
    len_pulos = len(self.pulos)
    pulada_atual = int(self.pulos[0])
    passadas_total = 0
    pulos_total = 0
    passada_anterior = 0
    
    while passadas_total < (len_pulos-1) and pulada_atual != 0:
      pulada_atual = int(self.pulos[passadas_total])
      passadas_total += pulada_atual
      pulos_total += 1
    
      
    if passadas_total >= (len_pulos-1):
      print(f"{self.nome} conseguiu!\n{self.nome} precisou pular {pulos_total} fogueiras")
    
    else:
      print(f"Ah, que pena, {self.nome} não conseguiu!")

      
for i in range(4):
  n = int(input())
  nome_pulos = input()
  nome_pulos = nome_pulos.split()
  nome = nome_pulos[0]
  pulos = nome_pulos
  pulos.remove(nome)
  
  participante = Pessoa(n, nome, pulos)
  participante.pular()