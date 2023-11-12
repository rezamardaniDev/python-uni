# ابتدا سه تا لیست تعریف میکنیم برای دریافت نام، شماره دانشجویی و نمره
names = []
students_number = []
scores = []

# این تابع مربوط میشه به اضافه کردن یک دانشجو جدید
def add_new_student():
    
    # سه تا ورودی گرفتم که یکی نام و یکی شماره دانشجویی و آخری نمره اش هست
    name = input("enter your name: ")
    stu_number = input("enter your student_number: ")
    score = float(input("enter student score: "))

    #  اینجا اومدیم چک کردیم که شماره دانشجویی شخصی که داریم اضافه میکنیم از قبل تو لیست ها نباشه
    # اگر بود بهم مون ارور نشون بده
    if stu_number in students_number:
        print("error this student exists")

    # اگر شماره دانشجویی شخص جدید بود. بیاد به لیست ها اطلاعات رو اضافه کنه
    else:
       names.append(name)
       students_number.append(stu_number)
       scores.append(score)
       print("data add seccessfuly")


# این تابع اطلاعات تمام دانشجو هارو برای ما پرینت میکنه
def display_student():
    
    # یک حلقه روی تعداد دانشجوها میزنیم و هر بار یکی شون رو به وسیله ایندکس چاپ میکنیم
    for count in range(len(names)):
        print(f"name: {names[count]} - st_number: {students_number[count]} - score: {scores[count]}\n")


# این تابع یک شماره دانشجویی میگیره و اون اطلاعات اون دانشجو رو از لیست ها حذف میکنه
def remove_student():
    
    # ابتدا یک ورودی که همون شماره دانشجویی هست از کاربر میگیریم
    stu_num = input("etner a student number for remove: ")
    if stu_num not in students_number:
        print("error this stu number not found")
    # حالا ایندکس اون شماره دانشجویی رو پیدا میکنیم
    else:
        found_student = students_number.index(stu_num)

        # با توجه به اینکه نام و شماره و نمره دانشجوی پیدا شده در ایندکس یکسانی قرار دارند
        # با استفاده از متد پاپ اون دانشجو رو حذف میکنیم
        names.pop(found_student)
        students_number.pop(found_student)
        scores.pop(found_student)
        print("student removed seccesfully")

#این تابع یک شماره دانشجویی میگیره
# چک میکنه اگر دانشجو وجود داشت، یک نمره جدید از ما میگیره
# و نمره جدید رو جایگزین نمره قبلی دانشجو میکنه
def edit_student():
    
    # شماره دانشجویی رو اینجا گرفتیم
    stu_num = input("etner a student number for remove: ")
    
    # چک میکنه اگر دانشجو وجود نداشته باشه ارور میده
    if stu_num not in students_number:
        print("error this stu number not found")
        
    # اگر وجود داشت
    else:
        found_student = students_number.index(stu_num)
        # یک نمره جدید از ما میگیره
        new_score = float(input("enter new score for student: "))
        
        # جایگزین نمره قبلی میکنه
        scores[found_student] = new_score
        print("edited student")

# این تابع یک اسم از ما میگیره 
# هر دانشجویی که اسمش با ورودی یکی باشه
# اطلاعات شو برای ما نشون میده
def search_student():
    student_name = input("etner student name: ")
    for name in names:
        if student_name in name:
            found = names.index(name)
            print(f"name: {names[found]} - st_number: {students_number[found]} - score: {scores[found]}\n")

# این تابع تعداد کل دانشجویان، میانگین نمرات شون و فردی که بالاترین نمره رو داره بهمون نشون میده     
def show_detail():
    print(f"total students: {len(names)}")

    avg = sum(scores) // len(scores)
    print(f"avg: {avg}")

    found_student = scores.index(max(scores))
    print(f"name: {names[found_student]} - st_number: {students_number[found_student]} - score: {scores[found_student]}\n")

# شروع برنامه ما از اینجاست که هربار باید کاربر یک ورودی وارد کنه
# حلقه باید بینهایت بار تکرار بشه تا فهرست هر بار نمایش داده بشه
# زمانی حلقه تموم میشه و دیگه فهرست نمایش داده نمیشه که کاربر گزینه 7 رو بزنه
while True:
    
    # ابتدا فهرست به کاربر نمایش داده میشه
    # بین گزینه ها از بک اسلش ان استفاده کردیم تا متن بعدی در خط بعدی چاپ بشه
    print("1. add student\n2. display all students\n3. remove students\n4. edite students\n5. search\n6. show class detail\n7. exit")
    
    # یک ورودی از کاربر میگیریم تا متوجه بشیم کاربر چه کاری میخواد انجام بده و طبق همون توابع رو فراخوانی کنیم
    choices = input("select a option: ")

    # اگر گزینه یک رو وارد کرد، تابع مربوط به اضافه کردن دانشجو اجرا بشه
    if choices == "1":
        add_new_student()
        
    # اگر گزینه دو رو وارد کرد، تابع مربوط به نمایش دانشجو ها اجرا بشه
    elif choices == "2":
        display_student()
    
    # اگر گزینه سه رو وارد کرد، تابع مربوط به حذف یک دانشجو اجرا بشه
    elif choices == "3":
        remove_student()

    elif choices == "4":
        edit_student()

    elif choices == "5":
        search_student()

    elif choices == "6":
        show_detail()
        
    # اگر گزینه هفت رو وارد کرد، برنامه متوقف بشه و فهرست دگه نمایش داده نشه
    elif choices == "7":
        print("goodby")
        break

