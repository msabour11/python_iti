"""In Python, an exception is a runtime error that occurs during the execution of a program. When an exceptional situation arises, such as a division by zero or an attempt to access an element that doesn't exist in a list, Python raises an exception to handle the error gracefully. Exceptions provide a way to detect and respond to errors in a more controlled manner.

Here's a detailed explanation of exceptions in Python with an example:

Exception Hierarchy:
Python has a hierarchy of exceptions, where more specific exceptions inherit from more general ones.
The base exception class is BaseException, and common exceptions derive from it. Some notable exceptions include:

Exception: The most general exception class.
TypeError: Raised when an operation or function is applied to an object of the incorrect type.
ValueError: Raised when a built-in operation or function receives an argument with the correct
type but an inappropriate value.
ZeroDivisionError: Raised when division or modulo operation is performed with zero as the denominator.
IndexError: Raised when a sequence subscript is out of range.
FileNotFoundError: Raised when an attempt to open a file or directory fails."""

"""
    syntax errors: parser --> must solve it
    logical errors: --> must be solved by developer
    runtime errors: --->  unexpected action caused the process (program) to stop


"""

"""
try:
    # Code that might raise an exception
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # Handle the specific exception
    print(f"Exception caught: {e}")
else:
    # Code to execute if no exception is raised
    print("No exception occurred.")
finally:
    # Code that always runs, regardless of whether an exception occurred or not
    print("This is the 'finally' block.")

"""

# logical error
# def sumnum(num1, num2):
#     res = num1 * num2
#     print(res)
#
# sumnum(2,2)
# sumnum(3,4)


""" runtime errors """


# print(name)  # Name Error

# print(6/0)  # ZeroDivisionError

# age = int(input('please enter age: '))
# print(age) #ValueError
#



# Exception handling


# try:
#     print(name)
# except:
#     print("---- problem happened----- ")
#     name = ''
#
#
#
# name +='iti'

""
# try:
#     print(name)
# except:
#     print("---- error with process----- ")
#     exit()


# try:
#     # print(name)
#     # print(34/0)
#     num = int(input('----: '))
# except NameError as ne:
#     print(f'=--problem happened {ne}')
#     name = ''
# except ZeroDivisionError as ze:
#     print(ze)
#     res = 0
# except TypeError:
#     print('--invalid types')
# except Exception as e:
#     print(e)
#     exit(1)
#
# else:
#     # dependent process --> will be executed only if there is no problem in the try block
#     print(num)
#     num +=10
#     print(num)
#
# finally:
#     print("---- bye ------")




def askforInt():
    done = False
    try:
        num = int(input('please enter number: '))
    except Exception as e:
        print(e)
        return  None
    else:
        done  =  True
        return num
    finally:
        """ execution finally precedes return in function """
        if done:
            print("--- valid input int ---")
        else:
            print("--- invalid input ")
#
#         # return done
#     # if done:
#     #     print("--- valid input int ---")
#     # else:
#     #     print("--- invalid input ")
#
#
res = askforInt()
print(res)
#
# #
# # done = False
# # while True:
# #     try:
# #         num = int(input('please enter number: '))
# #     except Exception as e:
# #         print(e)
# #         continue
# #     else:
# #         done  =  True
# #         break
# #     finally:
# #         """ execution finally precedes break in loop """
# #         if done:
# #             print("--- valid input int ---")
# #         else:
# #             print("--- invalid input ")
