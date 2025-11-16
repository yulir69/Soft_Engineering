from functools import lru_cache
import time
def fib_without_cache(n):
    if n < 2:
        return n
    return fib_without_cache(n-1) + fib_without_cache(n-2)

@lru_cache(maxsize=None)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n-1) + fib_with_cache(n-2)

start = time.time()
try:
    result1 = fib_without_cache(35)
    print(f"Результат без кэша: {result1}")
except Exception as e:
    print(f"Ошибка без кэша: {e}")
end = time.time()
print(f"Время без кэша: {end - start:.2f} сек")
start = time.time()
result2 = fib_with_cache(100)
print(f"Результат с кэшем: {result2}")
end = time.time()
print(f"Время с кэшем: {end - start:.2f} сек")