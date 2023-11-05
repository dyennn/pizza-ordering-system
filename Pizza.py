print("Welcome to Deaniel's Pizzeria!\n")
order = []
price = float(0)
while True:
    try:
        discount = 0
        size = ["L", "M", "S"]
        size_price = {"L": 50, "M": 40, "S": 30}
        toppings = ["Mushroom", "Salami", "Mozzarella Cheese"]

        decision = input("Do you want to order? Y/N >> ").capitalize()

        if decision == "N":
            print("Have a great day!")
            break
        elif decision == "Y":
            age = int(input("What is your age?"))
            if age < 0:
                print("Invalid age")
            elif age > 60:
                print("10% senior discount applied")
                discount += 10
            else:
                print("There is no discount applicable")

            sze = input(f"What size do you want?\n{size} : ").capitalize()
            order += [sze]
            price += size_price[sze]
            print()

            tp = input(f"What toppings do you want to add?\n{toppings}: ").split()
            order.append(tp)
            for i in tp:
                price += 15
            print()

            drinks = input("What drinks do you want?\n")
            order.append(drinks)
            price += 20
            print(order)
            print(price)

            if price > 90:
                print("To customers who have higher")
        elif decision != "N" and "Y":
            print("Y/N only")
    except ValueError:
        print("Invalid Input")

    print(f"You ordered a {order[0]} sized pizza, topped with {', '.join(order[1])}, and a side of {order[2]}. Your "
          f"total is ₱{price}")
