def calc(problem):
   operand_1, operator, operand_2 = problem.split()
   operand_1 = int(operand_1)
   operand_2 = int(operand_2)
   if operator == '+':
       return operand_1 + operand_2
   elif operator == '-':
       return operand_1 - operand_2
   elif operator == '*':
       return operand_1 * operand_2
   elif operator == '/':
       return operand_1 / operand_2

problem = input("Enter your problem here: ")
solution = calc(problem)
print(solution)

import math
for_factorial = input("Would you like to convert your final answer into a factorial?: ")
if for_factorial == "yes":
    value = math.factorial(solution)
    print(value)
else:
    for_binary = input("Would you like to convert your final answer to binary?: ")
    if for_binary == 'yes':
        value = bin(solution)[2:]
        print(value)