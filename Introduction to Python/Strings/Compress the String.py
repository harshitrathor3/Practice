import sys
def getCompressedString(input):
    res = input[0]
    t=input[0]
    cnt=-1
    for i in input:
        # print(res)
        if i==t:
            cnt+=1
        else:
            t = i
            if cnt>0:
                res+=str(cnt+1)
            res+=i
            cnt=0
    if cnt>0:
        res+=str(cnt+1)
    return res


string = sys.stdin.readline().strip()
ans = getCompressedString(string)
print(ans)
