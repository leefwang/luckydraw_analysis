import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

# ws = wb.active
sheet_list = ["13th Auction (12-13 Nov)", "14th Auction (14-15 Nov)", "15th Auction (16-17 Nov)",
              "16th Auction (19-20 Nov)", "17th Auction (21-22 Nov)", "18th Auction (23-24 Nov)",
              "19th Auction (26-27 Nov)", "20th Auction (28-29 Nov)"]

id_num_dict = dict()

for sheet in sheet_list:
    ws = wb.get_sheet_by_name(sheet)

    for r in ws.rows:
        row_index = r[0].row

        number = r[0].value
        email = r[2].value

        if email and number:
            if email not in id_num_dict.keys():
                id_num_dict[email] = dict()

            if sheet not in id_num_dict[email].keys():
                id_num_dict[email][sheet] = list()


            id_num_dict[email][sheet].append(number)

print(id_num_dict)

wb.close()