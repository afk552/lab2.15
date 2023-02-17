#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

# Разложить аудиофайлы по папкам с именами исполнителей,
# указанных в имени файла перед знаком ' - '.
# Типы звуковых файлов: mp3, wav, flac, ogg.

if __name__ == "__main__":
    path = os.getcwd()
    audio_ext = ["mp3", "wav", "flac", "ogg"]
    for filename in os.listdir(path):
        file_ext = filename.split('.')[-1]
        if file_ext in audio_ext:
            artist = filename.rpartition(' - ')[0]
            os.mkdir(artist)
            # Скопировать/переместить файл через os не получилось
            shutil.copy(f'{filename}', f'{artist}/{filename}')
            os.remove(f"{filename}")
