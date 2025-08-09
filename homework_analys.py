def text_analysis(text):
    punctuation = [",", ".", "!", "?", ":", ";", "'"]
    words = "".join(l for l in text if l not in punctuation).split()
    print(f"Количество слов в тексте: {len(words)}")
    print(f"Самое длинное слово в тексте: {max(words, key=len)}")

    count_vowels = 0
    vowel = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    for word in words:
        for i in word.lower():
            if i in vowel:
                count_vowels += 1
    print(f"Количество гласных в тексте: {count_vowels}")

    words_counts = []
    count = 0
    for word in words:
        for i in words:
            if i.lower() == word.lower(): count += 1
        words_counts.append(count)
        count = 0
    print("Количество раз, которое каждое слово встречается в тексте:")
    for i in range(len(words)):
        print(f"{words[i]}: {words_counts[i]}")


text_analysis("Дайте уже этому французу булочек! булочек")
