#variant 2

vowels = set('aeiouy')
numbers = set('1234567890')

#Задаем текст вручную
text1 = "QWERTYUIOPLKHGFDSAZXCVBNM1234567890" #Тут точно больше согласных
text2 = "AEIOUYBCD12387234"                   #Тут точно больше гласных
text3 = "abce1234"                            #Кол-во равно

def compare_items(text: str) -> None:
    number_vowels = sum(1 for x in text if x in vowels)
    number_others = sum(1 for x in text if x not in vowels)
    number_numbers = sum(1 for x in text if x in numbers)

    if number_vowels > number_others - number_numbers:
        print("Гласных больше")
    elif number_vowels < number_others - number_numbers:
        print("Согласных больше")
    else:
        print("Количества равны")

compare_items(text1)
compare_items(text2)
compare_items(text3)
