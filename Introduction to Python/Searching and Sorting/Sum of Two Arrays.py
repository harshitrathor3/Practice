from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output):
    num1 = 0
    for i in arr1:
        num1+=i
        num1*=10
    num1//=10
    num2 = 0
    for i in arr2:
        num2+=i
        num2*=10
    num2//=10
    s = num1+num2
    i = len(output)-1
    while s!=0:
        output[i]=s%10
        s//=10
        i-=1
    # print('o ', output)
           




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
    arr1, n = takeInput()
    arr2, m = takeInput()
    
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    
    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)
    
    t -= 1