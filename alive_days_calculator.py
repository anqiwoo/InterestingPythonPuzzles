from datetime import date
from datetime import datetime

today = date.today()
birthday = input(
    'Please enter your birthday in a format like "yyyy-mm-dd" or 1900-01-01: ')
birthday = datetime.strptime(birthday, '%Y-%m-%d').date()

print('Alive for', (today-birthday).days, 'days')
