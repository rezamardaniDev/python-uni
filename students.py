students = {
    '1': {
        'firstname': 'reza',
        'lastname': 'mardani',
        'class_number': '12',
        'scores': {
            'math': 9,
            'english': 12,
            'python': 20
        }
    }
}

def add_new_student():

    stu_number = input("enter studnent number: ")
    if stu_number not in students:
        firstname = input("Enter student firstname: ")
        lastname = input("Enter student lastname: ")
        class_number = input("enter student class number: ")
        math = int(input("Enter student match score: "))
        english = int(input("Enter student english score: "))
        python = int(input("Enter student python score: "))

        students[stu_number] = {
            'firstname': firstname,
            'lastname': lastname,
            'class_number': class_number,
            'scores': {
                'math': math,
                'english': english,
                'python': python
                }
            }
        print("student seccessfully added to students list")

    else:
        print("student number already")


def remove_student():
     stu_number = input("enter student number: ")
     if stu_number in students:
         del students[stu_number]
         print("student removed seccessfully")
     else:
        print("student not found")


def edit_student():
    stu_number = input("enter student number: ")
    if stu_number in students:
         course = input("what course edite? (math-python-english) ")
         new_score = int(input("enter new score: "))
         students[stu_number]['scores'][course] = new_score
         print("score updated seccessfully")
    else:
        print("student not found")

def search_student():
    stu_number = input("enter student number: ")
    if stu_number in students:
        information = students.get(stu_number, "student not found!")
        for key, value in information.items():
            print(f"{key} : {value}")
    else:
        print("student not found")


def display_students():
    for item in students.items():
        print(f"{item}\n")


def detail_score():
    math = []
    english = []
    python = []

    for stu in students:
       math.append(students[stu]['scores']['math'])
       english.append(students[stu]['scores']['english'])
       python.append(students[stu]['scores']['python'])

    print(f"python: max score is {max(python)} - min score is {min(python)} - average score is {sum(python) / len(python)}")
    print(f"math: max score is {max(math)} - min score is {min(math)} - average score is {sum(math) / len(math)}")
    print(f"english: max score is {max(english)} - min score is {min(english)} - average score is {sum(english) / len(english)}")

    print(f"number of students is {len(students)}")


while True:
    print("\n1.add a student\n2.remove a student\n3.edit a student\n4.search a student\n5.show all students\n6.detail scores\n7.exit")
    cmd = input("select a option: ")

    if cmd == '1':
        add_new_student()

    elif cmd == '2':
        remove_student()

    elif cmd == '3':
        edit_student()

    elif cmd == '4':
        search_student()

    elif cmd == '5':
        display_students()

    elif cmd == '6':
        detail_score()

    elif cmd == '7':
        print("good luck :)")
        break

    else:
        print("Unknown command")
