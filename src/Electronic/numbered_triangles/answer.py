# http://www.checkio.org/mission/numbered-triangles/solve/
__author__ = 'ken'
from copy import copy


def checkio(chips):
    chip_list = [Chip(i, ary) for i, ary in enumerate(chips)]
    cc = ChipCombination(chip_list)
    return cc.solve()


class ChipCombination(object):
    def __init__(self, chip_list):
        self.chip_list = chip_list[:]
        self.max_num = 0

    def solve(self, chip_list=None):
        chip_list = chip_list or self.chip_list[:]
        base_chip = self.find_unlinked_chip(chip_list)
        if not base_chip:
            self.max_num = max(self.max_num, sum([x.outside_num() for x in chip_list]))
            return self.max_num
        chip_list.remove(base_chip)
        candidates = []
        for chip in [c for c in chip_list if c != base_chip]:
            for num in set(base_chip.unlink_num_list):
                if chip.can_link_by_num(base_chip, num):
                    candidates.append((chip, num))
        for chip, num in candidates:
            new_chip_list = chip_list[:]
            new_chip_list.remove(chip)
            a = base_chip.clone().link_with(chip, num)
            b = chip.clone().link_with(base_chip, num)
            new_chip_list.extend((a, b))
            self.solve(new_chip_list)
        return self.max_num

    def find_unlinked_chip(self, chip_list):
        cl = [c for c in chip_list if not c.is_full_linking()]
        if cl:
            return cl[0]
        else:
            return None


class Chip(object):
    def __init__(self, id, ary, unlinks=None, links=None):
        self.id = id
        self.ary = ary
        self.unlink_num_list = unlinks or ary
        self.links = links or {}

    def __repr__(self):
        return "Chip: id=%s ary=%s unlink_nums=%s link=%s" % (self.id, self.ary, self.unlink_num_list, self.links)

    def clone(self):
        return Chip(self.id, self.ary[:], self.unlink_num_list[:], copy(self.links))

    def is_full_linking(self):
        return len(self.unlink_num_list) == 1

    def outside_num(self):
        if not self.is_full_linking():
            raise RuntimeError()
        return self.unlink_num_list[0]

    def can_link_by_num(self, chip, num):
        return chip.id not in self.links.values() and num in self.unlink_num_list and not self.is_full_linking()

    def link_with(self, chip, num):
        if self.can_link_by_num(chip, num) and chip.can_link_by_num(self, num):
            self.unlink_num_list.remove(num)
            self.links[num] = chip.id
            return self
        else:
            raise RuntimeError()

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"
