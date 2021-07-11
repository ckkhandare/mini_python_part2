dict1={}
while True:
  print(''' 1. Add new city and trees commonly found in the city.\n
  2. Display all cities and the list of trees for all cities.\n
  3. Display list of trees of a particular city.\n
  4. Display cities which have the given tree.\n
  5. Delete city\n
  6. Modify tree list\n
  7. Exit\n''')

  choice=int(input("enter choice: "))
  if choice==1:
    city=input("enter city name: ")
    if city in dict1:
      print("city already exists")
      tree = [item for item in input("Enter the tree items : ").split()]
      dict1[city]=dict1[city]+tree
    else:
      tree = [item for item in input("Enter the tree items : ").split()]
      dict1[city]=tree

  elif choice==2:
    print(dict1)
    
  elif choice==3:
    city=input('enter person name: ')
    if city in dict1:
      print(city,':',dict1[city])
    else:
      print('city does not exist')

  elif choice==4:
    for city in dict1:
      if (dict1[city]!=[]):
        print(city)


  elif choice==5:
    city=input('enter person name: ')
    if city in dict1:
      print(city,' will be permanently deleted')
      conf=input('type y to continue and n to cancel: ')
      if conf=='y':
        del(dict1[city])
        print('item deleted')
      else:
        print('item not deleted')
    else:
      print('city does not exist')
  elif choice==6:
    city=input("enter city name: ")
    if city in dict1:
      print("city already exists")
      tree = [item for item in input("Enter the tree items : ").split()]
      dict1[city]=dict1[city]+tree
    else:
      tree = [item for item in input("Enter the tree items : ").split()]
      dict1[city]=tree

  elif choice==7:
    break
  else:
    print("invalid choice")
