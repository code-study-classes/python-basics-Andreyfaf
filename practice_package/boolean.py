def check_between_numbers(A, B, C):
    return A < B < C or C < B < A


def check_odd_three(number):
    return 100 <= abs(number) <= 999 and number % 2 != 0


def check_unique_digits(number):
    
    if abs(number) < 100 or abs(number) > 999:
        return False
    
    
    digits = str(abs(number))
    
    
    return len(set(digits)) == len(digits)


def check_palindrome_number(number):
    
    return str(number) == str(number)[::-1]


def check_ascending_digits(number):
    
    if abs(number) < 100 or abs(number) > 999:
        return False
    
    
    digits = [int(digit) for digit in str(abs(number))]
    
    
    return digits[0] < digits[1] < digits[2]


