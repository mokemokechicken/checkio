# http://www.checkio.org/mission/x-o-referee/solve/
__author__ = 'ken'


def checkio(game_result):
    g = game_result
    for sym in "XO":
        for col in g:
            if col == sym * 3:
                return sym  # won: sym
        for row in zip(*g):
            if "".join(row) == sym * 3:
                return sym  # won: sym
        if (sym == g[0][0] == g[1][1] == g[2][2]) or (sym == g[0][2] == g[1][1] == g[2][0]):
            return sym

    return "D" or "X" or "O"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

