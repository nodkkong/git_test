          
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        print('Error: Too many problems')
    for problem in problems:
        split = problem.split()
        num1 = split[0]
        operator = split[1]
        num2 = split[2]
        if not operator == '+' or not operator == '-':
            print("Error: Operator must be '+' or '-'.")
        if not num1.isdigit() or not num2.isdigit():
            print('Error: Numbers must only contain digits.')
        if len(num1) or len(num2) > 4:
            print('Error: Numbers cannot be more than four digits')
        if operator == '+':
            answer = int(num1) + int(num2)
        if operator == '-':
            answer = int(num1) + int(num2)
        maximum = max(len(num1),len(num2))
        upperbound = maximum + 2
        lowerbound = len(num2) + 1
        def line_1(num1):
            line1 += (' ' * (upperbound - len(num1))) + int(num1) + '    '
            print(line1)
        def line_2(num2):
            line2 += operator + (' ' * (upperbound - len(num2) - 1)) + int(num2) + '    '
            print(line2)
        def line_3(upperbound):
            line3 = ('-' * upperbound) + '    '
            print(line3)
        def line_4(answer):
            line4 = ((' ' * (upperbound - len(answer))) + int(answer)) + '    '
            print(line4)    

arithmetic_arranger(["32 + 698"])