answer = input("Is this working? Y = yes, N = no: ")
answer = answer.strip().upper()

if answer == "Y":
    print("It is working! Great success!")
if answer == "N":
    print("Not working, totally not!")
else:
    print("Please read the instruction and give a valid answer.")
