import time
import numpy as np

size = 10_000_000

start = time.time()
a = [i for i in range(size)]
end = time.time()
print("Python List Time:", end - start)

start = time.time()
b = np.arange(size)
end = time.time()
print("NumPy Array Time:", end - start)
