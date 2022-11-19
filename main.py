def observed():
  observations = []

  for count in range(7):
    print("Please enter an observation:")
    observations.append(input())

  return observations

def run():
  print("Counting observations...")
  observations = observed()