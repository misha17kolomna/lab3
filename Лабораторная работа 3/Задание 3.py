# TODO  Напишите функцию count_letters
def count_letters(main_str):
    count = {}
    for char in main_str.lower():
        if char.isalpha():
            count[char] = count.get(char, 0) + 1
    return count



# TODO Напишите функцию calculate_frequency
def calculate_frequency(count):
    total_count = sum(count.values())
    frequency = {key: value / total_count for key, value in count.items()}
    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
count = count_letters(main_str)
frequencies = calculate_frequency(count)
print("\n".join([f"{key}: {value:.2f}" for key, value in frequencies.items()]))

#radius = 5
#print(f"Длина окружности с радиусом {radius}: {calculate_circumference(radius):.2f}")
#print(f"Площадь круга с радиусом {radius}: {calculate_area(radius):.4f}")