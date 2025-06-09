import numpy as np

def f(x):
    return 1.0004515*x-0.2853027

def trans():
    h = [409.98,433.93,486.54,657.26]
    d = [409.87,433.82,486.42,657.13]
    
    ht = []
    dt = []
    
    for i in range(4):
        ht.append(f(h[i]))
        dt.append(f(d[i]))
    print(ht)
    print(dt)
    
trans()