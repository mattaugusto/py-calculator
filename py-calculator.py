first_number = float(input('Give me the first number:'))
second_number = float(input('Give me the second number:'))

operator = str(input('Give me the operator (+,-,/,*,^):'))

if operator == '+':
    result = first_number + second_number
elif operator == '-':
    result = first_number - second_number
elif operator == '/':
    result = first_number / second_number
elif operator == '*':
    result = first_number * second_number
elif operator == '^':
    result = first_number
    for x in range(0, int(second_number-1)):
        result = result * first_number   
else:
    result = None
    print("Invalid operator!")

if result:    
    print("Result =", result) 

    
