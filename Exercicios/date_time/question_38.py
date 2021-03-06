""""
Escreva um programa Python para obter as últimas informações modificadas de um arquivo.
"""
from cgi import test
import os, time
def last_modified_fileinfo(filepath):

    filestat = os.stat(filepath)
    date = time.localtime((filestat.st_ntime))

    # Extract year, month and day from the date
    year = date[0]
    month =  date[1]
    day = date[2]

    # Extract hour, minute, second
    hour = date[3]
    minute = date[4]
    second = date[5]

    # Year
    strYear = str(year)[0:]

    # Month
    if (month <= 9):
        strMonth = '0' + str(month)
    else:
        strMonth = str(month)

    # Date
    if (day <= 9):
        strDay = '0' + str(day)
    else:
        strDay = str(day)

    return(strYear+"-"+strMonth+"-"+strDay+"-"+str(hour)+":"+str(minute)+":"+str(second))

print()
print(last_modified_fileinfo(test.txt))
print()
