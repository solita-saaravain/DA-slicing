start = input("Start calculation? Y/N ")
start = start.strip().upper()

if start == "Y":
    qty = input("How many products? ")
    unit_price = input("What is the unit price? ")
    total = float(qty) * float(unit_price)
    print("Total value of the order without discounts or taxes is $" + str(total))
    
    #Check state tax
    state = input("Give a 2-letter state code ")
    if state == "UT":
        state_tax = total * 0.0685
    if state == "NV":
        state_tax = total * 0.08
    if state == "TX":
        state_tax = total * 0.0625
    if state == "AL":
        state_tax = total * 0.04
    if state == "CA":
        state_tax = total * 0.0825

    state_tax = str(round(state_tax, 2))
    print("State tax is $" + str(state_tax))

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

    discount = str(round(discount, 2))
    print("Order discount is $" + str(discount))
    order_value = total + state_tax - discount
    #print("Your total order value is " + str(order_value))
else:
    print("Have a good day")
    