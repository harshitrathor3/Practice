from sys import stdin

def selectionSort(arr, n) :
    for i in range(n):
        m = i
        # t=0
        for j in range(i+1, n):
            if arr[j]<arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
        # print(t)
            



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    selectionSort(arr, n)
    printList(arr, n)

    t-= 1