def verify(mail):
    if '.' in mail and '@' in mail:
        print('Valid')
    else:
        print('Invalid')
mail= input('Enter Email')
verify(mail)


