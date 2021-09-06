import fermulerpy.elementary as fle
import timeit

'''
get divisors execution time
'''
print("get divisors")
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

'''
divisor count execution time
'''
print("divisor count")
n = 1000000
t1 = timeit.repeat(lambda: fle.divisor_count(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 10000000
t1 = timeit.repeat(lambda: fle.divisor_count(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 100000000
t1 = timeit.repeat(lambda: fle.divisor_count(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 1234567812312312
t1 = timeit.repeat(lambda: fle.divisor_count(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 1000000000100011
t1 = timeit.repeat(lambda: fle.divisor_count(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

'''
divisor sum execution time
'''
print("divisor sum")
n = 1000000
t1 = timeit.repeat(lambda: fle.divisor_sum(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 10000000
t1 = timeit.repeat(lambda: fle.divisor_sum(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 100000000
t1 = timeit.repeat(lambda: fle.divisor_sum(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 1234567812312312
t1 = timeit.repeat(lambda: fle.divisor_sum(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 1000000000100011
t1 = timeit.repeat(lambda: fle.divisor_sum(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

'''
divisor product execution time
'''
print("divisor product")
n = 1000000
t1 = timeit.repeat(lambda: fle.divisor_product(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 100
t1 = timeit.repeat(lambda: fle.divisor_product(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 1000
t1 = timeit.repeat(lambda: fle.divisor_product(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 12345
t1 = timeit.repeat(lambda: fle.divisor_product(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

