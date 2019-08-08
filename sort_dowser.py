import time
from random import randint

SIZE = 10
arr = [randint(1, 1000) for i in range(SIZE)]

def launch_memory_usage_server(port=8080):
    import cherrypy
    import dowser

    cherrypy.tree.mount(dowser.Root())
    cherrypy.config.update({
        'environment': 'embedded',
        'server.socket_port': port
    })
    cherrypy.engine.start()

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
    launch_memory_usage_server()
    bubble_sort()
