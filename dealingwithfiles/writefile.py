"""write in file
w  --> open file for writing ?
    when you try to open file for writing ---> and file
    doesn't exist --> python will try to create it ?

    when you open file with write mode --> open file for writing
    starting from the beginning of the file ?

"""
try:
    file =open("mycv.txt","w")
except Exception as e:
    print(e)
else:
    print(file)
    file.write('my name is ali\n')
    file.write('his name is saad')
    file.writelines(['Ahmed', 'Mohamed', 'Ali', 'test'])  # accept iterable of strings.

    file.close()