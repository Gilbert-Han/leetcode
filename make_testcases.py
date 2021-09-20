from random import randrange, choice
import string


def randlist(lengthfn=lambda: randrange(20), rng=lambda: randrange(100), postfns=None):
    if postfns is None:
        postfns = []
    result = [rng() for _ in range(lengthfn())]
    for fn in postfns:
        result = fn(result)
    return result

def testdata(trials=10, fns=[randlist]) -> list[list[int]]:
    return [[fn() for fn in fns] for _ in range(trials)]

def randstrings(trials=10, lengthfn=lambda: randrange(100), characters=string.ascii_lowercase):
    return testdata(trials=trials,
                    fns=[lambda: randlist(rng=lambda: choice(characters),
                                          lengthfn=lengthfn,
                                          postfns=[lambda chrs: ''.join(chrs),
                                                   lambda s: '"' + s + '"'])],
                    )

def randnums(trials=10, r=range(201), list_length=20):
    return testdata(trials=trials,
                    fns=[lambda: randlist(rng=lambda: randrange(r.start, r.stop, r.step),
                                          lengthfn=lambda: randrange(list_length),)],
                    )


def _quniq(x):
    t = type(x)
    return t(set(x))

def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    # datas = testdata(fns=[lambda: randlist(rng=lambda: randrange(1, 100),
    #                                        lengthfn=lambda: randrange(1, 20),
    #                                        postfns=[])])
    # datas = randstrings(trials=30, characters='ab')
    datas = randnums(trials=100, r=range(501), list_length=500)
    datas = [[r for r in d if not is_even(sum(r)) and is_even(len(r))] for d in datas]
    for data in datas:
        for row in data:
            print(row)
