import math

_INIT_PRIMES = (2, 3, 5)
_INCREMENTS = (4, 2, 4, 2, 4, 6, 2, 6)


def factorize(value):
    result = list()

    if value <= 1:
        return result

    for factor in _INIT_PRIMES:
        while value % factor == 0:
            result.append(factor)
            value //= factor

    factor = 7
    root = math.sqrt(value)
    increment_pos = 0

    while factor <= root:
        recalc_root = value % factor == 0

        while value % factor == 0:
            result.append(factor)
            value //= factor

        if recalc_root:
            root = math.sqrt(value)

        factor += _INCREMENTS[increment_pos]
        increment_pos += 1
        if increment_pos == len(_INCREMENTS):
            increment_pos = 0

    if value != 1:
        result.append(value)

    return result
