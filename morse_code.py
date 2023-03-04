import random


def main():
    list_words = ['orange', 'apple', 'pear', 'cherry', 'lime']
    answers = []

    cipher = {"a": ".-",
              "b": "-...",
              "c": "-.-.",
              "d": "-..",
              "e": ".",
              "f": "..-.",
              "g": "--.",
              "h": "....",
              "i": "..",
              "j": ".---",
              "k": "-.-",
              "l": ".-..",
              "m": "--",
              "n": "-.",
              "o": "---",
              "p": ".--.",
              "q": "--.-",
              "r": ".-.",
              "s": "...",
              "t": "-",
              "u": "..-",
              "v": "...-",
              "w": ".--",
              "x": "-..-",
              "y": "-.--",
              "z": "--.."}

    def morse_encode(word_1):
        """ Перевод слова на английском языке в последовательности точек и тирe """
        morze_code = ""
        for letter in word_1:
            morze_code += cipher.get(letter)
        return morze_code

    # print(morse_encode.__doc__)
    # test_1 = morse_encode("cherry")
    # print(test_1)

    def get_word():
        """ Выбор случайного слова из списка """
        morze_code = random.choice(list_words)
        return morze_code

    # print(get_word.__doc__)
    # test_2 = random.choice(list_words)
    # print(test_2)

    def print_statistics(answers):
        """ Вывод статистики """
        print(f'Всего задачек: {len(answers)}')
        print(f'Отвечено верно: {answers.count(True)}')
        print(f'Отвечено неверно: {answers.count(False)}')
        return

    # print(print_statistics.__doc__)
    # test_3 = print_statistics(answers)
    # print(test_3)

    print('\nСегодня мы потренируемся расшифровывать азбуку Морзе\nНажмите Enter и начнем')
    user = input()

    for word in range(len(list_words)):
        ask_word = get_word()

        # print(ask_word)
        print(f'Слово {word + 1} - {morse_encode(ask_word)}')
        user_answer = input().lower()
        if ask_word != user_answer:
            answers.append(False)
            print(f'Неверно, {ask_word}!\n')
        else:
            answers.append(True)
            print(f'Верно, {ask_word}!\n')

    print_statistics(answers)


if __name__ == "__main__":
    main()
