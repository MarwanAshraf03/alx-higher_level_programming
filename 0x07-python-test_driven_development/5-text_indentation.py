#!/usr/bin/python3
"""Text Indentation Module"""


def text_indentation(text):
    """
    prints text indented with ., ? and :

    Args:
    text: text to be indented
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    words = text.split()
    leng = len(words)
    i = 0
    while i < leng:
        if (words[i][-1] in ('.', '?', ':')) & (len(words[i])==1):
            words[i-1] += words[i]
            del words[i]
        i += 1
        leng = len(words)
    leng = len(words)
    i = 0
    while i < leng:
        if words[i][-1] in ('.', '?', ':'):
            print(f"{words[i]}\n\n", end='')
        else:
            print(words[i], end=' ' if i+1 != leng else '')
        i += 1
