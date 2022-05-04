#Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos.
# Imprima o resultado da soma de todos os valores da matriz no terminal;



import random



matriz_a = []



for i in range(10):
    
    matriz_aux = []
    
    for j in range(10):    
        matriz_aux.append(random.randint(0, 100))
    
    matriz_a.append(matriz_aux)        


for linha in matriz_a:
    print(linha)
    
print('\n \n')
    

resultado_soma = 0

for l in matriz_a:
    
    for c in l:
        
        resultado_soma += c

print(f'Resultado da Soma = {resultado_soma}')