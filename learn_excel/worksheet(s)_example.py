import pandas as pd

# For our writing mode example,
# we can create a new Excel file, learn_excel_56
# and write some student data into it.
excel_fp = 'learn_excel_56.xlsx'
class5_df = pd.DataFrame(
    {'ID': [51, 52], 'Major': ['English', 'Math'], 'Score': [98, 89]})
class6_df = pd.DataFrame(
    {'ID': [61, 62], 'Major': ['History', 'Math'], 'Score': [78, 96]})

with pd.ExcelWriter(excel_fp, mode='w') as writer:
    class5_df.to_excel(writer, sheet_name='Class 5',
                       index=True, index_label='No.')
    class6_df.to_excel(writer, sheet_name='Class 6',
                       index=True, index_label='No.')
