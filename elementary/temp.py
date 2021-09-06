import fermulerpy.elementary as fle
import timeit

n = 1000000
t1 = timeit.repeat(lambda: fle.get_divisors(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 10000000
t1 = timeit.repeat(lambda: fle.get_divisors(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 100000000
t1 = timeit.repeat(lambda: fle.get_divisors(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 1234567812312312
t1 = timeit.repeat(lambda: fle.get_divisors(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 1000000000100011
t1 = timeit.repeat(lambda: fle.get_divisors(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))


