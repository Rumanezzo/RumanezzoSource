import re

states = ['#alabama# ', '?Georgia!', 'FlOrIda', ' south carolina##', 'West virginia?']


def remove_punctuation(value):
    return re.sub('[!#&?]', '', value)


clean_ops = [str.strip, remove_punctuation, str.title]


def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


out = clean_strings(states, clean_ops)
print(out)