print("Enter the number of rows and columns")
n, m =map(int, input().split())
print("Enter Seat Status")
arr = []
for i in range(n):
    lst = []
    for j in range(m):
        lst.append(input())
    arr.append(lst)



print(arr)