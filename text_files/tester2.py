def sum_pairs(ints, s):
    cache = set()
    for i in ints:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

l1= [1, 2, 3, 4, 1, 0]
print(sum_pairs(l1, 2)) 