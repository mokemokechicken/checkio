# http://www.checkio.org/mission/brackets/solve/
__author__ = 'ken'

BRACES = ['{}', '()', '[]']


def checkio(expression):
    stack = []
    for s in expression:
        for brace in BRACES:
            if s == brace[0]:
                stack.append(s)
            elif s == brace[1]:
                if not stack or stack.pop() != brace[0]:
                    return False
    return len(stack) == 0


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
