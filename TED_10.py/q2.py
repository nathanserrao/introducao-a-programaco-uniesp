#Faça um algoritmo para ler 50 números e armazenar em um vetor VET,
#verificar e escrever se existem números repetidos no vetor VET e
#em que posições se encontram.


import random

vet = []


for x in range(50):
    
    vet.append(random.randint(0, 100))

print(f'O vetor criado foi: {vet}')


for i in range(0, len(vet)):
    
    print(f'VALOR TESTADO: {vet[i]} | ÍNDICE TESTADO: {i}')
    
    for j in range(0, len(vet)):
        
        if vet[i] == vet[j] and i != j:
            print(f'Índice: {j} | Valor: {vet[j]} \n')
