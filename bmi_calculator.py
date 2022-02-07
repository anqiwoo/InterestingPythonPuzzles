weight = float(input('Please enter the weight(kg): '))
height = float(input('Please enter the height(m): '))
bmi = weight / height**2
print(f'\nThe BMI index is {bmi}')
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
