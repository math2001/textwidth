# -*- encoding: utf-8 -*-
# allowdebugfeatures

def breakline(line, width):
    if len(line) <= width: return 
    index = line.rfind(' ', 0, width)
    if index == -1: return 
    return line[:index] + '\n' + line[index+1:]


def test():
    args_results = [
        (('this is a test', 10), 'this is a\ntest'),
        (('this is a  test', 10), 'this is a\n test'),
        (('this is a @3', 10), 'this is a\n@3'),
        (('sssssssssssssssssssss', 10), None),
        (('hello', 10), None),
    ]
    for args, result in args_results:
        actual = breakline(*args)
        if actual != result:
            'sdfsdf '
            'asdfsa'
            print('Invalid result for', args)
            print('     got {!r},\n'
                  'expected {!r}'.format(actual, result))

if __name__ == '__main__':
    test()