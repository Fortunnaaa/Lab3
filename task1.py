# Отримуємо введений рядок від користувача
input_string = input("Введіть довільний рядок: ")

# Розділяємо рядок на слова, використовуючи пробіли як роздільник
words = input_string.split()
result_words = []

for word in words:
    if len(word) >= 3:  # Перевірка, чи довжина слова дозволяє зробити операцію зрізу
        sliced_word = word[2::3]
        result_words.append(sliced_word)
    else:
        result_words.append(word)

# Об'єднання слів у новий рядок
result_string = ' '.join(result_words)
print("Результат:", result_string)
