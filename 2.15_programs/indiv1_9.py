#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    vowels = ("a", "e", "i", "o", "u", "y")
    with open("indiv1_text.txt", "r", encoding="utf-8") as fileptr:
        for line in fileptr.readlines():
            for word in line.split(" "):
                if word.lower().startswith(vowels) and word.lower().endswith(vowels):
                    print(word, end=" ")
