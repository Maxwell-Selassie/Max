# question 22
def analyze_feedback(filename):
    '''Analyze customer feedback and return ratings with comments, in descending order'''
    try:
        analyzer = {}
        with open(filename, 'r') as file:
            for line in file:
                stripped = line.rstrip()
                if stripped:
                    try:
                        parts = stripped.split(',')
                        if len(parts) == 3:
                            _, ratings, comments = parts
                            rating = int(ratings)
                            if 1 <= rating <= 5:
                                if rating not in analyzer:
                                    analyzer[rating] = []
                                analyzer[rating].append(comments.strip())
                    except (ValueError, IndexError):
                        continue
        return dict(sorted(analyzer.items(), reverse=True))
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return {}
print(analyze_feedback('feedback.txt'))

# question 23
def summarize_ingredient(filename):
    try:
        recipe = {}
        with open(filename, 'r') as file:
            for line in file:
                stripped = line.strip()
                if stripped:
                    try:
                        parts = stripped.split(',')
                        if len(parts) == 3:
                            _, ingredient, quant = parts
                            try:
                                quantity = float(quant.strip())
                                if quantity >= 0:
                                    recipe[ingredient] = recipe.get(ingredient, 0) + quantity
                            except ValueError:
                                continue
                    except (ValueError, IndexError):
                        continue
        return dict(sorted(recipe.items(), key=lambda x: x[1], reverse=True))
    except FileNotFoundError:
        print(f'File {filename} not found')
        return {}
print(summarize_ingredient('recipe.txt'))

# question 24
def generate_confirmations(filename, output_file):
    try:
        confirmation_counts = 0
        with open(filename, 'r') as file, open(output_file, 'w') as out_file:
            for line in file:
                stripped = line.strip()
                if stripped:
                    try:
                        parts = stripped.split(',')
                        if len(parts) == 3:
                            order_id, customer, total = parts
                            confirmation = f'Order {order_id} confirmed for {customer} - Total: ${total}\n'
                            out_file.write(confirmation)
                            confirmation_counts += 1
                    except IndexError:
                        continue
        return confirmation_counts
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return 0
print(generate_confirmations('orders.txt', 'confirmations.txt'))

# question 25
def average_grades(filename):
    try:
        grade_dict = {}
        with open(filename, 'r') as file:
            for line in file:
                stripped = line.strip()
                if stripped:
                    try:
                        parts = stripped.split(',')
                        if len(parts) == 2:
                            student, grade_str = parts
                            try:
                                grade = float(grade_str.strip())
                                if 0 <= grade <= 100:
                                    if student not in grade_dict:
                                        grade_dict[student] = []
                                    grade_dict[student].append(grade)
                            except ValueError:
                                continue
                    except (IndexError, ValueError):
                        continue
        averages = {}
        for student, grades in grade_dict.items():
            if grades:
                avg = sum(grades) / len(grades)
                averages[student] = avg
        return averages
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return {}
print(average_grades('grades.txt'))

# question 26
def track_workouts(filename):
    '''Track workouts and return the total minutes for each exercise'''
    try:
        workout_dict = {}
        with open(filename, 'r') as file:
            for line in file:
                stripped = line.strip()
                if stripped:
                    try:
                        parts = stripped.split(',')
                        if len(parts) == 3:
                            _, exercise, minutes = parts
                            try:
                                minutes = int(minutes.strip())
                                workout_dict[exercise] = workout_dict.get(exercise, 0) + minutes
                            except ValueError:
                                continue
                    except (IndexError, ValueError):
                        continue
        return sorted(workout_dict.items(), key=lambda x: x[1], reverse=True)
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []
print(track_workouts('workouts.txt'))

# question 27
def log_checkins(filename, date):
    try:
        checkin_list = []
        with open(filename, 'r') as file:
            for line in file:
                stripped = line.strip()
                if stripped:
                    try:
                        parts = stripped.split(',')
                        if len(parts) == 2:
                            guest, check_in_date = parts
                            if check_in_date == date:
                                checkin_list.append(guest)
                    except (IndexError, ValueError):
                        continue
        return sorted(checkin_list)
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []
print(log_checkins('guests.txt', '2023-01-01'))

# question 28
def borrowing_status(filename):
    try:
        status_dict = {}
        with open(filename, 'r') as file:
            for line in file:
                stripped = line.strip()
                if stripped:
                    try:
                        parts = stripped.split(',')
                        if len(parts) == 2:
                            book, status = parts
                            if status not in status_dict:
                                status_dict[status] = []
                            status_dict[status].append(book)
                    except (IndexError, ValueError):
                        continue
        return status_dict
    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return {}
print(borrowing_status('books.txt'))


def build_itinerary(filename, destination):
    try:
        itinerary_list = []
        with open(filename, 'r') as file:
            for line in file:
                stripped = line.strip()
                if stripped:
                    try:
                        parts = stripped.split(',')
                        if len(parts) == 2:
                            location, activity = parts
                            if location == destination:
                                itinerary_list.append(activity)
                    except (IndexError, ValueError):
                        continue
        return itinerary_list
    except FileNotFoundError:
        print(f'The file {filename} not found')
        return []
print(build_itinerary('travel.txt', 'Paris'))