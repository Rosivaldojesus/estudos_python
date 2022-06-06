from datetime import date, datetime

hoje = date.today()

print(f'A data de hoje é: {hoje}')
print(f'Dia atual: {hoje.day - 1}')
print(f'Mês atual: {hoje.month}')
print(f'Ano atual: {hoje.year}')
print('===========================================')

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)
print('===========================================')