def ask_number(message):
    while True:
        num = input(message)
        if num.isdigit():
            num = int(num)
            return num
        print("Please enter valid number")


'''
if __name__ == "__main__"::

This line checks whether the Python script is being run as the main program
 (not imported as a module). When you run a Python script, 
 the interpreter sets the special variable __name__ to "__main__" 
 for the script that is executed. So, this block of code 
 will only run if the script is executed directly.
'''

if __name__ == "__main__":
    age = ask_number("Enter your age")
    print(age)
