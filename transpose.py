x=[]
print('enter the elemets of the matrices')
for i in range(3):
  a=[]
  for j in range(3):

    a.append(int(input()))
  
  x.append(a)

b=[[0,0,0],[0,0,0],[0,0,0]]

for m in range(3):
  for n in range(3):
    b[m][n]=x[n][m]

if x==b:
  print('given matrices is transpose')

else:

  print('not transpose')


