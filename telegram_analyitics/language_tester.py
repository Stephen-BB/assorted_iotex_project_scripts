import xlrd

from collections import Counter

workbook = xlrd.open_workbook('telegramLang.xlsx')

worksheet = workbook.sheet_by_index(0)

i = 0
list_of_user_languages = []
while i < 10002:
    list_of_user_languages.append(worksheet.cell(i, 0).value)
    i += 1


def lang_adder(input_lang_string, input_list):
    temp = 0
    for item in input_list:
        if item == input_lang_string:
            temp += 1
    return temp


print(len(list_of_user_languages))

print(Counter(list_of_user_languages).most_common(20))
