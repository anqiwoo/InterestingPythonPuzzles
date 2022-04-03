import pandas as pd

# let’s create two workbooks, learn_excel_78 and learn_excel_910.
wb78_fp = 'learn_excel_78.xlsx'
wb910_fp = 'learn_excel_910.xlsx'

df = pd.DataFrame()

with pd.ExcelWriter(wb78_fp, mode='w') as writer_78, pd.ExcelWriter(wb910_fp, mode='w') as writer_910:
    df.to_excel(writer_78, sheet_name='Class 7', index=False)
    df.to_excel(writer_78, sheet_name='Class 8', index=False)
    df.to_excel(writer_910, sheet_name='Class 9', index=False)
    df.to_excel(writer_910, sheet_name='Class 10', index=False)
