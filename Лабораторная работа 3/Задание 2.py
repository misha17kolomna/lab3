# TODO Напишите функцию find_common_participants
def find_common_participants(first,second,x=","):
    first_array = first.split(x)
    second_array = second.split(x)

    common_participants = list(set(first_array).intersection(second_array))
    common_participants.sort()
    return common_participants



first = "Иванов|Петров|Сидоров"
second = "Петров|Сидоров|Смирнов"
print(find_common_participants(first,second,'|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
