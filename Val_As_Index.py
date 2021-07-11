A=[5,6,7,3,5,8]
B = [-1]*len(A)

for i, x in enumerate(A):
  B.insert(x,i)
print(B)