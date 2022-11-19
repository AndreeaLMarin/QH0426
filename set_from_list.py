def observed():
  observations = set()
  for i in range(7):
    item = input("Enter an item: ")
    observations.add(item)
  return observations
def run():
  print("Counting observations...")
  l = observed()
  for i in l:
    print(i)
    count = count + 1
    print(i)
  
  








#The program should consist of the following two functions:
#The first function should be named observed and should have no parameters.
The function should create a list named observations.
The function should populate the list with 7 values read in from the user.  There should be some duplicate values.
Finally, the function should return the list named observations.
The second function should be named run and should have no parameters.
The function should start by displaying the message "Counting observations...".
The function should then call the first function and store the returned list in a local variable.
The function should then create a set that contains a tuple for each unique value in the list along with a count for how many times that value appeared in the list e.g. ("Skyscraper", 2)
Finally, the function should display the content of the set.
