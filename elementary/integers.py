import timeit
import fermulerpy.elementary as fle

'''
isDivisible is O(1) operation
'''
a = 17357235923846048374593596398648565865086209693057390572973654653847523
b = 1325815387527883689463984689620846906139063868264064902
t1 = timeit.repeat(lambda: fle.isDivisible(a,b), number=1, repeat=1)
print("for a = ",a,"and b =",b, " execution time: ",sum(t1)/len(t1))

'''
GCD
'''
print("GCD execution times")
a = 17357235923846048374593596398648565865086209693057390572973654653847523
b = 1325815387527883689463984689620846906139063868264064902
t1 = timeit.repeat(lambda: fle.gcd(a,b), number=1, repeat=1)
print("for a = ",a,"and b =",b, " execution time: ",sum(t1)/len(t1))

a = 1000000000100011
b = 100123456789
t1 = timeit.repeat(lambda: fle.gcd(a,b), number=1, repeat=1)
print("for a = ",a,"and b =",b, " execution time: ",sum(t1)/len(t1))

'''
LCM
'''
print("LCM execution times")
a = 17357235923846048374593596398648565865086209693057390572973654653847523
b = 1325815387527883689463984689620846906139063868264064902
t1 = timeit.repeat(lambda: fle.lcm(a,b), number=1, repeat=1)
print("for a = ",a,"and b =",b, " execution time: ",sum(t1)/len(t1))

a = 1000000000100011
b = 100123456789
t1 = timeit.repeat(lambda: fle.lcm(a,b), number=1, repeat=1)
print("for a = ",a,"and b =",b, " execution time: ",sum(t1)/len(t1))