from sys import stdin 

def sort012(arr, n):
    i=0
    nz=0
    nt=n-1
    while i<=nt:
        if arr[i]==0:
            arr[i], arr[nz] = arr[nz], arr[i]
            i+=1
            nz+=1
        elif arr[i]==2:
            arr[i], arr[nt] = arr[nt], arr[i]
            nt-=1
        else:
            i+=1
        # print(arr)
            
    
    
        
    

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1
