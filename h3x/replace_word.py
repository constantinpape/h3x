import re
import os
import fileinput


def replace_word(file_path, word_src, word_dst, exact_match_only=False):
    with fileinput.FileInput(file_path, inplace=True) as f:
        for line in f:
            if exact_match_only:
                line = re.sub(r'\b%s\b' % word_src, word_dst, line)
                print(line, end='')
            else:
                print(line.replace(word_src, word_dst), end='')


# replace a string only if it does not have leading colons ...
def replace_stl(file_path, expression):
    # that's how much I don't get regex ...
    replace_word(file_path, '%s' % expression, 'std::%s' % expression, True)
    replace_word(file_path, 'std::std::%s' % expression, 'std::%s' % expression, True)
