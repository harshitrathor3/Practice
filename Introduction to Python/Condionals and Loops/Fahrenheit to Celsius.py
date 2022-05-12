# Read input as sepcified in the question
# Print output as specified in the question

def convert(i):
    print(i, int((i-32)*5/9))

i = int(input())
n = int(input())
t = int(input())

while i<=n:
    convert(i)
    i+=t