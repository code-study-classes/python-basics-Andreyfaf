def sum_even_digits(number):
    
    number = str(abs(number))
    
    
    return sum(int(digit) for digit in number if int(digit) % 2 == 0)


import re

def count_vowel_triplets(text):
    
    vowels = "aeiouy"
    text = text.lower()
    
    
    triplets = re.findall(r'[aeiouy]{3}', text)
    
   
    return len(triplets)


def find_fibonacci_index(number):
    
    a, b = 1, 1
    index = 2  
    
    
    if number == 1:
        return 1
    
    
    while b < number:
        a, b = b, a + b
        index += 1
    
    
    return index if b == number else -1


def remove_duplicates(string):
    
    result = []
    for char in string:
        if not result or result[-1] != char:
            result.append(char)
    
    
    return ''.join(result)


