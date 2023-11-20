import json
# read data from json file
def read_data(filename):
    try:
        file=open(filename,'r')
    except Exception as e:
        print(e)
        return False
    else:
        data=file.read()
        data=json.loads(data) # convert json string to dictionnary object
        print(data)
        file.close()

        return data

# write data into json file
def load_data(filename,inserted_data):
    old_data = read_data(filename)
    old_data['data'].append(inserted_data)
    try:
        file=open(filename,'w')

    except Exception as e:
        print(e)
        return False
    else:
        str_data = json.dumps(old_data)
        file.write(str_data)

        print(str_data)
        return True
"""The if __name__ == '__main__': block ensures that the code inside it is only executed
 if the script is run directly (not imported as a module). 
 """
if __name__=='__main__':
    # my_data=read_data('users.json')
    load_json=load_data('users.json',{'id':5,'name':'mohamed'})
