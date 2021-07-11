dict1={}
while True:
  print(''' 1. Add new person name and a vehicle name.\n
  2. Delete a person name and vehicle name from the dictionary.\n
  3. Modify vehicle name for the person\n
  4. Search vehicle for the given person’s name.\n
  5. Search list of people, who have given a vehicle\n
  6. Display all person names.\n
  7. Display all vehicle names.\n
  8 Exit''')

  choice=int(input("enter choice: "))
  if choice==1:
    person=input("enter persons name: ")
    if person in dict1:
      print("person already exists")
      vehicle=input('enter vehicle name: ')
      dict1[person]=vehicle
    else:
      vehicle=input('enter vehicle name: ')
      dict1[person]=vehicle

  elif choice==2:
    person=input('enter person name: ')
    if person in dict1:
      del(dict1[person])
    else:
      print('person does not exist')
    
  elif choice==3:
    person=input('enter person name: ')
    if person in dict1:
      print(person,':',dict1[person])
      vehicle=input('enter new vehicle name: ')
      dict1[person]=vehicle
    else:
      print('person does not exist')
  elif choice==4:
    person=input('enter name of person: ')
    if person in dict1:
      print(dict1[person])
    else:
      print('person does not exist')

  elif choice==5:
    for person in dict1:
      if(dict1[person]!=''):
        print(person)
  elif choice==6:
    for person in dict1:
      print(person)
  elif choice==7:
    for person in dict1:
      print(dict1[person])
  elif choice==8:
    break
  else:
    print("invalid choice")
