#!/usr/bin/env python


def process(s, depth=0):
    if s.startswith('<'):
        # is garbage
        pos = 0
        garbage_count = 0
        while True:
            pos += 1
            if s[pos] == '!':
                # skip next char
                pos += 1
                garbage_count += -2
                continue
            if s[pos] == '>':
                endpos = pos
                garbage_count += endpos - 1
                return 0, endpos, 0, garbage_count
    if s.startswith('{'):
        # is group
        score = depth + 1
        pos = 0
        garbage_count = 0
        while True:
            pos += 1
            if s[pos] == '!':
                # skip next char
                pos += 1
                continue
            if s[pos] == '<':
                # skip garbage
                _, pos_delta, _, garbage_delta = process(s[pos:])
                pos += pos_delta
                garbage_count += garbage_delta
                continue
            if s[pos] == '{':
                # process inner group
                _, pos_delta, score_delta, garbage_delta = process(
                        s[pos:], depth=depth+1)
                pos += pos_delta
                score += score_delta
                garbage_count += garbage_delta
                continue
            if s[pos] == '}':
                endpos = pos
                return 0, endpos, score, garbage_count


if __name__ == '__main__':
    total_score = 0
    total_garbage = 0
    with open('input', 'r') as f:
        for line in f:
            _, _, score, garbage = process(line)
            total_score += score
            total_garbage += garbage

    print('part 1: total group score is {0}'.format(total_score))
    print('part 2: total garbage is {0}'.format(total_garbage))

