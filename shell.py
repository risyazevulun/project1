# shell.py

import basic
import functions as fn
def is_part_b_command(command):
    part_b_commands = [
        'fibonacci', 'concatenate_strings', 'cumulative_sum_squares',
        'factorial', 'exponentiation', 'sum_squared_evens',
        'palindrome_count', 'prime_filter'
    ]
    return any(command.startswith(cmd) for cmd in part_b_commands)

def execute_part_b_command(command):
    try:
        if command.startswith('fibonacci '):
            n = int(command.split()[1])
            print(fn.fibonacci(n))
        elif command.startswith('concatenate_strings '):
            lst = command.split()[1:]
            print(fn.concatenate_strings(lst))
        elif command.startswith('cumulative_sum_squares '):
            lst = eval(command[len('cumulative_sum_squares '):])
            print(fn.cumulative_sum_squares(lst))
        elif command.startswith('factorial '):
            n = int(command.split()[1])
            print(fn.cumulative_operation(lambda x, y: x * y)(range(1, n + 1)))
        elif command.startswith('exponentiation '):
            lst = list(map(int, command.split()[1:]))
            print(fn.cumulative_operation(lambda x, y: x ** y)(lst))
        elif command.startswith('sum_squared_evens '):
            nums = list(map(int, command.split()[1:]))
            print(fn.sum_squared_evens(nums))
        elif command.startswith('palindrome_count '):
            lst = eval(command[len('palindrome_count '):])
            print(fn.palindrome_count(lst))
        elif command.startswith('prime_filter '):
            lst = list(map(int, command.split()[1:]))
            print(fn.prime_filter(lst))
        else:
            print("Unknown command.")
    except Exception as e:
        print(f"Error: {e}")
def repl():
    while True:
        try:
            command = input('>>> ')
            if command == 'exit':
                break
            elif is_part_b_command(command):
                execute_part_b_command(command)
            else:
                # Run the command using basic.run and display the result
                if command.strip() == "": continue
                result, error = basic.run('<stdin>', command)

                if error:
                    print(error.as_string())
                elif result:
                    if len(result.elements) == 1:
                        print(repr(result.elements[0]))
                    else:
                        print(repr(result))
        except Exception as e:
            print(f"REPL Error: {e}")

if __name__ == '__main__':
    repl()
