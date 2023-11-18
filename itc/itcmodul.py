def test_number(number):
    if isinstance(number,int) or isinstance(number,float):
        return number
    else:
        return False