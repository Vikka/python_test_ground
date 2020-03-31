def foobar(pos_1, pos_2, *args, kw_1=None, kw_2=None, kw_25=42, **kwargs):
    print('===========')
    print(pos_1, pos_2)
    print(args)
    print(*args)
    print(type(args))
    print(kw_1, kw_2, kw_25)
    print(kwargs)
    print(type(kwargs))
    print(kwargs['kw_3'], kwargs['kw_4'])


def barfoo(pos_1: int, pos_2: str, pos_3: bool, *args):
    ...


def foobar_2(*, kw_2: int = 5):
    ...


class A:
    def __init__(self, pos_1: int, pos_2: str, pos_3: bool, pos_4: float = 0.,
                 *args, kw_2: int = 5, **kwargs):
        ...


class B(A):
    def __init__(self, pos_1: int, pos_2: str, pos_3: bool, *args, **kwargs):
        super().__init__(pos_1, pos_2, pos_3, *args, **kwargs)


if __name__ == '__main__':
    foobar_2(1)
    # b = B(1, 'helloworld', True)
    # b = B(1, 'helloworld', True, 1.5)
    # b = B(1, 'helloworld', True, 1.5, 4, 123, 124, 152, jo=1)
    # print(jo=b)
    # barfoo()
    # some_dict = {'kw_1': 'k1', 'kw_2': 'k2', 'kw_3': 'k3', 'kw_4': 'k4'}
    # foobar(*range(4), **some_dict)
    # foobar(*[0, 1, 2, 3], **{'kw_1': 'k1', 'kw_2': 'k2', 'kw_3': 'k3', 'kw_4': 'k4'})
    # foobar(0, 1, 2, 3, kw_1='k1', kw_2='k2', kw_3='k3', kw_4='k4')
