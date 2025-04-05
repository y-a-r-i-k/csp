#variant 2

text = "В этом тексте есть числа 123, 4567 и 89, а также 12345."

#Умное решение
# import re #Регулярные выражения никто не запрещеал



# def find_longest_digit_sequence(text: str) -> str:
#     digit_sequences = re.findall(r'\d+', text) #Находим все последовательности цифр в тексте
    
#     if digit_sequences:
#         longest_sequence = max(digit_sequences, key=len)
#         return longest_sequence
#     else:
#         return None


def find_longest_digit_sequence(text: str) -> str:
    max_sequence = ""
    current_sequence = ""

    for char in text:
        if char.isdigit():  
            current_sequence += char  
        else:
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence
            current_sequence = ""  

    if len(current_sequence) > len(max_sequence):
        max_sequence = current_sequence

    return max_sequence


longest_sequence = find_longest_digit_sequence(text)
if longest_sequence:
    print(f"Максимальная последовательность цифр: {longest_sequence}")
else:
    print("Не найденно.")
