ini_list = []
ini_list = [item for item in input("Enter the list items space seprated: ").split()]
# printing initial list
print ("initial list", str(ini_list))
  
# code to sort list
ini_list.sort(key = lambda x: x[1])
      
# printing result
print ("result", str(ini_list))