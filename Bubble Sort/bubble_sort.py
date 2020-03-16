def bubble_sort(vetor):
    for i in range(len(vetor)-1,0,-1):
        for j in range(i):
            if vetor[j+1] < vetor[j] :
                aux =  vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = aux
                
if __name__ == "__main__":
    vetor = [9, 5, 2, 3, 1 ,0, 7, 13, 10]
    print("Vetor desordenado: " + str(vetor) )
    print()
    bubble_sort(vetor)
    print("Vetor Ordenado: " + str(vetor))