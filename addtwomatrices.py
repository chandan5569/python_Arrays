x=[]

print('enter the elements of first matrices')

for i in range(3):

  a=[]

  for j in range(3):

    a.append(int(input()))

  x.append(a)

print('first matrices after inserting will lokk like')

for g in range(3):
  print(x[g])

print('enter the elements of second matrices')
y=[]

for m in range(3):

  b=[]

  for n in range(3):

    b.append(int(input()))
  y.append(b)

print('second matrices after inserting will looks like')

for h in range(3):
  print(y[h])

print('After addition ')

z=[[0,0,0],[0,0,0],[0,0,0]]

for u in range(3):
  for v in range(3):
    z[u][v]=x[u][v]+y[u][v]

for t in range(3):

  print(z[t])


