#Greet the user
start = input("Start calculation? Y/N ")

#Strip and change to uppercase
start = start.strip().upper()

if start == "Y":
    qty = input("How many products? ")
    check_qty = qty.isnumeric()
    if check_qty == True:

        unit_price = input("What is the unit price? ")
    #    check_up = unit_price.isnumeric()
    # separators 
    #    if check_up == True:

        total = float(qty) * float(unit_price)
        order_total = tax = str(round(total, 2))
        print("Total value of the order without discounts or taxes is $" + str(order_total))
        
        #Check state tax

        state = input("Choose state UT, NV, TX, AL or CA: ")
        state = state.strip().upper()
        states = {"UT":"0.0685", "NV":"0.08", "TX":"0.0625", "AL":"0.04", "CA":"0.0825"}
        state_tax = total * float(states[""+ state + ""])
        '''if state == "UT":
            state_tax = total * 0.0685
        if state == "NV":
            state_tax = total * 0.08
        if state == "TX":
            state_tax = total * 0.0625
        if state == "AL":
            state_tax = total * 0.04
        if state == "CA":
            state_tax = total * 0.0825'''

        tax = str(round(state_tax, 2))
        print("State tax is             $" + str(tax))

        #Check discount
        if total <= 999:
            print("No discount")
        elif total <= 4999:
            discount = total * 0.03
        elif total <= 6999:
            discount = total * 0.05
        elif total <= 9999:
            discount = total * 0.07
        elif total <= 49999:
            discount = total * 0.10
        else:
            discount = total * 0.15

        disc = str(round(discount, 2))
        print("Order discount is         $-" + str(disc))
        order_value = total +state_tax - discount
        order_value = str(round(order_value, 2))
        print("Your total order value is $" + str(order_value))
    #    else:
    #        print("Give a number!")
    else: 
            print("Give a number!")
else:
    print("Have a good day")
    