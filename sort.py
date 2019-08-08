
import builtins
from random import randint

# line profiling을 안할때도 프로그램을 돌아가게 하려는 조치 (profile 이름의 빈 데코레이터를 정의한다.)
if 'builtins' not in dir() or not hasattr(builtins, 'profile'):
    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner

SIZE = 1000
arr = [randint(1, 1000) for i in range(SIZE)]

@profile
def bubble_sort():
    length = len(arr)
    a = {}
    for i in range(length-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp

def tim_sort():
    arr.sort()

if __name__ == '__main__':
    bubble_sort()
