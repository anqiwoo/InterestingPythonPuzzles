import pandas as pd

excel_wb12_filepath = 'learn_excel_12.xlsx'
excel_wb34_filepath = 'learn_excel_34.xlsx'

# To get multiple workbooks, we can just call the pandas.read_excel() multiple times:)
wb12 = pd.read_excel(excel_wb12_filepath, sheet_name=None)
wb34 = pd.read_excel(excel_wb34_filepath, sheet_name=None)

# Calculate the average score of each class
average_score_1 = wb12['Class 1']['Score'].mean()
average_score_2 = wb12['Class 2']['Score'].mean()
average_score_3 = wb34['Class 3']['Score'].mean()
average_score_4 = wb34['Class 4']['Score'].mean()

print(average_score_1, average_score_2,
      average_score_3, average_score_4, sep="\n")

'''
Multiple Excel Worksheets Example
# To get multiple worksheets in a workbook, we can pass a list
# to the sheet_name parameter.
# And we can pass either roman number or sheet name.
two_sheets = pd.read_excel(excel_wb12_filepath, sheet_name=['Class 1', 1])

# If we want all sheets in a workbook, we can set the sheet_name to be None.
all_sheets = pd.read_excel(excel_wb12_filepath, sheet_name=None)

print(type(all_sheets))
print(type(all_sheets['Class 1']))
print('-'*85)
print(all_sheets['Class 1'].head())
print('-'*85)
print(all_sheets['Class 2'].head())
'''

'''
Single Excel Worksheet Example
# To get a single worksheet in a workbook, we can
# pass the excel workbook filepath and the sheet_name respectively.
class1 = pd.read_excel(excel_wb12_filepath, sheet_name='Class 1')

# The sheet_name parameter can be a number, starting from 0.
# so, to get class 2, we need to pass 1 to the sheet_name parameter.
class2 = pd.read_excel(excel_wb12_filepath, sheet_name=1)

print(class1.head())
print('-'*85)
print(class2.head())
'''
