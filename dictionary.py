# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#         {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# print(dict)
# dict_new = set()
# for i in dict:
#     for value in i.values():
#         dict_new.add(value)
# print(dict_new)


lst = [{"V": "S001"},{"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII": " S005 "},{" V ":" S009 "},{" VIII ":" S007 "}]
lst1 = set()
for i in lst:
    for j in i.values():
        lst1.add(j)

# print(lst, end= '\n')
print(lst1, end= ',')
