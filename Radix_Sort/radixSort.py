
def countingSort(vetor, expoente):
    n = len(vetor)
    counter = [0]*(10)
    
    for i in range(0,n):
        index = (vetor[i]//expoente)
        counter[(index)%10 ] += 1

    acumulado = [0]*(n+1)

    for i in range(1,10):
        counter[i] += counter[i-1]

    i = n-1
    while i >= 0:
        aux = (vetor[i]//expoente)
        acumulado[counter[ (aux)%10 ] - 1] = vetor[i]
        counter[(aux)%10] -= 1
        i-=1
    vetor[:n] = acumulado[:n]

def radixSort(vetor):
    maior = max(vetor)
    expoente = 1

    while (maior/expoente) > 0 :
        countingSort(vetor,expoente)
        expoente *= 10


if __name__ == "__main__":

    vetor = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Vetor desordenado: " + str(vetor) )
    print()
    radixSort(vetor)
    print("Vetor Ordenado   : " + str(vetor))

