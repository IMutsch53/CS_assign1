def practiceCache(func):
    cache_dic={}
    def wrapper(*args):
        if args in cache_dic:
            return cache_dic[args]
        result = func(*args)
        cache_dic[args] = result
        return result
    return wrapper

@practiceCache
def divByThree(dividend):
    return dividend/3

print(divByThree(42))