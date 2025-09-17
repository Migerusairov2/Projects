import xlsxwriter

workbook = xlsxwriter.Workbook('sample.xlsx')
worksheet = workbook.add_worksheet("My Sheet")

name = 'Miguel'
age = 24
address = '#107 Villa Light Gumamela st.'


def download_xlsx():
    list = []
    list.append([name, age, address])

    for row, (x, y, z) in enumerate(list):
        worksheet.write(row, 0, x)
        worksheet.write(row, 1, y)
        worksheet.write(row, 2, z)

    workbook.close()


download_xlsx()
