def verify(num):
    for i in range (0,len(num)):
        if num[i] not in '0123456789':
            print('Invalid')
            break
    else:
       print('Valid')
num=input('Enter Aadhar Number')
verify(num)