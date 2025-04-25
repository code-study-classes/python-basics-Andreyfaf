def is_weekend(day):
    return day == 6 or day == 7


def get_discount(amount):
    if amount >= 5000:
        return amount * 0.10
    elif amount >= 1000:
        return amount * 0.05
    else:
        return 0


def describe_number(n):
    
    parity = "четное" if n % 2 == 0 else "нечетное"
    
    
    if 1 <= n <= 9:
        digit_count = "однозначное"
    elif 10 <= n <= 99:
        digit_count = "двузначное"
    elif 100 <= n <= 999:
        digit_count = "трехзначное"
    
    # Возвращаем описание числа
    return f"{parity} {digit_count} число"


def convert_to_meters(unitNumber, lengthInUnits):
    
    conversion_factors = {
        1: 0.1,    
        2: 1000,   
        3: 1,      
        4: 0.001,  
        5: 0.01    
    }
    
    
    if unitNumber in conversion_factors:
        return lengthInUnits * conversion_factors[unitNumber]
    else:
        raise ValueError("Invalid unit number")


def describe_age(age):
    
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", 
            "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", 
            "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", 
            "восемьдесят", "девяносто"]
    
    
    tens_digit = age // 10
    ones_digit = age % 10
    
    
    if age < 20:
        age_in_words = ones[age]
    else:
        age_in_words = tens[tens_digit] + " " + ones[ones_digit] if ones_digit != 0 else tens[tens_digit]
    
    
    if 10 <= age % 100 <= 20:
        return f"{age_in_words} лет"
    elif ones_digit == 1:
        return f"{age_in_words} год"
    elif 2 <= ones_digit <= 4:
        return f"{age_in_words} года"
    else:
        return f"{age_in_words} лет"
