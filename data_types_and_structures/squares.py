def square(n):
    dict = {}
    for i in range(1, n + 1):
        dict.update({i: i ** 2})
    print(dict)


square(10)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}