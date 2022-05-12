def f_to_c(f):
    return (f-32)*5/9


def printTable(start,end,step):
    for i in range(start, end+1, step):
        print(i, int(f_to_c(i)))

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)

