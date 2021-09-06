import fermulerpy.elementary as fle
import timeit

#Two digit prime number
t1 = timeit.repeat(lambda: fle.isPrime(97), number=1, repeat=5)
print("two digit prime number: ",sum(t1)/len(t1))

#Three digit prime number
t1 = timeit.repeat(lambda: fle.isPrime(997), number=1, repeat=5)
print("three digit prime number: ",sum(t1)/len(t1))

#Four digit prime number
t1 = timeit.repeat(lambda: fle.isPrime(9973), number=1, repeat=5)
print("four digit prime number: ",sum(t1)/len(t1))

#Seven digit prime number
t1 = timeit.repeat(lambda: fle.isPrime(9999991), number=1, repeat=5)
print("Seven digit prime number: ",sum(t1)/len(t1))

#Eight digit prime number
t1 = timeit.repeat(lambda: fle.isPrime(99999997), number=1, repeat=5)
print("eight digit prime number: ",sum(t1)/len(t1))

#Nine digit prime number
t1 = timeit.repeat(lambda: fle.isPrime(999999937), number=1, repeat=5)
print("nine digit prime number: ",sum(t1)/len(t1))

#Ten digit prime number
t1 = timeit.repeat(lambda: fle.isPrime(9999999967), number=1, repeat=5)
print("ten digit prime number: ",sum(t1)/len(t1))

#Twelve digit prime number
t1 = timeit.repeat(lambda: fle.isPrime(100123456789), number=1, repeat=5)
print("twelve digit prime number: ",sum(t1)/len(t1))

#Sixteen digit prime number
t1 = timeit.repeat(lambda: fle.isPrime(1000000000100011), number=1, repeat=5)
print("Sixteen digit prime number: ",sum(t1)/len(t1))

'''
N'th prime number for different n values
'''
print("n'th prime number")
n = 1000
t1 = timeit.repeat(lambda: fle.prime(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 10000
t1 = timeit.repeat(lambda: fle.prime(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 100000
t1 = timeit.repeat(lambda: fle.prime(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 1000000
t1 = timeit.repeat(lambda: fle.prime(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

'''
prime series
'''
print("prime series")
n = 1000
t1 = timeit.repeat(lambda: fle.prime_series(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 10000
t1 = timeit.repeat(lambda: fle.prime_series(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 100000
t1 = timeit.repeat(lambda: fle.prime_series(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 1000000
t1 = timeit.repeat(lambda: fle.prime_series(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

'''
prime divisors execution time
'''
print("prime divisors")
n = 1000000000000000000
t1 = timeit.repeat(lambda: fle.prime_divisors(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 111111111111
t1 = timeit.repeat(lambda: fle.prime_divisors(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 100123456789
t1 = timeit.repeat(lambda: fle.prime_divisors(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

'''
prime factorization
'''
print("prime factorization")
n = 1000000000100011
t1 = timeit.repeat(lambda: fle.prime_factorization(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 10000000000000000000
t1 = timeit.repeat(lambda: fle.prime_factorization(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))

n = 123467891234569690
t1 = timeit.repeat(lambda: fle.prime_factorization(n), number=1, repeat=1)
print("for n = ",n, " execution time: ",sum(t1)/len(t1))