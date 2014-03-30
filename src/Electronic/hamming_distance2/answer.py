# http://www.checkio.org/mission/hamming-distance2/
__author__ = 'ken'


def checkio(n, m):
    ns = bin(n)[2:]
    ms = bin(m)[2:]
    ns = ("0" * max(0, len(ms)-len(ns))) + ns
    ms = ("0" * max(0, len(ns)-len(ms))) + ms
    cnt = [1 for a, b in zip(ns, ms) if a != b]
    return len(cnt)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
