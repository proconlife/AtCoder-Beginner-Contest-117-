n,m=map(int,input().split())
x=list(map(int,input().split()))
if n >= m :
    print(0)
    exit()
x.sort()

dif=[]
tmp=0
for i, xi in enumerate(x) :
    if i == 0 :
        tmp = xi
        continue
    dif.append(xi-tmp)
    tmp=xi

dif.sort()
for i in range(n-1):
    dif.pop()

print(sum(dif))
    
