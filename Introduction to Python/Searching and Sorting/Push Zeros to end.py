from sys import stdin

def pushZerosAtEnd(arr, n):
    i=0
    j=1
    while j<n and i<n:
        # print(arr)
        # print(i, j)
        if arr[i]!=0:
            i+=1
        if arr[j]==0:
            j+=1
        if j>=n or i>=n:
            break
        if arr[i]==0 and arr[j]!=0:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j+=1
        






#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split()))
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

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1
