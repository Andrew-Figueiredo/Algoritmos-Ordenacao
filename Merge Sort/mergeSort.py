def intercalacao(vetor, esq, d):
    i=j=k=0

    while i < len(esq) and j < len(d): 
        if esq[i] < d[j]: 
            vetor[k] = esq[i] 
            i+=1
        else: 
            vetor[k] = d[j] 
            j+=1
        k+=1

    while i < len(esq): 
        vetor[k] = esq[i] 
        i+=1
        k+=1
        
    while j < len(d): 
        vetor[k] = d[j] 
        j+=1
        k+=1

def mergeSort(vetor):
    n = len(vetor)
    if n > 1:
        m = n//2
        l = vetor[:m]
        r = vetor[m:]
        mergeSort(l)
        mergeSort(r)
        intercalacao(vetor,l,r)    


if __name__ == "__main__":
    
    vetor = [1,3,5,7,4,2,4,6,10,8]
    
    print(vetor)

    mergeSort(vetor)
    print()


    print(vetor)
