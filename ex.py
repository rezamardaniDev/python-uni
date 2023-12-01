students = {
    '1':{
        'first_name': 'reza',
        'last_name': 'mardani',
        'math': 90,
        'english': 11
    },
    '2':{
        'first_name': 'omid',
        'last_name': 'mardani',
        'math': 80,
        'english': 72
    },
    '3':{
        'first_name': 'ali',
        'last_name': 'mardani',
        'math': 20,
        'english': 80
    }
}


def fucntion_1():
    count = 0
    for student in students:
        if students[student]['math'] >= 70 and students[student]['english'] >= 70:
            count += 1
    print(count)
    
    
def function_2():
    lowest_math_score = float('inf')
    lowest_math_score_student = ''

    for student_id, student_info in students.items():
        if student_info['math'] < lowest_math_score:
            lowest_math_score = student_info['math']
            lowest_math_score_student = student_info['first_name'] + ' ' + student_info['last_name']
    print('The student with the lowest Math score is', lowest_math_score_student, 'with a score of', lowest_math_score)


def function_3():
    total_math_score = 0
    num_students = len(students)

    for student_id in students:
        total_math_score += students[student_id]['math']

    average_math_score = total_math_score / num_students
    print("The average math score of all students is:", average_math_score)


def function_4():
    highest_score = 0
    student_name = ''
    student_last_name = ''

    for student_id, student_data in students.items():
        if student_data['english'] > highest_score:
            highest_score = student_data['english']
            student_name = student_data['first_name']
            student_last_name = student_data['last_name']

    print(f"{student_name} {student_last_name} has the highest score in English class with a score of {highest_score}.")


def function_5():
    count = 0
    for student in students.values():
        if student['math'] >= 90:
            count += 1
    print(count, "students have a score of 90 or above in Math")


def function_6():
    for key, value in students.items():
        total_score = value['math'] + value['english']
        print(f"{value['first_name']} {value['last_name']}'s total score is {total_score}")
        

def function_7():

    scores = []
    for student in students.values():
        scores.append(student['math'])
      
    highest_score = max(scores)
    lowest_score = min(scores)

    score_difference = highest_score - lowest_score
    print(f"The difference between the highest and lowest scores in the class is {score_difference}.")


fucntion_1()
function_2()
function_3()
function_4()
function_5()
function_6()
function_7()