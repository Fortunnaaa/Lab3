def find_duplicate_words(sentence):
    words = sentence.split()
    word_count = {}

    # Ітеруємося по словах у реченні і підраховуємо їх кількість
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Шукаємо перше слово, яке зустрічається двічі
    for word, count in word_count.items():
        if count == 2:
            return word

    return None

sentence = input("Введіть речення: ")

# Визначаємо два однакових слова та виводимо їх
duplicate_word = find_duplicate_words(sentence)

if duplicate_word:
    print(f"Два однакових слова у реченні: ", duplicate_word)
else:
    print("У реченні немає двох однакових слів.")
