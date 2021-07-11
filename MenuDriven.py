while True:  
  print("1. display characters from even position")  
  print("2. display characters from odd position")  
  print("3. display length of a string")  
  print("4. add a at the end of string length times")  
  print("5. exit")  

  choice1 = int(input("Enter the Choice:"))  
  
  if choice1 == 1:  
    str = input("Enter a string\n")
    modified_string = str[::2]
    print(modified_string)
  
      
  elif choice1 == 2:
    str = input("Enter a string\n")
    modified_string = str[1::2]
    print(modified_string)
      
  elif choice1 == 3:  
    str = input("Enter a string\n")
    print(len(str)) 
  elif choice1 == 4:  
    str = input("Enter a string\n")
    for i in range(len(str)):
      str=str+'a'
    print(str)
  elif choice1 == 5:  
    break
      
  else:  
        print("Incorrect Choice.")
