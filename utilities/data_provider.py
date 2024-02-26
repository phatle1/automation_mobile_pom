import openpyxl
from pathlib import Path

parent_path = Path(__file__).resolve().parents[1]


def get_data(sheet_name):
    try:
        test_data = openpyxl.load_workbook(f"{parent_path}/test_data/testdata.xlsx")
        sheet = test_data[sheet_name]
        total_rows = sheet.max_row
        total_cols = sheet.max_column
        print("total cols are ", str(total_cols))
        print("total rows are ", str(total_rows))
        main_list = []

        for i in range(2, total_rows + 1):
            dataList = []
            for j in range(1, total_cols + 1):
                data = sheet.cell(row=i, column=j).value
                dataList.insert(j, data)
            main_list.insert(i, dataList)
            print(main_list)
        return main_list
    except PermissionError:
        print('Permission error')


def get_authentication(account_type):
    try:
        data_set = openpyxl.load_workbook(f"{parent_path}/test_data/testdata.xlsx")
        sheet = data_set["authentication"]
        total_rows = sheet.max_row
        total_cols = sheet.max_column
        print("total cols are ", str(total_cols))
        print("total rows are ", str(total_rows))
        main_data = []

        for i in range(2, total_rows + 1):
            temp_data = []
            for j in range(1, total_cols + 1):
                data = sheet.cell(row=i, column=j).value
                if str(data).lower() == str(account_type).lower():
                    temp_data.insert(j, sheet.cell(row=i, column=j + 1).value)
                    temp_data.insert(j, sheet.cell(row=i, column=j + 2).value)
                    main_data.insert(i, temp_data)
                    return main_data
    except PermissionError:
        print('Permission error')
