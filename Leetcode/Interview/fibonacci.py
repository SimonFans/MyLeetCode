# get a fib number
def getNthFib(num, cache):
    if num in cache:
        return cache[num]
    cache[num] = getNthFib(num - 1, cache) + getNthFib(num - 2, cache)
    return cache[num]

cache = {1:1, 2:1}
ans = getNthFib(5, cache)
print(ans)

# check if a number is fib
def check(num):
    fib = []
    fib.extend([0,1])
    while fib[-1] < num:
        fib.append(fib[-1] + fib[-2])
    return fib[-1] == num
print(check(4))
