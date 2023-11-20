try:
    file =open("users.txt","r")
except Exception as e:
    print(e)
else:
    print(file)
    data=file.read()
    print(data,type(data))
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5')
    file.seek(0) # to rest pointer to beginning of file
    lines=file.readlines() # read file content line by line as list
    print(lines,type(lines))
    file.close()