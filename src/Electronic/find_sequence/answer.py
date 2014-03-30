# http://www.checkio.org/mission/find-sequence/solve/
__author__ = 'ken'


def checkio(matrix):
    size = len(matrix)
    for y in range(size):
        for x in range(size):
            if find_sequence(matrix, (x, y)):
                return True
    return False


def find_sequence(matrix, pos):
    """ search only way to 1, 2, 3, 6 (ten key)"""
    for direction in [(-1, 1), (0, 1), (1, 1), (1, 0)]:
        is_found = find_sequence_to_direction(matrix, pos, direction)
        if is_found:
            return True
    return False


def find_sequence_to_direction(matrix, pos, direction, n=1):
    if n == 4:
        return True
    here = get_number(matrix, pos)
    new_pos = (pos[0]+direction[0], pos[1]+direction[1])
    near = get_number(matrix, new_pos)
    if here == near:
        is_found = find_sequence_to_direction(matrix, new_pos, direction, n+1)
        if is_found:
            return True
    return False


def get_number(matrix, pos):
    if (0 <= pos[0] < len(matrix)) and (0 <= pos[1] < len(matrix)):
        return matrix[pos[1]][pos[0]]
    return None


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
