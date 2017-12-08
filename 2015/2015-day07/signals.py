#!/usr/bin/env python

import re

# singleton, flat dictionary of all signal values
# name => signal
signals = {}

# TODO make this better
regex = re.compile(r'((?P<in1>\d+|[a-z]+) )?((?P<op>AND|OR|NOT|LSHIFT|RSHIFT) )?(?P<in2>\d+|\w+) -> (\w+)')


def parse_source(s):
    s = s.split()
    signal = None

    # TODO use regex instead

    unary_operands = ('NOT')
    binary_operands = ('AND', 'OR', 'LSHIFT', 'RSHIFT')

    def is_unary(t):
        return t.strip() in unary_operands

    def is_binary(t):
        return t.strip() in binary_operands

    def is_op(t):
        return is_unary(t) or is_binary(t)

    def signal_val(t):
        try:
            return int(t.strip())
        except ValueError:
            return signals[t.strip()]

    def apply_unary(o, v):
        if o.strip() == 'NOT':
            return (~ v) & (2**16 - 1)
        else:
            raise ValueError('parse error!')

    def apply_binary(o, v1, v2):
        o = o.strip()
        if o == 'AND':
            return (v1 & v2) & (2**16 - 1)
        elif o == 'OR':
            return (v1 | v2) & (2**16 - 1)
        elif o == 'LSHIFT':
            return (v1 << v2) & (2**16 - 1)
        elif o == 'RSHIFT':
            return (v1 >> v2) & (2**16 - 1)
        else:
            raise ValueError('parse error!')

    history = []

    for item in [t.strip() for t in s if t]:
        if is_op(item):
            history.append(item) # push
            continue
        val = signal_val(item)
        try:
            prev_op = history.pop()
            if is_unary(prev_op):
                val = apply_unary(prev_op, val)
            elif is_binary(prev_op):
                try:
                    prev_val = history.pop()
                    val = apply_binary(prev_op, prev_val, val)
                except IndexError as e:
                    raise ValueError('parse error!')
        except IndexError:
            pass
        history.append(val) # push

    return history.pop()


def parse_line(line, noop=False):
    '''parse a line of input, create a Node object, and append it to nodes'''
    global signals

    source, target = (x.strip() for x in line.split(' -> '))
    source_val = parse_source(source)
    signals[target] = source_val


def parse_all(lines):
    '''input may not be in correct order'''
    lines.reverse()

    def is_int(num):
        try:
            foo = int(num)
            return True
        except ValueError:
            return False

    def connected(inputs):
        return not [i for i in inputs if not (is_int(i) or i in signals)]


    while lines:
        line = lines.pop()
        groups = regex.match(line).groupdict()
        inputs = [x for x in [groups['in1'], groups['in2']] if x is not None]
        if connected(inputs):
            parse_line(line)
        else:
            # check again later
            lines.insert(0, line)


if __name__ == '__main__':

    lines = []

    # slurp input file into lines
    with open('input', 'r') as f:
        for line in f:
            lines.append(line)

    parse_all(lines)

    # part 1: find value of a
    print('part 1: a value: {0}'.format(signals['a']))


