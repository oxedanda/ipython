def main():
    amount_due = 50
    accepted_coins = [25, 10, 5]

    while amount_due > 0:
        coin = int(input("Insert Coin: "))

        if coin in accepted_coins:
            amount_due -= coin

        if amount_due > 0:
            print("Amount Due:", amount_due)

    print("Change Owed:", -amount_due)

main()