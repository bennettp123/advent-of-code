#!/usr/bin/env python


def process(s, depth=0):
    if s.startswith('<'):
        # is garbage
        pos = 0
        while True:
            pos += 1
            if s[pos] == '!':
                # skip next char
                pos += 1
                continue
            if s[pos] == '>':
                endpos = pos
                return 0, endpos, 0
    if s.startswith('{'):
        # is group
        score = depth + 1
        pos = 0
        while True:
            pos += 1
            if s[pos] == '!':
                # skip next char
                pos += 1
                continue
            if s[pos] == '<':
                # skip garbage
                _, pos_delta, _ = process(s[pos:])
                pos += pos_delta
                continue
            if s[pos] == '{':
                # process inner group
                _, pos_delta, score_delta = process(s[pos:], depth=depth+1)
                pos += pos_delta
                score += score_delta
                continue
            if s[pos] == '}':
                endpos = pos
                return 0, endpos, score


if __name__ == '__main__':
    total = 0
    with open('input', 'r') as f:
        for line in f:
            _, _, score = process(line)
            total += score

    print('part 1: total group score is {0}'.format(total))

