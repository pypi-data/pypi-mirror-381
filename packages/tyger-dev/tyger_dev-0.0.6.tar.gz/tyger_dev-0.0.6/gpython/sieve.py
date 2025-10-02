

class Stream:
    def __init__(self, h:int, t: Callable[[], 'Stream']):
        self.h = h
        self.t = t

def countFrom(n: int) -> Stream:
    return Stream(n, lambda:countFrom(n+1))

def sift(n: int, s: Stream) -> Stream:
    if s.h % n == 0:
        return sift(n, s.t())
    else:
        return Stream(s.h, lambda: sift(n, s.t()))

def sieve(s: Stream) -> Stream:
    return Stream(s.h, lambda: sieve(sift(s.h, s.t())))


def take(n: int, s: Stream) -> list[int]:
    if n==0:
        return []
    else:
        return [s.h] + take(n-1, s.t())


print(take(200, sieve(countFrom(2))))
#take(100, sieve(countFrom(2)))














