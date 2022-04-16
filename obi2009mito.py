n = int(input())
arr = []
s = 0 
for i in range(0, n):
    x, y = [int(v) for v in input().split()]
    val = [x,y]
    arr.append(val)
for i in range(0, len(arr)):
    if arr.count(arr[i]) > 1:
        s += 1
if s >= 1:
    print(1)
elif s == 0:
    print(0)
    
      