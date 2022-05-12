from sys import stdin

def reverse(arr, i, j):
    if j-i==1:
        arr[i], arr[j] = arr[j], arr[i]
        return
    while i<=(i+j)//2:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1

def rotate(arr, n, d):
    # print(arr)
    reverse(arr, 0, n-1)
    # print(arr)
    reverse(arr, 0, n-d-1)
    # print(arr)
    reverse(arr, n-d, n-1)
    # print(arr)
    
    


#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
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
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1