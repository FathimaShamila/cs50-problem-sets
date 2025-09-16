from cs50 import get_float
def main():

    while True:
        cents = get_float("Change:")
        if cents > 0:
            break
    cents = int(cents*100)
    #print(f"cents: {cents}")
    quarters = calculate_quarters(cents)
    #print(quarters)
    change = cents % 25
    dimes = calculate_dimes(change)
        #print(dimes)
    change = change % 10
    nickels = calculate_nickels(change)
        #print(nickels)
    pennies = change % 5
        #print(pennies)
    total_coins = quarters + dimes + nickels + pennies
    print(total_coins)

def calculate_quarters(cents):
    quarters = cents//25
    return quarters

def calculate_dimes(cents):
    dimes = cents//10
    return dimes

def calculate_nickels(cents):
    nickels = cents//5
    return nickels

def calculate_pennies(cents):
    pennies = cents//1
    return pennies




if __name__ == "__main__":
    main()
