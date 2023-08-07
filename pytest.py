def shell_sort(lista, bianca_m=0):
  intervalo = len(lista)//2
  
  while intervalo >= 1:
    for indice in range(intervalo, (len(lista))-1):
      if lista[indice-intervalo] < lista[indice]:
        bianca_m += 1
        
        lista[indice-intervalo], lista[indice] = lista[indice], lista[indice-intervalo]
        bianca_m += 2
        
    intervalo //= 2    

  print(lista)
  return bianca_m

lista = input()
lista = lista.split()

#isabela = heapSort(lista)
#mateus = quickSort(lista)
#joaquim = selectionSort(lista)
#bianca = shell_sort(lista)

print(shell_sort(lista))

#print(min(isabela_m, mateus_m, joaquim_m, bianca_m))

