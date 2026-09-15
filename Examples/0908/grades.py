'''
    Get some grades.  Average and output them

    Authors: Steve K, Bailey, Declan, Dusty, Lark, Cole,
        Quinn,

    Exam Grades are weighted 15% each, but final is 20%.
'''

# get some exam grades
exam1 = float(input("exam1>"))
exam2 = float(input("exam2>"))
exam3 = float(input("exam3>"))

exam_list = [exam1 * .15, exam2 * .15, exam3 * .20]
print(exam_list)
result = sum(exam_list)
result = result / len(exam_list)
result = result + 50

print(f'Your grade is {result:.02f}')
