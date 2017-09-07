
import sys
import timeit
import numpy as np

"""
  Vector addition

  > python vectorsum.py n

  a vector - squared
  b vector - cubed

"""

def numpysum(n):
    a = np.arange(n)**2
    b = np.arange(n)**3
    c = a+b
    return c

def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []

    for i in range(len(a)):
        sq = i**2
        cu = i**3
        c.append(sq + cu)
        return c

def wrapper(func, *args):
    def wrapped():
        return func(*args)
    return wrapped



size = int(sys.argv[1])
print(size)

#start = datetime.now()
wrappedPySum = wrapper(pythonsum, size)
pyResult = timeit.timeit(wrappedPySum, number=size)
#delta = datetime.now() -start
print("pythonsum time: ", pyResult)

#start = datetime.now()
wrappedNumPySum = wrapper(numpysum, size)
numResult = timeit.timeit(wrappedPySum, number=size)
print("numpysum  time: ", numResult)
#delta = datetime.now -start
#print("Last 2 elements: ", c[-2:])
#print("numpysum time: ", delta.microseconds)
