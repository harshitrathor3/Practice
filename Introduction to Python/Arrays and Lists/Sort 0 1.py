from sys import stdin

def sortZeroesAndOne(arr, n) :
    cnt=0
    i=0
    j=n-1
    while i<=j-1:
        if arr[i]==0:
            i+=1
        if arr[j]==1:
            j-=1
        if arr[i]==1 and arr[j]==0 and i<=j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
        # print(arr, i, j)
        
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    # print()

    t -= 1
