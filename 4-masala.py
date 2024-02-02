a = [int(x) for x in input().split()]
s = int(input())
c = 0
for i in a:
  c+=i
if s-c>0:
  print(s-c)
else:
  print(0)
