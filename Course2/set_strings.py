# question 7
def unique_words(filename):
    try:
        word_set = set()
        with open(filename, 'r') as file:
            for line in file:
                words = line.lower().split()
                word_set.update(words)
        return list(word_set)
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []
print(unique_words('poem.txt'))

# question 8
def reversed_lines(filename):
    try:
        reversed_lines_list = []
        with open(filename, 'r') as file:
            for line in file:
                reversed_lines_list.append(line.rstrip()[::-1])
        return reversed_lines_list
    except FileNotFoundError:
        print(f'Error: The file {filename} not found')
        return []
print(reversed_lines('text.txt'))

# question 25 (string/set-like manipulation)
def remove_duplicates(filename):
    try:
        dup_list = []
        with open(filename, 'r') as file:
            for line in file:
                stripped = line.strip()
                if stripped and stripped not in dup_list:
                    dup_list.append(stripped)
        return dup_list
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []
print(remove_duplicates('numbers.txt'))