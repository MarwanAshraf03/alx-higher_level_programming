#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        return
    leng = len(text)
    i = 0
    while i < leng:
        # print(i, end='')
        if text[i] in ('.', '?', ':'):
            print(f"{text[i]}\n\n", end='')
            i += 1
        else:
            print(text[i], end='')
        i += 1