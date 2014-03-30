# http://www.checkio.org/mission/speechmodule/solve/
__author__ = 'ken'

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    words = []
    if number >= 100:
        n = int(number / 100)
        words.extend((FIRST_TEN[n-1], HUNDRED))
        number %= 100
    if 20 <= number:
        words.append(OTHER_TENS[int(number / 10) - 2])
        number %= 10
    if 10 <= number <= 19:
        words.append(SECOND_TEN[number-10])
        number = 0
    if 0 < number:
        words.append(FIRST_TEN[number-1])
    return " ".join(words)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
