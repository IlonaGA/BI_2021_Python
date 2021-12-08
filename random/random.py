# %%
import numpy as np
import random
from time import time
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# %% prepare
def count_time(func, n):
    start = time()
    for i in range(n):
        func()
    end = time()

    return (end - start) / n


# %% task 1
random_time = []
numpy_time = []
numpy_shape_time = []
lengths = [i * 10 for i in range(1, 100)]

for length in lengths:
    random_time.append(count_time(lambda: [random.random()
                                           for i in range(length)], 100))

    numpy_time.append(count_time(lambda: [np.random.random()
                                          for i in range(length)], 100))

    numpy_shape_time.append(count_time(lambda: np.random.random(length), 100))

# %%
plt.plot(lengths, random_time, label='random')
plt.plot(lengths, numpy_time, label='numpy')
plt.plot(lengths, numpy_shape_time, label='numpy_shape')
plt.legend()
plt.show()

# %% task 2


def is_sorted(arr):
    return np.all(arr[:-1] < arr[1:])


def monkey_sort(arr):
    while not is_sorted(arr):
        permut = np.random.permutation(len(arr))
        arr = arr[permut]


df = {'time': [], 'length': []}
for length in [1, 3, 6, 9]:
    print(length)
    for _ in range(10):
        arr = np.random.permutation(length)
        took = count_time(lambda: monkey_sort(arr), 1)
        df['time'].append(took)
        df['length'].append(length)

df = pd.DataFrame(df)
df.head()

# %%
sns.boxplot(data=df, x='length', y='time')
plt.show()

# %% task 3
# Я очень люблю функцию cumsum
# Мне очень понравилось такое решение

steps = 1000
x = np.zeros(steps, dtype=int)
y = np.zeros(steps, dtype=int)

up_or_right = np.random.randint(0, 2, size=steps, dtype=bool)
x[up_or_right] = 1
y[~up_or_right] = 1

switch_up_down = np.random.randint(0, 2, size=steps, dtype=bool)
x[switch_up_down] *= -1

switch_right_left = np.random.randint(0, 2, size=steps, dtype=bool)
y[switch_right_left] *= -1

x_total = np.cumsum(x)
y_total = np.cumsum(y)

plt.scatter(x, y, alpha=10 / steps)
plt.show()

plt.scatter(x_total, y_total, c=np.arange(steps))
plt.show()


# %% task 4

size = 10000
vertices = np.array([[0, 0], [0.5, np.sqrt(3) / 2], [1, 0]])
points = np.zeros(shape=(size, 2))
# frac = 1 / 2

for i in range(1, size):
    j = np.random.randint(0, len(vertices))
    points[i] = (vertices[j] - points[i - 1]) / 2 + points[i - 1]

plt.scatter(points[:, 0], points[:, 1], s=0.1)
plt.show()

# %% task 5

text = input()


def random_word_permut(word):
    mid = np.array([letter for letter in word[1: -1]])
    mid = mid[np.random.permutation(len(mid))]

    return word[0] + ''.join(mid) + word[-1]


print(' '.join(map(random_word_permut, text.split())))