def observed():
  observations = set
  observations = {"Flying Car", "Sky Scaper", "Lase", "Dome"}
  return observations
def run():
  print(observed())
run()


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
  #print(l)
  #mySet = ()
  #mySet = {("a", 1) , ("b", 4), ("c", 1), ("d", 1)}

run()