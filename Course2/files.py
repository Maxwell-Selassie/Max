# Scenario 1
def line_counters(filename):
    '''Count the number of non-blank lines'''
    try:
        non_blank_counters = 0
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():  # Non-empty after stripping whitespace
                    non_blank_counters += 1
        return non_blank_counters
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return 0
print(line_counters('notes.txt'))

# Scenario 2
def word_frequency(filename):
    '''Returns a dictionary of the top 3 most frequent words (case-insensitive)'''
    try:
        word_counts = {}
        with open(filename, 'r') as file:
            for line in file:
                words = line.rstrip().split()
                for word in words:
                    word = word.lower()
                    word_counts[word] = word_counts.get(word, 0) + 1
        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        top_3_dict = dict(sorted_words[:3])
        return top_3_dict
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return {}
print(word_frequency('story.txt'))

# Scenario 3
def longest_line(filename):
    '''Returns the length of the longest line in the file'''
    try:
        longest = 0
        with open(filename, 'r') as file:
            for line in file:
                line_length = len(line.rstrip())
                if line_length > longest:
                    longest = line_length
        return longest
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return 0
print(longest_line('notes.txt'))

# Scenario 4
def count_vowels(filename):
    '''Counts the number of vowels in a file'''
    try:
        total_count = 0
        with open(filename, 'r') as file:
            for line in file:
                for char in line.lower():
                    if char in 'aeiou':
                        total_count += 1
        return total_count
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return 0
print(count_vowels('poem.txt'))

# Scenario 5
def find_word(filename, word):
    try:
        count = 0
        with open(filename, 'r') as file:
            for line in file:
                words = line.rstrip().lower().split()
                count += words.count(word.lower())
        return count
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return 0
print(find_word('story.txt', 'the'))

# Scenario 6
def first_words(filename):
    '''Returns the first words in each line'''
    try:
        firsts = []
        with open(filename, 'r') as file:
            for line in file:
                words = line.rstrip().split()
                if words:
                    firsts.append(words[0])
        return firsts
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []
print(first_words('word.txt'))

# Scenario 7
def count_enders(filename, letter):
    try:
        count = 0
        with open(filename, 'r') as file:
            for line in file:
                stripped = line.rstrip()
                if stripped and stripped[-1] == letter:
                    count += 1
        return count
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return 0
print(count_enders('word.txt', 't'))

# Scenario 8
def capital_lines(filename):
    try:
        cap_lines = []
        with open(filename, 'r') as file:
            for line in file:
                words = line.rstrip()
                if words and words[0].isupper():
                    cap_lines.append(words)
        return cap_lines
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []
print(capital_lines('caps.txt'))

# Scenario 9
def avg_length(filename):
    try:
        total_len = 0
        count = 0
        with open(filename, 'r') as file:
            for line in file:
                words = line.rstrip().split()
                for word in words:
                    if word:
                        total_len += len(word)
                        count += 1
        return total_len / count if count > 0 else 0
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return 0
print(avg_length('word.txt'))

# Scenario 10
def palindrome(filename):
    try:
        pal = []
        with open(filename, 'r') as file:
            for line in file:
                words = line.rstrip().split()
                for word in words:
                    word = word.lower()
                    if word == word[::-1] and word not in pal:
                        pal.append(word)
        return pal
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []
print(palindrome('palindrome.txt'))

# Scenario 11
def longest_word(filename):
    '''Returns the length of the first longest word in the file'''
    try:
        longest_word = ''
        longest_length = 0
        with open(filename, 'r') as file:
            for line in file:
                words = line.rstrip().split()
                for word in words:
                    if len(word) > longest_length:
                        longest_word = word
                        longest_length = len(word)
        return longest_length
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return 0
print(longest_word('longest_word.txt'))

# Scenario 12
def prefix(filename):
    try:
        prefixes = []
        with open(filename, 'r') as file:
            for i, line in enumerate(file, 1):
                word = line.rstrip()
                prefixes.append(f'{i}:{word}')
        return prefixes
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []
for line in prefix('text.txt'):
    print(line)

# Scenario 13
def concat_lines(filename):
    try:
        lines = []
        with open(filename, 'r') as file:
            for line in file:
                lines.append(line.rstrip())
        return ' '.join(lines)
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return ''
print(concat_lines('text.txt'))

# Scenario 14
def last_words(filename):
    try:
        last_word_list = []
        with open(filename, 'r') as file:
            for line in file:
                words = line.rstrip().split()
                if words:
                    last_word_list.append(words[-1])
        return last_word_list
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []
print(last_words('last.txt'))

# Scenario 15
def upper_words(filename):
    try:
        upper_list = []
        with open(filename, 'r') as file:
            for line in file:
                words = line.rstrip().split()
                for word in words:
                    if word and word.isupper():
                        upper_list.append(word)
        return upper_list
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []
print(upper_words(input('Enter the file name: ')))

# Scenario 16
def shortest_line(filename):
    try:
        shortest_line = None
        shortest_len = float('inf')
        with open(filename, 'r') as file:
            for line in file:
                line = line.rstrip()
                if line:  # Ignore empty lines
                    line_len = len(line)
                    if line_len < shortest_len:
                        shortest_len = line_len
                        shortest_line = line
        return shortest_line if shortest_line is not None else ''
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return ''
print(shortest_line(input('Enter the file name: ')))

# Scenario 17
def odd_word(filename):
    try:
        odd_list = []
        with open(filename, 'r') as file:
            for line in file:
                words = line.rstrip().split()
                for word in words:
                    if word and len(word) % 2 == 1:
                        odd_list.append(word)
        return odd_list
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []
print(odd_word('odds.txt'))