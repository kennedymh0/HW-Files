import numpy as np

# 1. Hey Twin. Given an array, find the rows where all the values are equal.
def findEqual(arr):
    equal_rows = [row for row in arr if np.all(row ==row[0])]
    return np.array(equal_rows)

arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
result = findEqual(arr)
print(result)

# 2. Checkers. Create a checkerboard pattern of zeros and ones using a slicing + sliding approach.
arr = np.zeros((8, 8), dtype=int)

arr[1::2, ::2] = 1
arr[::2, 1::2] = 1

print(arr)


# 3. I need some space. Give an array of strings, return an array where each letter in each string is separated by a space.
def spaceBetween(arr):
    separated = np.array([' '.join(word) for word in arr], dtype='<U{}'.format(max(map(len, arr))))
    return separated

myarr = np.array(['python', 'is', 'cool!'])

def add_space(word):
    return ' '.join(list(word))

space_between = np.vectorize(add_space)
result = space_between(myarr)
print(result)


# 4. Everything is in Order. Given a multidimensional matrix, sort the matrix along the columns.
def sorting(matrix):
    return np.sort(matrix, axis=0)

np.random.seed(12345)
a = np.random.randint(1, 50, (4, 5))

print("Sorted matrix along columns:")
print(sorting(a))