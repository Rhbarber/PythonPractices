from functools import cache, lru_cache


# @cache
@lru_cache(maxsize=5)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    for i in range(250):
        print(i, fib(i))
    print("Done!")


if __name__ == '__main__':
    main()
