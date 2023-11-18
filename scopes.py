"""

    how the variable is represented in the memory ?

"""
""" any variable defined in the python script --> module --> variable with global scope """

# course = 'python'  # global scope

# print(course)

# """  local scope """
#
#
# # any variable defined inside the function --> has local scope  --> can be accessed only inside the function
# def formatname():
#     name = input('please enter name : ')  # local variable
#     name = name.strip().capitalize()
#     print(name)
# formatname()
# print(name)
#
#
# """ access global variable from inside the function"""
# """ you can access global variable from inside the function"""
course = 'python'


# def printCourse():
#     course=input('input course name: ')
#     print(f"course from function = {course}")
# printCourse()
# print(f'course after update function {course}') # note that global variable not affected with local variable

# """ modify global variable"""
# print(f'course before modify it in function {course}')
# def modifycourse():
#     global course
#     course = input("please enter coursename: ")
#     print(f"after update {course}")
#
#
#
# modifycourse()
# print(f"after modify {course}")

# note that if and loops except from global scope concept
# for i in range(10):
#     pass
#
#
# print(i)
# name = 'Ali'
# while True:
#     name = 'Ali'
#     break
#
#
# print(name)


# grade variable can access only if the condition is true
# name = 'ali'
# if name =='ali':
#     grade = 10
# else:
#     pass
#
#
# print(grade)
#
# ##### function inside a function
#
def outerfun():
    course = 'python'  # local scope

    def formatCourse():
        # # you can access local variable from inner function
        print(course.upper())
    formatCourse()

# outerfun()


#
    def modifyCourse1():
        course = input('please enter course: ')  # new local variable for the inner function
        print(course)

    modifyCourse1()
    print(course)  
outerfun()

#     def modifyCourse():
#         nonlocal course
#         course = input('please enter course: ')  # new local variable for the inner function
#         print(course)
#
#     modifyCourse()
#     print(f'course= {course}')
#
#
# outerfun()
