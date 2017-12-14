#!usr/bin/env python


layers = {}


def was_caught(t, layer):
    if not layer in layers:
        return False
    return not bool(t % layers[layer])


def severity(l):
    return l * layers[l]


if __name__ == '__main__':
    with open('input', 'r') as f:
        for line in f:
            layer, depth = line.strip().split(': ')
            layer, depth = int(layer), int(depth)
            layers[layer] = depth

    print sum([severity(x) for x in layers if was_caught(x, x)])

