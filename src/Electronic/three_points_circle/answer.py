# http://www.checkio.org/mission/three-points-circle/solve/
# 美しくない。中心が原点のところは考えなくて良いのかな。

__author__ = 'ken'

from collections import namedtuple
import re
import math

Point = namedtuple('Point', "x y")

def add(self, other):
    return Point(self.x + other.x, self.y+other.y)

Point.__add__ = add


def checkio(data):
    points = parse_points(data)
    cp = Point(0.0, 0.0)
    w = 100.0
    while True:
        ok_way = [distance_diff(cp, points), None]
        if ok_way[0] < 0.0000001:
            break
        mvs = [Point(w, 0), Point(-w, 0), Point(0, w), Point(0, -w)]
        mvs += [Point(w,w), Point(w,-w), Point(-w,w), Point(-w, -w)]
        for way in mvs:
            new_diff = distance_diff(cp + way, points)
            if new_diff < ok_way[0]:
                ok_way = [new_diff, cp + way]
        if ok_way[1]:
            cp = ok_way[1]
        else:
            w /= 2
    r = math.sqrt(distance2(points[0], cp))
    ret = "(x%s)^2+(y%s)^2=%s^2" % (num2str(-cp.x), num2str(-cp.y), num2str(r, False))
    return ret


def distance2(p1, p2):
    return (p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y)


def num2str(num, add_sign=True):
    num = round(num, 2)
    ret = re.sub(r"\.?0+$", "", str(abs(num)))
    if num > 0 and add_sign:
        ret = "+%s" % ret
    elif num < 0:
        ret = "-%s" % ret
    return ret


def distance_diff(p, points):
    dists = [distance2(p, px) for px in points]
    avg = sum(dists) / len(dists)
    return sum([abs(x - avg) for x in dists])


def parse_points(data):
    ret = []
    for x, y in re.findall(r"\((\d+),(\d+)\)", data):
        ret.append(Point(int(x), int(y)))
    return ret


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
