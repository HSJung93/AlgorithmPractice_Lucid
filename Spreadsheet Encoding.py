def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str) - 1
    for s in col_str:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1 
    return num

# Encoding Tests:
print(spreadsheet_encode_column("A")) # 1
print(spreadsheet_encode_column("AA")) # 27
print(spreadsheet_encode_column("ZZ")) # 702