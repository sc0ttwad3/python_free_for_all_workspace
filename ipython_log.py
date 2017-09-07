# IPython log file

get_ipython().magic('logstart')
map(lambda *a: a, range(3))
list(map(lambda *a: a, range(3)))
list(map(lambda *a: a, range(3), 'abc', range(4,7)))
# map stops when shortest iterables is exhausted
quit()
