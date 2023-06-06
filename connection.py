import pymysql

def Connect():
    con = pymysql.connect(
        host='localhost',
        user='root',
     #Password of MySql Server
        password='   ',
     #Name Of the Database
        database='tkinter_project',

    )
    return con


def verify(mail):
    if '.' in mail and '@' in mail:
        return'Valid'
    else:
        return'Invalid'





def check(num):
    if len(num)==10:
        if num[0] in '6789':
            return'Valid '
        else:
            return'Invalid'
    else:
        return'Invalid'




