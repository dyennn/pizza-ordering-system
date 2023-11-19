pizza = []
drink = []
price: int = 0
mode_of_payment = ""
remove_this = ""

pizza_choice: dict[str, int] = {"Hawaiian": 299,
                                "Cheesy Bacon": 299,
                                "Vegetarian": 259,
                                "Margherita": 299,
                                "Pepperoni": 299}

drinks_choice: dict[str, int] = {"Coca Cola": 20,
                                 "Iced Lemon Tea": 20,
                                 "Pineapple Juice": 20,
                                 "Royal": 20,
                                 "Orange Juice": 20}


def get_pizza():
    """A function that asks the user what pizza they want to order"""
    while True:
        try:
            global price

            for p in pizza_choice:
                print(f"\t{p} : ₱{pizza_choice[p]}")

            get_this_pizza = input(f"\n\tWhat pizza would you like to get?: ").capitalize().strip()

            if "Cheesy" and "bacon" in get_this_pizza:
                get_this_pizza = "Cheesy Bacon"

            elif get_this_pizza not in pizza_choice:
                raise ValueError

            price += pizza_choice[get_this_pizza]
            pizza.append(get_this_pizza)

            print(f"\tCurrent total is: ₱{price}")

            decision = input("\n\tAdd more? [1]Yes [2] No : ")

            if decision == "1":
                continue
            elif decision == "2":
                break
            elif decision != "1" or "2":
                print("\tInvalid option")
                raise ValueError

        except ValueError:
            print(f"\tThere is no such option\n")


def get_drink():
    """A function that will ask the user what drinks they want to order"""
    while True:
        try:
            global price

            print(f"\n\tWhat drinks would you like to get?\t")

            for d in drinks_choice:
                print(f"\t{d} : ₱{drinks_choice[d]}")

            get_this_drink = input(f"\n\t: ").capitalize().strip()

            if "Coca" and "cola" in get_this_drink:
                get_this_drink = "Coca Cola"

            elif "Iced" and "lemon" and "tea" in get_this_drink:
                get_this_drink = "Iced Lemon Tea"

            elif "Pineapple" and "juice" in get_this_drink:
                get_this_drink = "Pineapple Juice"

            elif "Orange" and "juice" in get_this_drink:
                get_this_drink = "Orange Juice"

            price += drinks_choice[get_this_drink]
            drink.append(get_this_drink)

            print(f"\tCurrent total is: ₱{price}")

            decision = input("\n\tAdd more? [1]Yes [2] No : ")

            if decision == "1":
                continue

            elif decision == "2":
                break

            elif decision != "1" or "2":
                print("\tInvalid option")
                raise ValueError

        except ValueError:
            print(f"\tThere is no such option")


def leave():
    """A function that makes the user sure if they want to quit the program"""
    while True:
        try:
            sure = input(f"\n\tAre you sure you want to quit?\n\t[1]Yes\n\t[2]No\n\t: ").strip()
            if sure == "1":
                print(f"\n\tHave a great day!")
                quit()
            elif sure == "2":
                break
        except ValueError:
            print("Invalid input")


def change_order():
    """Asks the user if they want to replace/change an order"""
    while True:
        try:
            global price
            global remove_this

            if len(pizza) < 1 and len(drink) < 1:
                print("\tYou have no order")
                break
            else:
                what_to_change = input("\n\t[1]Remove an order [2]Replace an order [3]Back: ").strip()
                if what_to_change == "1":

                    if len(drink) < 1 <= len(pizza):
                        remove_this = input(f"\tWhat do you want to remove?"
                                            f"Your current order is {', '.join(pizza[::1])}: ")

                        if remove_this in pizza:

                            pizza.remove(remove_this)
                            price -= pizza_choice[remove_this]

                            print(f"\tYour current pizza/s are {', '.join(pizza[::1])}."
                                  f" Your current total is ₱{price} ")

                            decision = input("Change Order? [1]Yes [N]No").strip()
                            if decision == "1":
                                continue

                            elif decision == "2":
                                break

                            elif decision != "1" or "2":
                                raise TypeError

                        elif len(pizza) < 1 <= len(drink):
                            remove_this = input(f"\tWhat do you want to remove? "
                                                f"Your order is/are {', '.join(drink[::1])}: ")
                            if remove_this in drink:
                                drink.remove(remove_this)
                                print(f"\tYour current drink/s are {', '.join(drink[::1])}")

                                decision = input("\tChange Order? [1]Yes [N]No").strip()
                                if decision == "1":
                                    continue

                                elif decision == "2":
                                    break

                                elif decision != "1" or "2":
                                    raise TypeError

                        elif len(pizza) and len(drink) > 1:
                            remove_this = input(f"\tWhat do you want to remove? Pizza:{', '.join(pizza[::1])}."
                                                f" Drinks: {', '.join(drink[::1])} : ")

                            if remove_this in drink:
                                drink.remove(remove_this)
                                print(f"\tYour current drink/s are {', '.join(drink[::1])}")

                            elif remove_this in pizza:
                                pizza.remove(remove_this)
                                print(f"\tYour current pizza/s are {', '.join(pizza[::1])}")

                                decision = input("\tChange Order? [1]Yes [N]No").strip()
                                if decision == "1":
                                    continue

                                elif decision == "2":
                                    break

                                elif decision != "1" or "2":
                                    raise TypeError

                    else:
                        print("\tThere is no such order")

                elif what_to_change == "2":

                    if len(pizza) and len(drink) > 1:
                        remove_this = input(f"\tWhat do you want to replace? Pizza:{', '.join(pizza[::1])}."
                                            f" Drinks: {', '.join(drink[::1])} : ").capitalize()

                    if remove_this in drink:

                        for d in drinks_choice:
                            print(f"\t{d} : ₱{drinks_choice[d]}", end="")
                        change_with_what = input(f"\tWhat do you want to change it with? ").capitalize()

                        if "Coca" and "cola" in change_with_what:
                            change_with_what = "Coca Cola"

                        elif "Iced" and "lemon" and "tea" in change_with_what:
                            change_with_what = "Iced Lemon Tea"

                        elif "Pineapple" and "juice" in change_with_what:
                            change_with_what = "Pineapple Juice"

                        elif "Orange" and "juice" in change_with_what:
                            change_with_what = "Orange Juice"

                            drink[len(remove_this)] = change_with_what
                            price -= drinks_choice[remove_this]
                            price += drinks_choice[change_with_what]

                        print(f"\tYour current pizza/s are {', '.join(drink[::1])}."
                              f" Your current total is ₱{price} ")
                    elif remove_this in pizza:

                        for p in pizza_choice:
                            print(f"\t{p} : ₱{pizza_choice[p]}", end="")

                        change_with_what = input(f"\tWhat do you want to change it with?").capitalize()

                        if "Cheesy" and "bacon" in change_with_what:
                            change_with_what = "Cheesy Bacon"

                            pizza[len(remove_this)] = change_with_what
                            price -= pizza_choice[remove_this]
                            price += pizza_choice[change_with_what]

                            print(f"\tYour current pizza/s are {', '.join(pizza[::1])}."
                                  f" Your current total is ₱{price} ")

                    elif len(drink) < 1 <= len(pizza):

                        remove_this = input(f"\tWhat do you want to replace? {', '.join(pizza[::1])}: ")

                        for p in pizza_choice:
                            print(f"\t{p} : ₱{pizza_choice[p]}", end="")

                        change_with_what = input(f"\tWhat do you want to change it with?").capitalize()

                        if "Cheesy" and "bacon" in change_with_what:
                            change_with_what = "Cheesy Bacon"

                        if remove_this in pizza:

                            pizza[len(remove_this)] = change_with_what
                            price -= pizza_choice[remove_this]
                            price += pizza_choice[change_with_what]

                            print(
                                f"\tYour current pizza/s are {', '.join(pizza[::1])}. Your current total is ₱{price} ")

                            decision = input("\tChange Order? [1]Yes [N]No: ").strip()
                            if decision == "1":
                                continue

                            elif decision == "2":
                                break

                            elif decision != "1" or "2":
                                raise TypeError

                        elif len(pizza) < 1 <= len(drink):

                            remove_this = input(f"\tWhat do you want to replace? {', '.join(drink[::1])}: ")
                            for d in drinks_choice:
                                print(f"\t{d} : ₱{drinks_choice[d]}", end="")
                            change_with_what = input(f"\tWhat do you want to change it with? ").capitalize()

                            if "Coca" and "cola" in change_with_what:
                                change_with_what = "Coca Cola"

                            elif "Iced" and "lemon" and "tea" in change_with_what:
                                change_with_what = "Iced Lemon Tea"

                            elif "Pineapple" and "juice" in change_with_what:
                                change_with_what = "Pineapple Juice"

                            elif "Orange" and "juice" in change_with_what:
                                change_with_what = "Orange Juice"

                            if remove_this in drink:

                                drink[len(remove_this)] = change_with_what
                                price -= drinks_choice[remove_this]
                                price += drinks_choice[change_with_what]

                                print(f"\tYour current pizza/s are {', '.join(drink[::1])}."
                                      f" Your current total is ₱{price} ")

                                decision = input("Change Order? [1]Yes [N]No: ").strip()
                                if decision == "1":
                                    continue

                                elif decision == "2":
                                    break

                                elif decision != "1" or "2":
                                    raise TypeError

                                if decision == "1":
                                    continue

                                elif decision == "2":
                                    break

                                elif decision != "1" or "2":
                                    raise TypeError

                elif what_to_change == "3":
                    break

        except ValueError:
            print("\tInvalid input\n")

        except TypeError:
            print("\tInvalid choice\n")


def clear_order():
    """Asks the user if they want to clear their order"""
    while True:
        try:
            if len(pizza) < 1 and len(drink) < 1:
                print("\tYou have no order")
                break

            else:
                decision = input("\n\tAre you sure you want to clear your order? \n\t[1]Yes [2] No: ").strip()
                if decision == "1":
                    pizza.clear()
                    drink.clear()
                    print(f"\tYou have deleted your order")
                    break

                elif decision == "2":
                    break
        except ValueError:
            print("\tInvalid input")


def delivery():
    """Asks the user if delivery or no. Shows the total order at the end"""
    while True:
        try:
            decision = input("\n\tDeliver to your doorstep? [1]Yes [2] No: ")

            if decision == "1":

                address = input("\tInput your delivery address: ")

                if len(drink) < 1 <= len(pizza):
                    print(f"\n\tYour order of {len(pizza)} pizza/s : {', '.join(pizza[::1])}, is going to be delivered"
                          f" at {address}. Please prepare ₱{price} to be paid through {mode_of_payment}.")
                    break

                elif len(pizza) < 1 <= len(drink):
                    print(f"\n\tYour order of {len(drink)} drink/s : {', '.join(drink[::1])}, is going to be delivered"
                          f" at {address}. Please prepare ₱{price} to be paid through {mode_of_payment}.")

                elif len(drink) > 1 and len(pizza) > 1:
                    print(f"\n\tYour order of {len(drink)} drink/s : {', '.join(drink[::1])}. And {len(pizza)} pizza/s"
                          f": {', '.join(pizza[::1])} is going to be delivered"
                          f" at {address}. Please prepare ₱{price} to be paid through {mode_of_payment}.")

                elif len(drink) < 1 and len(pizza) < 1:
                    print("You did not order anything.")
                    break

            elif decision == "2":

                print("\n\tOkay.")
                print(len(pizza))
                print(len(drink))

                if len(drink) < 1 <= len(pizza):
                    print(f"\n\tYour order of {len(pizza)} pizza/s : {', '.join(pizza[::1])}. Please prepare ₱{price}"
                          f" to be paid through {mode_of_payment}.")

                elif len(pizza) < 1 <= len(drink):
                    print(f"\n\tYour order of {len(drink)} drink/s : {', '.join(drink[::1])}. Please prepare ₱{price}"
                          f" to be paid through {mode_of_payment}.")

                elif len(drink) >= 1 and len(pizza) >= 1:
                    print(f"\n\tYour order of {len(drink)} drink/s : {', '.join(drink[::1])}. And {len(pizza)} pizza/s"
                          f": {', '.join(pizza[::1])}. Please prepare ₱{price} to be paid through {mode_of_payment}.")

                elif len(drink) < 1 and len(pizza) < 1:
                    print("You did not order anything.")
                    break
            else:
                raise ValueError

        except ValueError:
            print("\tInvalid input\n")


def payment():
    """A function that will define the mode of payment"""
    global mode_of_payment
    while True:
        try:
            pay_with = input(f"\n\tMode of Payment\n\t[1]Cash\n\t[2]Credit/Debit\n\t[3]GCash\n\t:")
            if pay_with == "1":
                mode_of_payment = "Cash"

            elif pay_with == "2":
                mode_of_payment = "Credit/Debit"

            elif pay_with == "3":
                mode_of_payment = "GCash"

            else:
                print("\tNo such option")

            return mode_of_payment
        except ValueError:
            print("\tInvalid input")


def order():
    """The pizza ordering system"""
    while True:
        try:
            print(f"\n\tHow may I help you?")
            do: str = input("\t[1]Order\n\t[2]Leave\n\t[3]Change Order\n\t[4]Clear Order\n\t[5]Current order"
                            "\n\t: ")

            if do == "1":
                What_to_order()

            elif do == "2":
                leave()

            elif do == "3":
                change_order()

            elif do == "4":
                clear_order()

            elif do == "5":
                current_order()

            elif do != "2" or do != "1":
                print("\tNo such options")

        except ValueError:
            print(f"\tInvalid input\n")


def What_to_order():
    while True:
        try:

            what_to_order = input("\n\tWhat would you like to order?\n\t[1]Pizza [2]Drinks [3]Back : ")

            if what_to_order == "1":
                get_pizza()

            elif what_to_order == "2":
                get_drink()

            elif what_to_order == "3":
                break
            else:
                raise ValueError

            decision = input(f"\tAdd / Change order? [1]Yes [2] No: ").strip()

            if decision == "1":
                continue

            elif decision == "2":
                payment()
                delivery()
                order_again()

        except ValueError:
            print("\n\tInvalid input")


def order_again():
    """A function that asks the user if they want to order again"""
    while True:
        try:
            decision = input(f"\n\tDo you want to order again? [1]Yes [2]No: ").strip()
            if decision == "1":
                break
            elif decision == "2":
                quit()
        except ValueError:
            print("\tInvalid input")


def current_order():
    """See current order"""
    while True:
        try:
            if len(pizza) < 1 and len(drink) < 1:
                print("\n\tYou have no order")
                break

            decision = input(f"\n\tDo you want to see your order? [1]Yes [2]No: ").strip()
            if decision == "1":
                pass
            elif decision == "2":
                break

            print("\n\t======ORDER======")

            if len(drink) < 1 <= len(pizza):
                print("\n\tPizza/s: ")
                for p in pizza:
                    print(f"\t{p}")
                print(f"\tTotal: {price}")
                break

            elif len(pizza) < 1 <= len(drink):
                print("\n\tDrink/s: ")
                for d in drink:
                    print(f"\t{d}")
                print(f"\tTotal: {price}")
                break

            elif len(drink) > 1 and len(pizza) > 1:
                print("\n\tPizza/s: ")
                for p in pizza:
                    print(f"\t{p}")
                print("\n\tDrink/s: ")
                for d in drink:
                    print(f"\t{d}")
                print(f"\tTotal: {price}")
                break

        except ValueError:
            print(f"\tInvalid input")


print(f"\n\tWelcome to Deaniel's Pizzeria!")
order()
