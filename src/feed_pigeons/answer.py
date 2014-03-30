# http://www.checkio.org/mission/feed-pigeons/solve/
__author__ = 'ken'


def checkio(number):
    pigeons = 0
    for turn in range(1, 1000000):
        # consume by current pigeons
        number -= pigeons
        if number < 1:
            break
        new_pigeons = min(number, turn)
        number -= new_pigeons
        pigeons += new_pigeons
    return pigeons


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
