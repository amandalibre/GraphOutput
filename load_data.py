from xlrd import open_workbook

def load_data(file, dictionary):

    # open xlsx file
    book = open_workbook(file)
    sheet = book.sheet_by_index(0)

    # read header values into the list
    keys = [sheet.cell(0, col_index).value.strip() for col_index in range(sheet.ncols)]

    # read other rows and make into dict
    for row_index in range(1, sheet.nrows):
        row = {keys[col_index]: sheet.cell(row_index, col_index).value for col_index in range(sheet.ncols)}
        dictionary.append(row)

    return dictionary
