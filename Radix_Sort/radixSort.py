from Counting_Sort.countingSort import countingSort

def separacao(x):
    teste = []
    i = 1
    p = 0
    while(p!=len(str(x))):
        olha = x // i % 10
        teste.append(olha)
        i *= 10
        p += 1
    
    return teste.reverse()


def radixSort(A):
    pass

    

if __name__ == "__main__":
    A = [222, 333, 111, 555, 444, 777, 666 ]

