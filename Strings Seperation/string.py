n=int(input())
a=[]
if n>=1 and n<=10:
    for i in range(n):
        a.append(input())
for j in a:
    print("{} {}".format(j[::2],j[1::2]))
