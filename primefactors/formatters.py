def power(factors):
    last_factor = 0
    count = 0
    powerform = []
    for factor in factors:
        if factor != last_factor:
            if count:
                powerform.append('%d^%d' % (last_factor, count))
            count = 0
            last_factor = factor
        count += 1
    if count:
        powerform.append('%d^%d' % (last_factor, count))
    return ' * '.join(powerform)

formats = {
    'repr': repr,
    'power': power
}
