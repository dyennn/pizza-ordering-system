pizza = []
drink = []
price: int = 0

pizza_choice = {"Hawaiian": 299,
                "Cheesy Bacon": 299,
                "Vegetarian": 259,
                "Margherita": 299,
                "Pepperoni": 299}

pizza_code = {"P1": "Hawaiian",
              "P2": "Cheesy Bacon",
              "P3": "Vegetarian",
              "P4": "Margherita",
              "P5": "Pepperoni"}

drinks_choice = {"Coca Cola": 20,
                 "Iced Lemon Tea": 20,
                 "Pineapple Juice": 20,
                 "Royal": 20,
                 "Orange Juice": 20}

drinks_code = {"D1": "Coca Cola",
               "D2": "Iced Lemon Tea",
               "D3": "Pineapple Juice",
               "D4": "Royal",
               "D5": "Orange Juice"}


def What_to_order():
    """Asks the user what to order (pizza or drink)"""
    while True:
        try:

            what_to_order = input("\n\tWhat would you like to order?\n\t[1] Pizza \n\t[2] Drinks \n\t[3] Back\n\t: ")

            if what_to_order == "1":
                get_pizza()
            elif what_to_order == "2":
                get_drink()
            elif what_to_order == "3":
                break
            else:
                raise ValueError

            decision = input(f"\n\tProceed to checkout? \n\t[1] Yes \n\t[2] No\n\t: ").strip()

            if decision == "1":
                payment()
                delivery()
                order_again()
            elif decision == "2":
                break
        except ValueError:
            print("\n\tInvalid input")
        except Exception:
            print()


# Update choosing methods from words to numbers
def get_pizza():
    """A function that asks the user what pizza they want to order"""
    while True:
        try:
            global price

            print()

            for p in pizza_code:
                print(f"\t[{p}] {pizza_code[p]} : ₱{pizza_choice[pizza_code[p]]}")

            get_this_pizza = input(f"\n\tWhat pizza would you like to get?: ").capitalize().strip()

            if get_this_pizza not in pizza_code:
                raise ValueError

            # quantity = int(input(f"\tHow man
            # y {pizza_code[get_this_pizza]} pizza/s would you like to get?\n\t: ")).strip()
            # print(quantity)

            price += pizza_choice[pizza_code[get_this_pizza]]  # * quantity
            pizza.append(pizza_code[get_this_pizza])

            current_order()

            decision = input("\n\tAdd more? \n\t[1] Yes \n\t[2] No \n\t: ")

            if decision == "1":
                continue
            elif decision == "2":
                break
            elif decision != "1" or "2":
                print("\tInvalid option")
                raise ValueError

        except ValueError:
            print(f"\tThere is no such option\n")


# Option to change the ordering process from words to numbers
def get_drink():
    """A function that will ask the user what drinks they want to order"""
    while True:
        try:
            global price

            print(f"\n\tWhat drinks would you like to get?\t")

            print()

            for d in drinks_code:
                print(f"\t[{d}] {drinks_code[d]} : ₱{drinks_choice[drinks_code[d]]}")

            get_this_drink = input(f"\n\t: ").capitalize().strip()

            if get_this_drink not in drinks_code:
                raise ValueError

            price += drinks_choice[drinks_code[get_this_drink]]
            drink.append(drinks_code[get_this_drink])

            current_order()

            decision = input("\n\tAdd more?\n\t[1] Yes\n\t[2] No : ")

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
            sure = input(f"\n\tAre you sure you want to quit?\n\t[1] Yes\n\t[2] No\n\t: ").strip()
            if sure == "1":
                print(f"\n\tHave a great day!")
                quit()
            elif sure == "2":
                print("\tOkay!")
                break
        except ValueError:
            print("Invalid input")


# problem with replacing order
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
                what_to_change = input("\n\t[1] Remove an order\n\t[2] Replace an order\n\t[3] Back: ").strip()
                if what_to_change == "1":

                    if len(drink) < 1 <= len(pizza):
                        current_order()
                        remove_this = input(f"\n\tWhat do you want to remove?: ")

                        if remove_this in pizza:

                            pizza.remove(remove_this)
                            price -= pizza_choice[remove_this]

                            if len(pizza) < 1:
                                print("\ttYou have cleared your order")
                            else:
                                print(f"\tYour current pizza/s are {', '.join(pizza[::1])}."
                                      f" Your current total is ₱{price} ")

                            decision = input("\n\tChange Order? \n\t[1] Yes\n\t[N] No\n\t:").strip()
                            if decision == "1":
                                continue

                            elif decision == "2":
                                break

                            elif decision != "1" or "2":
                                raise TypeError

                    elif len(pizza) < 1 <= len(drink):
                        current_order()
                        remove_this = input(f"\tWhat do you want to remove? : ")

                        if remove_this in drink:
                            drink.remove(remove_this)

                            if len(drink) < 1:
                                print("\tYou have cleared your order")
                            else:
                                print(f"\tYour current drink/s are {', '.join(drink[::1])}")

                            decision = input("\n\tChange Order? \n\t[1] Yes\n\t[N] No\n\t:").strip()
                            if decision == "1":
                                continue

                            elif decision == "2":
                                break

                            elif decision != "1" or "2":
                                raise TypeError

                    elif len(pizza) and len(drink) >= 1:
                        remove_this = input(f"\tWhat do you want to remove? Pizza:{', '.join(pizza[::1])}."
                                            f" Drinks: {', '.join(drink[::1])} : ")

                        if remove_this in drink:
                            drink.remove(remove_this)
                            print(f"\tYour current drink/s are {', '.join(drink[::1])}")

                        elif remove_this in pizza:
                            pizza.remove(remove_this)
                            print(f"\tYour current pizza/s are {', '.join(pizza[::1])}")

                            decision = input("\tChange Order?\n\t[1]Yes\n\t[N]No\n\t:").strip()
                            if decision == "1":
                                continue

                            elif decision == "2":
                                break

                            elif decision != "1" or "2":
                                raise TypeError

                    else:
                        print("\tYou have no order")

                elif what_to_change == "2":

                    if len(pizza) >= 1 and len(drink) >= 1:
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

                            decision = input("\tChange Order? \n\t[1] Yes\n\t[N] No\n\t: ").strip()
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

                                decision = input("\n\tChange Order? \n\t[1] Yes\n\t[N] \n\tNo\n\t: ").strip()
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
            global price

            if len(pizza) < 1 and len(drink) < 1:
                print("\tYou have no order")
                break

            else:
                decision = input("\n\tAre you sure you want to clear your order? \n\t[1] Yes \n\t[2] No\n\t: ").strip()
                if decision == "1":
                    pizza.clear()
                    drink.clear()
                    price = 0
                    print(f"\tYou have deleted your order")
                    break

                elif decision == "2":
                    break
        except ValueError:
            print("\tInvalid input")


def payment():
    """A function that will define the mode of payment"""
    global mode_of_payment
    while True:
        try:
            pay_with = input(f"\n\tMode of Payment\n\t[1] Cash\n\t[2] Credit\n\t[3] Debit [4] GCash\n\t:")
            if pay_with == "1":
                mode_of_payment = "Cash"

            elif pay_with == "2":
                mode_of_payment = "Credit"

            elif pay_with == "3":
                mode_of_payment = "Debit"

            elif pay_with == "4":
                mode_of_payment = "GCash"

            else:
                print("\tNo such option")

            return mode_of_payment
        except ValueError:
            print("\tInvalid input")


def delivery():
    """Asks the user if delivery or no. Shows the total order at the end"""
    while True:
        try:
            decision = input("\n\tDeliver to your doorstep? [1] Yes [2] No: ")

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

                if len(drink) < 1 <= len(pizza):
                    print(f"\n\tYour order of {len(pizza)} pizza/s : {', '.join(pizza[::1])}. Please prepare ₱{price}"
                          f" to be paid through {mode_of_payment}.")
                    order_again()
                elif len(pizza) < 1 <= len(drink):
                    print(f"\n\tYour order of {len(drink)} drink/s : {', '.join(drink[::1])}. Please prepare ₱{price}"
                          f" to be paid through {mode_of_payment}.")
                    order_again()
                elif len(drink) >= 1 and len(pizza) >= 1:
                    print(f"\n\tYour order of {len(drink)} drink/s : {', '.join(drink[::1])}. And {len(pizza)} pizza/s"
                          f": {', '.join(pizza[::1])}. Please prepare ₱{price} to be paid through {mode_of_payment}.")
                    order_again()
                elif len(drink) < 1 and len(pizza) < 1:
                    print("You did not order anything.")
                    break
            else:
                raise ValueError

        except ValueError:
            print("\tInvalid input\n")


def order_again():
    """A function that asks the user if they want to order again"""
    while True:
        try:
            decision = input(f"\n\tDo you want to order again? [1] Yes [2] No: ").strip()
            if decision == "1":
                print("\n\tEnjoy your meal!")
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

            print("\n\t======ORDER======")

            if len(drink) < 1 <= len(pizza):
                print("\n\tPizza/s: ")
                for p in pizza:
                    print(f"\t{p}")
                print(f"\tTotal: ₱{price}")
                break

            elif len(pizza) < 1 <= len(drink):
                print("\n\tDrink/s: ")
                for d in drink:
                    print(f"\t{d}")
                print(f"\tTotal: ₱{price}")
                break

            elif len(drink) >= 1 and len(pizza) >= 1:
                print("\n\tPizza/s: ")
                for p in pizza:
                    print(f"\t{p}")
                print("\n\tDrink/s: ")
                for d in drink:
                    print(f"\t{d}")
                print(f"\tTotal: ₱{price}")
                break

        except ValueError:
            print(f"\tInvalid input")


def order():
    """The pizza ordering system"""
    while True:
        try:
            print(f"\n\tHow may I help you?")
            do = input("\t[1] Order\n\t[2] Leave\n\t[3] Change Order\n\t[4] Clear Order\n\t[5] Current order"
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


print(f"\n\tWelcome to Deaniel's Pizzeria!")
order()
