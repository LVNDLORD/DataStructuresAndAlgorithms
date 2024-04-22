def sum_of_first_n_positive_integers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(f"The sum of the first {n} positive integers is {sum}")


sum_of_first_n_positive_integers(10)  # The sum of the first 10 positive integers is 55
