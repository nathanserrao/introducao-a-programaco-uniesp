#Faça um algoritmo para ler 20 números e armazenar em um vetor.
#Após a leitura total dos 20 números, o algoritmo deve escrever 
#esses 20 números lidos na ordem inversa.



import random

lista_de_numeros = []


for n in range(0, 20):
    lista_de_numeros.append(random.randint(0, 1000))
    
print(f'Lista de Números: {lista_de_numeros}')


for i in range(0, len(lista_de_numeros)):
    
    maior_numero = lista_de_numeros[i]
    maior_indice = i
    
    for j in range((i+1), len(lista_de_numeros)):
        
        if lista_de_numeros[j] >= maior_numero:
            maior_numero = lista_de_numeros[j]
            maior_indice = j
            
            
    lista_de_numeros.insert(i, lista_de_numeros.pop(maior_indice))
            
      
print(lista_de_numeros)