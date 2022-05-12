from sys import stdin

def merge(arr1, n, arr2, m):
    new = []
    if n==0 or m==0:
        return arr1+arr2
    i=j=0
    while i<n and j<m:
        # print(new)
        if arr1[i]<=arr2[j]:
            new.append(arr1[i])
            i+=1
        else:
            new.append(arr2[j])
            j+=1
    new+=arr1[i:]
    new+=arr2[j:]
    return new


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()

#main
t = int(stdin.readline().rstrip())
while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()
    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))
    t -= 1
