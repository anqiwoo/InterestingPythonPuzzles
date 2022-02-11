# Give your birthday,
# calculate your age in days.
# Compensate for leap years. Assume that the birthday date is a correct date.
# Simply put, if you were born 1 Jan 2022 and today's date
# is 2 Jan 2022, you are 1 days old.
from datetime import date
from datetime import datetime

today = date.today()
birthday = input(
    'Please enter your birthday in a format like "yyyy-mm-dd" or 1900-01-01: ')
birthday = datetime.strptime(birthday, '%Y-%m-%d').date()

print('Alive for', (today-birthday).days, 'days')
