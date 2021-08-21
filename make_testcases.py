
from random import randrange, choice
import string


def randlist(lengthfn=lambda: randrange(20), rng=None, postfns=None):
    if postfns is None:
        postfns = []
    if rng is None:
        def rng(): return randrange(100)
    result = [rng() for _ in range(lengthfn())]
    for fn in postfns:
        result = fn(result)
    return result


def testdata(trials=10, fns=None):
    if fns is None:
        fns = [randlist]
    return [[fn() for fn in fns] for _ in range(trials)]


def randstrings(trials=10, characters=string.ascii_lowercase):
    return testdata(trials=trials,
                    fns=[lambda: randlist(rng=lambda: choice(characters),
                                          postfns=[lambda chrs: ''.join(chrs),
                                                   lambda s: '"' + s + '"'])],
                    )


def randnums(trials=10):
    return testdata(trials=trials,
                    fns=[lambda: randlist(rng=lambda: randrange(200),
                                          lengthfn=lambda: randrange(1, 21),)],
                    )


def _quniq(x):
    t = type(x)
    return t(set(x))


if __name__ == '__main__':
    datas = testdata(fns=[lambda: randlist(rng=lambda: randrange(1, 100),
                                           lengthfn=lambda: randrange(1, 20),
                                           postfns=[])])
    datas = randnums()
    for data in datas:
        for row in data:
            print(row)
