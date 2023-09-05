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

    text = text.strip()
    for i in range(10):
        text = text.replace("? ", "?")
        text = text.replace(". ", ".")
        text = text.replace(": ", ":")
        text = text.replace(" ?", "?")
        text = text.replace(" .", ".")
        text = text.replace(" :", ":")
    for i in text:
        if i in ('?', '.', ':'):
            print(i, end="\n\n")
        else:
            print(i, end='')


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
