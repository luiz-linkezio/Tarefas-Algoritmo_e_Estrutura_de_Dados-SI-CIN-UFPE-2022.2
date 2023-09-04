def roubo_maximo(joias): #Achar o maior roubo possível
    n = len(joias) #Quantidade de salas
    
    somas = [0] * n #Lista que vai armazenas as somas até o momento
    
    for i in range(n): #Percorre a lista de somas...      
      somas[i] = max(joias[i] + somas[i-2], somas[i-1]) #...escolhendo o máximo entre n-1 e n + n-2
    
    return somas[-1] #Retorna o último elemento da lista de somas

#Tratamento de input
salas = int(input())
joias_temp = input().split()
joias = []
for joia in joias_temp:
  joias.append(int(joia))

#Atribuindo o retorno da função à variável, função esta que descobre o maior roubo possível
roubo = roubo_maximo(joias)

print(f"{roubo} colares podem ser retirados.") #Print que a tarefa solicita