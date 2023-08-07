def heapify(arr, n, i):
  global isabela_m
  
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2

  isabela_m += 1
  if left < n and arr[i] < arr[left]:
    largest = left

  isabela_m += 1
  if right < n and arr[largest] < arr[right]:
    largest = right
  
  isabela_m += 1
  if largest != i:
    isabela_m += 2
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)
  
def heap_sort(arr):
  global isabela_m
  
  n = len(arr)

  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  #for i in range(n - 1, 0, -1):
  #  isabela_m += 2
  #  arr[i], arr[0] = arr[0], arr[i]
  #  isabela_m += heapify(arr, i, 0)


def shell_sort(lista, bianca_m=0):
  intervalo = len(lista)//2
  
  while intervalo >= 1:
    for indice in range(intervalo, len(lista)):
      j = indice
      while j >= intervalo and lista[j-intervalo] > lista[j]:
        bianca_m += 1
  
        lista[j-intervalo], lista[j] = lista[j], lista[j-intervalo]
        j -= intervalo
        bianca_m += 2
        
      if j >= intervalo:
        bianca_m += 1
        
    intervalo //= 2    

  return bianca_m
 
  
def selection_sort(arr, joaquim_m=0):
    n = len(arr)

    # Percorre todo o array
    for i in range(n):
        # Encontra o índice do menor elemento não ordenado
        min_idx = i
        for j in range(i + 1, n):
            joaquim_m += 1    #MINUTAGEM AQUIIIIIIIIIIII
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Troca o elemento encontrado com o primeiro elemento não ordenado
        if i != min_idx:  
          joaquim_m += 2   #MINUTAGEM AQUIIIIIIIIIIII
          arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return joaquim_m


def partition(arr, low, high):
    global mateus_m
  
    # Seleciona o pivô (último elemento)
    pivot = arr[high]
    # Inicializa o índice do menor elemento
    i = low - 1

    for j in range(low, high):
        # Se o elemento atual for menor ou igual ao pivô
        mateus_m += 1
        if arr[j] <= pivot:
            # Incrementa o índice do menor elemento e troca os elementos
            i += 1
            mateus_m += 2
            arr[i], arr[j] = arr[j], arr[i]

    # Coloca o pivô na posição correta
    mateus_m += 2
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    global mateus_m
  
    if low < high:
        # Obtém o índice do pivô
        pi = partition(arr, low, high)

        # Ordena os elementos à esquerda e à direita do pivô
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


lista = input()
lista = lista.split()
for i in range(len(lista)):
  lista[i] = int(lista[i])


lista_heap = lista[:]
lista_quick = lista[:]
lista_selection = lista[:]
lista_shell = lista[:]


isabela_m = 0
heap_sort(lista_heap)

mateus_m = 0
quick_sort(lista_quick, 0, len(lista_quick) - 1)

bianca_m = shell_sort(lista_shell)

joaquim_m = selection_sort(lista_selection)

class Node:
  def __init__(self, nome, tempo):
    self.nome = nome
    self.tempo = tempo

isabela = Node("Isabela", isabela_m)
mateus = Node("Mateus", mateus_m)
joaquim = Node("Joaquim", joaquim_m)
bianca = Node("Bianca", bianca_m)

menor_tempo = min(isabela_m, mateus_m, joaquim_m, bianca_m)
lista_nomes = [isabela, mateus, joaquim, bianca]
lista_nomes_menor_tempo = list()

for node in lista_nomes:
  if node.tempo == menor_tempo:
    lista_nomes_menor_tempo.append(node)
    
if len(lista_nomes_menor_tempo) == 1:
  print(f"{lista_nomes_menor_tempo[0].nome} vai assistir o filme da Barbie com seu combo novo após levar {menor_tempo} minutos para descobrir o assassino.")
else:
  for c in range(len(lista_nomes_menor_tempo)):
    if len(lista_nomes_menor_tempo) == c+1:
      print(f"{lista_nomes_menor_tempo[c].nome}", end=" ")
    else:
      print(f"{lista_nomes_menor_tempo[c].nome}", end=", ")
  print(f"vão assistir o filme da Barbie com seu combo novo após levar {menor_tempo} minutos para descobrir o assassino.")