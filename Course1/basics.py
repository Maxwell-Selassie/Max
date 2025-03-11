# question 1
def greet_all(names):
    '''Prints the name of individuals'''
    for name in names:
        print(f'Hello, {name}!')
greet_all(['Alice', 'Bob', 'Charlie'])

# question 2
def classify_numbers(numbers):
    '''Classifies numbers into positive and negative'''
    ps_count = 0
    ng_count = 0
    for number in numbers:
        if number >= 1:
            ps_count += 1
        elif number <= -1:
            ng_count += 1
    return (ps_count, ng_count)
print(classify_numbers([3, -1, 0, 5, -7, 2]))

# question 5 (part of basics: input handling)
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(sum_to_n(5))

# question 6 (basic function with input)
def fav_number(number):
    try:
        number = int(number)
        if number > 10:
            return f'Your favorite number {number} is a big number!'
        else:
            return f'Your favorite number {number} is a small number!'
    except ValueError:
        print(f'You have entered an invalid number')
        return 0
print(fav_number(input('Enter your favorite number: ')))

# question 9 (basic loop with condition)
def sum_even(number):
    total = 0
    for i in range(1, number + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_even(6))