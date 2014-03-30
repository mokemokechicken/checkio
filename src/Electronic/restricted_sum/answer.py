# http://www.checkio.org/mission/restricted-%73um/
__author__ = 'ken'

def checkio(data, s=0):
    return (not data and s) or checkio(data[1:], s+data[0])
