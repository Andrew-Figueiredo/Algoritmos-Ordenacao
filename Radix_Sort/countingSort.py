from countingSort import countingSort

def countingSort(vetor):
    n = max(vetor)
    counter = [0 for i in range(n+1)]
    
    for i in range(len(vetor)):
        counter[vetor[i]] += 1

    acumulado = copy.deepcopy(counter)

    for i in range(1,n+1):
        acumulado[i] = acumulado[i] + acumulado[i-1]

    Ordenado= [0 for i in vetor]
    for i in range(len(vetor)-1,-1,-1):
        aux = acumulado[vetor[i]]
        Ordenado[aux-1] = vetor[i]
        acumulado[vetor[i]] -= 1
    vetor[:] = Ordenado[:]



if __name__ == "__main__":

    vetor = [9, 5, 2, 3, 1 ,0, 7, 13, 10]
    print("Vetor desordenado: " + str(vetor) )
    print()
    countingSort(vetor)
    print("Vetor Ordenado   : " + str(vetor))

