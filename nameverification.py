def verify(name):
    for i in range (0,len(name)):
        if name[i] not in 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
            print('Invalid')
            break
    else:
       print('Valid')
name=input('Enter Name')
verify(name)