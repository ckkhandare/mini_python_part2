s=input("Enter a string\n")
p=input("Enter a string\n")
count=0
i = s.find(p)
while i != -1:
  print('occurence on position=',i)
  i = s.find(p, i+1)
  count=count+1
print('count=',count)