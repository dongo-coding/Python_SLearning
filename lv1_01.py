j=[]
m=int(input())
n=int(input())
for i in range(m,n+1):
  if i%7==0 and i%5!=0:
    j.append(str(i))
print(','.join(j))
