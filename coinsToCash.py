def calc_dollars(**coins):
    # The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it.
    dollarAmount = 0
    for key, value in coins.items():
        if key == "pennies":
            dollarAmount += value / 100
        elif key == "nickels":
            dollarAmount += value / 20
        elif key == "dimes":
            dollarAmount += value / 10
        elif key == "quarters":
            dollarAmount += value / 4
    print(dollarAmount)
        

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)