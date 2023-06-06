def verify(num):
    if len(num)==10:
        if num[0] in '6789':
            print('Valid ')
        else:
            print('Invalid')
    else:
        print('Invalid')
num=input('Enter Mobile Number')
verify(num)
