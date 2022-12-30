import random
ask = input("Wanna roll a dice?(y/n)")
if(ask == "y"):
    no = random.randint(1,6)
    print("---",no,"---")
    if (no == 1):
      print()
      print("    0    ")
      print()
    elif (no == 2):
      print("0        ")
      print()
      print("        0")
    elif (no == 3):
      print("        0")
      print("    0    ")
      print("0        ")
    elif (no == 4):
      print("0       0")
      print()
      print("0       0")
    elif (no == 5):
      print("0       0")
      print("    0    ")
      print("0       0")
    else:
      print("0      0")
      print("0      0")
      print("0      0")
    print("---",no,"---")
    
elif(ask == "n" ):
   ask = input("Wanna roll a dice?(y/n)")
else: 
   print("Error! dumbass type y for yes n for no")
