#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
length2, first2 = multiple_returns("")
print("Length: {:d} - First character: {}".format(length, first))
print("Length: {:d} - First character: {}".format(length2, first2))

