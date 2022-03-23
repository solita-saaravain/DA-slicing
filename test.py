#simple test to prepare for next excerise to see if IDE is working
answer = input("Is this working? Y = yes, N = no: ")

#let's trim the given input and change it into UpperCase
answer = answer.strip().upper()

#check the input and act accordingly
if answer == "Y":
    print("It is working! Great success!")
if answer == "N":
    print("Not working, totally not!")
else:
    print("Please read the instruction and give a valid answer.")
