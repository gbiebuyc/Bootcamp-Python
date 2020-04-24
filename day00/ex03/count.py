#!/usr/bin/env python3
import string

def text_analyzer(text=None):
    if text is None:
        text = input('What is the text to analyse?\n>> ')
    num_upper_char = 0
    num_lower_char = 0
    num_punctuation = 0
    num_spaces = 0
    for c in text:
        if c.isupper():
            num_upper_char += 1
        if c.islower():
            num_lower_char += 1
        if c in string.punctuation:
            num_punctuation += 1
        if c == ' ':
            num_spaces += 1
    print('The text contains %d characters:\n' % len(text))
    print('- %d upper letters\n' % num_upper_char)
    print('- %d lower letters\n' % num_lower_char)
    print('- %d punctuation marks\n' % num_punctuation)
    print('- %d spaces' % num_spaces)


