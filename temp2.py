"""
input:
123

output:
1,3,123,231,312
"""

n=input()
a=[]
for i in range(len(n)):
    k=[]
    c=""
    val=n
    for i in val:
        c=c+i
        j=c
        j=int(j)
        k.append(j)
    val=int(val)
    sans=[]
    for i in k:
        if i!=0 and val%i==0:
            if i not in sans:
                sans.append(i)
    if val not in sans:
        val.append(sans)
    a=a+sans
    n=n[1:]+n[0]

a=list(set(a))
a.sort()
print(*a,sep=",")
