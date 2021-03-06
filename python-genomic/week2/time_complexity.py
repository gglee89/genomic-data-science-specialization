import time
import random
def create_dna(n, alphabet='acgt'):
    return ''.join([random.choice(alphabet) for i in range(n)])

def count1(dna, base):
    i = 0
    for c in dna:
        if c == base:
	        i += 1 
    return i

def count2(dna, base):
    i = 0 
    for j in range(len(dna)):
        if dna[j] == base:
	        i += 1 
    return i 

def count3(dna, base):
    match = [c == base for c in dna]
    return sum(match)

def count4(dna, base):
    return dna.count(base)

def count5(dna, base):
    return len([i for i in range(len(dna)) if dna[i] == base])

def count6(dna,base):
    return sum(c == base for c in dna)

dna = create_dna(1000000)
start = time.perf_counter()
count1(dna, 'A')
print('[count1] Time elapsed %d', time.perf_counter() - start)

start = time.perf_counter()
count2(dna, 'A')
print('[count2] Time elapsed %d', time.perf_counter() - start)

start = time.perf_counter()
count3(dna, 'A')
print('[count3] Time elapsed %d', time.perf_counter() - start)

start = time.perf_counter()
count4(dna, 'A')
print('[count4] Time elapsed %d', time.perf_counter() - start)

start = time.perf_counter()
count5(dna, 'A')
print('[count5] Time elapsed %d', time.perf_counter() - start)

start = time.perf_counter()
count6(dna, 'A')
print('[count6] Time elapsed %d', time.perf_counter() - start)
