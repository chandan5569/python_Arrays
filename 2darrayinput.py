x=[]
print('enter the elements inside the 2d array')
for i in range(0,3):

  a=[]

  for j in range(0,3):

    a.append(int(input()))                  # a is the sub array


  x.append(a)                               # x is the final array


for c in range(3):

  print(x[c])

