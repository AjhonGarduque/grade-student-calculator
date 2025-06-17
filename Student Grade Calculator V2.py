while True: 
    try:
        total_items = int(input("How many subjects do you have? "))
        items = []

   
        for i in range(1, total_items + 1):
            value = float(input(f"Enter Grade for subject #{i}: "))
            items.append(value)

        if any(value > 100 or value < 0 for value in items):
            print("Please enter a valid value of grades")

        total = sum(items)
        subs = len(items)
        average = total / subs
    
        print(f"\nYou entered {total_items} subjects.")
        print("--------------------------------------")
        print(f"Total grade is: {total}")
        print("--------------------------------------")
        print(f"Your average is: {average:.2f}") 

        if average >= 75:
            print("Congrats! You passed " ,end="")
            if average >= 98:
                print("With highest honors")
            elif average >= 94.5:
                print("With high honors!")
            elif average >= 89.5:
                print("With honors")
        else:
            print("Try better next time")
    
    except ValueError:
            print("please only enter numbers")

    except ZeroDivisionError:
            print("cannot divide by zero")

    except Exception:
            print("something went wrong")

    break
    