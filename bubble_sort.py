import time

def bubble_sort(data,drawdata):
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            data[i],data[i+1] = data[i+1],data[i]
            
            drawdata(data)
            time.sleep(0.1)
    return data
