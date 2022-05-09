"""
Escreva um programa Python para exibir a data e a hora em uma sequência amigável ao homem.
"""

import time
def time_struct(s):
    print('tm_year: ', s.tm_year)

time_struct(time.gmtime())