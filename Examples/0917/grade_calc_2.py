'''
Write a program to calculate a course grade given points for homework, quizzes, midterm exam, and final exam. Grades are calculated differently for undergrads, grads and distance learners.

Note: this program is designed for incremental development. Complete each step and submit for grading before starting the next step. Only a portion of tests pass after each step but confirm progress. 

Special Thanks:
    Dusty, Trent, Bailey, Cole, Lark, Declan
'''

# Constant value (need to remember these for grade later)
# Constants traditionally go at the front of the source code
HOMEWORK_MAX = 800.0
QUIZZEZ_MAX = 400.0
MIDTERM_MAX = 150.0
FINAL_MAX = 200.0

# input to figure out student type
student_type = input("What type of student? >") # You don't need prompt
valid_types = ("UG", "G", "DL")

# print an error, if type is invalid
if student_type not in valid_types:
    print("Error: student status must be UG, G or DL")
else:  # It's not an error, so it's okay
    the_input = input("What points? >")
    the_points = the_input.split()

    #print(the_points) # just so we can see if this worked

    # calculate the grades
    homework = float(the_points[0]) / HOMEWORK_MAX * 100
    quizzes = float(the_points[1]) / QUIZZES_MAX * 100
    midterm = float(the_points[2]) / MIDTERM_MAX * 100
    final_exam = float(the_points[3]) / FINAL_MAX * 100

    # Step 2: if its over 100, it becomes 100
    if homework > 100:
        homework = 100.0
    if quizzes > 100:
        quizzes = 100.0
    if midterm > 100:
        midterm = 100.0
    if final_exam > 100:
        final_exam = 100.0  

    # Step 3: calculate weighted grades
    '''
        Category 	UG 	G 	DL
        Homework 	20% 	15% 	5%
        Quizzes 	20% 	5% 	5%
        Midterm 	30% 	35% 	40%
        Final Exam 	30% 	45% 	50%
    '''

    # Set aside a variable, so we are ready to use it and then print it later
    grade = 0 # The scope of grade is wide enough to reach the print statement below
    if student_type == "UG":
        grade = (homework * 0.2) + (quizzes * 0.2) + (midterm * 0.3) + (final_exam * 0.3)
    elif student_type == "G":
        grade = (homework * 0.15) + (quizzes * 0.05) + (midterm * 0.35) + (final_exam * 0.45)
    elif student_type == "DL":
        grade = (homework * 0.05) + (quizzes * 0.05) + (midterm * 0.4) + (final_exam * 0.5)


    # Step 4: Get the letter grade
    course_grade = 'F'
    if grade >= 90:
        course_grade = 'A'
    elif grade >= 80:
        course_grade = 'B'
    elif grade >= 70:
        course_grade = 'C'
    elif grade >= 60:
        course_grade = 'D'

    # print out the grades
    print(f"Homework: {homework:2.1f}%")
    print(f"Quizzes: {quizzes:2.1f}%")
    print(f"Midterm: {midterm:2.1f}%")
    print(f"Final exam: {final_exam:2.1f}%")

    print(f"{student_type} average: {grade:2.1f}%")

    print(f"Course grade: {course_grade}")






