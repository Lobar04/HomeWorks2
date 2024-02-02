n = int(input())
if n>=38 and ((n+1)%5==0 or (n+2)%5==0):
  if (n+1)%5==0:
    print(n+1)
  else:
    print(n+2)
else:
  print(n)
