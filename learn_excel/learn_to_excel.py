import pandas as pd

df = pd.DataFrame()
excel_wb56_filepath = 'learn_excel_56.xlsx'

# Syntax for create an ExcelWriter object in the with statement
# To create a new empty Excel file, learn_excel_56.xlsx with two new sheets!
with pd.ExcelWriter(excel_wb56_filepath) as writer:
    df.to_excel(writer, sheet_name='Class 5')
    df.to_excel(writer, sheet_name='Class 6')
