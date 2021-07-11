x = []
while True:  
  print("1. Add number")
  print("2. exit")

  choice1 = int(input("Enter the Choice:"))  
  
  if choice1 == 1:
       
    num=int(input('enter num: '))
    n=num%10
    y=n+1
    if(len(x)>=y):
      x[[n][0]].append(num)
      print(x)
    else:
      z=y-len(x)
      for i in range(z):
        x.append([])
      x[[n][0]].append(num)    
      print(x)
  elif choice1 == 2:
    break