def sum_a_collection_of_numbers():
    sum = 0
    while True:
        num = input()
        try:
            num = int(num)
            if (num == 0):
                print(f"The grand total is {float(sum)}")
                break
            else:
                sum += num
                print(f"The total is now {float(sum)}")
        except ValueError:
            print("That wasn’t a number.")


sum_a_collection_of_numbers()
