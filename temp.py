def pr(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
n = input()
l=list(ord(x) for x in n)
le=len(n)
sl=[]
for i in range(le):
    for j in range(le):
        for k in range(le):
            sl.append(str(l[i])+str(l[j])+str(l[k]))
nl = list(int(x) for x in sl)
pl = list(str(x) for x in nl if pr(x))
al=[]
for x in pl:
    al.append(chr(int(x[0:2]))+chr(int(x[2:4]))+chr(int(x[4:6])))
if(al):
    print(",".join(al))
else:
    print(-1)