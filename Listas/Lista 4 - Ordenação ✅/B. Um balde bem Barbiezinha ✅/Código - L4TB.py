def bolha_sortuda(letras, numeros):
  
  for ii in range(len(letras)):
    
    teve_troca = False
    for i in range(0, len(letras)-ii-1):

      if (letras[i] > letras[i+1]) or (letras[i] == letras[i+1] and numeros[i] > numeros[i+1]):
        letras[i], letras[i+1] = letras[i+1], letras[i]
        numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
        
        teve_troca = True
  
    if not teve_troca:
      break
    
  return letras, numeros     


n_sorteado = int(input())
letras = list()
numeros = list()

cadeiras = input()
cadeiras = cadeiras.split()

for cadeira in cadeiras:
  letras.append(cadeira[0])
  numeros.append(int(cadeira[1:]))

letras, numeros = bolha_sortuda(letras, numeros)

#print(cadeiras)
print(f"O vencedor está na fila {letras[n_sorteado-1]} poltrona {numeros[n_sorteado-1]}!")