import time
maxnum = int(input("Max: "))
def mersenne(p):
    s = 4
    m = 2 ** p - 1
    for _ in range(p - 2):
        s = ((s * s) - 2) % m
    return s == 0

def prime(number):

    if number % 2 == 0:
        return number == 2

    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2

    return True
for i in range(1, maxnum, 2):  # generate up to M20, found in 1961
    start = time.time()
    if prime(i) and mersenne(i):
        end = time.time()
        b = ((2 ** i) - 1)
        z = (end-start)
        z = round(z,4)
        print("2^"+str(i)+" -1 is a mersenne prime and it took",z,"seconds to compute")
print("done")

