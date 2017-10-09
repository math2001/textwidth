# -*- encoding: utf-8 -*-
# allowdebugfeatures


def breakline(line, width):
    index = line.rfind(' ', 0, width + 1)
    if index == -1: return
    return line[:index], line[index+1:]

def breaklines(text, width):
    if len(text) <= width or ' ' not in text:
        return 
    lines = []
    while len(text) > width:
        index = text.rfind(' ', 0, width + 1)
        # print(text)
        # print(" " * (index - 1), '^', sep='', end='  ({})\n'.format(index))
        if index == -1:
            break
        lines.append(text[:index])
        text = text[index + 1:]
    return '\n'.join(lines) + '\n' + text

def test():
    args_results = [
        (('this is a test', 10), 'this is a\ntest'),
        (('0123456789', 10), None),
        (('0123456789 0123456789', 10), '0123456789\n0123456789'),
        (('0123456789 0123456789 0123456789', 10), '0123456789\n0123456789\n0123456789'),
        (('this is a @3', 10), 'this is a\n@3'),
        (('this is e ', 10), None),
        (('sssssssssssssssssssss', 10), None),
        (('hello', 10), None),
        (('this is 10 and this is more!', 10), ('this is 10\nand this\nis more!')),
    ]
    for args, result in args_results:
        actual = breaklines(*args)
        if actual != result:
            print('Invalid result for', args)
            print('  expected {!r}'.format(result))
            print('       got {!r}'.format(actual))
            break
    print('Done.')

if __name__ == '__main__':
    test()