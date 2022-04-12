# %%
import time
import numpy as np


def time_measure(func):
    def inner_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        return end - start
    return inner_func


@time_measure
def test_time_measure(sleep, msg='I love functional programming'):
    print(msg)
    time.sleep(sleep)

print(test_time_measure(5, msg='Does printing takes musch time?'))

# %%


def my_logger(func):
    def inner_func(*args, **kwargs):
        if len(args) == 0 and len(kwargs) == 0:
            print(f'function {func.__name__} was called with ' +
                  'no arguments')
        elif len(args) != 0 and len(kwargs) == 0:
            print(f'function {func.__name__} was called with ' +
                  'positional arguments {args}')
        elif len(args) == 0 and len(kwargs) != 0:
            print(f'function {func.__name__} was called with ' +
                  ' keyword arguments {kwargs}')
        else:
            print(f'function {func.__name__} was called with' +
                  'positional arguments {args} and keyword arguments {kwargs}')

        ans = func(*args, **kwargs)
        print(f'function {func.__name__} ' +
               'returns output of type {type(ans).__name__}')
        return ans
    return inner_func


@my_logger
def test_logger(a, b, c, d):
    return {a: b, c: d}

print(test_logger(1, 2, c='3', d='4'))

# %%


def roulette(prob=0, value='Alive'):
    def decor(func):
        def inner_func(*args, **kwargs):
            if np.random.random() < prob:
                return value
            else:
                return func(*args, **kwargs)

        return inner_func
    return decor


@roulette(prob=1/6, value='Dead')
def test_roulette(msg):
    return msg

for i in range(10):
    print(test_roulette(i))
