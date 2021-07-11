# set T is the base set 

names=input("Enter in names separated by a comma: ")
splt= names.split(",")
t=set()
for i in splt:
    t.add(i)
while True:
  print("""\n1. delete element if exists otherwise do not show any errr""")
  print("2. add a elemet")
  print("3. create one more set")
  print("4. union of 2 sets")
  print("5. intersection of 2 sets")
  print("6. difference of 2 sets")
  print("7. convert set into frozenset")
  print("8. exit")

  choice1 = int(input("Enter the Choice:"))  
  
  if choice1 == 1:  
    elem=input('enter the name you want to delete: ')
    t.discard(elem)
    print(t)

  elif choice1 == 2:
    x=input('enter a name to add: ')
    t.add(x)
      
  elif choice1 == 3:                                        #create as many sets but do not forget the set number
    names=input("Enter in names separated by a comma: ")    # the set no. can be used to call a perticular set
    enter=int(input('enter set number: '))
    splt= names.split(",")
    globals()['string%s' % enter]=set()
    for i in splt:
      globals()['string%s' % enter].add(i)
    print(globals()['string%s' % enter])


#All operations will be performed with the base set and the set that you select giving the set number 

  elif choice1 == 4:
    enter=int(input('enter set number: '))
    x=t |(globals()['string%s' % enter])
    print(x)

  elif choice1 == 5:
    enter=int(input('enter set number: '))
    y=t &(globals()['string%s' % enter])
    print(y)
  elif choice1 == 6:  
    enter=int(input('enter set number: '))
    z=t -(globals()['string%s' % enter])
    print(z)
  elif choice1 == 7:               # the base set is selected by default to be frozen
    x=frozenset(t)
    print(x)
  elif choice1 == 8:  
    break
  else:  
        print("Incorrect Choice.")

