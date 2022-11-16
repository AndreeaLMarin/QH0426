print("Program Started")
print("Please enter an ASCII code:")
code = int(input())
if (code not in range(32, 127)):
  print ("The character represented by the ASCII code {} is {}".format (code, chr(code)))
else:
  print("Sorry input a given range")


print("Program Ended")
