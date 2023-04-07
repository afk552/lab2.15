#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    words = []
    vowels = ("a", "e", "i", "o", "u", "y")
    with open("indiv1_text.txt", "r", encoding="utf-8") as fileptr:
        for line in fileptr.read().split(" "):
            words.append(line)

    for word in words:
        if word.lower().startswith(vowels) and word.lower().endswith(vowels):
            print(word, end=" ")
