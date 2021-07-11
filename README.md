# mini_python_part2
More challenging small python codes to test your logic

## Problem statements

1. Write a menu driven program to practice String functions
    Design following meu
    a. display characters from even position
    b. display characters from odd position
    c. display length of a string
    d. add a at the end of string length times
    e. exit
2. Write a program to accept a string from user.
    Accept a second string and find all occurrences of second string in the first string.
    e.g
    s1=This is string
    check=is
    is-2
    is-5
    count=2

    s1=”this is cat and cat is cute, where is your cat?”
    check=cat
    cat-8
    cat-16
    cat-43
    count=3

3. Write a menu driven program to practice List functions. Validate input data wherever
    required.
    Display following menu:
    1. Accept Data
    a) add at last position
    b) add at given position
    2. Delete data by value
    display message deleted successfully
    or not found
    3. delete data by position
    a) delete last element
    b) delete from particular position
    4. sort
    a) ascending
    b) descending
    5. reverse
    6. Print in sorted order without changing original list
    7. print in reverse order without changing original list
    8. display data
    a) normal
    b) numbered

4. Create two lists to store cities and locations by accepting values from user.
    Display 1st city and 1st location
    then 2nd city and 2nd location ....... (zip function)
5. Create a list and exchange the values as index and index as values.
    lst=[12, 1, 3, 7, 8, 5, 8]
    0 1 2 3 4 5 6
    Output should be as follows.
    lst1=[-1 ,1, -1, 2, -1, 5, -1, 3, 6, -1, -1, -1, 0]

6. Write a menu driven program to practice Set functions.
    Write a program to accept names from users and store it in a set.
    Display the following menu:
    print("""1. delete element if exists otherwise
    do not show any errr""")
    print("2. add a elemet")
    print("3. create one more set")
    print("4. union of 2 sets")
    print("4. intersection of 2 sets")
    print("5. difference of 2 sets")
    print("6. convert set into frozenset")
    print("6. exit")

7. Generate a list of lists (NOTE: List should get generated dynamically)
    Accept a number from user and check last digit of the number.
    If it is 1 then add it in the list at 1st position.
    If 0 then it should get added at list in 0th position.
    e.g list should look as follows
    [[10],[51],[52]]
    [[10,30,20,40],[11,31,41,31],[22,32,42]....]
    if user enters 15 then the resultant list should be
    [[10,30,20,40],[11,32,41,31],[22,32,42],[],[],[15]]
8. Create a list to store strings in a list in following manner list
    [dxz,axz,bat,rat,cat,pat,bbc,bbm,cbm,....] pat axz
    All list with same character at second position should be consecutive.
    If user adds sat, then the resultant list will be:
    [bat,rat,cat,sat,bbc,bbm,cbm,....]
    If user adds pick, then it should be added at
    [bat,rat,cat,bbc,bbm,cbm,pick]

9. Write a menu driven program to practice Dictionary functions.
    Write a program to accept name of a person and their vehicle and store it in a dictionary.
    Ask user if they want to continue to accept multiple values.
    Display following menu:
    1. Add new person name and a vehicle name.
    2. Delete a person name and vehicle name from the dictionary.
    ----Accept person name from user.
    ----Check whether person name exists in the dictionary.
    ----If exists show person name and vehicle name to the user.
    ----Confirm for deletion, if user enters y
    then delete otherwise no. Display appropriate message.
    3. Modify vehicle name for the person
    ----Accept a person name from user.
    ----Check whether the person’s name exists.
    ----If the name exists, show the person’s name and vehicle name to user.
    Ask for new value and then overwrite the old value.
    4. Search vehicle for the given person’s name.
    5. Search list of people, who have given a vehicle
    6. Display all person names.
    7. Display all vehicle names.
    8 Exit

10. Write a program to display following menu and do the following:
    1. Add new city and trees commonly found in the city.
    2. Display all cities and the list of trees for all cities.
    3. Display list of trees of a particular city.
    ---- Accept a city from user search city and if found display list of trees otherwise
    ---- Display message not found
    4. Display cities which have the given tree.
    ---- Accept a tree name from user and display all cities in which the tree is found.
    5. Delete city
    ---- Accept city from user and delete the city if found.
    ---- Prompt user before deletion
    6. Modify tree list
    ---- Accept city and trees to be added in the city. if city exist add trees at the end
    of the list
    ---- Otherwise add city and list
    7. Exit
