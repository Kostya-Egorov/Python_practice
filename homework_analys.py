def text_len(words):
    print(f"Количество слов в тексте: {len(words)}")


def most_large(words):
    print(f"Самое длинное слово в тексте: {max(words, key=len)}")


def vowels_count(words):
    count_vowels = 0
    vowel = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    for word in words:
        for i in word.lower():
            if i in vowel:
                count_vowels += 1
    print(f"Количество гласных в тексте: {count_vowels}")


def repeat_words(words):
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


punctuation = [",", ".", "!", "?", ":", ";", "'"]
words = "".join(l for l in input("Введите текст: ") if l not in punctuation).split()
text_len(words)
most_large(words)
vowels_count(words)
repeat_words(words)
