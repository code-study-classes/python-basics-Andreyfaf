def extract_file_name(full_file_name):
    
    filename = full_file_name.split('/')[-1].split('\\')[-1]
    
    
    name_without_extension = filename.split('.')[0]
    
    return name_without_extension


def encrypt_sentence(sentence):
    even_chars = []  
    odd_chars = []  

    for i, char in enumerate(sentence):
        if i % 2 == 0:
            even_chars.append(char)
        else:
            odd_chars.append(char)

    return ''.join(even_chars) + ''.join(reversed(odd_chars))


def check_brackets(expression):
    stack = []

    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return i  

    
    return 0 if not stack else -1


def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(reversed(parts))



def count_vowel_groups(word):
    vowels = 'aeiouyAEIOUY'
    count = 0
    in_group = False

    for char in word:
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False

    return count
