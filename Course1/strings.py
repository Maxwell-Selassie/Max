# question 7
def reverse_string(text):
    return text[::-1]
print(reverse_string('Hello'))

# question 8
def convert_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return f'You have entered an invalid score {score}'
print(convert_grade(14.5))

# question 10
def is_palindrome(text):
    checked = ''.join(char.lower() for char in text if char.isalnum())
    return 'True' if checked == checked[::-1] else 'False'
print(is_palindrome('A man a plan a canal Panama'))
print(is_palindrome('hello'))

# question 11
def count_unique_char(text):
    char_count = ''
    for char in text:
        if char not in char_count:
            char_count += char
    return char_count
print(count_unique_char('Hello, World'))