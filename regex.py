## buil-in modules ?


# import  os
#
# print(os.getcwd())  # pwd
# #
# print(os.getlogin())
# print(os.getenv('HOME'))


import math

# print(math.pi)

"""
.	Any character except newline
a	The character a
ab	The string ab
a|b	a or b
a*	0 or more a's
\ Escapes a special character

Regular Expression Character Classes
[ab-d]	One character of: a, b, c, d
[^ab-d]	One character except: a, b, c, d
[\b]	Backspace character
\d	One digit
\D	One non-digit
\s	One whitespace
\S	One non-whitespace
\w	One word character
\W	One non-word character

Regular Expression Quantifiers
*	0 or more
+	1 or more
?	0 or 1
{2}	Exactly 2
{2, 5}	Between 2 and 5
{2,}	2 or more
(,5}	Up to 5
"""

# import re
#
# str = 'an example word:cat!!'
# match = re.search(r'word:\w\w\w', str)
# # If-statement after search() tests if it succeeded
# if match:
#     print('found', match.group())  ## 'found word:cat'
# else:
#     print('did not find')

#
# def askforEmail(message = 'please enter your mail'):
#     pattern =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-._]+\.[A-Z|a-z]{2,7}\b'
#     while True:
#         email = input(message)
#         # vallidate emaill ?
#         """ if input follow pattern ? match object : None """
#         # valid_email = re.match(pattern, email)  # match function returns with match object if the part of the string follows the pattern
#         valid_email= re.fullmatch(pattern, email)
#         if valid_email:
#             return  email, valid_email
#         print(f"---- incorrect input please re-enter it again ----, {valid_email}")


# # myemail=askforEmail()
# # print(myemail)

#
#
# """ json  """
#
import  json
info = {'id':1, "name": "noha"}
info=json.dumps(info)  # convert any object to string
print(info)
#
users = json.dumps(['44',44,'ahmed', 'ffff'])
print(users)
#
#
# 'string  ---> return to its datatype '
#
#
users_data = json.loads(users)
print(users_data)

"""
Serialization in programming refers to the process of converting an object or
 data structure into a format that can be easily stored, transmitted, or reconstructed later.
  The primary purpose of serialization is to make it possible to save the state of an object 
  or data structure and recreate it when needed. This is particularly useful in 
  scenarios such as saving data to a file, sending it over a network, or storing it in a database.
  """

