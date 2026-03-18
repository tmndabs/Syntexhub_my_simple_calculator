
def get_choice():
    while True:
        option = input("Enter 'c' to calculate, 'r' to reset, or 'q' to quit: ").lower()
        if option in ['c', 'r', 'q']:
            return option
        else:
            print('Invalid choice. Please enter c, r, or q.')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x / y

def clear():
    return 0

def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Invalid input. Please enter a number.')


def get_operator():
    while True:
        operator = input('Enter an operator (+, -, *, /, =): ')
        if operator in ['+', '-', '*', '/', '=']:
            return operator
        else:
            print('Invalid operator. Please enter +, -, *, /, or =.')

def calculate():
    current_result = get_input('Enter the first number: ')
    while True:
        operator = get_operator()
        if operator == '=':
            print(f'Result: {current_result}')
            return current_result 
            
        
        next_number = get_input('Enter the next number: ')

        try:
            if operator == '+':
                current_result = add(current_result, next_number)
            elif operator == '-':
                current_result = subtract(current_result, next_number)
            elif operator == '*':
                current_result = multiply(current_result, next_number)
            elif operator == '/':
                current_result = divide(current_result, next_number)
        except ValueError as e:
            print(f'Calculation error: {e}')
            
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

def main():
    print('###### A Simple Calculator ######')
    print('            #########            ')

    last_result = 0

    while True:
        option = get_choice()

        if option == 'c':
            last_result = calculate()
        elif option == 'r':
            last_result = clear()
            print('Calculator reset. Current value is 0.')
        elif option == 'q':
            print('Exiting calculator...')
            break

if __name__ == '__main__':
    main()