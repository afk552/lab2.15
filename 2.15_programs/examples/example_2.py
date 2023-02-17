#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # open the file.txt in write mode.
    fileptr = open("file2.txt", "a")

    # overwriting the content of the file
    fileptr.write("Python has an easy syntax and user-friendly interaction.")

    # closing the opened file
    fileptr.close()
