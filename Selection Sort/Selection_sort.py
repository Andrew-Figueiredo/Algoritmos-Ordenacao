def Selection_Sort(vector):
    for id in range(0,len(vector)):
        min_id = id

        for r in range(id + 1, len(vector)):
            if vector[r] < vector[min_id]:
                min_id = r

        vector[id], vector[min_id] = vector[min_id], vector[id]

if __name__ == "__main__":
    vetor = [9, 5, 2, 3, 1 ,0, 7, 13, 10]
    print("Vetor desordenado: " + str(vetor) )
    print()
    Selection_Sort(vetor)
    print("Vetor Ordenado: " + str(vetor))