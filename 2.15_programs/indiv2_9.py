#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from random import choice

if __name__ == "__main__":
    pwd = ""
    error_cnt = 0
    with open("indiv2_words.txt", "r", encoding="utf-8") as fileptr:
        words = fileptr.readlines()

    if len(words) <= 1:
        print("В файле недостаточно слов!", file=sys.stderr)
        exit(1)
    # Отбрасываем слова менее чем из трех букв
    words = [i for i in words if len(i) >= 3]

    while len(pwd) < 8:
        word1 = choice(words).capitalize()
        word2 = choice(words).capitalize()
        if word1 != word2:
            pwd = f"{word1}{word2}"
        error_cnt += 1
        if len(pwd) > 10:
            pwd = ""
        # Проверка на невозможность создания пароля из заданных слов
        if error_cnt > len(words):
            print("Из слов невозможно создать пароль!", file=sys.stderr)
            exit(1)
    print(f"Сгенерированный пароль: {pwd}")
