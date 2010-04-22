##
## This uses numpy + h5py to construct some example h5 files. 
##
import h5py
from numpy import *

## file 1
f = h5py.File("ex_1.h5")
g = f.create_group("group_1")
m = array([ random.normal(1, 1, 1000) for i in xrange(0, 10) ]).reshape(1000, 10)
d = g.create_dataset("ds_1", data = m, maxshape = (None, None))
s = array([ "".join(array(['A','C','G','T'])[random.randint(0, 4, i)]) for i in random.randint(1, 100, 20) ], 
          dtype = h5py.new_vlen(str))
ds = g.create_dataset("ds_2", data = s, maxshape = (None))

ds.attrs.create("x", array([1,2,3], dtype = "uint32"))
ds.attrs.create("y", array([[1,2,3], [5,6,7]], dtype = "uint32"))
ds.attrs.create("z", s)

a = random.randint(0, int(1e6), 3 * 7 * 9)
a = a.reshape((3, 7, 9))
g.create_dataset("ds_3", data = a, maxshape = (None, None, None))

g.create_dataset("ds_4", data = s.reshape((2, 10)))

g.create_dataset("ds_5", data = a.reshape(21, 9))


g.create_dataset("ds_6", data = random.randint(0, int(1e4), int(1e5)), dtype = "uint32")


f.close()

##
## some reading and testing.
##
f = h5py.File("ex_1.h5")
g = f["group_1"]
d = g["ds_6"]

import time

s = time.time()
k = 100000
n = 100

for i in xrange(0, n):
    b    = random.randint(0, d.shape[0] - k)
    e    = b + k
    print len(d[b:e])

print "total time %d" % int(time.time() - s)
