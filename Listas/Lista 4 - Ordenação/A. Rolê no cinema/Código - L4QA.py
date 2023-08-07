def merge(lista1, lista2):
  lista_mergeada = list()
  indice_lista1, indice_lista2 = 0, 0
  
  while indice_lista1 < len(lista1) and indice_lista2 < len(lista2):
    if lista1[indice_lista1] < lista2[indice_lista2]:
      lista_mergeada.append(lista1[indice_lista1])
      indice_lista1 += 1
    else:
      lista_mergeada.append(lista2[indice_lista2])
      indice_lista2 += 1

  lista_mergeada += lista1[indice_lista1:]
  lista_mergeada += lista2[indice_lista2:]
  
  return lista_mergeada

def merge_sort(lista):
  if len(lista) <= 1:
    return lista
  
  lista_esquerda = lista[:(len(lista)//2)]
  lista_direita = lista[(len(lista)//2):]  

  lista_esquerda = merge_sort(lista_esquerda)
  lista_direita = merge_sort(lista_direita)

  return merge(lista_esquerda, lista_direita)  



lista1 = input()
lista2 = input()

lista_total = lista1+","+lista2

lista_total = lista_total.split(",")

resultado_merge = merge_sort(lista_total)


print(f"Os amigos decidiram assistir a {resultado_merge[len(resultado_merge)//2]} que estava na posição {(len(resultado_merge)//2)+1} da lista.")