'''
Source: https://towardsdatascience.com/how-to-combine-python-pandas-xlsxwriter-8edd25678a6f ; https://towardsdatascience.com/how-to-build-a-multi-tabbed-excel-file-using-pandas-731391c2cc53

XlsxWriter is a powerful package that you can use to auto-format Excel worksheets, change the styling and insert objects such as tables.

You can use XlsxWriter as an engine for Pandas ExcelWriter class to output a DataFrame to Excel.
'''

from traceback import format_tb
import xlsxwriter
import numpy as np
import pandas as pd


def format_excel(df: pd.DataFrame, sheet_name: str, writer):
    '''Add table formatting and auto-fit Excel columns'''
    # Reference the worksheet we need to update.
    worksheet = writer.sheets[sheet_name]

    # Collect the column and shape of the passed DataFrame.
    column_settings = [{'header': column} for column in df.columns]
    max_row, max_col = df.shape

    # Apply table formatting to the shape of the DataFrame on the sheet.
    worksheet.add_table(0, 0, max_row, max_col,
                        {'columns': column_settings})

    # Loop over the columns and change the width.
    for i, col in enumerate(df.columns):
        column_len = max(df[col].astype(str).str.len().max(), len(col) + 2)
        worksheet.set_column(i, i, column_len)


if __name__ == '__main__':
    data = {f'column_{i}': pd.Series(np.random.randint(0, 100, 7), index=[
                                     'i', 'l', 'o', 'v', 'e', 'p', 'y']) for i in range(5)}
    df = pd.DataFrame(data)
    with pd.ExcelWriter('testing_xlsxwriter.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='data', index=True)
        format_excel(df, 'data', writer)

# workbook = xlsxwriter.Workbook('testing_xlsxwriter.xlsx')
# worksheet = workbook.add_worksheet()

# write 'Hello Excel!' into the position 'A1' in an excel sheet
# worksheet.write('A1', 'Hello Excel!')

# workbook.close()
