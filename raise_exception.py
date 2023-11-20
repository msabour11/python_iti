"""Raising Exceptions:
You can also raise exceptions manually using the raise statement. This is useful when you want to indicate
 that a certain condition is not met or to signal an error in your code."""

# def askdivnums(num1, num2):
#     if num2 ==0:
#         raise  ValueError("cannot divide by zero")
#     print(f"{num1}/ {num2}= ", end=' ')
#     res = num1/num2
#     print(res)
#
#
#
# askdivnums(3,0)


# def sumnums(num1: int, num2: int):
#     if isinstance(num1, int )and isinstance(num2, int):
#         return num1 + num2
#
#     raise TypeError('num1 and num2 should be integers')
#
#
# print(sumnums(3094,444.44))

def example_function(value):
    if value < 0:
        raise ValueError("Value must be non-negative.")
    return value * 2

try:
    result = example_function(-5)
except ValueError as e:
    print(f"Exception caught: {e}")
else:
    print(f"Result: {result}")
