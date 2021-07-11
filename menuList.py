myList=[]
while True:  
  print("1. Accept Data")  
  print("2. Delete data by value")  
  print("3. delete data by position")  
  print("4. sort")  
  print("5. reverse")  
  print("6. Print in sorted order without changing original list")  
  print("7. print in reverse order without changing original list")  
  print("8. display data") 
  print("0. Exit") 

  choice1 = int(input("Enter the Choice: "))  
  
  if choice1 == 1:
    element=input('enter Data: ')
    print("1) add at last position")
    print("2) add at given position")
    option=int(input('enter option: '))
    if option == 1:
      myList.append(element)
    elif option == 2:
      position=int(input('enter position: '))
      myList.insert(position, element)
        
  elif choice1 == 2:
    value=input('enter value to delete: ')
    myList.remove(value)
      
  elif choice1 == 3:
    print("1) delete last element")
    print("2) delete from particular position")
    option=int(input('enter option: '))
    if option == 1: 
      myList.pop()
    elif option == 2:
      position=int(input('enter position: '))
      myList.pop(position)
      
  elif choice1 == 4:
    print("1) ascending")
    print("2) descending")
    option=int(input('enter option: '))
    if option == 1: 
      myList.sort()
    elif option == 2:
      myList.sort(reverse=True)
    

  elif choice1 == 5:  
    myList.reverse()
  
  elif choice1 == 6:  
    K=[]
    K.extend(myList)
    K.sort()
    print(K)

  elif choice1 == 7:  
    K=[]
    K.extend(myList)
    K.sort(reverse=True)
    print(K)

  elif choice1 == 8:
    print("1) normal")
    print("2) numbered")
    option=int(input('enter option: '))
    if option == 1: 
      print(myList)
    elif option == 2:
      n=0
      for p in myList:
        print(n,p)
        n=n+1
    
  elif choice1 == 0:  
    break
      
  else:  
        print("Incorrect Choice.")  