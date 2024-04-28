vowels = ['a', 'e', 'i', 'o', 'u']


def count_vowels(string):
    vowel_count = 0
    for ch in string.lower():
        if ch in vowels:
            vowel_count += 1
    print(f"Number of vowels: {vowel_count}")


count_vowels("Restaurant")  # Number of vowels: 4
count_vowels("Air")  # Number of vowels: 2
