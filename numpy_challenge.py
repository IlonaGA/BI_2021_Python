# %%
import numpy as np


def task_1(n):
    # Solution 1

    arr = np.zeros(n)
    arr[0] = 0
    arr[1] = 1

    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i - 2]

    print(arr)

    # Solution 2

    arr = np.arange(n)
    phi = (1 + np.sqrt(5)) / 2

    arr = (phi ** arr - (-1 / phi) ** arr) / np.sqrt(5)

    print(arr)

    # Solution 3

    arr = np.arange(n)
    phi = (1 + np.sqrt(5)) / 2

    def f(x):
        return (phi ** x - (-1 / phi) ** x) / np.sqrt(5)

    vecf = np.vectorize(f)
    arr = vecf(arr)
    print(arr)


def matrix_multiplication(a, b):
    a = np.asarray(a)
    b = np.asarray(b)

    return a @ b


def multiplication_check(list_mat):
    list_mat = [np.asarray(a) for a in list_mat] 

    m, n = list_mat[0].shape

    for i in range(1, len(list_mat)):
        if n == list_mat[i].shape[0]:
            n = list_mat[i].shape[1]
        else:
            return False

    return True


def multiply_matrices(list_mat):
    list_mat = [np.asarray(a) for a in list_mat] 

    ans = list_mat[0]

    for i in range(1, len(list_mat)):
        if ans.shape[1] == list_mat[i].shape[0]:
            ans = ans @ list_mat[i]
        else:
            return None

    return ans


def compute_2d_distance(a, b):
    a = np.asarray(a)
    b = np.asarray(b)

    return np.sqrt((a - b) @ (a - b))


def compute_multidimensional_distance(a, b):
    a = np.asarray(a)
    b = np.asarray(b)

    return np.sqrt((a - b) @ (a - b))


def compute_pair_distances(X):
    X = np.asarray(X)

    dist = np.zeros(shape=(X.shape[0], X.shape[0]))

    for i in range(1, len(X)):
        for j in range(i):
            dist[i][j] = compute_multidimensional_distance(X[i], X[j])
            dist[j][i] = dist[i][j]

    return dict


# %%
if __name__ == '__main__':
    task_1(10)

    print(matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]))

    print(multiplication_check([[[1, 2], [3, 4]], [[5, 6, 10], [7, 8, 11]]]))
    print(multiplication_check([[[1, 2, 5], [3, 4, 10]], [[5, 6], [7, 8]]]))

    print(multiply_matrices([[[1, 2], [3, 4]], [[5, 6, 10], [7, 8, 11]]]))
    print(multiply_matrices([[[1, 2, 5], [3, 4, 10]], [[5, 6], [7, 8]]]))

    print(compute_2d_distance([0, 0], [3, 4]))
