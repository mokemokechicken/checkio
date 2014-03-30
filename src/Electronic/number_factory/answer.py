# http://www.checkio.org/mission/number-factory/solve/


def checkio(number):
    factors = []
    for n in [9-x for x in range(8)]:
        while number % n == 0:
            factors.append(n)
            number /= n
    if number > 1:
        return 0
    return int("".join([str(y) for y in sorted(factors)]))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
