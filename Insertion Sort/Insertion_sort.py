def Insertion_sort(list):
    for index in range (1, len(list)):
        value = list[index]
        i = index -1
        while i>=0: 
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i = i-1
            else:
                break

if __name__ == "__main__":
    vetor = [9, 5, 2, 3, 1 ,0, 7, 13, 10]
    print("Vetor desordenado: " + str(vetor) )
    print()
    Insertion_sort(vetor)
    print("Vetor Ordenado: " + str(vetor))