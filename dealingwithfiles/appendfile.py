
"""a --> open file for appending ?
    when you try to open file for writing ---> and file
    doesn't exist --> python will try to create it ?

    when you open file with append mode --> open file for writing
    starting from the end of the file
"""
try:
    file =open("mycv1.txt","w")
except Exception as e:
    print(e)
else:
    print(file)
    file.write('my name is ali\n')
    file.close()