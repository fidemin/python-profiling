
from random import randint
import objgraph

print('--- start ---')
objgraph.show_growth()
SIZE = 1000
arr = [randint(1, 1000) for i in range(SIZE)]

print('--- after arr created --')
objgraph.show_growth()

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

    print('--- after bubble sort ---')
    objgraph.show_growth()
