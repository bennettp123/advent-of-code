#!/usr/bin/env python


def unescape(s):
    return s[1:-1].decode('string_escape')


def escape(s):
    return '"' + s.replace('\\', '\\\\').replace('"', r'\"') + '"'


if __name__ == '__main__':

    unescaped_len = 0
    orig_code_len = 0
    escaped_len = 0

    with open('input', 'r') as f:
        for line in f:
            line = line.strip()
            orig_code_len += len(line)
            unescaped_len += len(unescape(line))
            escaped_len += len(escape(line))

    print('part 1: original len {0}, unescaped len {1}, difference {2}'
            .format(orig_code_len, unescaped_len,
                orig_code_len - unescaped_len))

    print('part 2: original len {0}, escaped len {1}, difference {2}'
            .format(orig_code_len, escaped_len,
                orig_code_len - escaped_len))

