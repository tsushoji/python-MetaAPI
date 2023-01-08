import openpyxl

def convert_result_to_excel(result,excel_file_path):
  wb=openpyxl.Workbook()
  sheet=wb['Sheet']

  header_list=list(result[0].keys())
  for c in range(len(header_list)):
    sheet.cell(row=1,column=c+1).value=header_list[c]

  for r in range(len(result)):
    for c in range(len(header_list)):
      sheet.cell(row=r+2,column=c+1).value=result[r][header_list[c]]

  wb.save(excel_file_path)
